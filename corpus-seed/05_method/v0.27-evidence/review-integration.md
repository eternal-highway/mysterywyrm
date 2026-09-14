# Current v0.27 findings after the requested sub-agent review

Integrated 2026-09-13. The initial bounded pass is preserved in commit
`de9790c`; its frozen observations and report remain historical records.
This addendum records the subsequent review's effects, not a silent rewrite.
No canonical release or seed mutation has occurred.

The sub-agent inspected five named carriers in one bounded review. The parent
read its report and checked the original-pixel skull, ice-field and final-leaf
crops. The P161 bottom-left crop had already been independently checked by the
parent after the first pass. Both agents had prior exposure to the proposed
readings, so agreement is not described as blind corroboration.

The detailed counts, source SHA-256 values, alternate rules and crop rectangles
are in [unresolved-review.md](unresolved-review.md). Those evidence identities
continue to apply to every amended finding here.

## Accepted changes to the first-pass recommendations

| Carrier | Current disposition | Accepted finding | Remaining limit |
|---|---|---|---|
| P161 Œdipean | unresolved | Bottom-left 2.4 is supported, excluding inherited 4.3. The middle-right face provides a color-class control favoring top-row face 2 at 2.1. | NIGHT / AND / DAY requires reversing each spatial row; that direction is not explicitly marked. |
| P055 It Never Deceives | neither | Repeated upper-fan/lower-object construction favors final 3.1. Primary literal sequence is GUARDIAT. | 2.2 remains a weaker alternative under a different shape-class rule; no semantic repair to GUARDIAN is adopted. |
| P209 Shh | unresolved | All six local bough counts are supported. | Neither LISTEN nor SILENT has a uniquely indicated starting point and traversal. |
| P109 You Knew it Beforehand | neither | Skull counts 3.8 / 3.3 / 4.1 / 1.3 give DEATH. Together with the checked smiling faces, the candidate is WHAT IS OUR FATE? / CHEER UP IT IS DEATH. | Medium confidence overall: replacing lash-count with whole-bone count is an explicit inferred feature rule. This is a supported complete candidate, not proof of unique authorial intention. |
| P125 Soon After it Becomes Water | neither | First-line pieces remain countable. Preserve both 2.8 4.2 and 2.8 2.1 2.1, giving SAE and SHH. | The right-field group boundary is not marked. Neither candidate is selected by word sense, and neither validates seed SO. |

The P109 skull extraction supersedes the first pass's four unknown units.
The candidate's lower phrase now has an explicit count-based derivation; it is
not merely the seed's final word copied into the harvest's incomplete reading.
The full result matches neither historical full-carrier record, hence `neither`.
The conditional P and S assignments remain marked and separately supported as
described in [key-corroboration.md](key-corroboration.md).

P055's final 3.1 was already one of the frozen alternatives; the review supplies
a carrier-local reason to prefer it. `Neither` describes the literal primary
reading, not a claim that its intended meaning has been solved.

P125's SHH alternative is a new segmentation of the same six right-field
pieces, not newly discovered ice. The original SAE must no longer be presented
as the only candidate. The shared lower lines remain LET / US / MELT.

## Findings outside this review

The initial recommendations for Axaxaxas (harvest), Always (harvest), The Way
(harvest), and For Anybody (seed) stand unchanged. Octave remains an
inscription-present classification; it has not been transcribed in this work.

## What remains to decide

- P161 and P209: traversal lacks a unique visible selector.
- P125: first-line segmentation remains uncertain.
- P055 and P109: retain their stated feature-rule qualifications; the literal
  results must not be converted into unqualified semantic conclusions.

These limits can be recorded in v0.27 without forcing complete certainty.
The next release candidate should import the checkpoint and this review
addendum together, keeping both stages and their changes inspectable.

## Verification

`tools/render_v027_unresolved_review.py` authenticates the five reviewed source
files and reproduces 14 original-pixel crops. `tools/render_v027_pass.py --check`
continues to verify the frozen initial report. Neither program claims to test
the correctness of the visual interpretation. The initial checkpoint contains
no canonical seed changes; the review likewise edits no seed or source bytes.
