# Repository lineages

This repository contains two complementary representations of **Letters for Titles**. They are kept together so ChatGPT, Claude, and human reviewers can work from one shared state, but they do not have the same evidentiary role.

## Canonical corpus seed

Path: `corpus-seed/`

- Imported payload (publication pending): `letters_for_titles_corpus_seed_v0.27.0.zip`
- ZIP SHA-256: `72c85305702f1074598c6f8f0285c41ad19f19d71011a1880c9eb0cc78753b1a`
- Parent: `letters_for_titles_corpus_seed_v0.26.2.zip`
- Parent SHA-256: `cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75`

The seed is the canonical evidence and provenance record. It contains page-level capture folders, inventories, claims and correspondence registers, structural reconstructions, source packets, validation scripts, release reports, and its cumulative lineage log.

`corpus-seed/` reproduces the approved v0.27.0 payload: 1,521 files and 1,520
manifest hashes. All 46 modified parent files retain byte-exact historical copies.
The owner authorized import and publication on 2026-09-14; CI, merge and publication
are pending. See [release record](RELEASE-v0.27.0.md). Preparation-time candidate
wording inside the immutable package is historical; subsequent release status
belongs outside the seed so its manifest remains valid.

## Full-site harvest and derived research

The original harvest readings remain historical evidence. The v0.27.0 register
records qualified dispositions for nine disputes, Octave classification and the
conditional Loop key. It does not assert complete decoding or Gate 0 Outcome B.

Paths: `archive/`, `data/`, `book/`, `research/`, and `tools/`

These paths contain the 262-post site harvest, rendered pages and image references, full-resolution checksum manifests, the assembled Rune Poem, derived structural and cipher analysis, and reproducible harvesting and decoding tools.

This layer can independently confirm, extend, or challenge corpus-seed claims. It does not retroactively rewrite the imported evidence record.

## Authority rule

- Use `corpus-seed/` for acquisition provenance, page-level evidence states, registered claims, release history, and bounded uncertainty.
- Use the harvest and research paths for complete-site enumeration, reproducible derivations, full-resolution media checks, assembled editions, and analytical synthesis.
- When the two disagree, record the disagreement and resolve it through a new reviewed commit or corpus release. Do not silently choose one representation and erase the other.

The standing record of those disagreements is [`CROSS-LINEAGE-FINDINGS.md`](CROSS-LINEAGE-FINDINGS.md). It is an evidence ledger: entries are added when a conflict is found and struck only when a release adjudicates them. The approved v0.27.0 import records all nine dispositions together; its unresolved traversal, segmentation and feature-rule qualifications remain binding. Cite its current register with those qualifications rather than treating historical plaintext as settled.

## Update rule

Future corpus releases update the stable `corpus-seed/` paths on a dedicated integration branch. Before merging:

1. identify and checksum the exact canonical parent and candidate ZIP;
2. verify ZIP integrity and the internal `MANIFEST.sha256`;
3. run the release's state verifiers;
4. inspect the lineage log, changelog, re-entry capsule, and release validation;
5. review any interaction with the harvest/research layer;
6. merge only after the committed tree reproduces the release payload.

Each merged corpus release receives an annotated Git tag of the form `corpus-vX.Y.Z`, pointing at the import commit itself. Original ZIPs belong as release artifacts rather than repeated binary snapshots in the Git tree.

Releases are scoped by what they change:

- a **metadata/provenance patch** (`0.26.2`-style) carries factual corrections only — carrier dimensions, media registration, source-byte hashes, open-question statuses, canonical URLs. It changes no transcription.
- a **transcription adjudication** (`0.27.0`-style) rules on contested readings. Contested plates are adjudicated together in one bounded comparative pass, not one at a time.

## Enforcement

`tools/verify-corpus-seed.sh` is the mechanical guard on the boundary. It verifies every manifest hash, compares the manifest's path set against the actual tree — derived, never a hardcoded count, so a differently sized future release still passes — and runs both of the release's state verifiers. `.github/workflows/lineage-integrity.yml` runs it on every push, alongside a check that the harvest layer's generators still reproduce their committed output.

The guard lives outside `corpus-seed/` by necessity: anything inside that tree would have to appear in the manifest it checks. The same constraint applies to corrections. An in-place edit to `corpus-seed/` breaks the release payload and fails CI; a correction either lands outside the tree or arrives as a new release with a regenerated manifest.

## Model roles

Codex owns acquisition integration, validation, and release numbering. Claude may perform bounded review or independent tests against named evidence packets. Review findings enter through separate branches or commits and do not initiate a competing corpus lineage.
