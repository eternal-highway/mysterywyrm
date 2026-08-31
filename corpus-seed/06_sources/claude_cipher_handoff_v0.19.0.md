# Handoff: two ciphers in *Letters for Titles*

Paste-ready brief for another assistant (ChatGPT). Everything here is
established from a full harvest of the site; the open questions are marked
as open. Source repo: `mysterywyrm` (`research/ciphers.md`,
`tools/cipher.py`).

---

## 1. What the site is

*Letters for Titles* — <https://www.lettersfortitles.com> — is an alphabet
book by **Vern Tonkin** built on the Old English Rune Poem (29 stanzas, one
per rune). It was published as a WordPress blog: **262 posts**, one per
weekday for a year, **2022-03-21 → 2023-03-20**, plus one seed post from
2020. Every post carries at least one image; there are 479 images in all.
85,942 words.

It looks abandoned. It is finished. Three things you need to know about
its shape, because both ciphers depend on them:

1. **The book is a chiasm.** Its chapters pair stanza *n* with stanza
   *30−n* — 1+29, 2+28, … 14+16 — reading the poem inward from both ends
   at once. Stanza **15** (*eolhx*, "Helix") has no partner and stands
   alone at the centre, in a half-length chapter called *Twist*. The
   author states this plan in the 2020 seed post and again in the final
   post, "The Middle."
2. **The centre is the point.** *Eolhx* is the one rune name in the poem
   that occurs nowhere else in Old English and cannot be translated. A
   project organized around translating all 29 stanzas converges by
   construction on the one word that resists translation.
3. **The site says it is written in code.** From the last post: *"make it
   an instruction manual and a book of divination, show its sounds and
   shapes and write it in code and hide stuff in it like they used to do
   in Old English manuscripts."* The site header's alt text, on all 262
   pages: **"Look close and more will appear."**

Both ciphers are carried by the **artwork and its filenames**, not by the
prose. A text-only reading of the corpus misses both.

---

## 2. Cipher 1 — the letter run (solved)

### Mechanism

216 of the 479 images carry a number in front of their filename, and 214
of those name a single letter or a punctuation mark:

```
254-M-harley-ms-3045-hrabanus-maurus-de-laudibus-sanctae-crusis-....jpg
7-exclamation-point-letters-for-titles-vern-tonkin.jpg
261-Period-Letters-for-Titles-Vern-Tonkin.jpg
```

The numbers run **1–261**, and 261 is the length of the run (262 posts
minus the 2020 seed post). One numbered image per post, one post per slot.

**The numbering is the run folded at its own centre**, not publication
order:

- Slot **1** is the post **"Turn"** (2022-09-19) — a 22-word hinge post,
  and by count post **131 of 261**, the exact middle of the run.
- **Odd** slots walk *forward* in time from Turn (3, 5, 7 …); slot **261**
  is "The Middle" (2023-03-20), the last post.
- **Even** slots walk *backward* (2, 4, 6 …); slot **260** is "O Yes, W."
  (2022-03-21), the first.

So reading the letters 1 → 261 means reading the year inward from both
ends toward the middle: the same fold the chapters apply to the poem,
applied to the calendar. Three filenames are misnumbered by the author
(`29-R`, `79-N`, `142-M` belong at slots 39, 77, 144); deriving each slot
from the post's fold position instead of the filename resolves them, and
the sentence confirms the correction.

### The message

216 slots recovered of 261. Every blank but two is a word space:

> **LISTEN! COME TO THE MIRROR. SEE[?] YOU ARE SLIPPING AWAY. MOMENTARY.
> WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR CONSORT AND ONLY IN
> THE MEMORIES OF OTHERS WILL YOU PERSIST. WE ARE EACH OTHER'S ONLY
> IMMORTALITY ON EARTH, OTHERWISE EVERYTHING IS TEMPORARY.**

Details worth keeping:

- Slot **78**, the missing R of WRITTEN, falls on the post titled **"R is
  for Riddle."**
- Slot **182**, the missing E of WE, falls on "X≠Y≠Z: What is that?".
- Slot **32** is numbered but not named for a letter
  (`32-Letters-for-Titles-Vern-Tonkin-1.gif`); it sits between SEE and
  YOU, so it is punctuation of some kind — **which mark is open**.
- Slot **194** is `194-Twist-...jpg` and stands where the T of OTHER'S
  belongs: the letter is named for the book's centre chapter.
- Slot **261**, the closing period, is the final post, "The Middle."
- "WRITTEN IN LIGHT" quotes that post's last line; "EVERYTHING IS
  TEMPORARY" is the title of the first chapter.

### Verify it

`python3 tools/cipher.py` in the repo rebuilds the message from
`data/corpus.json` alone and prints coverage, the blanks, and the three
numbering slips. `--table` dumps the slot-by-slot table.

---

## 3. Cipher 2 — the rune code (mechanism solved, one plate of ~17 read)

### The key, given openly on the site

The post **"Octave"** (2022-04-06) states it:

> The runes are arranged in three rows of eight, three octaves, with a
> bunch of vowels tacked onto the end to get to 29 total. … **The runes
> are really numbered a different way: by which octave it sits in and what
> place in it.** Feoh, Wealth is 1.1 … One octave away from Feoh at spot
> 2.1 is Hægl … one more octave away is 3.1 Tiw.

and the notation:

> They used to play with rune code in manuscript drawings … A decoration
> might have one of something on this side and one on that side for F and
> so on, **a figure might show three fingers on one hand and five on the
> other for the letter L** … The runes hold a numeric code, hidden in
> plain sight.

Three-and-five is Lagu (rune 21, third octave, fifth place) = **L**. This
is the manuscript practice of **twig runes** (*kvistrúnir*): a stave with
*a* twigs on one side and *b* on the other spells rune *a.b*. The
project's own dictionary entry calls the poem "three octaves with an
amended quintet" — the five late vowels are a short fourth group.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **1.** | Feoh F | Ur U | Thorn TH | Os O | Rad R | Cen C | Gifu G | Wyn W |
| **2.** | Hægl H | Nyd N | Is I | Ger J | Eoh EO | Peorþ P | Eolhx X | Sigel S |
| **3.** | Tiw T | Beorc B | Eh E | Mann M | Lagu L | Ing NG | Eþel OE | Dæg D |
| **4.** | Ac A | Æsc Æ | Yr Y | Ior IO | Ear EA | | | |

### Where it is written

**Seventeen posts are tagged "Rune Code."** Fourteen of them have no text
at all: the post *is* the drawing. The drawn objects differ — barbed
arrows, fir trees, rows of wrapped presents, a curling tree — but each
object is one stave with a count above and below (or left and right of)
its spine.

Octave · Everything is Temporary · Axaxaxas mlö · **Arrows** · For Anybody
Who Rests With Them · Shh · The Way · Present · Œ is for Œdipean Riddle ·
Soon After it Becomes Water · You Knew it Beforehand · Friþ · Bright
Fruits · It Never Deceives · Always · Battle · Loop. ("Twigs for
Divination," 2023-01-04, is untagged but draws the same staves.)

### The one plate read so far: "Arrows" (2022-06-06)

`Arrows-Letters-for-titles-verntonkin-1.jpg` — a photograph of a notebook,
seven rows of arrows. Twigs above the shaft = octave, twigs below = place.
The facing notebook page, caught in the same photograph, is the author's
own working key: **T 3.1, O 1.4, A 4.1** — which fixes the reading
direction and confirms the fourth group.

```
row 1   3.1 2.1 3.3                            THE
row 2   4.1 1.5 1.5 1.4 1.8                    ARROW
row 3   1.4 2.2 3.3                            ONE
row 4   1.1 1.4 1.5 3.3 2.8 3.3 3.3 2.8        FORESEES
row 5   4.1 1.5 1.5 2.3 [V] 3.3 2.8            ARRIVES
row 6   3.4 1.4 1.5 3.3                        MORE
row 7   2.8 3.5 1.4 1.8 3.5 [Y]                SLOWLY
```

> **THE ARROW ONE FORESEES ARRIVES MORE SLOWLY**

The page is headed **"Par 17.27"** — Dante, *Paradiso* XVII.27, *"ché
saetta previsa vien più lenta"* — in a chapter about arrows (*They'll Cut
You*: stanza 3 Thorn + stanza 27 Bow). V and the final Y are drawn as
Roman letters, not staves (the futhorc has no V).

Practical notes for reading the others: work from the **full-resolution
originals** (the site serves them under `/wp-content/uploads/YYYY/MM/`;
`data/media.json` lists every URL with a SHA-256, and
`python3 tools/archive.py --variant full` fetches them — 479 files, 742
MB, deliberately not in git). Counts of 5+ need a 4–8× crop to separate.
Transcribe any page number or citation in the corner first: on "Arrows"
it named the source before a single letter was read.

---

## 4. What we would like help with

1. **Decode the remaining rune-code plates** — "The Way" (fir trees) and
   "Present" (rows of presents) are the most legible after "Arrows."
2. **Establish whether the plates form one continuous text** in some order
   (publication order? the fold order that governs cipher 1?) or are
   seventeen separate epigraphs. Each of the four decoded-or-visible
   headers is a citation, which hints at epigraphs.
3. **Resolve slot 32 of cipher 1** — the numbered but unlettered gif
   between SEE and YOU.
4. **Third layer?** Cipher 1 and cipher 2 run on the same posts (the
   "Arrows" post carries both `150-E`, cipher 1's slot 150, and the twig
   plate) but say different things. Whether anything further is keyed on
   the 45 slots that carry no letter — or on the X≠Y≠Z strand, which is
   the one post-series with no obvious role in either cipher — is open.

Two cautions. First, the corpus is the evidence: claims about the site
should be checkable against `data/corpus.json` (every post's text, dates,
tags, image URLs) rather than reconstructed from memory of the site.
Second, don't take the WordPress reading order at face value — an archive
lists newest first, so a visitor lands on "The Middle" and reads backwards
out of the centre. `book/reading-order.md` has the work in built order.
