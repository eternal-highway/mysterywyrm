# Letters for Titles — the two ciphers

The site says outright that it is written in code. The last post, "The
Middle," describes the plan: *"make it an instruction manual and a book of
divination, show its sounds and shapes and write it in code and hide stuff
in it like they used to do in Old English manuscripts."* The site's
header image carries one line of alt text on all 262 pages: **"Look close
and more will appear."**

Two codes are actually there. Both are carried by the artwork rather than
the prose, which is why a text-only reading of the corpus misses them.

- **Cipher 1 — the letter run.** Every post of the year-long run carries
  one numbered letter image. Ordered 1 → 261 they spell a single sentence.
  Decoded in full below; regenerate with `python3 tools/cipher.py`.
- **Cipher 2 — the rune code.** The drawings on the posts tagged *Rune
  Code* write text in twig runes: a stave with *a* twigs above and *b*
  below is the *b*-th rune of the *a*-th octave. One plate is decoded
  below; the rest are open.

---

## Cipher 1 — the letter run

### The mechanism

479 images are attached to the corpus. 216 of them carry a number in front
of the filename, and 214 of those name a single letter or a punctuation
mark:

```
254-M-harley-ms-3045-hrabanus-maurus-de-laudibus-sanctae-crusis-...jpg
27-period-letters-for-titles-vern-tonkin.jpg
261-Period-Letters-for-Titles-Vern-Tonkin.jpg
```

The numbers run 1–261 and each post of the run carries at most one. **261
is the length of the run** — 262 posts less "Alphybettyformed Verbage,"
the 2020 seed post that predates it. One slot per post, one post per slot.

The numbering is not publication order. It is the run **folded at its own
centre**, exactly as the book folds the poem at stanza 15:

- Slot 1 is **"Turn"** (2022-09-19) — the 22-word hinge post, and by count
  post **131 of 261**, the dead centre of the run.
- Odd slots walk forward in time from Turn: 3, 5, 7 … 261 ends on "The
  Middle" (2023-03-20), the last post.
- Even slots walk backward: 2, 4, 6 … 260 ends on "O Yes, W."
  (2022-03-21), the first.

So reading the letters in numerical order means reading the run inward
from both ends toward the middle — the same chiasm the chapters apply to
the poem (`research/structure.md`), applied here to the calendar.

`tools/cipher.py` derives each slot from a post's fold position rather than
from the number the author wrote on the file, which makes the three
filename slips visible and self-correcting: the files written `29-R`,
`79-N` and `142-M` belong at slots 39, 77 and 144, and the sentence
confirms it (they are the R of ARE, the N of IN and the M of MEMORIES).

### The message

216 of 261 slots are recovered. Every blank but two is a word space; the
two exceptions are fixed by the sentence:

> **LISTEN! COME TO THE MIRROR. SEE[?] YOU ARE SLIPPING AWAY. MOMENTARY.
> WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR CONSORT AND ONLY IN
> THE MEMORIES OF OTHERS WILL YOU PERSIST. WE ARE EACH OTHER'S ONLY
> IMMORTALITY ON EARTH, OTHERWISE EVERYTHING IS TEMPORARY.**

Notes on the reading:

- **Slot 78** — the missing R of WRITTEN — falls on the post titled
  **"R is for Riddle."**
- **Slot 182** — the missing E of WE — falls on "X≠Y≠Z: What is that?",
  whose two images are both unnumbered.
- **Slot 32** (post ᚷ) carries `32-Letters-for-Titles-Vern-Tonkin-1.gif`,
  numbered but not named for a letter. It sits between SEE and YOU, so it
  is a mark of punctuation of some kind; which one is unresolved.
- **Slot 194** carries `194-Twist-...jpg` and stands where the T of
  OTHER'S belongs — the letter is named for the book's centre chapter
  rather than for itself.
- **Slot 261**, the closing period, is "The Middle," the final post.
- The last clause is the title of the first chapter, *Everything is
  Temporary*, and the sentence as a whole restates that chapter's theme.
  "WRITTEN IN LIGHT" is the closing line of "The Middle": *"Write it in
  light, more fragile than paper, because everything is temporary."*

### Reproducing it

```sh
python3 tools/cipher.py           # message, coverage, the three numbering slips
python3 tools/cipher.py --table   # slot-by-slot: number, mark, date, post
```

It reads `data/corpus.json` only, and exits non-zero if the run is not 261
posts or "Turn" is not its centre.

---

## Cipher 2 — the rune code

### The key, stated on the site

The post **"Octave"** (2022-04-06, tagged *Code* and *Rune Code*) gives the
whole scheme:

> The runes are arranged in three rows of eight, three octaves, with a
> bunch of vowels tacked onto the end to get to 29 total. That's our number
> for it. We did that, numbering the runes 1 to 29. **The runes are really
> numbered a different way: by which octave it sits in and what place in
> it.** Feoh, Wealth is 1.1 … One octave away from Feoh at spot 2.1 is
> Hægl … one more octave away is 3.1 Tiw.

and then describes the notation:

> They used to play with rune code in manuscript drawings: they would hide
> coded meaning in main images and doodle it into the margins. A decoration
> might have one of something on this side and one on that side for F and
> so on, **a figure might show three fingers on one hand and five on the
> other for the letter L** and be grouped with others to spell out a word.
> The runes hold a numeric code, hidden in plain sight.

Three and five is Lagu, rune 21, the fifth of the third octave: 3.5 = L.
This is the manuscript practice of twig runes (*kvistrúnir*) — a stave with
*a* twigs on one side and *b* on the other, addressing rune *a.b*. The
project's own dictionary entry ("L is for Letters for Titles") calls the
poem's runes *"three octaves with an amended quintet"*: the five late
vowels form a short fourth group.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **1.** | Feoh F | Ur U | Thorn TH | Os O | Rad R | Cen C | Gifu G | Wyn W |
| **2.** | Hægl H | Nyd N | Is I | Ger J | Eoh EO | Peorþ P | Eolhx X | Sigel S |
| **3.** | Tiw T | Beorc B | Eh E | Mann M | Lagu L | Ing NG | Eþel OE | Dæg D |
| **4.** | Ac A | Æsc Æ | Yr Y | Ior IO | Ear EA | | | |

`python3 tools/cipher.py --key` prints this table.

### The plates

Seventeen posts are tagged **Rune Code**. Fourteen are wordless: the post
is the drawing. The drawn objects vary — barbed arrows, fir trees, rows of
wrapped presents, a curling tree — but each object is one stave carrying a
count above and below (or left and right of) its spine.

| Date | Post | Drawing |
|---|---|---|
| 2022-04-06 | Octave | (the key itself) |
| 2022-04-11 | Everything is Temporary | |
| 2022-05-05 | Axaxaxas mlö | grotesque alphabet |
| 2022-06-06 | **Arrows** | barbed arrows — **decoded, below** |
| 2022-06-07 | For Anybody Who Rests With Them | |
| 2022-06-24 | Shh | branching tree |
| 2022-07-19 | The Way | fir trees |
| 2022-09-05 | Present | rows of wrapped presents |
| 2022-09-12 | Œ is for Œdipean Riddle | |
| 2022-10-27 | Soon After it Becomes Water | |
| 2022-11-22 | You Knew it Beforehand | |
| 2022-12-09 | Friþ | |
| 2023-01-03 | Bright Fruits | |
| 2023-01-26 | It Never Deceives | |
| 2023-02-20 | Always | |
| 2023-02-24 | Battle | |
| 2023-03-14 | Loop | |

"Twigs for Divination" (2023-01-04) is untagged but draws the same staves.

### One plate decoded: "Arrows"

`Arrows-Letters-for-titles-verntonkin-1.jpg` (1080×1080, a photograph of a
notebook) holds seven lines of arrows. Each arrow is a stave: twigs above
the shaft give the octave, twigs below give the place in it. The facing
page of the notebook, caught in the photograph, is the author's own
working key — **T 3.1, O 1.4, A 4.1** — which fixes the direction of the
reading and confirms the fourth group.

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

The page is headed **"Par 17.27"**: Dante, *Paradiso* XVII.27, *"ché
saetta previsa vien più lenta."* Cacciaguida's line about foreknowledge,
in a chapter (*They'll Cut You*, stanzas 3 Thorn + 27 Bow) about arrows.
Dante is all over the project's bibliography and tags, and the post
immediately after this one, "For Anybody Who Rests With Them," continues
the same thought.

Two letters are drawn as Roman letters rather than staves: **V** in
ARRIVES (the futhorc has no V) and the final **Y** of SLOWLY. Counts of
five and above are readable but tight at 1080px; the counts above are read
from 4–8× crops of the original.

### What is open

- The other sixteen plates are undecoded. The full-resolution originals
  are not in git (`data/media.json` has their URLs and checksums;
  `python3 tools/archive.py --variant full` materializes them).
- Several plates carry a page number or citation in the corner, as
  "Arrows" carries *Par 17.27* — worth transcribing first, since it names
  the source of the quotation.
- The relationship between the two ciphers is only partly clear: they run
  on the same posts (the "Arrows" post carries both `150-E`, cipher 1's
  slot 150, and the twig plate) but say different things. Whether the
  rune-code plates form one continuous text in some order, or are
  seventeen separate epigraphs, is unresolved.
