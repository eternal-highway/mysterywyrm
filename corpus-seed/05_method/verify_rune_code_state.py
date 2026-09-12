#!/usr/bin/env python3
"""Check current Rune Code classifications and guard against stale status text."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


with (ROOT / "01_inventory/code_register.csv").open(encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))

rune_rows = [row for row in rows if row["rune_code_archive"] == "yes"]
if len(rune_rows) != 17:
    fail(f"expected 17 Rune Code rows, found {len(rune_rows)}")

statuses = [row["decoding_status"] for row in rune_rows]
decoded = sum(status.startswith("decoded ") for status in statuses)
question_rebus = sum(status.startswith("complete carrier:") for status in statuses)
key_carriers = sum(
    row["page_id"] in {"P005", "P261"} and "key" in row["decoding_status"]
    for row in rune_rows
)
if (decoded, question_rebus, key_carriers) != (14, 1, 2):
    fail(
        "expected Rune Code classification 14 ordered inscriptions + "
        f"1 question-and-rebus + 2 key carriers; found {decoded} + "
        f"{question_rebus} + {key_carriers}"
    )

forbidden_status = ("opaque", "unresolved", "untranscribed")
for row in rune_rows:
    lowered = row["decoding_status"].lower()
    if any(term in lowered for term in forbidden_status):
        fail(f"stale status for {row['title']}: {row['decoding_status']}")

with (ROOT / "01_inventory/verified_page_register.csv").open(
    encoding="utf-8", newline=""
) as handle:
    verified_rows = list(csv.DictReader(handle))
verified_by_id = {row["id"]: row for row in verified_rows}
for row in rune_rows:
    status_note = verified_by_id[row["page_id"]]["status_note"].lower()
    if any(term in status_note for term in forbidden_status):
        fail(f"stale verified-page status for {row['title']}: {status_note}")

current_files = {
    "05_method/reentry_capsule.md": (
        "Soon After it Becomes Water* remains opaque code",
    ),
    "07_capture/bright-fruits/notes.md": ("does not yield the code",),
    "07_capture/frith/notes.md": ("Code remains opaque",),
    "07_capture/frith/claims.csv": ("preserve as opaque",),
    "07_capture/soon-after-it-becomes-water/notes.md": ("Preserve the code as opaque",),
    "07_capture/you-knew-it-beforehand/claims.csv": ("keep the lower field unresolved",),
}
for relative, forbidden_phrases in current_files.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    for phrase in forbidden_phrases:
        if phrase in text:
            fail(f"stale phrase {phrase!r} in {relative}")

count_phrase = "twelve coordinate-valued face units plus one direct roman"
count_files = (
    "05_method/reentry_capsule.md",
    "05_method/rune_code_plate_reconciliation_v0.24.0.md",
    "07_capture/you-knew-it-beforehand/record.md",
    "04_registers/claims_evidence_register.csv",
)
for relative in count_files:
    if count_phrase not in (ROOT / relative).read_text(encoding="utf-8").lower():
        fail(f"corrected face-unit accounting absent from {relative}")

with (ROOT / "01_inventory/rune_code_carrier_fingerprints.csv").open(
    encoding="utf-8", newline=""
) as handle:
    fingerprint_rows = list(csv.DictReader(handle))
if len(fingerprint_rows) != 17:
    fail(f"expected 17 carrier fingerprint rows, found {len(fingerprint_rows)}")
if {row["page_id"] for row in fingerprint_rows} != {row["page_id"] for row in rune_rows}:
    fail("carrier fingerprint page IDs do not match Rune Code archive membership")
media = json.loads((ROOT / "01_inventory/rune_code_source_media.json").read_text(encoding="utf-8"))
images = media["images"]
if len(images) != 31 or len({row["url"] for row in images}) != 31:
    fail("expected 31 uniquely identified source-media records")
by_url = {row["url"]: row for row in images}
for row in images:
    if not re.fullmatch(r"[0-9a-f]{64}", row["sha256"]):
        fail(f"invalid source hash for {row['url']}")
    if min(row["bytes"], row["width"], row["height"]) <= 0:
        fail(f"invalid source-media dimensions/size for {row['url']}")
for row in fingerprint_rows:
    source = by_url.get(row["source_url"])
    if source is None or row["source_sha256"] != source["sha256"]:
        fail(f"carrier does not match imported source manifest: {row['page_id']}")
    if row["natural_dimensions"] != f"{source['width']}x{source['height']}":
        fail(f"carrier dimensions disagree with source manifest: {row['page_id']}")
    if row["visual_fingerprint_sha256"] and not row["visual_source_url"]:
        fail(f"historical visual fingerprint has no source identity: {row['page_id']}")
    if not row["source_hash_provenance"] or row["source_retrieved_on"] != media["retrieved"]:
        fail(f"missing or inconsistent imported hash provenance: {row['page_id']}")

print("Rune Code state: 17/17 classified (14 ordered + 1 rebus + 2 key carriers)")
print("Stale current-state phrases: 0")
print("Carrier fingerprints: 17/17 rows; imported source-byte hashes: 17/17 named carriers, 31/31 media records")
