#!/usr/bin/env python3
"""Standalone v0.27 candidate integrity and state check; no visual judgment.

The builder installs this at 05_method/verify_rune_code_state.py. Run it there.
Only the Python standard library and bundled package data are required.
"""
from pathlib import Path, PurePosixPath
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = "05_method/v0.27-evidence/"
SOURCES = "06_sources/v0.27/"
REGISTRY = "01_inventory/rune_code_adjudication_v0.27.0.json"
EXPECTED = {"P241": "harvest", "P161": "unresolved", "P055": "neither", "P209": "unresolved",
            "P229": "seed", "P046": "harvest", "P109": "neither", "P189": "harvest", "P125": "neither",
            "P261": "harvest", "P005": "conditional-key"}
sha = lambda b: hashlib.sha256(b).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def content(path):
    parts = PurePosixPath(path)
    require(not parts.is_absolute() and ".." not in parts.parts and "\\" not in path and ":" not in path,
            "unsafe payload path")
    return (ROOT / path).read_bytes()


def jsonfile(path):
    return json.loads(content(path).decode("utf-8-sig"))


def rows(path):
    return list(csv.DictReader(content(path).decode("utf-8-sig").splitlines()))


def index(items, key):
    result = {row[key]: row for row in items}
    require(len(result) == len(items), "duplicate " + key)
    return result


def pixel_size(b):
    if b[:8] == b"\x89PNG\r\n\x1a\n":
        return int.from_bytes(b[16:20], "big"), int.from_bytes(b[20:24], "big")
    if b[:3] == b"GIF":
        return int.from_bytes(b[6:8], "little"), int.from_bytes(b[8:10], "little")
    if b[:2] == b"\xff\xd8":
        i = 2
        while i < len(b) - 9:
            if b[i] != 0xFF:
                i += 1
                continue
            marker = b[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                return int.from_bytes(b[i + 7:i + 9], "big"), int.from_bytes(b[i + 5:i + 7], "big")
            step = int.from_bytes(b[i + 2:i + 4], "big")
            require(step > 0, "malformed JPEG segment")
            i += 2 + step
    raise SystemExit("FAIL: unsupported or corrupt image")


registry = jsonfile(REGISTRY)
records = registry["records"]
require(registry["version"] == "0.27.0", "wrong version")
require({p: r["disposition"] for p, r in records.items()} == EXPECTED, "incomplete or changed reviewed dispositions")
require(registry["conditional_coordinates"] == ["2.6", "2.7", "2.8", "3.7"], "conditional key provenance missing")
require("no Gate 0 Outcome B" in registry["key_basis"], "key limitation missing")
code = index(rows("01_inventory/code_register.csv"), "page_id")
rune = {p: r for p, r in code.items() if r["rune_code_archive"] == "yes"}
require(len(rune) == 17 and set(records) <= set(rune), "Rune Code archive membership changed")
verified = index(rows("01_inventory/verified_page_register.csv"), "id")
claims = index(rows("04_registers/claims_evidence_register.csv"), "claim_id")
questions = index(rows("01_inventory/open_questions.csv"), "id")
reviewed = jsonfile(EVIDENCE + "reviewed-decisions.json")["decisions"]
initial = jsonfile(EVIDENCE + "comparison-decisions.json")
frozen = index(jsonfile(EVIDENCE + "independent-observations.json")["carriers"], "page")
for page, record in records.items():
    require(record["qualification"] and code[page]["decoding_status"] == record["current_status"], "code register mismatch: " + page)
    require(verified[page]["status_note"] == record["current_status"] + " See " + REGISTRY, "verified register mismatch: " + page)
    require(claims["V027-" + page]["claim"] == record["current_status"], "claim register mismatch: " + page)
    for name in ("record.md", "notes.md", "claims.csv"):
        path = "07_capture/" + record["post"] + "/" + name
        if (ROOT / path).exists():
            require(REGISTRY in content(path).decode("utf-8-sig"), "capture authority missing: " + page)
    if page != "P005":
        require(all(record[k] == v for k, v in reviewed[page].items()), "reviewed finding mismatch: " + page)
        require(record["initial_recommendation"] == initial[page], "first-pass history overwritten: " + page)
        require(record["rows"] == reviewed[page].get("reviewed_rows", frozen[page]["rows"]), "coordinate record mismatch: " + page)
for page in ("P005", "P161", "P209", "P125", "P055", "P109", "P261"):
    require(questions["OQ027-" + page]["blocking_condition"] == records[page]["qualification"], "open question mismatch: " + page)
require(records["P261"]["rows"] == [] and records["P261"]["reading"] is None, "Octave transcription out of scope")
require(records["P109"]["rows"][-1] == ["3.8", "3.3", "4.1", "1.3"], "skull derivation missing")
require(records["P125"]["first_line_alternatives"] == [["2.8", "4.2"], ["2.8", "2.1", "2.1"]], "ice alternative lost")

# Frozen hash checks keep this from silently ratifying edits to the original pass.
require(sha(content(EVIDENCE + "independent-observations.json")) ==
        "41cc3a03b6cb2c899e431fedd69897f7a8fbf084c1204dc204091eca19cedce9", "frozen observations changed")
require(sha(content(EVIDENCE + "loop-candidate-key.csv")) ==
        "721dccd4d07b4691f8820aeca8c2d4b9817a48bc2bb806f549007f5ac5a9ebde", "frozen key changed")
key = index(rows(EVIDENCE + "loop-candidate-key.csv"), "coordinate")
require(set(key) == {f"{group}.{place}" for group, size in ((1, 8), (2, 8), (3, 8), (4, 5)) for place in range(1, size+1)}, "29-cell key incomplete")


def transliterate(sequence):
    return "".join(key[x]["transliteration"].upper() if x in key else x for x in sequence)


for page in ("P241", "P055", "P229", "P046", "P109", "P189"):
    observed = transliterate([unit for row in records[page]["rows"] for unit in row])
    expected = re.sub(r"[\s/]", "", records[page]["reading"])
    require(observed == expected, f"transliteration inconsistency for {page}: {observed} != {expected}")
require("/".join(transliterate(row[::-1]) for row in records["P161"]["rows"]) == "NIGHT/AND/DAY", "P161 candidate derivation mismatch")
require([transliterate(row) for row in records["P125"]["first_line_alternatives"]] == ["SAE", "SHH"], "ice transliteration mismatch")

fingerprints = index(rows("01_inventory/rune_code_carrier_fingerprints.csv"), "page_id")
require(set(fingerprints) == set(rune), "fingerprint membership mismatch")
media = jsonfile("01_inventory/rune_code_source_media.json")
images = index(media["images"], "url")
require(len(images) == 31, "imported media count changed")
for row in images.values():
    require(re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) and min(row["bytes"], row["width"], row["height"]) > 0, "invalid media metadata")
for page, row in fingerprints.items():
    source = images.get(row["source_url"])
    require(source is not None and source["sha256"] == row["source_sha256"], "fingerprint hash mismatch")
    require(row["natural_dimensions"] == f"{source['width']}x{source['height']}", "fingerprint dimension mismatch")
    require(not row["visual_fingerprint_sha256"] or row["visual_source_url"], "historical visual identity lost")
    require(row["source_hash_provenance"] and row["source_retrieved_on"] == media["retrieved"], "historical provenance lost")
    if page in records:
        require(records[page]["source_sha256"] == source["sha256"], "adjudication source identity mismatch")
authentication = jsonfile(EVIDENCE + "source-authentication.json")
require(sha(content("01_inventory/rune_code_source_media.json").replace(b"\r\n", b"\n")) == authentication["manifest_lf_sha256"], "authentication manifest identity mismatch")
authenticated = index(authentication["carriers"], "url")
require(len(authenticated) == 17 and set(authenticated) == {r["source_url"] for r in fingerprints.values()}, "named source identity mismatch")
for url, row in authenticated.items():
    original = content(SOURCES + "originals/" + row["file"])
    require((sha(original), len(original), pixel_size(original)) ==
            (row["sha256"], row["bytes"], (row["width"], row["height"])), "bundled original mismatch")
    require(row["status"] == "verified" and not row["differences"], "source authentication did not pass")
    require(all(row[k] == images[url][k] for k in ("sha256", "bytes", "width", "height")), "source attestation differs")
bundle = jsonfile(SOURCES + "bundle-map.json")
for item in bundle.values():
    require(sha(content(item["path"])) == item["sha256"], "bundled input mismatch: " + item["path"])
html_sources = jsonfile(EVIDENCE + "key-corroboration-sources.json")
require(len(html_sources) == 5, "authored support source count changed")
for row in html_sources:
    require(sha(content(bundle[row["page"]]["path"])) == row["lf_sha256"], "authored text changed")

delta = jsonfile("05_method/v0.27-parent-delta.json")
require(delta["parent_zip_sha256"] == registry["parent_zip_sha256"] ==
        "cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75", "parent lineage changed")
modified = set(delta["modified_parent_files"])
for path, digest in delta["parent_payload_hashes"].items():
    if path == "MANIFEST.sha256":
        continue
    require(sha(content(delta["history_prefix"] + path if path in modified else path)) == digest,
            "parent history or untouched payload changed: " + path)
old_code = index(rows(delta["history_prefix"] + "01_inventory/code_register.csv"), "page_id")
require(set(old_code) == set(code), "code membership changed")
for page, row in code.items():
    if page in records:
        require(records[page]["inherited_seed_status"] == old_code[page]["decoding_status"], "old reading lost")
        require(all(row[k] == old_code[page][k] for k in row if k != "decoding_status"), "code metadata changed")
    else:
        require(row == old_code[page], "unreviewed code entry changed")

print("Rune Code state: 17 archive entries; 9 disputes + Octave classification + conditional Loop accounted for")
print("Current code/page/claim registers and open research limits: consistent; frozen first pass retained")
print("Mechanical transliteration consistency: pass; this does not verify visual counts or traversal")
print("Source evidence: 17 original images authenticated; 5 authored HTML texts verified; 31 imported media identities preserved")
print(f"Parent preservation: {len(modified)} modified files have exact historical snapshots; all other parent payloads unchanged")
