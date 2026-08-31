#!/usr/bin/env python3
"""Verify the locally captured portion of the 261-slot filename cipher."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


MESSAGE = (
    "LISTEN! COME TO THE MIRROR. SEE? YOU ARE SLIPPING AWAY. MOMENTARY. "
    "WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR CONSORT AND ONLY "
    "IN THE MEMORIES OF OTHERS WILL YOU PERSIST. WE ARE EACH OTHER'S ONLY "
    "IMMORTALITY ON EARTH, OTHERWISE EVERYTHING IS TEMPORARY."
)

TOKEN_MAP = {
    "apostrophe": "'",
    "Comma": ",",
    "Twist": "T",
}


def captured_tokens(root: Path):
    for path in root.glob("07_capture/*/media.csv"):
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                filename = unquote(Path(urlparse(row.get("source_url", "")).path).name)
                match = re.match(r"^(\d+)-([^-\.]+)", filename)
                if not match:
                    continue
                slot = int(match.group(1))
                if slot > 261:
                    continue
                token = match.group(2)
                # The authorial 142-M filename is one of the three known slips.
                if slot == 142 and token == "M":
                    slot = 144
                value = TOKEN_MAP.get(token, token.upper())
                if len(value) == 1:
                    yield slot, value, filename, path.parent.name


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    if len(MESSAGE) != 261:
        raise RuntimeError(f"expected 261-character message, got {len(MESSAGE)}")

    rows = sorted(captured_tokens(root))
    failures = []
    for slot, value, filename, capture in rows:
        expected = MESSAGE[slot - 1]
        if value != expected:
            failures.append((slot, value, expected, filename, capture))

    print(f"message length: {len(MESSAGE)}")
    print(f"locally captured cipher tokens: {len(rows)}")
    print(f"matches: {len(rows) - len(failures)}")
    print(f"failures: {len(failures)}")
    if "--table" in sys.argv:
        for slot, value, filename, capture in rows:
            expected = MESSAGE[slot - 1]
            state = "PASS" if value == expected else "FAIL"
            print(f"{slot:3} {value!r:4} {expected!r:4} {state:4} {capture:38} {filename}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
