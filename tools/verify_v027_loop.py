#!/usr/bin/env python3
"""Authenticate the Gate 0 carrier without opening any transcription table.

This verifies source identity only. A successful exit does not pass Gate 0.
The source image remains in the ignored archive, never in the release seed.
"""
import hashlib
import json
from pathlib import Path
import sys

from archive import pixel_size

ROOT = Path(__file__).resolve().parents[1]
URL = "https://lettersfortitles.com/wp-content/uploads/2021/11/Loop.lettersfortitles-verntonkin.jpg"
FILE = "2021_11_Loop.lettersfortitles-verntonkin.jpg"
EXPECTED = {
    "url": URL,
    "file": FILE,
    "bytes": 5734273,
    "sha256": "33b777ed8f09bd0c3421d4b17c2f87bef8e878e77c8d75939e4dd2d58158874c",
    "width": 2062,
    "height": 1528,
}


def main():
    manifest = json.loads((ROOT / "data/media-code.json").read_text(encoding="utf-8"))
    matches = [row for row in manifest["images"] if row["url"] == URL]
    errors = []
    if len(matches) != 1:
        errors.append("Expected exactly one canonical URL match in media-code.json")
    else:
        row = matches[0]
        for key, value in EXPECTED.items():
            if row.get(key) != value:
                errors.append(f"Manifest differs from packet: {key}")
        if "loop" not in row.get("posts", []):
            errors.append("Manifest carrier is not associated with Loop")
    path = ROOT / "archive/code" / FILE
    actual = None
    if not path.is_file():
        errors.append("Required archive file is absent")
    else:
        blob = path.read_bytes()
        width, height = pixel_size(blob)
        actual = {
            "bytes": len(blob), "sha256": hashlib.sha256(blob).hexdigest(),
            "width": width, "height": height,
        }
        for key, value in actual.items():
            if value != EXPECTED[key]:
                errors.append(f"Source bytes differ from packet: {key}")
    print(json.dumps({
        "page": "P005", "expected": EXPECTED, "actual": actual,
        "source_identity": "verified" if not errors else "failed",
        "gate_0": "not_determined_by_this_tool", "errors": errors,
    }, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
