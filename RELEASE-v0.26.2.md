# v0.26.2 release record

Prepared and validated: 2026-09-12
Branch: `corpus-v0.26.2-integration`
Status: merged through [PR #7](https://github.com/eternal-highway/mysterywyrm/pull/7) and [published](https://github.com/eternal-highway/mysterywyrm/releases/tag/corpus-v0.26.2) on 2026-09-12 at 15:04:41 UTC.
Import commit: `a493e074b115760fb488d71698830773d1811c17`
Merge commit: `c12cc65ded218ceca32499e1a2d0097161082f39`
Annotated tag: `corpus-v0.26.2`, pointing to the import commit.

Release ZIP (local copy): `dist/letters_for_titles_corpus_seed_v0.26.2.zip`
SHA-256: `cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75`
Parent SHA-256: `ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327`

## Result

The candidate corrects Loop/Œ source dimensions and media URLs, registers Octave's image, imports all 31 source-byte hash attestations, adds 262 day-level publication records, updates OQ001/OQ003/OQ007 and corrects Translating Is to `/translating-ice/`. Its readings and retained media are unchanged from v0.26.1.

The pre-existing one-frame local GIF is preserved under ignored `local-recovery/`; canonical AS001 was restored from the parent ZIP and again has six frames. Its source is unknown.

## Verification

- 1420 files; 1419 payload hashes; complete path-set agreement.
- ZIP CRC, single root, all extracted bytes, manifest hashes, and clean-extraction seed verifiers: pass.
- 813 rectangular CSVs; code register and every retained media file identical to parent.
- Seed filename check: 74/74; full harvest: 211/211 direct characters, seven context-supplied characters.
- Site structure derivation: pass under Python UTF-8 mode. Initial Windows default-codepage execution failed; no source change was needed.
- 31 imported hash identities agree with the full harvest manifest; full-resolution media not present locally or re-fetched.
- Canonical URL supported by archived canonical tag and harvest. Live retrieval failed; no new live capture claimed.

## Release delta (23 files)

- `corpus-seed/01_inventory/harvest_publication_dates.csv`
- `corpus-seed/01_inventory/open_questions.csv`
- `corpus-seed/01_inventory/rune_code_carrier_fingerprints.csv`
- `corpus-seed/01_inventory/rune_code_source_media.json`
- `corpus-seed/01_inventory/translation_register.csv`
- `corpus-seed/01_inventory/verified_page_register.csv`
- `corpus-seed/02_structure/core_stream_alignment.csv`
- `corpus-seed/05_method/lineage_log.md`
- `corpus-seed/05_method/metadata_provenance_v0.26.2.md`
- `corpus-seed/05_method/reentry_capsule.md`
- `corpus-seed/05_method/release_validation_v0.26.2.md`
- `corpus-seed/05_method/rune_code_plate_reconciliation_v0.26.0.md`
- `corpus-seed/05_method/verify_rune_code_state.py`
- `corpus-seed/05_method/version_control_protocol.md`
- `corpus-seed/06_sources/source_notes.md`
- `corpus-seed/07_capture/stanza-11-ice/links.csv`
- `corpus-seed/07_capture/translating-eh/links.csv`
- `corpus-seed/07_capture/translating-is/record.md`
- `corpus-seed/CHANGELOG.md`
- `corpus-seed/CLAUDE_HANDOFF.md`
- `corpus-seed/CODEX_HANDOFF.md`
- `corpus-seed/MANIFEST.sha256`
- `corpus-seed/README.md`

## Publication verification and next boundary

Both lineage-integrity jobs passed on the integration branch and pull request before merge. GitHub's uploaded ZIP digest equals the SHA-256 above; the checksum sidecar is also published. The release is neither draft nor prerelease. All 1,420 files in the import commit match the packaged ZIP byte-for-byte.

Preparation-time candidate wording inside the immutable seed ZIP is historical and is superseded for publication status by this record. The original package and manifest have not been rewritten after approval.

v0.26.2's prerequisite work is complete. The next research step is v0.27 Gate 0: authenticate the Loop source bytes and independently reconstruct its 29 key cells before the bounded comparative adjudication. Gate 0, the nine disputed readings, and the separate Octave classification question remain untouched.
