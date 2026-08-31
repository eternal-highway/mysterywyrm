# Rune Code QA Reconciliation — 0.26.1

Date: 2026-08-30  
Scope: mechanical accounting correction, current-state synchronization, provenance strengthening, and regression checking

## Outcome

The 0.26.0 Rune Code readings survive review. The live archive remains a seventeen-entry set comprising fourteen ordered page-local inscriptions, one complete question-and-rebus, and two key carriers. No evidence supports promoting those objects into one continuous Rune Code plaintext.

## Corrected face-unit accounting

The upper field of *You Knew it Beforehand* has thirteen face units in total: twelve coordinate-valued face units plus one direct Roman `K`, followed by a direct question mark. Earlier wording that described thirteen coordinates in addition to the direct `K` double-counted the direct-letter unit. The displayed reading remains `WHAT DO YOU KNOW?`; no plaintext or ordering judgment changes.

## Current-state synchronization

Current inventory and capture notes for *Bright Fruits*, *Friþ*, and *Soon After it Becomes Water* now record their completed readings rather than their earlier opaque status. The stale next action on the upper *You Knew it Beforehand* claim has also been replaced. Dated historical changelog and lineage entries remain intact as acquisition history.

## Carrier provenance

`01_inventory/rune_code_carrier_fingerprints.csv` covers all seventeen Rune Code archive entries.

- *Arrows*, *The Way*, and *Present* retain exact served-media bytes and therefore have source-byte SHA-256 values.
- Other visual carriers receive SHA-256 fingerprints of 1363 × 936 browser-rendered viewport JPEGs captured at default zoom on 2026-08-30 UTC.
- Those visual fingerprints are change-detection aids, not source-byte hashes. Browser rendering, scaling, color handling, or viewport changes can alter them even when the source file is unchanged.
- The animated *Everything is Temporary* value fingerprints one captured rendered state, not the complete GIF.
- *Octave* supplies the key in page prose and has no separate visual carrier fingerprint.

Exact served-byte hashes for the remaining carriers are recorded as `OQ007` and should be added only if those media bytes become directly accessible. Their absence does not reopen the completed transcription queue.

## Automated guard

Run:

```text
python3 05_method/verify_rune_code_state.py
```

The checker enforces the 14 + 1 + 2 classification, rejects stale opaque/unresolved wording in current-state files, checks the corrected face-unit language, and verifies that the fingerprint register covers exactly the Rune Code archive membership.

## Unchanged boundaries

This patch changes no decoded text, coordinate path, archive membership, page path, capture folder, retained media payload, chapter structure, source chronology, or filename-run result.
