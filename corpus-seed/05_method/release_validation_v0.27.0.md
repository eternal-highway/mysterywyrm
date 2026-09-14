# v0.27.0 candidate validation

Prepared 2026-09-13. Not a publication record.
Parent SHA-256: `cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75`.

- Exact published parent ZIP CRC, path safety, manifest and canonical seed equality: pass.
- 46 modified parent files, each with a byte-exact history snapshot.
- No parent path deleted; retained images and imported 31-record media manifest unchanged.
- 17 bundled originals authenticated by hash, bytes and dimensions; 5 authored HTML sources by portable LF hash.
- 829 rectangular CSVs, including preserved history and key table.
- All nine disputes plus Octave classification imported together; Loop remains conditional.
- Candidate generation never writes the canonical seed.

```text
Rune Code state: 17 archive entries; 9 disputes + Octave classification + conditional Loop accounted for
Current code/page/claim registers and open research limits: consistent; frozen first pass retained
Mechanical transliteration consistency: pass; this does not verify visual counts or traversal
Source evidence: 17 original images authenticated; 5 authored HTML texts verified; 31 imported media identities preserved
Parent preservation: 46 modified files have exact historical snapshots; all other parent payloads unchanged
message length: 261
locally captured cipher tokens: 74
matches: 74
failures: 0
```

The builder then regenerates the manifest, creates a deterministic ZIP, verifies
CRC, exact bytes, path-set equality and every payload hash, and runs both verifiers
in a second clean extraction. Final counts and ZIP hash are outside the payload
in RELEASE-v0.27.0.md to avoid self-reference. These checks validate record and
byte integrity, not the correctness of a visual interpretation.
