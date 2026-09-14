# Candidate key derivation

Frozen before opening `research/rune-code.md` or the seed key table. This is a
second-pass candidate, not a replacement for the first observation record.

Evidence is the same authenticated P005 Loop file, SHA-256
`33b777ed8f09bd0c3421d4b17c2f87bef8e878e77c8d75939e4dd2d58158874c`,
2062 × 1528, 5,734,273 bytes, canonical URL
<https://lettersfortitles.com/wp-content/uploads/2021/11/Loop.lettersfortitles-verntonkin.jpg>.

The candidate distinguishes direct inscriptions, partial inscriptions, and
structural reconstruction. Rune names normalize visible shapes, letters, or
glosses using general rune knowledge. This normalization is interpretation;
the image does not spell out all the conventional rune names. In particular,
Peorth and Ethel remain weak identifications, not fully exposed glyph readings.

The candidate transliterations are also normalized interpretations. `th`, `ng`,
`oe`, `ae`, and `ea` spellings are not claims of fully legible Latin text in each
cell. The visible Y at Ger and the bow-rune identity at Yr do not by themselves
settle which glyph a separate plate uses for English y.

## Reproducible views

Original-pixel crops, Pillow left/top/right/bottom, exclusive right/bottom:

- top: `(0, 0, 2062, 455)`
- reverse band: `(0, 430, 2062, 790)`
- middle: `(0, 770, 2062, 1120)`
- bottom: `(0, 1080, 2062, 1528)`
- cells 14–15: `(1510, 760, 2005, 1110)`, additionally displayed at 2× with
  Pillow's default RGB resize filter (bicubic). Enlargement adds no evidence.

The lower-band crop exposes enough of cell 17's coordinate to read 3.1.
Cell 16 exposes parts consistent with 2.8; the sequence still contributes to
that reading. This corrects the first pass's blanket treatment of four
coordinates as unreadable: two remain wholly dependent on reconstruction,
one partly depends on it, and one is now directly readable.

## Structural reconstruction

The visible ordinal/coordinate pairs follow eight-position groups: 1 → 1.1,
8 → 1.8, 9 → 2.1, 13 → 2.5, 18 → 3.2, 24 → 3.8, 25 → 4.1, 29 → 4.5.
Every readable pair is consistent with
`group = floor((ordinal - 1) / 8) + 1`,
`position = ((ordinal - 1) mod 8) + 1`.
Applying that observed rule predicts 14 → 2.6, 15 → 2.7, 16 → 2.8.
These predictions are derived without consulting either inherited table.
They are not observations of the hidden ink and do not exclude a local
exception or annotation underneath a coil.

The quilled pieces cross cell boundaries and do not supply an independently
validated pair-count method for the obscured cells. Their mere number must
not be used to claim the missing key coordinates were read.

## Comparison boundary

`loop-candidate-key.csv` is the complete 29-row candidate for comparison.
Its agreement with an inherited table can identify compatibility, but cannot
turn its low-confidence or reconstructed entries into independently observed
facts. Gate 0 still requires a separate disposition after comparison.
