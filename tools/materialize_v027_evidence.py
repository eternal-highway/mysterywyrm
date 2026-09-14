#!/usr/bin/env python3
"""Fetch/check the 17 named plate carriers without displaying or reading them.

The 14 numbered filename-run assets are outside this pass. The committed
manifest is read-only. Existing files are never silently repaired or replaced.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import urllib.request

from archive import pixel_size

ROOT = Path(__file__).resolve().parents[1]


def check(blob, row):
    width, height = pixel_size(blob)
    actual = {"bytes": len(blob), "sha256": hashlib.sha256(blob).hexdigest(),
              "width": width, "height": height}
    return actual, [key for key in actual if actual[key] != row[key]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true", help="Download absent named carriers")
    args = parser.parse_args()
    manifest_path = ROOT / "data/media-code.json"
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    rows = [row for row in manifest["images"]
            if not re.match(r"^\d{4}_\d{2}_\d+-", row["file"])]
    if len(rows) != 17 or len({row["file"] for row in rows}) != 17:
        raise ValueError("Expected exactly 17 unique named plate carriers")
    folder = ROOT / "archive/code"
    if args.fetch:
        folder.mkdir(parents=True, exist_ok=True)
    results = []
    for row in rows:
        name = row["file"]
        if Path(name).name != name or "/" in name or "\\" in name:
            raise ValueError("Manifest filename is not a simple local basename")
        if not row["url"].startswith("https://lettersfortitles.com/wp-content/uploads/"):
            raise ValueError("Carrier URL is outside the canonical media source")
        path = folder / name
        result = {key: row[key] for key in ("file", "url", "posts", "sha256", "bytes", "width", "height")}
        try:
            if path.is_file():
                blob = path.read_bytes()
                result["acquisition"] = "existing"
            elif args.fetch:
                req = urllib.request.Request(row["url"], headers={
                    "User-Agent": "letters-for-titles-research/1.0"})
                with urllib.request.urlopen(req, timeout=30) as response:
                    blob = response.read()
                    result["response_url"] = response.url
                result["acquisition"] = "downloaded"
            else:
                raise FileNotFoundError("Carrier absent; use --fetch to materialize")
            actual, differences = check(blob, row)
            result["actual"] = actual
            result["differences"] = differences
            result["status"] = "failed" if differences else "verified"
            if args.fetch and not differences and not path.exists():
                # Exclusive creation refuses to overwrite a concurrently created file.
                with path.open("xb") as output:
                    output.write(blob)
        except (OSError, ValueError) as exc:
            result["status"] = "failed"
            result["error"] = str(exc)
        results.append(result)
        print(f"{result['status']}: {name}", flush=True)
    report = {
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "manifest_lf_sha256": hashlib.sha256(manifest_bytes.replace(b"\r\n", b"\n")).hexdigest(),
        "scope": "17 named carriers; no visual transcription performed",
        "verified": sum(row["status"] == "verified" for row in results),
        "count": len(results), "carriers": results,
    }
    report_folder = ROOT / "research/v0.27"
    report_folder.mkdir(parents=True, exist_ok=True)
    (report_folder / "source-authentication.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {report['verified']}/{report['count']} named carriers")
    return 0 if report["verified"] == report["count"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
