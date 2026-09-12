# Release validation — v0.26.2

Date: 2026-09-12
Scope: metadata/provenance patch candidate; no transcription adjudication.
Parent: `letters_for_titles_corpus_seed_v0.26.1.zip`
Parent SHA-256: `ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327`

## Checks

- Parent ZIP CRC and exact SHA-256 verified; parent payload is the comparison baseline.
- Candidate modifications are restricted to the declared metadata, provenance, guidance and verifier paths.
- `code_register.csv` is byte-identical to the parent. Every retained image/GIF payload is byte-identical to the parent.
- 813 CSV files parse as rectangular tables.
- All 31 imported media hash records agree with the co-located full-resolution manifest; no new download verification is claimed.
- Harvest publication-date export preserves 262 records at day precision.
- Source-URL correction agrees with archived canonical tag and harvest metadata; live retrieval did not succeed in this pass.
- Repository filename derivation passes: 211/211 directly recovered characters; seven characters supplied from context.
- Repository structure verifier passes in Python UTF-8 mode: all 29 stanzas, castings and translations; reflected pairs and central chapter confirmed.

## Seed verifier output

```text
Rune Code state: 17/17 classified (14 ordered + 1 rebus + 2 key carriers)
Stale current-state phrases: 0
Carrier fingerprints: 17/17 rows; imported source-byte hashes: 17/17 named carriers, 31/31 media records

message length: 261
locally captured cipher tokens: 74
matches: 74
failures: 0
```

## Packaging

The regenerated manifest excludes only itself. `tools/package_v0262.py` verifies ZIP CRC, a single safe root, every manifest hash, exact path-set equality and both seed verifiers in a clean extraction. The candidate ZIP checksum and resulting counts are recorded outside this payload in `RELEASE-v0.26.2.md`, avoiding a self-referential hash.

## Boundaries

Historical visual fingerprints keep their original identity/date. Original-media hash availability does not authenticate any future downloaded bytes. Nine carrier transcription disputes and the Octave classification question remain open; Gate 0 has not been performed. The published release remains v0.26.1 until this candidate is integrated and published.
