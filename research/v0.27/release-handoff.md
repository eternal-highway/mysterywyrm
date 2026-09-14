# v0.27.0 release handoff

Rechecked 2026-09-14 from candidate checkpoint `4ba89e8` on
`corpus-v0.27-adjudication`. Owner approved import and publication on 2026-09-14.
The approved import is in progress; see [release record](../../RELEASE-v0.27.0.md)
for subsequent execution status. The pre-import observations below are historical.

## Verified release identity

- Candidate: `dist/letters_for_titles_corpus_seed_v0.27.0.zip`
- SHA-256: `72c85305702f1074598c6f8f0285c41ad19f19d71011a1880c9eb0cc78753b1a`
- Parent: `dist/letters_for_titles_corpus_seed_v0.26.2.zip`
- Parent SHA-256: `cdb93397daffd236261686609eb0da027ee2081f42bbb333032d0405b2247b75`

The independent [preflight report](release-preflight.json) verifies the existing
ZIP without invoking its builder. Run `python -X utf8 -B
tools/preflight_v027_release.py` from the repository to repeat this pre-import
check. It intentionally fails after the canonical seed changes from the parent.

Both ZIP sidecars, CRCs, safe path sets, manifests and exact extracted bytes
pass. The candidate contains 1,521 files and 1,520 payload hashes. All 829 CSVs
have rectangular nonempty records; 162 inherited blank records remain preserved.
The fresh extraction passes both bundled verifiers, including 74/74 captured
filename tokens, and the verifiers leave its bytes unchanged.

The independently calculated import delta is 101 additions, 46 modified parent
files plus the regenerated manifest, and no removals. Each of the 46 files has
an exact parent snapshot in the package. The retained parent media is unchanged;
the 17 added originals authenticate and five authored HTML sources verify.
The largest individual payload is 15,900,872 bytes. The canonical seed still
equals the published parent exactly. The repository structure check also passes.

Live GitHub verification found main at
`6f8abee9e7718a4ae431dcc6d9323c6103bf8cbd`, v0.26.2 latest, no open PRs,
and no remote v0.27 branch or tag. The latest main
[CI run](https://github.com/eternal-highway/mysterywyrm/actions/runs/34701220622)
passed. This is a dated observation and must be refreshed before publication.

## Review conclusion

No blocking package or record-consistency defect was found. README, changelog,
lineage log, re-entry capsule and validation describe the same bounded scope.
Preparation-time candidate wording remains historical inside the immutable ZIP;
subsequent publication must be established in external repository documentation,
as with v0.26.2. Do not rebuild or edit this numbered package to change its status.

This review does not add visual corroboration. Two traversal disputes remain
unresolved; the ice first line retains SAE/SHH alternatives; GUARDIAT and the skull
DEATH extraction retain their feature-rule qualifications. Loop is conditional,
and Octave is classified as inscription-present without transcription. The
existing harvest reading documents remain historical and must retain clear
links to the released adjudication once imported.

## Authorized execution after owner approval

1. Refresh remote main, branch, tag, PR and release state; stop on unexpected
   changes or a conflicting v0.27.0 identity. Repeat the pinned preflight.
2. Import the existing candidate bytes into `corpus-seed/` on the dedicated
   integration branch. The reviewed delta contains no deletions. Update root
   README, LINEAGES, CROSS-LINEAGE-FINDINGS, the adjudication packet, release
   record and work-record status so the staged import and remaining uncertainty
   are explicit. Keep the ZIP byte-exact and retain historical comparison text.
3. Verify the entire seed tree and the staged/committed Git blobs against the
   ZIP, run both seed verifiers and the harvest checks, then commit the import.
4. Push the integration branch and open the PR with the description below.
   Require passing CI and confirm the exact reviewed head before merging.
5. Create annotated `corpus-v0.27.0` at the verified import commit, then publish
   the existing ZIP and its sidecar with the release notes below.
6. Download the published assets into a fresh folder. Verify sidecar, CRC,
   complete manifest, exact ZIP identity and tag target. Record the PR, tag,
   import/merge commits and release URL outside the immutable seed.

Historical approval boundary (satisfied 2026-09-14): the previous task presented
canonical import and publication for approval, and the
[cross-lineage ledger](../../CROSS-LINEAGE-FINDINGS.md) requires explicit owner
adjudication before either lineage changes. The request
to resume has been used to complete the review and release preparation.

## Prepared PR description

The canonical seed and harvest contain conflicting Rune Code readings. Import
the complete reviewed v0.27.0 payload to record qualified dispositions for all
nine disputed carriers together, classify Octave separately, and preserve the
conditional Loop key and unresolved findings.

Three dispositions favor harvest, one favors seed, three favor neither historical
full reading, and two retain unresolved traversal. All 46 changed parent files
have byte-exact history; original evidence and both review stages are bundled.

Validation: pinned ZIP and parent identities; 1,520 manifest hashes; 829 CSVs;
exact fresh extraction; both bundled verifiers; 74/74 captured filename tokens;
17 authenticated original carriers and five authored support pages. Record
post-import committed-tree equality and CI results before merging. Mechanical
checks do not certify visual interpretation or complete Gate 0 Outcome B.

## Prepared release notes

Canonical corpus seed v0.27.0 records the bounded Rune Code comparison and its
review, retaining evidence, historical readings and explicit uncertainty.

- All nine disputed carriers receive qualified dispositions together.
- Octave is classified as inscription-present and remains untranscribed.
- Loop remains conditional; complete independent key confirmation is not claimed.
- Shh and Oedipean traversal, ice segmentation and stated feature-rule limits
  remain open. This release does not claim a completely solved corpus.
- 17 authenticated original images, five authored support pages, frozen
  observations and exact copies of 46 modified parent files are included.

Payload: 1,521 files, 1,520 manifest hashes, 829 CSVs. Both bundled verifiers
passed in a fresh extraction. Parent: published v0.26.2.

ZIP SHA-256:
`72c85305702f1074598c6f8f0285c41ad19f19d71011a1880c9eb0cc78753b1a`.
