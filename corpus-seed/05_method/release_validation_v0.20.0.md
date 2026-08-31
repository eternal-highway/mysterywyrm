# Release Validation — 0.20.0

Date: 2026-08-29  
Scope: series coverage; Decode acquisition; X≠Y≠Z, Code, Rune Code, Duets, and Translation archive-state repair

## Lineage

- immutable supplied 0.19.0 parent SHA-256: `955db97faec03cb3b576dc4a5b1a46b85fe16510f2f599d207d06333641c8823`
- release semantics: one omitted threshold-page acquisition plus live archive/register reconciliation
- chapter acquisition semantics: unchanged from 0.19.0

## Coverage checks

| Check | Result |
|---|---:|
| X≠Y≠Z archive | 16 / 16 registered and captured |
| Code archive | 25 / 25 registered; 24 captured |
| Rune Code archive | 17 / 17 registered; 16 captured |
| Duets archive | 15 / 15 registered; 14 captured |
| Instruction Manual | 34 / 34 |
| Alphabet Book | 34 / 34 registered; 33 captured |
| Rune Casting | 31 / 31 |
| Stanzas | 29 / 29 |
| Current Translation archive | 34 / 34 |
| Known Translation-tag pages | 35 |
| Riddles / Mathematical Esoterica / Past / Future / Letter | 6 / 9 / 14 / 6 / 4 |
| Additional missing entry pages in inspected archives | 0 after Decode repair |

## Corpus checks

| Check | Result |
|---|---:|
| Completed reflected-pair braids | 14 / 14; unchanged |
| Middle status | 2 observed paths; completeness open |
| Capture folders | 253 |
| Required files in capture folders | 253 / 253 pass |
| Capture canonical URLs registered | 253 / 253 |
| Registered URLs without capture folders | 25; reconciliation ledger exact |
| Verified-page evidence rows | 286 |
| Verified-page unique URLs | 278 |
| Intentional duplicated-lineage URLs | 8 |
| Local folded-message tokens | 66 / 66 pass |
| Documented local slip applied | served `142-M` mapped to slot 144 |
| CSV files parsed and rectangular | 779 / 779 pass |
| Central claim IDs | 216 / 216 unique |
| Correspondence IDs | 186 / 186 unique |
| Local capture claim IDs | 430 / 430 unique |
| Release-tree files | 1,348 |
| Payload files covered by manifest | 1,347 |

All CSV checks ignore empty spacer rows and require every substantive row to match its header width. All capture folders contain `record.md`, `links.csv`, `media.csv`, `claims.csv`, and `notes.md`. The register/capture difference must equal the 25-row reconciliation ledger exactly. `MANIFEST.sha256` excludes itself and is regenerated only after all content is final.
