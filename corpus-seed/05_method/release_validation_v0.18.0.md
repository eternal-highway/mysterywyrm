# Release Validation — 0.18.0

Date: 2026-08-28  
Scope: bounded cipher reconciliation for *IO is for I/O*, *COW*, and *Night Riddle*; canonical AS001 negative control; corpus integrity and lineage

## Lineage

- immutable 0.17.0 parent SHA-256: `782c9d1665d2ac851c96f4190bb76e4c4abe08a2a7f2a688f33e21bc86d3768e`
- parent ZIP integrity: pass
- release semantics: exact page-local cipher outputs, bounded reproduction evidence, frame-level negative control, and updated current-state handoff
- chapter acquisition semantics: unchanged from 0.17.0

## Cipher checks

| Check | Result |
|---|---:|
| I/O normalized bitstream SHA-256 | `0efe29f4532adfb38a48db45a2f981594fb26487de449fdd028c2e0de45130b8` |
| I/O decoded length | 79 bytes |
| I/O trailing encoded space | preserved |
| COW normalized program SHA-256 | `026626cdde6af5359789dd24c2bfea44a30682db8d789a98855f49695ffb4708` |
| COW tokens | 6,086 |
| COW loop pairs | 317 / 317 balanced |
| COW execution | normal halt after 83,144 steps under 10,000,000-step cap |
| COW input / integer-output / dynamic-execution commands | 0 / 0 / 0 |
| COW output terminator | two newline bytes preserved |
| Night Riddle lineation | 5 lines; 12 / 8 / 7 / 6 / 5 characters including spaces and final `?` |
| Night Riddle method | symbol-by-symbol Carroll Nyctographic Square Alphabet transcription |
| Shared master decoder | rejected; three distinct mechanisms |
| AS001 SHA-256 | `20fd510698180bc1e36a3bae2ebcf769341e45cd15e7d21f093c9b89ef400910` |
| AS001 technical state | 360 × 360; 6 frames; 10 cs each; infinite loop |
| AS001 plaintext or frame key | none mechanically supported |

## Corpus checks

| Check | Result |
|---|---:|
| Completed reflected-pair braids | 14 / 14; unchanged |
| Middle status | 2 observed paths; completeness open |
| Archive/navigation audit state | unchanged from 0.17.0 |
| Capture folders | 252 |
| Required files in capture folders | 252 / 252 pass |
| Capture canonical URLs registered | 252 / 252 |
| Registered URLs without capture folders | 14; reconciliation ledger exact |
| Verified-page evidence rows | 274 |
| Verified-page unique URLs | 266 |
| Intentional duplicated-lineage URLs | 8 |
| CSV files parsed and rectangular | 771 / 771 |
| Central claim identifiers unique | 199 / 199 |
| Correspondence identifiers unique | 175 / 175 |
| Local capture-claim identifiers unique | 424 / 424 |
| Release-tree files | 1,331 |
| Payload files covered by manifest | 1,330 |

All CSV checks ignore empty spacer rows and require every substantive row to match its header width. All capture folders contain `record.md`, `links.csv`, `media.csv`, `claims.csv`, and `notes.md`. Central claim, correspondence, and local capture-claim identifiers are unique. The register/capture comparison matches its fourteen-row reconciliation ledger exactly.

The three plaintexts were reproduced only from their page-local media and identified mechanisms. Semantics were applied after exact output, not used to guess it. Unrelated code pages remain unresolved. `MANIFEST.sha256` excludes itself. Manifest verification, ZIP CRC, single archive-root verification, and clean-extraction manifest verification are performed after packaging.
