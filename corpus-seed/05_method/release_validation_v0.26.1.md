# Release Validation — 0.26.1

Date: 2026-08-30  
Scope: Rune Code quality-assurance correction with no new decipherment or structural acquisition

## Lineage

- supplied canonical parent: `letters_for_titles_corpus_seed_v0.26.0.zip`
- supplied canonical parent SHA-256: `3f9b2c307b4763d97bfdfcbb801cf9ee575242595bf3eaf7bfbbac1a09f814a0`
- release semantics: patch correction and evidence-preserving provenance refinement
- historical release reports: preserved as dated states except for the factual upper-field unit-count correction in the 0.24.0 report

## Rune Code QA

| Check | Result |
|---|---:|
| Rune Code archive entries classified | 17 / 17 |
| Ordered page-local inscriptions | 14 |
| Complete question-and-rebus carriers | 1 |
| Key carriers | 2 |
| Rune Code entries with opaque, unresolved, or untranscribed current status | 0 |
| *You Knew it Beforehand* upper coordinate-valued units | 12 |
| *You Knew it Beforehand* upper direct marks | Roman `K`; `?` |
| Carrier-fingerprint register rows | 17 / 17 |
| Exact retained source-byte SHA-256 values | 3 |
| Browser-rendered visual fingerprints | 16 |
| Continuous Rune Code text asserted | no |

Visual fingerprints are SHA-256 hashes of browser-rendered 1363 × 936 viewport JPEGs, not hashes of the served media bytes. The animated carrier fingerprint covers one captured rendered state rather than the complete GIF.

## Corpus integrity checks

| Check | Result |
|---|---:|
| Registered evidence rows | 286 |
| Registered unique URLs | 278 |
| Registered content URLs with capture folders | 263 / 263 pass |
| Capture folders | 263 |
| Required files in capture folders | 263 / 263 pass |
| CSV files parsed and rectangular | 812 / 812 pass |
| Central claim IDs | 238 / 238 unique |
| Correspondence IDs | 203 / 203 unique |
| Local capture claim IDs | 473 / 473 unique |
| Rune Code state verifier | pass |
| Local folded-message tokens | 74 / 74 pass |
| Cipher verifier failures | 0 |
| Release-tree files | 1,416 |
| Payload files covered by manifest | 1,415 |

`MANIFEST.sha256` excludes itself. Manifest verification, ZIP CRC, single-root verification, and clean-extraction manifest verification are performed after all content is final.

## Scope boundary

No Rune Code plaintext, coordinate path, archive membership, page path, chapter braid, capture folder, retained media payload, archive count, source chronology, or filename-run result changes. The patch corrects one accounting statement, synchronizes current-state records, and improves future visual-change detection without claiming unavailable source-byte provenance.
