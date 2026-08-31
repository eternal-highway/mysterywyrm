# Release Validation — 0.21.0

Date: 2026-08-29  
Scope: structural consolidation, complete Middle path, content-page backlog closure, stale-state repair, sustainable maintenance boundary

## Lineage

- canonical 0.20.0 parent SHA-256: `87f5f9cba54d30695c4fccb2a7e5732e53bd0b307bdfeaeb3b7758c2983b3b7b`
- release semantics: one completed consolidation batch, not a sequence of isolated micro-patches
- historical release reports: preserved as dated states

## Coverage checks

| Check | Result |
|---|---:|
| Registered evidence rows | 286 |
| Registered unique URLs | 278 |
| Intentional duplicated-lineage URLs | 8 |
| Registered content URLs | 263 |
| Content URLs with capture folders | 263 / 263 pass |
| Registered archive/index surfaces without captures | 15 |
| Reconciliation ledger | 15 / 15 exact |
| Middle / Twist path | 10 / 10 registered and captured |
| Middle direct path versus category archive | exact reverse-order match |
| Reflected-pair braids | 14 / 14 unchanged |
| Alphabet Book / Code / Rune Code / Duets capture coverage | 34 / 34; 25 / 25; 17 / 17; 15 / 15 |

## Integrity checks

| Check | Result |
|---|---:|
| Capture folders | 263 |
| Required files in capture folders | 263 / 263 pass |
| Capture canonical URLs registered | 263 / 263 |
| CSV files parsed and rectangular | 811 / 811 pass |
| Central claim IDs | 221 / 221 unique |
| Correspondence IDs | 189 / 189 unique |
| Local capture claim IDs | 458 / 458 unique |
| Broken supersession references | 0 |
| Missing explicit local Markdown/CSV/Python references | 0 |
| Local folded-message tokens | 73 / 73 pass |
| Cipher verifier failures | 0 |
| Release-tree files | 1,402 |
| Payload files covered by manifest | 1,401 |

## Resolved stale state

- *Stanza 12: Year* now records its directly observed next link to the Eoh glyph.
- *Translating Ear* records the 2026-08-29 live state: page tag present, Translation archive entry absent.
- The Middle is no longer described as two incomplete fragments; `Fen → Twist → Loop` joins the complete direct path.
- The unavailable *X≠Y≠Z: Divination* page is no longer an indefinite acquisition task; its missing speaker/media detail is bounded as open question OQ006.
- Counts for Alphabet Book, Code, Rune Code, Duets, capture folders, and reconciliation are current.

## Sustainable boundary

`05_method/maintenance_policy.md` distinguishes defects from open research. `01_inventory/open_questions.csv` contains the bounded continuation queue. Unavailable harvest data, unsolved plates, exact publication chronology, and external source adjudication do not keep structural acquisition artificially open.

`MANIFEST.sha256` excludes itself. Manifest verification, ZIP CRC, single-root verification, and clean-extraction manifest verification are performed after all content is final.
