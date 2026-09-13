# v0.27 work record

Started 2026-09-12 on `corpus-v0.27-adjudication`, from
`6f8abee9e7718a4ae431dcc6d9323c6103bf8cbd`.

**Status: conditional continuation authorized by the user on 2026-09-12;
independent Loop key confirmation incomplete. The bounded comparative pass is
complete and verified as of 2026-09-13. No released adjudication has occurred.**

Read the [complete comparative report](comparative-pass.md). Among the nine
disputes, the recommendations support the harvest on Axaxaxas, Always and The
Way; the seed on For Anybody; neither complete reading on Soon After it Becomes
Water; and retain four unresolved carriers. Octave separately has an inscription
present classification, without a new transcription.

Subsequent user-requested review: read [current findings after review](review-integration.md)
and the [sub-agent's evidence report](unresolved-review.md). The skull sequence
now has a supported DEATH extraction; the leaf plate favors literal GUARDIAT;
the ice first line retains both SAE and SHH segmentations. The initial report
above remains the historical first pass, committed as `de9790c`.

Second-pass update: a frozen candidate now matches all 29 coordinate-to-rune
assignments in the harvest table. This does not confirm the reconstructed
entries. See [candidate method](loop-candidate-method.md),
[candidate CSV](loop-candidate-key.csv), and the
[conditional-continuation proposal](gate-0-conditional-proposal.md), which has
been authorized by the user.

The v0.26.2 prerequisite was checked live on GitHub: published 2026-09-12
15:04:41 UTC, not a draft. The remote main tip matched the starting commit.

## Completed work

- Downloaded the exact P005 Loop carrier directly from its canonical media URL.
- Verified SHA-256, byte count, dimensions, exact manifest URL/file identity,
  and association with the Loop post. The committed source manifest was retained.
- Recorded all 29 cell positions before consulting either lineage's key table,
  distinguishing legible inscriptions from reconstructed text and missing marks.
- Inspected an original-pixel crop of the unresolved region. Physical objects
  cover several inscriptions; a larger display does not expose those marks.
- Added `tools/verify_v027_loop.py` as a repeatable, read-only identity check.
  Exit success means authentication only, never visual key confirmation.
- Authenticated all 17 named carriers against their exact committed file/URL,
  SHA-256, byte-count, and dimension identities. Sixteen were downloaded on
  2026-09-12 and Loop was reused after verification. See
  [source authentication report](source-authentication.json). No other plate
  was visually inspected during this preparation.
- Compared the frozen 29-row candidate against the harvest table: 29 rune
  assignments match, with one normalized transliteration difference (Ger Y/J).
  See [comparison report](loop-key-comparison.json).

See [independent observation](loop-independent-observation.md) for the exact
evidence identity, visual results, and reproducible crop rectangle.

## Gate disposition

The source bytes authenticate; no key-assignment mismatch is demonstrated.
Outcome B is not asserted because the Loop reading itself remains incomplete.
The user authorized the exact conditional exception recorded in
`gate-0-conditional-proposal.md`, so the comparative pass proceeded under that
exception. No further approval of that same scope is pending.

The four provisional assignments were then supported by separate authored
evidence: [Octave's grouping rule and the numbered stanza pages](key-corroboration.md).
This source-based derivation supports their use under the exception without
pretending the obscured Loop marks were read. The report retains markers for
those assignments and explicit count/traversal uncertainty where it remains.

All nine disputed carriers and the Octave classification were examined in this
one pass. The canonical seed and both inherited reading records remain intact;
the new dispositions have not been applied as a corpus release.

## Re-run

With the authenticated image at the ignored archive path:

```sh
python tools/verify_v027_loop.py
python tools/compare_v027_loop.py
python tools/materialize_v027_evidence.py
python tools/render_v027_pass.py --check
```

These tools require only the standard library and the adjacent `archive.py`.
The identity verifier does not read transcription tables. The comparison tool
reads the frozen candidate and harvest table but never declares Gate 0 passed.
The materializer checks the 17 named carriers and writes an authentication
report; `--fetch` additionally downloads absent files without overwriting
existing evidence or the committed manifest. It performs no visual reading.
The renderer validates the frozen inputs and evidence identities, then checks
that the report reproduces its structured records. It is a consistency check,
not an automated judge of visual correctness.

## Validation through 2026-09-13

- Loop identity verifier: pass; observed bytes equal all required values.
- Named source carriers: 17/17 authenticate; committed media manifest unchanged.
- Frozen candidate comparison: 29/29 rune assignments match; uncertainty retained.
- Canonical seed: all 1,419 manifest hashes pass, with exact path-set agreement.
- Both seed state verifiers: pass (17 carriers; 74/74 local filename tokens).
- `git diff --check`: pass.

The next release mutation is to stage a v0.27 candidate **outside** the immutable
seed, importing this entire comparison together, including unresolved entries
and the conditional-key provenance. Octave transcription is a later bounded
pass; inscription classification alone does not authorize filling it in here.
