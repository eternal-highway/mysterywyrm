# Release Validation — 0.19.0

Date: 2026-08-28  
Scope: Claude folded-letter and Rune Code integration; slot-32 / AS001 provenance repair; corpus integrity and lineage

## Lineage

- immutable 0.18.0 parent SHA-256: `eaa2fb6a28f4f555f8879edcc8f34d016ca68b7cd9788af548af211baa810550`
- parent ZIP integrity: pass
- supplied Claude handoff SHA-256: `f40a2cc32dc65d0170787a46fd5aca621f91fae5085eab63979b9ff0017a16f8`
- release semantics: independent cipher-branch reconciliation, two additional Rune plate readings, media provenance correction, and updated current-state handoff
- chapter acquisition semantics: unchanged from 0.18.0

## Cipher checks

| Check | Result |
|---|---:|
| Claude-reported folded message length | 261 characters |
| Claude-reported full-harvest numbered images | 216; repository absent and count remains attributed |
| Local numbered letter/punctuation tokens | 65 |
| Local comparison | 65 / 65 pass |
| Local comparison span | slots 102–252 |
| Documented local slip applied | served `142-M` mapped to slot 144 |
| Slot 32 | `?`; live 1000 × 1000 six-frame GIF |
| Live slot-32 GIF SHA-256 | `2fa10f8e9dd9027627316ca715e745085c0a08efd13fff5cdb085c2ca3d87b0c` |
| AS001 SHA-256 | `20fd510698180bc1e36a3bae2ebcf769341e45cd15e7d21f093c9b89ef400910` |
| AS001/source relation | resized/optimized derivative; 6 corresponding frames; equal 10 cs timing; normalized RMSE 0.01148–0.01167 after resize |
| Arrows source SHA-256 | `c6c740008d00d5778cb482c6acb8072ce109fb24589fc4deca52a1c23c2f48f0` |
| Arrows reading | 7 lines / 39 letters; complete group/place transcription |
| The Way source SHA-256 | `a10c4012955caad9088226a6ede0dc3446ea0e26573223d9f2e3258cb6b137a6` |
| The Way reading | 6 lines / 52 letters; complete group/place transcription |
| Present source SHA-256 | `c2e1c1abd6af4d4fe61dcd54456a07bb3b2325dc0cec710710df721e67f63f56` |
| Present reading | 4 words / 18 letters; complete group/place transcription |
| Continuous Rune Code text | not established; three page-local inscriptions |

## Corpus checks

| Check | Result |
|---|---:|
| Completed reflected-pair braids | 14 / 14; unchanged |
| Middle status | 2 observed paths; completeness open |
| Archive/navigation audit state | unchanged from 0.18.0 |
| Capture folders | 252 |
| Required files in capture folders | 252 / 252 pass |
| Capture canonical URLs registered | 252 / 252 |
| Registered URLs without capture folders | 14; reconciliation ledger exact |
| Verified-page evidence rows | 274 |
| Verified-page unique URLs | 266 |
| Intentional duplicated-lineage URLs | 8 |
| CSV files parsed and rectangular | 771 / 771 |
| Central claim identifiers unique | 208 / 208 |
| Correspondence identifiers unique | 181 / 181 |
| Local capture-claim identifiers unique | 427 / 427 |
| Release-tree files | 1,335 |
| Payload files covered by manifest | 1,334 |

All CSV checks ignore empty spacer rows and require every substantive row to match its header width. All capture folders contain `record.md`, `links.csv`, `media.csv`, `claims.csv`, and `notes.md`. Central claim, correspondence, and local capture-claim identifiers are unique. The register/capture comparison matches its fourteen-row reconciliation ledger exactly.

The exact Claude handoff is preserved separately from local reproduction. The complete 216-image harvest was not supplied, so 65/65 is reported as a substantial subset check rather than an end-to-end rerun. Rune plaintexts were transcribed from their own visual coordinates; titles, quotations, and chapter position were applied afterward as interpretation. `MANIFEST.sha256` excludes itself. Manifest verification, ZIP CRC, single archive-root verification, and clean-extraction manifest verification are performed after packaging.
