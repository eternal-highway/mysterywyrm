# Letters for Titles — corpus structure

Findings from a full harvest of <https://lettersfortitles.com> (262 posts,
85,942 words, 479 images, published 2022-03-25 → 2023-03-20).

Everything below is regenerated and checked by `tools/structure.py`, which
exits non-zero if the architecture it asserts no longer holds.

## What the site is

*Letters for Titles* is an alphabet book by Vern Tonkin built on the Old
English Rune Poem — a 29-stanza poem, one stanza per rune. As the *Twist*
chapter puts it, the poem survives in "the only copy we have … printed in
1705 from the only surviving manuscript copy, which burned to ashes in a
fire 26 years later" (the 1705 printing is George Hickes's *Thesaurus*; the
fire is Ashburnham House, 1731 — the project marks it with a post called
"How to Burn the Cotton Library"). Tonkin translates each stanza, casts
each rune, and hangs essays, poems, riddles and artwork off it. The stated
design, from the project's own "Vern Tonkin" entry: *"I'm singing a song
too, making it simple to last a whole year."*

## The work is complete, not abandoned

Posts stop on 2023-03-20, which reads at first like an unfinished project.
It is not. All 29 stanzas are present, each with its `Rune Casting:` and
`Translating:` companion (29/29 in every series), and the final post is
titled **"The Middle."** The site ends because it arrived at its center.

## The author states the plan up front

This is not only an inference from the data. The earliest post,
"Alphybettyformed Verbage" (2020-05-26, two years before the run began),
describes the whole design:

> Take the letters, cut them apart from each other, carve them into bits of
> wood if that helps you, and line them up in a row. Now fold your line in
> half so number 1 is next to 29, 2 next to 28, etc. Make the pairs and read
> them together. They match each other. They sing duets about light,
> renewal, a song of home and exile. A song of the water cycle. […] until
> you get to the clue, the key to the secret, number 15 in the middle —
> Helix, standing alone all twisted, singing we should twine this poem
> aound itself and look at it again.

Every chapter title in the finished work is named in that paragraph or
follows from it — "Light", "The Water Cycle", "You Have Nothing Else",
"Everything is Temporary", "Twist". The derived structure below and the
stated plan agree exactly.

## The chiastic architecture

Chapters (WordPress categories) each cover **two** stanzas — one counting
up from the start, one counting down from the end. Every pair sums to 30:

| Chapter | Stanzas | Posts |
|---|---|---|
| Everything is Temporary | 1 Wealth + 29 The Grave | 23 |
| Moody Joy | 2 Aurochs + 28 Beaver | 19 |
| They'll Cut You | 3 Thorn + 27 Bow | 17 |
| Axis Mundi | 4 God + 26 Ash | 17 |
| By Land and By Sea | 5 The Ride + 25 Oak | 17 |
| Light | 6 Torch + 24 Day | 17 |
| You Have Nothing Else | 7 Gift + 23 Home | 17 |
| Prosperity | 8 Joy + 22 Ing | 17 |
| The Water Cycle | 9 Hail + 21 The Sea | 17 |
| Fate | 10 Need + 20 Human | 17 |
| War and Peace | 11 Ice + 19 War Horse | 17 |
| The Future | 12 Year + 18 Birch | 17 |
| Trust | 13 Yew + 17 Tiw | 17 |
| Sitting to Battle | 14 The Game + 16 Sun | 17 |
| **Twist** | **15 Helix — unpaired** | **10** |

The poem is read from both ends inward simultaneously. Stanza 15 (Eolhx,
glossed "Helix") is the fixed point of `n ↔ 30-n` and has no partner, so
the last chapter is half-length and is called *Twist* — the turn where the
two reading directions meet. The chapter's closing post, "The Middle," is
the book's center and its end at once.

The center is chosen, not incidental. Eolhx is the one rune name in the
poem that nobody can translate: it "appears nowhere else in Old English
writing, so whatever it means, we have no clues apart from its Rune Poem
stanza riddle," and it may not even have been in the manuscript that
burned. A project organized around translating all 29 stanzas converges,
by construction, on the single word that cannot be translated.

This also explains the two anomalies in the post counts: the 17-post
chapter template carries two of each per-rune element, so the single-rune
center needs only 10; and the first two chapters run long (23, 19) because
they absorb the framing pieces that set the method up.

## And restates it at the close

The last post, "The Middle" (2023-03-20), names the method again and warns
the reader that the blog's own presentation misleads:

> If you have just found this Alphabet Book, this is not the beginning, this
> is the middle. […] There's an arrangement to it, a fluidity of motion,
> meaning hidden in structure. A beginning, an ending, a thematic pairing of
> first and last, then of their adjacent runes and so on until you run out
> and come to an end, which is to say the middle: the mother of all endings
> and beginnings.

A WordPress archive lists newest first, so a visitor lands on "The Middle"
and reads backwards out of the center. That is the reason for
`book/reading-order.md`: the work reassembled in the sequence it was built.

## The 17-post chapter template

Each full chapter runs a fixed sequence over ~17 weekdays:

1. two **rune-glyph posts** — title is the bare rune (ᚠ, ᛠ, …), 29 in total
2. two **`Rune Casting:`** posts — the divinatory reading of each rune
3. two to three **`How to …`** posts (34 overall) — instructional prose poems
4. one to three **`<letter> is for …`** posts (32 overall) — the alphabet-book spine
5. one **`X≠Y≠Z`** post (15 overall) — a recurring argumentative/absurdist strand
6. one **chapter-namesake** post stating the theme ("Light", "Fate", "Twist")
7. one or two **image-only posts** — artwork carrying no text (20 overall)
8. two **`Translating:`** posts — the philological working-out of each stanza
9. two closing **`Stanza N:`** posts — the finished translations, high stanza first

Order within a chapter is consistent: glyphs and castings open, translations
and stanzas close. Every one of the 262 posts carries at least one image;
the work is visual as much as textual.

The regularity is exact. Counting posts by role (`tools/structure.py` prints
this table) every full chapter carries **two** castings, **two**
translations and **two** stanzas, and exactly **one** X≠Y≠Z:

| Chapter | glyph | casting | transl | stanza | how-to | alphabet | X≠Y≠Z | other | total |
|---|---|---|---|---|---|---|---|---|---|
| Everything is Temporary | 3 | 2 | 2 | 2 | 3 | 3 | 2 | 6 | 23 |
| Moody Joy | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 5 | 19 |
| They'll Cut You | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 3 | 17 |
| Axis Mundi | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 5 | 17 |
| By Land and By Sea | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 3 | 17 |
| Light | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 3 | 17 |
| You Have Nothing Else | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 4 | 17 |
| Prosperity | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 3 | 17 |
| The Water Cycle | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 3 | 17 |
| Fate | 3 | 2 | 2 | 2 | 2 | 2 | 1 | 3 | 17 |
| War and Peace | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 3 | 17 |
| The Future | 2 | 2 | 2 | 2 | 2 | 3 | 1 | 3 | 17 |
| Trust | 3 | 2 | 2 | 2 | 2 | 2 | 1 | 3 | 17 |
| Sitting to Battle | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 4 | 17 |
| **Twist** | **1** | **1** | **1** | **1** | **1** | 0 | 0 | 5 | **10** |

*Twist* is the template halved, exactly as a one-rune chapter should be —
independent confirmation that the center is structural rather than a place
the project happened to stop.

## Cadence

257 publication days, spread almost perfectly evenly across weekdays
(Mon 52, Fri 52, Tue/Wed/Thu 51 each) with no weekend posts — a
one-post-per-weekday discipline held for very nearly exactly one year.

## Front matter

Five posts sit outside the chapter scheme, in the `Hwat` category:

- **Alphybettyformed Verbage** (2020-05-26) — the earliest post, predating
  the run by ~2 years; the project's seed.
- **O Yes, W.** — the complete Rune Poem, Old English with Tonkin's
  facing translation, in one piece.
- **Vern Tonkin** — the artist's statement (Spanish first language, Old
  English taken instead of a Spanish requirement in grad school, Beowulf
  translated ten hours a day for six months, the Rune Poem read as the
  *Sesame Street* of Old English poetry: "it's kind of upbeat").
- **Bibliography** — ~346 MLA entries with 45 outbound links, mostly JSTOR,
  plus Bosworth-Toller and the Dictionary of Old English Plant Names.
  The scholarly apparatus for the whole project.
- **Turn** — a 22-word hinge posted mid-run (2022-09-19), quoting Dante at
  the foot of the hill. It is the pivot of the filename cipher: the point
  where the image numbering stops counting down and starts counting up.
  See [`cipher.md`](cipher.md).

## Data

- `data/corpus.json` — all 262 posts, normalized: slug, title, date,
  chapter, tags, plain text, word/image counts, image and outbound links.
- `tools/harvest.py` — rebuilds the dataset from the site's WordPress REST API.
- `tools/structure.py` — re-derives and checks every claim above; it exits
  non-zero if the pairing or the series completeness ever stops holding.
- `book/reading-order.md` — the work reassembled in the sequence described here.
- `book/poem-order.md` — the same material cut the other way, stanzas 1–29.
- `research/archive.md` — the preservation copy and what it does not contain.
- `research/bibliography.md` — the project's 375 sources.
