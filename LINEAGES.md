# Repository lineages

This repository contains two complementary representations of **Letters for Titles**. They are kept together so ChatGPT, Claude, and human reviewers can work from one shared state, but they do not have the same evidentiary role.

## Canonical corpus seed

Path: `corpus-seed/`

Imported release: `letters_for_titles_corpus_seed_v0.26.1.zip`  
ZIP SHA-256: `ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327`  
Parent: `letters_for_titles_corpus_seed_v0.26.0.zip`  
Parent SHA-256: `3f9b2c307b4763d97bfdfcbb801cf9ee575242595bf3eaf7bfbbac1a09f814a0`

The seed is the canonical evidence and provenance record. It contains page-level capture folders, inventories, claims and correspondence registers, structural reconstructions, source packets, validation scripts, release reports, and its cumulative lineage log.

The imported `corpus-seed/` tree is byte-for-byte the extracted v0.26.1 payload. Its internal `MANIFEST.sha256` covers 1,415 payload files and excludes only itself. Repository documentation belongs outside that tree so the release manifest remains valid.

## Full-site harvest and derived research

Paths: `archive/`, `data/`, `book/`, `research/`, and `tools/`

These paths contain the 262-post site harvest, rendered pages and image references, full-resolution checksum manifests, the assembled Rune Poem, derived structural and cipher analysis, and reproducible harvesting and decoding tools.

This layer can independently confirm, extend, or challenge corpus-seed claims. It does not retroactively rewrite the imported evidence record.

## Authority rule

- Use `corpus-seed/` for acquisition provenance, page-level evidence states, registered claims, release history, and bounded uncertainty.
- Use the harvest and research paths for complete-site enumeration, reproducible derivations, full-resolution media checks, assembled editions, and analytical synthesis.
- When the two disagree, record the disagreement and resolve it through a new reviewed commit or corpus release. Do not silently choose one representation and erase the other.

## Update rule

Future corpus releases update the stable `corpus-seed/` paths on a dedicated integration branch. Before merging:

1. identify and checksum the exact canonical parent and candidate ZIP;
2. verify ZIP integrity and the internal `MANIFEST.sha256`;
3. run the release's state verifiers;
4. inspect the lineage log, changelog, re-entry capsule, and release validation;
5. review any interaction with the harvest/research layer;
6. merge only after the committed tree reproduces the release payload.

Each merged corpus release receives a Git tag of the form `corpus-vX.Y.Z`. Original ZIPs belong as release artifacts rather than repeated binary snapshots in the Git tree.

## Model roles

Codex owns acquisition integration, validation, and release numbering. Claude may perform bounded review or independent tests against named evidence packets. Review findings enter through separate branches or commits and do not initiate a competing corpus lineage.
