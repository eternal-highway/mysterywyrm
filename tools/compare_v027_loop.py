#!/usr/bin/env python3
"""Compare the frozen Loop candidate with the harvest key; never pass Gate 0."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "research/v0.27/loop-candidate-key.csv"
FROZEN_SHA256 = "721dccd4d07b4691f8820aeca8c2d4b9817a48bc2bb806f549007f5ac5a9ebde"


def normalize(value):
    value = value.casefold().replace("æ", "ae").replace("œ", "oe").replace("þ", "th")
    return "".join(c for c in unicodedata.normalize("NFD", value)
                   if unicodedata.category(c) != "Mn")


def main():
    blob = CANDIDATE.read_bytes()
    # Normalize checkout line endings for the frozen logical-text comparison.
    normalized = blob.replace(b"\r\n", b"\n")
    if hashlib.sha256(normalized).hexdigest() != FROZEN_SHA256:
        raise ValueError("Candidate changed after the independent reading was frozen")
    candidates = list(csv.DictReader(io.StringIO(normalized.decode("utf-8"))))
    key_path = ROOT / "research/rune-code.md"
    inherited = {}
    for line in key_path.read_text(encoding="utf-8").splitlines():
        if not re.match(r"\| \*\*[1-4]\*\* \|", line):
            continue
        fields = [part.strip() for part in line.strip("|").split("|")]
        group = int(fields[0].strip("*"))
        for position, cell in enumerate(fields[1:], 1):
            if not cell:
                continue
            match = re.fullmatch(r"(.+?) \((.+?)\)", cell)
            if not match:
                raise ValueError(f"Unexpected table cell: {cell}")
            inherited[f"{group}.{position}"] = {
                "transliteration": match[1], "rune": match[2],
            }
    expected_coordinates = {f"{(n-1)//8+1}.{(n-1)%8+1}" for n in range(1, 30)}
    if len(candidates) != 29 or {int(row["cell"]) for row in candidates} != set(range(1, 30)):
        raise ValueError("Candidate must contain exactly the 29 unique ordinal cells")
    if len(inherited) != 29 or set(inherited) != expected_coordinates:
        raise ValueError("Inherited table did not yield the complete key")
    if {row["coordinate"] for row in candidates} != expected_coordinates:
        raise ValueError("Candidate coordinates are incomplete or duplicated")
    mismatches, letter_differences = [], []
    for row in candidates:
        other = inherited[row["coordinate"]]
        if normalize(row["rune"]) != normalize(other["rune"]):
            mismatches.append({"cell": row["cell"], "candidate": row, "inherited": other})
        if normalize(row["transliteration"]) != normalize(other["transliteration"]):
            letter_differences.append({
                "cell": int(row["cell"]), "coordinate": row["coordinate"],
                "candidate": row["transliteration"], "inherited": other["transliteration"],
            })
    print(json.dumps({
        "candidate_text_sha256": FROZEN_SHA256,
        "inherited_file_sha256": hashlib.sha256(key_path.read_bytes()).hexdigest(),
        "normalization": "case, diacritics, ae/oe/th expansions only",
        "coordinate_rune_matches": 29 - len(mismatches),
        "coordinate_rune_mismatches": mismatches,
        "transliteration_differences": letter_differences,
        "reconstructed_or_partial_coordinates": [int(row["cell"]) for row in candidates
            if row["coordinate_basis"] not in ("visible", "visible in lower-band crop")],
        "low_confidence_identities": [int(row["cell"]) for row in candidates
            if row["confidence"] == "low"],
        "gate_0": "pending; table agreement does not validate reconstruction",
    }, indent=2))


if __name__ == "__main__":
    main()
