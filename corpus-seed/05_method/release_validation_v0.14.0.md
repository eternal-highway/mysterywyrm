# Release Validation — 0.14.0

Date: 2026-08-27  
Scope: Axis Mundi direct-walk acquisition, prediction adjudication, and corpus reconciliation

## Lineage

- immutable 0.13.2 parent SHA-256: `47c205b0d388189cca282dee774c9654c8a6633ab866460aa8d629a7dfe3d35a`
- parent ZIP integrity: pass
- patch semantics: seventeen-page acquisition, structural and source reconciliation, explicit model falsification, and current-state handoff

## Mechanical checks

| Check | Result |
|---|---:|
| Completed reflected-pair braids | 11 / 14 |
| Middle status | 2 observed paths; completeness open |
| Paired braids with 17 pages | 11 / 11 |
| `2 + 2 + 9 + 2 + 2` within tested pair sample | 11 / 11 |
| Eponymous pages at position 9 | 11 / 11 |
| Directly verified *Duets* tags | 3 / 11 |
| Axis Mundi direct internal adjacencies | 16 / 16 pass |
| Axis Mundi pre-registered structural tests | 2 / 2 pass |
| Exceptionless displayed-asset model | falsified at position 11 |
| Independent archive-order retrochecks | 36 / 36 pass |
| Prospective Axis Mundi direct-walk checks | 4 / 4 pass |
| Derived same-source BLBS comparisons | 4 / 4 consistent |
| Capture folders | 194 |
| Capture canonical URLs registered | 194 / 194 |
| Registered URLs without capture folders | 19 enumerated |
| Verified-page evidence rows | 219 |
| Verified-page unique URLs | 213 |
| Intentional duplicated URLs | 6 |
| Broken supersession references | 0 |
| CSV files parsed and rectangular | 597 / 597 |
| Claims identifiers unique | 156 / 156 |
| Correspondence identifiers unique | 143 / 143 |
| Release-tree files | 1,030 |
| Payload files covered by manifest | 1,029 |

Blank terminal CSV lines are ignored during rectangularity checks. All substantive CSV rows match their headers; all page, claim, and correspondence identifiers are unique; all six supersession pairs are reciprocal; and the register/capture comparison matches its 19-row reconciliation ledger exactly.

The category archive was consulted only after the direct walk and matched its seventeen-page set exactly in reverse order. `MANIFEST.sha256` excludes itself. Manifest verification, ZIP CRC, single archive-root verification, and release hash calculation are performed after packaging.
