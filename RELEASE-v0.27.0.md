# v0.27.0 release record

Prepared and validated: 2026-09-13. Owner approved import and publication on
2026-09-14. The exact candidate is now imported on the integration branch;
merge, tag and publication await passing CI.

Candidate: [ZIP](dist/letters_for_titles_corpus_seed_v0.27.0.zip) · [checksum](dist/letters_for_titles_corpus_seed_v0.27.0.zip.sha256)
Extracted candidate: `dist/v027-candidate/letters_for_titles_corpus_seed/`.
SHA-256: `72c85305702f1074598c6f8f0285c41ad19f19d71011a1880c9eb0cc78753b1a`
Parent SHA-256: `cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75`

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

- 1521 files; 1520 manifest hashes; 829 rectangular CSVs.
- ZIP CRC, safe single root, exact clean-extraction bytes and manifest path set: pass.
- Candidate state and 74/74 filename verifier: pass in construction and clean extraction.
- 46 modified parent files, all retained byte-exact under `05_method/v0.26.2-history/`.
- Every retained parent image unchanged; canonical import equals the approved ZIP exactly.
- 17 original images bundled and authenticated; 5 source HTML texts bundled and LF-hash verified.
- Repository input paths and exact/normalized identities are mapped inside the package.
- Historical reports are preserved; active code/page/claim registers identify the new authority.

Validation checks bytes and consistency, not visual interpretation correctness.
Open research limits are recorded and do not imply a fully solved corpus.

## Next release boundary

Independent pre-import review, 2026-09-14: pass. The existing ZIP, fresh
extraction, 1,520 hashes, both verifiers and exact parent delta were rechecked.
See [release handoff](research/v0.27/release-handoff.md) and
[machine-readable preflight](research/v0.27/release-preflight.json) for the
verified identity, remote checkpoint and prepared PR/release text.

Owner authorization received 2026-09-14. Next: verify committed-tree equality,
pass CI, merge, tag the import commit and publish the approved immutable assets.
The versioned ZIP is immutable; do not overwrite it. If a defect is found, resolve
candidate lineage under the version protocol before preparing a replacement.

## Modified parent files

- `01_inventory/code_register.csv`
- `01_inventory/open_questions.csv`
- `01_inventory/verified_page_register.csv`
- `04_registers/claims_evidence_register.csv`
- `05_method/lineage_log.md`
- `05_method/reentry_capsule.md`
- `05_method/verify_rune_code_state.py`
- `05_method/version_control_protocol.md`
- `06_sources/source_notes.md`
- `07_capture/always/claims.csv`
- `07_capture/always/notes.md`
- `07_capture/always/record.md`
- `07_capture/axaxaxas-mlo/claims.csv`
- `07_capture/axaxaxas-mlo/notes.md`
- `07_capture/axaxaxas-mlo/record.md`
- `07_capture/for-anybody-who-rests-with-them/claims.csv`
- `07_capture/for-anybody-who-rests-with-them/notes.md`
- `07_capture/for-anybody-who-rests-with-them/record.md`
- `07_capture/it-never-deceives/claims.csv`
- `07_capture/it-never-deceives/notes.md`
- `07_capture/it-never-deceives/record.md`
- `07_capture/loop/claims.csv`
- `07_capture/loop/notes.md`
- `07_capture/loop/record.md`
- `07_capture/octave/claims.csv`
- `07_capture/octave/notes.md`
- `07_capture/octave/record.md`
- `07_capture/oe-is-for-oedipean-riddle/claims.csv`
- `07_capture/oe-is-for-oedipean-riddle/notes.md`
- `07_capture/oe-is-for-oedipean-riddle/record.md`
- `07_capture/shh/claims.csv`
- `07_capture/shh/notes.md`
- `07_capture/shh/record.md`
- `07_capture/soon-after-it-becomes-water/claims.csv`
- `07_capture/soon-after-it-becomes-water/notes.md`
- `07_capture/soon-after-it-becomes-water/record.md`
- `07_capture/the-way/claims.csv`
- `07_capture/the-way/notes.md`
- `07_capture/the-way/record.md`
- `07_capture/you-knew-it-beforehand/claims.csv`
- `07_capture/you-knew-it-beforehand/notes.md`
- `07_capture/you-knew-it-beforehand/record.md`
- `CHANGELOG.md`
- `CLAUDE_HANDOFF.md`
- `CODEX_HANDOFF.md`
- `README.md`
