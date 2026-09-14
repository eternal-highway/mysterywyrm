# Cross-cutting tests — conditional pass, 2026-09-12

These results precede the per-carrier comparison. The authorized conditional
key governs; Gate 0 Outcome B is not asserted. Evidence identities are fixed
by `source-authentication.json`. All coordinates below were recorded before
consulting either lineage's detailed coordinate records. The packet's disputed
wordings and the harvest overview/tool documentation were already visible:
this is independent coordinate extraction, not a blind semantic experiment.

## 1. Axaxaxas row 4 has 12 units

P241 source SHA-256:
`6953e91183de5f2365ea68cafc325aa27bd2b1dea3211a01c577d83d3029c14b`.
Count separately bounded upright/coil groups, not individual strokes or words.
The fourth line has ten groups before the large gap and two after it: 12.
All five line counts are 10 / 8 / 10 / 12 / 8, excluding the dash and question
mark. Total: 48. Confidence high for unit count; dense internal coil counts
have lower confidence and are recorded separately in the per-carrier record.

Original-pixel crop `(280,825,1330,1190)` inspects rows 3–4; the whole source
supplies the rightmost group cropped off that rectangle. The full-image count
and the crop agree. No detector output was used to supply the count.

## 2. Ger/Yr must be selected by glyph, not desired English

The authenticated Loop image visibly places Y beside Ger's cell 2.4. P241's
first glyph has two uprights and four coil arms, hence 2.4, not four uprights
and three arms (4.3). This supports Ger in that position independently of the
expected word. The candidate decoder renders Ger as `y`; the harvest's `J`
is a transliteration convention. Keep the raw coordinate in every case.

This is not a rule that every English y is Ger, nor a claim that Yr cannot be
used elsewhere. Resolve each observed glyph or retain alternatives. Do not
infer consonant/vowel intent merely from a plate's expected sentence.

## 3. Traversal is not fixed by one universal rule

P209 source SHA-256:
`87a257f7fed20e2b4fea4aa6c404a77fa166160f89f7c5fec859ed0ad263a4e1`.
The image gives these local bough counts (above/below):

| Location | Coordinate |
|---|---|
| Lower left | 3.5 |
| Middle left | 2.3 |
| Upper left | 2.8 |
| Crown | 3.1 |
| Upper right | 3.3 |
| Lower right | 2.2 |

A perimeter sweep from lower left up to crown and down right yields
`li[s]ten`; brackets flag the provisional 2.8 key assignment. A side-first
order upper-left → middle-left → lower-left → upper-right → lower-right →
crown yields `[s]ilent`. The image has neither an explicit start marker nor
direction arrows. Its connected trunk does not select one ordered traversal
through all six boughs. Perimeter continuity favors the former as a proposal,
but does not establish it as the uniquely encoded reading. Traversal remains
unresolved. Do not transfer a Shh convention into Always or You Knew It
Beforehand; record their spatial arrangements separately.

## 4. Source identity and historical equivalence

All 17 named originals authenticate against the committed manifest (file,
exact canonical URL, byte count, dimensions, SHA-256). This is stronger than
matching dimensions alone. It establishes the current bytes used in this pass.
It does not prove which historical bytes a reader actually viewed.

The packet and v0.26.2 provenance record identify historical smaller Loop and
Œdipean derivatives. This pass uses the authenticated 2062×1528 Loop and
2560×2560 Œdipean originals. Historical source equivalence must not be claimed
merely because the revised register now points to the same original.

Tests 1–3 now have recorded answers; an unresolved traversal is an answer,
not permission to choose the sentence that reads best.
