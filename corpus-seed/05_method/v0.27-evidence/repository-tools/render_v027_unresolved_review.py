"""Authenticate five carriers and make unenhanced crops for the bounded review.

Requires Pillow. Run from any directory. Derived PNGs live only under dist/.
This checks bytes and renders pixels; it does not validate visual readings.
"""
from pathlib import Path
import hashlib
import json

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "v027-unresolved-review"
SPECS = {
    "P161": ("oe-is-for-oedipean-riddle", {
        "top2": (560, 80, 1080, 690),
        "bottomleft": (290, 1900, 1120, 2510),
        "middle-right": (1430, 880, 2010, 1480),
    }),
    "P055": ("it-never-deceives", {
        "lasttwo": (1270, 820, 2320, 1770),
        "firstthree": (80, 140, 1760, 800),
    }),
    "P209": ("shh", {"whole": (0, 0, 1080, 1309)}),
    "P109": ("you-knew-it-beforehand", {
        "skull1": (230, 1580, 710, 2080),
        "skull2": (640, 1610, 1040, 2110),
        "skull3": (995, 1620, 1380, 2110),
        "skull4": (1350, 1610, 1749, 2130),
        "lower-first": (45, 770, 1535, 1390),
        "lower-second": (100, 1180, 1730, 1640),
    }),
    "P125": ("soon-after-it-becomes-water", {
        "top-left": (200, 90, 1140, 430),
        "top-right": (1230, 45, 1980, 440),
    }),
}


def main():
    auth = json.loads((ROOT / "research/v0.27/source-authentication.json").read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    for page, (post, crops) in SPECS.items():
        matches = [r for r in auth["carriers"] if post in r["posts"]]
        if len(matches) != 1:
            raise ValueError(f"{page}: expected one authenticated carrier")
        record = matches[0]
        source = ROOT / "archive/code" / record["file"]
        raw = source.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != record["sha256"] or len(raw) != record["bytes"]:
            raise ValueError(f"{page}: source bytes differ")
        with Image.open(source) as im:
            im.load()
            if im.size != (record["width"], record["height"]):
                raise ValueError(f"{page}: source dimensions differ")
            overview = im.copy()
            overview.thumbnail((1200, 1200))
            overview.save(OUT / f"{page}-overview.png")
            for name, box in crops.items():
                if not (0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height):
                    raise ValueError(f"{page}/{name}: invalid crop")
                im.crop(box).save(OUT / f"{page}-{name}.png")
            records.append({
                "page": page, "source": source.relative_to(ROOT).as_posix(),
                "source_url": record["url"], "sha256": digest,
                "bytes": len(raw), "width": im.width, "height": im.height,
                "crop_rectangles": crops,
            })
    (OUT / "evidence.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    print(f"Authenticated {len(records)} carriers; rendered {sum(len(x[1]) for x in SPECS.values())} original-pixel crops to {OUT}")


if __name__ == "__main__":
    main()
