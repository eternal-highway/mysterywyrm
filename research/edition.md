# The poem, collated

The research in [`structure.md`](structure.md) describes the machine: 15
chapters reading the Rune Poem inward from both ends to a fixed centre. It
does not deliver the thing the machine was built to produce. This does —
and, in assembling it, finds that the corpus carries the poem *twice*.

The edition is [`../book/rune-poem.md`](../book/rune-poem.md), generated and
checked by `tools/edition.py`.

## Two independent witnesses

| | Witness A | Witness B |
|---|---|---|
| What | the 29 `Stanza N:` posts | "O Yes, W.", one post |
| Where | one per chapter, closing it | the front matter |
| Published | 2022-04-25 → 2023-03-17 | 2022-03-21 |

Witness B went up four days *before* the year-long run began: the whole
poem, laid out in advance, as the thing about to be taken apart. Witness A
is the same poem delivered a stanza at a time, each after its chapter had
worked the stanza over in a `Translating:` post.

Neither derives from the other in the corpus, so they can be collated. The
parse is mechanical in both: the Old English of every stanza closes with the
manuscript punctus `᛬᛫`, and the facing translation follows it. `tools/edition.py`
exits non-zero if either witness ever stops parsing as 29 stanzas in futhorc
order with both halves present.

## What the collation found

**All 29 Old English texts agree exactly.** Across roughly 3,000 words of
Old English — with thorns, eths, wynns, the Tironian *⁊* and the abbreviation
*ꝥ* — the two settings are character-for-character identical. Whatever
Tonkin was working from, he transcribed it the same way twice.

**Five differences, all in the translation.** Three are punctuation: stanzas
26, 27 and 28 close with a full stop in the stanza posts and without one in
the collected poem. Two are wording:

| Stanza | Stanza post | Collected poem |
|---|---|---|
| 3 Thorn | "for all of the **thegns**" | "for all of the **attendants**" |
| 23 Home | "inspiration in the **hall**" | "inspiration in the **house**" |

## The variants point in opposite directions

The obvious reading — the later text is the revised one — does not survive
contact with the evidence. Each variant is the reading argued for in the
project's own philological post, but not by the same witness.

For stanza 3, "Translating Thorn" (2022-06-13) settles on the technical term
and keeps the Old English word in view:

> Let's worry about the þegna, the **thegns**. They set up camp at night,
> prepare food, tend to horses, fires. Get ordered around.

The stanza post, published the next day, reads *thegns*. The collected poem
still reads *attendants* — the plainer gloss, never updated.

For stanza 23 the direction reverses. "Translating Eþel" (2022-09-14) works
*bolde* out as a house, twice, and never once says *hall*:

> And where? In the bolde, in the **house**, the big one we all can fit into
> together.

Here it is the collected poem that carries *house* and the stanza post that
reads *hall*. The modification dates fit: the collected poem was last edited
2022-10-04, after the Eþel chapter ran; the stanza post was last touched
before its own publication.

So the two texts drifted apart in both directions, each picking up a revision
the other missed. Neither is uniformly the later text, and no single witness
is authoritative throughout.

## Copy-text

`book/rune-poem.md` sets the stanza posts as copy-text: they carry the
terminal punctuation the collected setting drops, and each stanza appears
there in the chapter that argued it out. Every disagreement is recorded in
an apparatus note at the stanza where it falls, so the other reading is never
lost — and for stanza 23 the note is where the better reading is.

## A correction to the corpus

The first pass of this collation reported **thirteen** differences, not five.
Eight were manufactured by our own harvester.

`tools/harvest.py` turned rendered HTML into text by replacing every tag with
a space. That is right for block tags and wrong for inline ones. The site's
editor wraps styled runs mid-word, so the corpus recorded

> Fruits fall, **p leasures** depart, **c ovenants** are betrayed.

where the page reads *pleasures* and *covenants*. The HTML is
`Fruits fall, p</span><span style="font-size: 12pt;">leasures`.

The fix distinguishes inline elements — `span`, `em`, `strong`, `a` and the
rest — which now vanish, from block elements, which still become spaces.
Re-harvesting changed **157 of 262 posts** and removed **1,362** spurious
word splits; the corpus word count falls from 87,304 to **85,942**, the
earlier figure having counted fragments as words.

The commonest casualty was the italicised title: `<em>Beowulf</em>.` had been
recording as "Beowulf ." throughout, which is why the bibliography was full
of floating full stops.

To be sure the changes were ours and not the site's, the *old* extractor was
re-run against the live site: it reproduces the previous corpus exactly,
all 262 posts, text and paragraphs. Every one of the 1,362 changes is the
fix.

## The site is still tended

A side observation from the harvest. Twenty-three posts carry a last-modified
date of 2026-01-18, and "The Middle" — the final post, the centre of the
book — was edited on **2026-02-06**, nearly three years after it was
published.

A single-day batch across 23 posts looks like maintenance rather than
revision, and a modification date alone says nothing about what changed. But
it is evidence against reading the site as abandoned: someone is still
there.
