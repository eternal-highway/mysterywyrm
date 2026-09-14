#!/usr/bin/env python3
"""Recheck the immutable v0.27 ZIP before import, without changing seed or Git.

Independent of the candidate builder. Emits JSON to stdout; diagnostics and
nonzero exit on failure. Uses only the standard library. Run from any directory.
"""
from pathlib import Path, PurePosixPath
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "letters_for_titles_corpus_seed/"
PARENT_SHA = "cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75"
CANDIDATE_SHA = "72c85305702f1074598c6f8f0285c41ad19f19d71011a1880c9eb0cc78753b1a"
sha = lambda data: hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def safe(path):
    parts = PurePosixPath(path)
    return (bool(path) and not parts.is_absolute() and
            all(p not in ("", ".", "..") for p in path.split("/")) and
            not any(c in path for c in "\\:\x00"))


def manifest(files):
    entries = {}
    for line in files["MANIFEST.sha256"].decode("ascii").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  \./(.+)", line)
        require(match is not None, "malformed manifest line")
        digest, path = match.groups()
        require(safe(path) and path not in entries, "unsafe or duplicate manifest path")
        entries[path] = digest
    require(set(files) == set(entries) | {"MANIFEST.sha256"}, "manifest path-set mismatch")
    require(all(sha(files[p]) == h for p, h in entries.items()), "manifest hash mismatch")
    return len(entries)


def package(path, digest):
    require(sha(path.read_bytes()) == digest, "unexpected ZIP identity: " + path.name)
    sidecar = path.with_suffix(".zip.sha256").read_text(encoding="utf-8").strip()
    require(sidecar == digest + "  " + path.name, "sidecar mismatch")
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        require(len(names) == len(set(names)), "duplicate ZIP members")
        require(all(n.startswith(PREFIX) and safe(n[len(PREFIX):]) for n in names),
                "ZIP must contain regular files under a single safe root")
        require(all((i.external_attr >> 16) & 0o170000 in (0, 0o100000)
                    for i in archive.infolist()), "nonregular ZIP member")
        require(archive.testzip() is None, "ZIP CRC failure")
        files = {n[len(PREFIX):]: archive.read(n) for n in names}
    manifest(files)
    return files


def tree(path):
    return {p.relative_to(path).as_posix(): p.read_bytes()
            for p in path.rglob("*") if p.is_file()}


def main():
    candidate_path = ROOT / "dist/letters_for_titles_corpus_seed_v0.27.0.zip"
    parent = package(ROOT / "dist/letters_for_titles_corpus_seed_v0.26.2.zip", PARENT_SHA)
    candidate = package(candidate_path, CANDIDATE_SHA)
    for path in ROOT.rglob("letters_for_titles_corpus_seed*.zip"):
        require("(1)" not in path.name, "duplicate-suffixed corpus package")
        if "v0.27.0" in path.name:
            require(sha(path.read_bytes()) == CANDIDATE_SHA, "competing v0.27.0 identity")
    require(tree(ROOT / "corpus-seed") == parent, "canonical seed no longer equals parent")
    require(tree(ROOT / "dist/v027-candidate" / PREFIX.rstrip("/")) == candidate,
            "saved candidate extraction differs from ZIP")
    removed = sorted(set(parent) - set(candidate))
    added = sorted(set(candidate) - set(parent))
    changed = sorted(p for p in parent if p in candidate and parent[p] != candidate[p])
    require(not removed, "parent payload removed")
    delta = json.loads(candidate["05_method/v0.27-parent-delta.json"])
    require(delta["parent_payload_hashes"] == {p: sha(b) for p, b in parent.items()},
            "bundled parent hashes differ from independently read parent")
    modified = [p for p in changed if p != "MANIFEST.sha256"]
    require(modified == sorted(delta["modified_parent_files"]), "declared parent delta mismatch")
    for path in modified:
        require(candidate[delta["history_prefix"] + path] == parent[path], "parent snapshot differs")
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
    media = [p for p in parent if PurePosixPath(p).suffix.lower() in image_extensions]
    require(all(candidate[p] == parent[p] for p in media), "retained parent media changed")
    csv_count = 0
    blank_csv_records = 0
    for path, data in candidate.items():
        if path.endswith(".csv"):
            rows = list(csv.reader(io.StringIO(data.decode("utf-8-sig"), newline="")))
            # Empty physical records are inherited separators, not data rows.
            # Preserve them byte-for-byte while checking every nonempty record.
            blank_csv_records += sum(not row for row in rows)
            rows = [row for row in rows if row]
            require(bool(rows) and all(len(r) == len(rows[0]) for r in rows), "nonrectangular CSV: " + path)
            csv_count += 1
    largest = max(candidate, key=lambda p: len(candidate[p]))
    require(len(candidate[largest]) < 100 * 1024 * 1024, "payload exceeds GitHub file limit")
    logs = {}
    with tempfile.TemporaryDirectory(prefix="v027-release-preflight-") as folder:
        clean = Path(folder) / "seed"
        for path, data in candidate.items():
            target = clean / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        require(tree(clean) == candidate, "fresh extraction byte mismatch")
        for name in ("verify_rune_code_state.py", "verify_cipher_letter_run.py"):
            run = subprocess.run([sys.executable, "-X", "utf8", "-B", str(clean / "05_method" / name)],
                                 cwd=clean, capture_output=True, text=True, encoding="utf-8")
            require(run.returncode == 0, name + ": " + run.stdout + run.stderr)
            logs[name] = run.stdout.strip()
        require(tree(clean) == candidate, "verifier changed extraction")
    require(tree(ROOT / "corpus-seed") == parent, "preflight changed canonical seed")
    print(json.dumps({
        "result": "pass", "scope": "pre-import byte and record integrity; no new visual adjudication",
        "candidate_zip_sha256": CANDIDATE_SHA, "parent_zip_sha256": PARENT_SHA,
        "payload_files": len(candidate), "manifest_hashes": manifest(candidate),
        "rectangular_csvs": csv_count, "blank_csv_records_preserved": blank_csv_records,
        "modified_parent_files": modified,
        "manifest_changed": "MANIFEST.sha256" in changed,
        "added_files": added, "removed_files": removed,
        "retained_parent_media_unchanged": len(media),
        "largest_payload": {"path": largest, "bytes": len(candidate[largest])},
        "canonical_seed": "exact published v0.26.2 parent",
        "clean_extraction_verifiers": logs,
    }, indent=2))


if __name__ == "__main__":
    main()
