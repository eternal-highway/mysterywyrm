#!/usr/bin/env python3
"""Build an isolated, evidence-preserving v0.27.0 candidate from the exact parent ZIP.

Does not write corpus-seed, git state, or published releases. A versioned ZIP
is never overwritten. All construction and verification happen before delivery.
"""
from pathlib import Path, PurePosixPath
import csv
import hashlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile

from archive import pixel_size

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PARENT = DIST / "letters_for_titles_corpus_seed_v0.26.2.zip"
PARENT_SHA = "cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75"
VERSION = "0.27.0"
PREFIX = "letters_for_titles_corpus_seed/"
TARGET = DIST / f"letters_for_titles_corpus_seed_v{VERSION}.zip"
TREE = DIST / "v027-candidate" / PREFIX.rstrip("/")
EVIDENCE = "05_method/v0.27-evidence/"
HISTORY = "05_method/v0.26.2-history/"
SOURCES = "06_sources/v0.27/"
REGISTRY = "01_inventory/rune_code_adjudication_v0.27.0.json"
sha = lambda b: hashlib.sha256(b).hexdigest()
lf = lambda b: b.replace(b"\r\n", b"\n")


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def jbytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def table(data):
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline="")))


def csvbytes(rows):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode("utf-8")


def verify_manifest(files):
    entries = {}
    for line in files["MANIFEST.sha256"].decode().splitlines():
        digest, path = line.split("  ", 1)
        path = path.removeprefix("./")
        require(path not in entries, "duplicate manifest entry")
        entries[path] = digest
    require(set(files) == set(entries) | {"MANIFEST.sha256"}, "manifest path set mismatch")
    require(all(sha(files[p]) == h for p, h in entries.items()), "manifest digest mismatch")


def run_verifiers(tree):
    logs = []
    for script in ("verify_rune_code_state.py", "verify_cipher_letter_run.py"):
        run = subprocess.run([sys.executable, "-X", "utf8", "-B", str(tree / "05_method" / script)],
                             check=True, capture_output=True, text=True, encoding="utf-8")
        logs.append(run.stdout.strip())
    return "\n".join(logs)


def main():
    # Inventory the durable project, including ignored ZIPs, before reserving a version.
    packages = sorted(ROOT.rglob("letters_for_titles_corpus_seed*.zip"))
    require(not any("v0.27" in p.name or "(1)" in p.name for p in packages),
            "v0.27 package or duplicate-suffixed package already exists; resolve lineage first")
    require(not TREE.parent.exists() and not TARGET.exists(), "candidate output already exists")
    require(sha(PARENT.read_bytes()) == PARENT_SHA, "parent ZIP is not the verified published v0.26.2")
    for package in packages:
        if "v0.26.2" in package.name:
            require(sha(package.read_bytes()) == PARENT_SHA, "competing v0.26.2 ZIP identity")
    with zipfile.ZipFile(PARENT) as z:
        require(z.testzip() is None, "parent CRC failure")
        names = z.namelist()
        require(len(names) == len(set(names)), "duplicate parent ZIP members")
        require(all(n.startswith(PREFIX) and ".." not in PurePosixPath(n).parts
                    and "\\" not in n for n in names), "unsafe parent path")
        parent = {n[len(PREFIX):]: z.read(n) for n in names if not n.endswith("/")}
    verify_manifest(parent)
    live_seed = {p.relative_to(ROOT / "corpus-seed").as_posix(): p.read_bytes()
                 for p in (ROOT / "corpus-seed").rglob("*") if p.is_file()}
    require(live_seed == parent, "canonical seed differs from published parent")
    files = dict(parent)
    bundle = {}

    def put(path, content):
        require(path != "MANIFEST.sha256", "manifest is generated last")
        if path in parent and path not in {"05_method/release_validation_v0.27.0.md"}:
            files[HISTORY + path] = parent[path]
        files[path] = content.encode("utf-8") if isinstance(content, str) else content

    def bundle_file(source, destination, normalize=True):
        original = (ROOT / source).read_bytes()
        content = lf(original) if normalize else original
        files[destination] = content
        bundle[source] = {"path": destination, "sha256": sha(content),
                          "input_sha256": sha(original), "normalization": "LF" if normalize else "none"}

    for path in sorted((ROOT / "research/v0.27").iterdir()):
        if path.is_file():
            bundle_file(path.relative_to(ROOT).as_posix(), EVIDENCE + path.name)
    for name in ("CROSS-LINEAGE-FINDINGS.md", "V0.27-ADJUDICATION-PACKET.md", "research/rune-code.md"):
        bundle_file(name, EVIDENCE + "lineage-inputs/" + Path(name).name)
    for name in ("build_v027_candidate.py", "verify_v027_candidate_state.py", "archive.py",
                 "render_v027_pass.py", "render_v027_unresolved_review.py", "verify_v027_loop.py",
                 "compare_v027_loop.py", "materialize_v027_evidence.py"):
        bundle_file("tools/" + name, EVIDENCE + "repository-tools/" + name)
    # Original media remain byte-exact. No network request occurs during packaging.
    authentication = json.loads(files[EVIDENCE + "source-authentication.json"])
    require(authentication["verified"] == authentication["count"] == 17, "incomplete authentication record")
    for row in authentication["carriers"]:
        source = "archive/code/" + row["file"]
        data = (ROOT / source).read_bytes()
        require((sha(data), len(data), pixel_size(data)) ==
                (row["sha256"], row["bytes"], (row["width"], row["height"])), "source identity mismatch: " + source)
        bundle_file(source, SOURCES + "originals/" + row["file"], normalize=False)
    for row in json.loads(files[EVIDENCE + "key-corroboration-sources.json"]):
        content = (ROOT / row["page"]).read_bytes()
        require(sha(lf(content)) == row["lf_sha256"], "authored source text drift")
        bundle_file(row["page"], SOURCES + "primary-html/" + Path(row["page"]).name)
    files[SOURCES + "bundle-map.json"] = jbytes(bundle)
    files[SOURCES + "README.md"] = """# Bundled v0.27 evidence

Seventeen original carrier images are authenticated by exact SHA-256, size and
dimensions. Fourteen numbered filename assets from the 31-entry imported media
manifest were outside this acquisition and are not bundled here.

Five archived author pages support the conditional key derivation. Their text
is normalized to LF for portability, checked against the recorded LF hashes.
The original Windows read hashes are retained in the source records. This is
archived source support, not a new live retrieval during packaging.

`bundle-map.json` maps original repository paths to standalone package paths,
with input and bundled hashes. The evidence reports retain their historical
repository path references; resolve those through this map. Repository tool
copies document reproducibility and are intended to run from their original
repository layout. The standalone verifier is `05_method/verify_rune_code_state.py`.
""".encode()

    reviewed = json.loads(files[EVIDENCE + "reviewed-decisions.json"])
    initial = json.loads(files[EVIDENCE + "comparison-decisions.json"])
    observed = {r["page"]: r for r in json.loads(files[EVIDENCE + "independent-observations.json"])["carriers"]}
    code = table(parent["01_inventory/code_register.csv"])
    by_id = {r["page_id"]: r for r in code}
    fingerprints = {r["page_id"]: r for r in table(parent["01_inventory/rune_code_carrier_fingerprints.csv"])}
    records = {}
    for page, decision in reviewed["decisions"].items():
        records[page] = dict(decision, title=by_id[page]["title"], post=observed[page]["post"],
                             source_sha256=fingerprints[page]["source_sha256"],
                             inherited_seed_status=by_id[page]["decoding_status"],
                             initial_recommendation=initial[page],
                             rows=decision.get("reviewed_rows", observed[page]["rows"]))
    records["P005"] = {
        "title": "Loop", "post": "loop", "disposition": "conditional-key", "reading": None,
        "source_sha256": fingerprints["P005"]["source_sha256"],
        "inherited_seed_status": by_id["P005"]["decoding_status"],
        "qualification": "29-cell candidate agrees with inherited table; direct independent reconstruction remains incomplete. Conditional continuation authorized; four assignments separately supported by authored grouping/stanza evidence. Gate 0 Outcome B is not asserted."
    }
    for page, record in records.items():
        reading = record["reading"] or ("inscription present; untranscribed" if page == "P261" else "conditional key")
        record["current_status"] = f"v0.27 {record['disposition']}: {reading}. {record['qualification']}"
        by_id[page]["decoding_status"] = record["current_status"]
    registry = {"version": VERSION, "release_status": "local candidate; not published",
                "parent_zip_sha256": PARENT_SHA, "key_basis": reviewed["key_basis"],
                "conditional_coordinates": reviewed["conditional_coordinates"],
                "authority": reviewed["authority"], "records": records}
    put(REGISTRY, jbytes(registry))
    put("01_inventory/code_register.csv", csvbytes(code))
    verified = table(parent["01_inventory/verified_page_register.csv"])
    for row in verified:
        if row["id"] in records:
            row["status_note"] = records[row["id"]]["current_status"] + " See " + REGISTRY
    put("01_inventory/verified_page_register.csv", csvbytes(verified))
    claims = table(parent["04_registers/claims_evidence_register.csv"])
    superseded = {"C075": "P109", "C082": "P125", "C136": "P189", "C206": "P189",
                  "C222": "P209", "C223": "P229", "C225": "P046", "C226": "P055",
                  "C229": "P109", "C230": "P241", "C231": "P125", "C233": "P109",
                  "C234": "P005", "C235": "P161", "C236": "P109"}
    require(set(superseded) <= {r["claim_id"] for r in claims}, "missing historical claim IDs")
    for row in claims:
        if row["claim_id"] in superseded:
            page = superseded[row["claim_id"]]
            row["current_assessment"] = "historical v0.26.2 assessment: " + row["current_assessment"] + "; current authority V027-" + page
            row["next_check"] = "Use " + REGISTRY + " entry " + page + "; original wording retained in v0.26.2-history"
    for page, record in records.items():
        claims.append(dict(claim_id="V027-" + page, claim=record["current_status"], claimant="bounded v0.27 comparison and requested review",
                           evidence_location=REGISTRY + " entry " + page, evidence_class="authenticated pixels; qualified interpretation under conditional key",
                           current_assessment=record["disposition"], next_check=record["qualification"]))
    put("04_registers/claims_evidence_register.csv", csvbytes(claims))
    for page, record in records.items():
        base = "07_capture/" + record["post"] + "/"
        banner = (f"# v0.27 current authority — {record['title']}\n\n{record['current_status']}\n\n"
                  f"See [current adjudication](../../{REGISTRY}). The inherited text below is a historical source and analysis record. "
                  "Its transcription conclusions are superseded by the qualified entry above; source quotations remain source quotations.\n\n"
                  "## Inherited v0.26.2 record\n\n")
        for name in ("record.md", "notes.md"):
            if base + name in parent:
                put(base + name, banner + parent[base + name].decode("utf-8-sig"))
        if base + "claims.csv" in parent:
            page_claims = table(parent[base + "claims.csv"])
            for row in page_claims:
                row["v027_authority"] = "Historical claim/assessment; current transcription: " + REGISTRY + " entry " + page
            put(base + "claims.csv", csvbytes(page_claims))
    questions = table(parent["01_inventory/open_questions.csv"])
    q7 = next(r for r in questions if r["id"] == "OQ007")
    q7.update(status="17_named_carriers_authenticated_and_bundled", blocking_condition="none for 17 named carriers; 14 numbered assets remain imported hash attestations",
              allowed_next_action="Verify bundled originals using 05_method/verify_rune_code_state.py",
              not_a_fix_because="Byte authentication does not establish transcription correctness or pass independent key reconstruction")
    for page in ("P005", "P161", "P209", "P125", "P055", "P109", "P261"):
        questions.append(dict(id="OQ027-" + page, question="What evidence would resolve the remaining limit for " + records[page]["title"] + "?",
                              status="open_research_limit", blocking_condition=records[page]["qualification"],
                              allowed_next_action="A later bounded source or feature review; preserve the current alternatives until distinguishing evidence is found",
                              not_a_fix_because="Explicit research uncertainty is not a packaging defect and must not be replaced by semantic completion"))
    put("01_inventory/open_questions.csv", csvbytes(questions))

    landing = f"""# Letters for Titles — v{VERSION} candidate

Prepared: 2026-09-13. Status: local candidate, not merged, tagged or published.
Published parent remains v0.26.2 (ZIP SHA-256 `{PARENT_SHA}`).

This candidate integrates all nine carrier disputes together and the separate
Octave classification, using the authorized conditional key. Direct independent
Loop reconstruction remains incomplete; Gate 0 Outcome B is not asserted.

## Current authority

Read `{REGISTRY}`, then `05_method/v0.27-evidence/review-integration.md` and
`unresolved-review.md`. The initial `comparative-pass.md` and frozen observations
remain inspectable history. Updated code and verified-page registers follow the
reviewed decisions. Untouched carriers retain inherited assessments; they were
authenticated but not independently re-transcribed in this pass.

- Harvest supported: Axaxaxas, Always, The Way.
- Seed supported: For Anybody Who Rests With Them.
- Neither historical full reading: It Never Deceives (literal GUARDIAT),
  You Knew it Beforehand (WHAT IS OUR FATE? / CHEER UP IT IS DEATH),
  Soon After it Becomes Water (SAE or SHH / LET / US / MELT).
- Traversal unresolved: Œdipean Riddle and Shh.
- Octave: inscription present, untranscribed; classification only.

GUARDIAT retains its stated grouping rule and weaker alternative. The skull
reading retains medium confidence and its inferred bone/hair rule. Ice retains
both segmentations. Conditional coordinates 2.6, 2.7, 2.8 and 3.7 are separately
supported by authored stanza/grouping evidence, not direct reading of hidden ink.

## Evidence and history

Seventeen authenticated original images and five archived author pages are
bundled under `06_sources/v0.27/`; its bundle map resolves repository references.
Every changed inherited file has a byte-exact snapshot under
`05_method/v0.26.2-history/`. Existing versioned method reports are historical.
Capture banners and claim pointers distinguish inherited analysis from current
adjudication; original claim wording is preserved. The old README in that history
retains the broader project orientation and directory map.

Keep source, observation, attribution, interpretation and uncertainty distinct.
Do not infer authorial intent from grammatical fluency. All retained parent
media bytes, the 31-record imported source manifest and archive membership remain
unchanged. New source files are separately identified additions.

## Checks and next boundary

Run `python -X utf8 -B 05_method/verify_rune_code_state.py` and
`python -X utf8 -B 05_method/verify_cipher_letter_run.py` from the extracted package.
Manifest/path checks and exact parent delta are recorded in the validation report
and `05_method/v0.27-parent-delta.json`. Open research limits are in
`01_inventory/open_questions.csv`. Verification checks evidence identity and
record consistency; it does not automate visual judgment.

Review this complete candidate before canonical import and release publication.
Do not repeat the completed comparison or fill Octave's transcription by inference.
"""
    for path in ("README.md", "CODEX_HANDOFF.md", "CLAUDE_HANDOFF.md", "05_method/reentry_capsule.md"):
        put(path, landing)
    for path, heading in (("CHANGELOG.md", "v0.27.0 candidate — qualified cross-lineage adjudication"),
                          ("05_method/lineage_log.md", "v0.27.0 candidate lineage"),
                          ("06_sources/source_notes.md", "v0.27 evidence addition")):
        put(path, f"# {heading}\n\nPrepared 2026-09-13 from published v0.26.2; local candidate only.\n\n"
            f"Parent SHA-256: `{PARENT_SHA}`. See README.md and `{REGISTRY}` for current scope, "
            "qualifications and evidence. All earlier entries below retain their historical date and authority.\n\n"
            + parent[path].decode("utf-8-sig"))
    put("05_method/version_control_protocol.md", "# v0.27 staging status\n\n"
        "Published parent: v0.26.2. This package is an isolated v0.27.0 candidate, not a published successor. "
        "The protocol below remains mandatory; its closing version line is historical v0.26.2 text.\n\n"
        + parent["05_method/version_control_protocol.md"].decode("utf-8-sig"))
    put("05_method/verify_rune_code_state.py", lf((ROOT / "tools/verify_v027_candidate_state.py").read_bytes()))

    modified = sorted(p for p in parent if p != "MANIFEST.sha256" and files[p] != parent[p])
    allowed = {"README.md", "CHANGELOG.md", "CODEX_HANDOFF.md", "CLAUDE_HANDOFF.md",
               "01_inventory/code_register.csv", "01_inventory/verified_page_register.csv", "01_inventory/open_questions.csv",
               "04_registers/claims_evidence_register.csv", "05_method/verify_rune_code_state.py", "05_method/reentry_capsule.md",
               "05_method/lineage_log.md", "05_method/version_control_protocol.md", "06_sources/source_notes.md"}
    allowed |= {"07_capture/" + r["post"] + "/" + name for r in records.values() for name in ("record.md", "notes.md", "claims.csv")}
    require(set(modified) <= allowed, "unscoped parent modification")
    require(all(files[p] == b for p, b in parent.items() if Path(p).suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".webp"}), "parent image changed")
    require(files["01_inventory/rune_code_source_media.json"] == parent["01_inventory/rune_code_source_media.json"], "imported manifest changed")
    delta = {"parent_zip_sha256": PARENT_SHA, "parent_payload_hashes": {p: sha(b) for p, b in parent.items()},
             "modified_parent_files": modified, "history_prefix": HISTORY,
             "added_files_except_delta_manifest_validation": sorted(set(files) - set(parent))}
    files["05_method/v0.27-parent-delta.json"] = jbytes(delta)
    csv_count = 0
    for path, content in files.items():
        if path.endswith(".csv"):
            rows = [r for r in csv.reader(io.StringIO(content.decode("utf-8-sig"), newline="")) if r]
            require(bool(rows) and all(len(r) == len(rows[0]) for r in rows), "nonrectangular CSV: " + path)
            csv_count += 1
    with tempfile.TemporaryDirectory(prefix="v027-build-", dir=DIST) as tmp:
        tree = Path(tmp) / PREFIX.rstrip("/")
        for path, content in files.items():
            dest = tree / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(content)
        logs = run_verifiers(tree)
        report = f"""# v0.27.0 candidate validation

Prepared 2026-09-13. Not a publication record.
Parent SHA-256: `{PARENT_SHA}`.

- Exact published parent ZIP CRC, path safety, manifest and canonical seed equality: pass.
- {len(modified)} modified parent files, each with a byte-exact history snapshot.
- No parent path deleted; retained images and imported 31-record media manifest unchanged.
- 17 bundled originals authenticated by hash, bytes and dimensions; 5 authored HTML sources by portable LF hash.
- {csv_count} rectangular CSVs, including preserved history and key table.
- All nine disputes plus Octave classification imported together; Loop remains conditional.
- Candidate generation never writes the canonical seed.

```text
{logs}
```

The builder then regenerates the manifest, creates a deterministic ZIP, verifies
CRC, exact bytes, path-set equality and every payload hash, and runs both verifiers
in a second clean extraction. Final counts and ZIP hash are outside the payload
in RELEASE-v0.27.0.md to avoid self-reference. These checks validate record and
byte integrity, not the correctness of a visual interpretation.
"""
        files["05_method/release_validation_v0.27.0.md"] = report.encode("utf-8")
        files["MANIFEST.sha256"] = "".join(f"{sha(b)}  ./{p}\n" for p, b in sorted(files.items()) if p != "MANIFEST.sha256").encode()
        verify_manifest(files)
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for path, content in sorted(files.items()):
                info = zipfile.ZipInfo(PREFIX + path, date_time=(2026, 9, 13, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, content)
        raw_zip = buffer.getvalue()
        with zipfile.ZipFile(io.BytesIO(raw_zip)) as z:
            require(z.testzip() is None, "candidate ZIP CRC failure")
            require(set(z.namelist()) == {PREFIX + p for p in files}, "ZIP path-set mismatch")
            require(all(z.read(PREFIX + p) == b for p, b in files.items()), "ZIP byte mismatch")
            clean = Path(tmp) / "clean"
            z.extractall(clean)
        extracted = clean / PREFIX.rstrip("/")
        extracted_files = {p.relative_to(extracted).as_posix(): p.read_bytes() for p in extracted.rglob("*") if p.is_file()}
        require(extracted_files == files, "clean extraction differs")
        verify_manifest(extracted_files)
        run_verifiers(extracted)
        require({p.relative_to(ROOT / "corpus-seed").as_posix(): p.read_bytes()
                 for p in (ROOT / "corpus-seed").rglob("*") if p.is_file()} == live_seed, "canonical seed mutated")
        # Exclusive creation: never overwrite a versioned package.
        with TARGET.open("xb") as handle:
            handle.write(raw_zip)
        shutil.copytree(extracted, TREE)
    digest = sha(raw_zip)
    TARGET.with_suffix(".zip.sha256").write_text(f"{digest}  {TARGET.name}\n", encoding="utf-8", newline="\n")
    summary = f"""# v0.27.0 local release candidate

Prepared and validated: 2026-09-13. Not imported, merged, tagged or published.
Published v0.26.2 and `corpus-seed/` remain unchanged.

Candidate: [ZIP](dist/{TARGET.name}) · [checksum](dist/{TARGET.name}.sha256)
Extracted candidate: `dist/v027-candidate/letters_for_titles_corpus_seed/`.
SHA-256: `{digest}`
Parent SHA-256: `{PARENT_SHA}`

The candidate incorporates the initial checkpoint `de9790c` and review addendum
`0b3a76e` together. All nine disputed carriers receive qualified dispositions;
Octave is classified as inscription-present without transcription. Loop remains
conditional, with four assignments supported by separate authored evidence.

Three readings favor harvest, one favors seed, three favor neither historical
full reading, and two remain traversal-unresolved. P125 retains SAE/SHH alternatives;
P055 literal GUARDIAT and P109's skull-derived DEATH retain feature-rule qualifications.
See [reviewed decisions](research/v0.27/reviewed-decisions.json) and
[review integration](research/v0.27/review-integration.md).

## Verification

- {len(files)} files; {len(files)-1} manifest hashes; {csv_count} rectangular CSVs.
- ZIP CRC, safe single root, exact clean-extraction bytes and manifest path set: pass.
- Candidate state and 74/74 filename verifier: pass in construction and clean extraction.
- {len(modified)} modified parent files, all retained byte-exact under `05_method/v0.26.2-history/`.
- Every retained parent image and all canonical seed bytes unchanged.
- 17 original images bundled and authenticated; 5 source HTML texts bundled and LF-hash verified.
- Repository input paths and exact/normalized identities are mapped inside the package.
- Historical reports are preserved; active code/page/claim registers identify the new authority.

Validation checks bytes and consistency, not visual interpretation correctness.
Open research limits are recorded and do not imply a fully solved corpus.

## Next release boundary

Review this complete candidate, then authorize its canonical import and publication.
The versioned ZIP is immutable; do not overwrite it. If a defect is found, resolve
candidate lineage under the version protocol before preparing a replacement.

## Modified parent files

""" + "\n".join("- `" + p + "`" for p in modified) + "\n"
    (ROOT / "RELEASE-v0.27.0.md").write_text(summary, encoding="utf-8", newline="\n")
    print(f"PASS: {len(files)} files; {len(files)-1} hashes; {len(modified)} modified parent files; {csv_count} CSVs")
    print(f"ZIP SHA-256: {digest}")
    print(logs)


if __name__ == "__main__":
    main()
