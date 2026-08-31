# Release Validation — 0.13.1

Date: 2026-08-26  
Status: historical validation; corrected current counts and classifications are in `release_validation_v0.13.2.md`  
Scope: final package polish and Claude handoff; no live-site acquisition

## Lineage

- canonical 0.12.0 input SHA-256: `55887e1e85eae240b38bade4f9483afb17c2b09db4ca9298fc7b48203228d230`
- immutable 0.13.0 parent SHA-256: `a67962a8ef377bc5c5fdc7c1131c33d7afa0432b948ec201a6f5a052607bb6b6`
- version semantics: 0.13.1 remains a correction and evidence-preserving audit patch; no chapter acquisition occurred after 0.13.0

The independent audit's 841-file statement concerns the two source bundles it ingested. The combined canonical 0.12.0 ZIP supplied for reconciliation contains 842 filesystem files. These are different count scopes; the branch audit remains preserved verbatim.

## Mechanical checks

| Check | Result |
|---|---:|
| Chapter structures reconstructed | 11 / 15 |
| Reflected-pair chapters reconstructed | 10 / 14 |
| Completed paired chapter path tables or sequences | 10 / 10 at 17 pages |
| Fixed `2 + 2 + 9 + 2 + 2` envelopes | 10 / 10 |
| Eponymous *Duets* hinges at position 9 | 10 / 10 |
| Paired-stream archive-order checks | 40 / 40 pass |
| Capture folders | 177 |
| Required files present per capture folder | 177 / 177 |
| Unique capture canonical URLs | 177 |
| Capture canonical URLs present in verified-page register | 177 / 177 |
| Verified-page evidence rows | 204 |
| Verified-page unique URLs | 198 |
| Intentional duplicated URLs | 6 |
| Broken supersession references | 0 |
| Duplicate identifiers in principal inventory registers | 0 |
| Malformed nonblank CSV records | 0 |
| Missing referenced local Markdown/CSV files | 0 |
| Release-tree files including manifest | 936 |
| Payload files covered by manifest | 935 |

Blank separator records remain in some capture CSVs from earlier releases; they do not contain data and all nonblank records conform to their local headers. Some early media manifests legitimately use a five-column schema with alt-text while later compact manifests use four columns.

## Register reconciliation

The polished handoff adds P199–P203 for five pages that already had complete capture folders and entries in their appropriate stream registers:

- Eolhx glyph;
- Dæg glyph;
- Rune Casting: Eolhx;
- Translating Ear;
- Translating Peorð.

This repairs register coverage only. Their original evidence dates and acquisition claims are unchanged.

## Integrity boundary

`MANIFEST.sha256` contains SHA-256 checksums for every other file in the release tree. The manifest excludes itself to avoid a self-referential checksum. ZIP CRC, manifest verification, file count, and archive-root checks must be rerun after final packaging; the published ZIP checksum belongs in the external handoff message because a file cannot contain the checksum of the ZIP that contains it without changing that checksum.
