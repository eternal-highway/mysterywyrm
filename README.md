# mysterywyrm

Research on **Letters for Titles** — <https://www.lettersfortitles.com> — an
alphabet book by Vern Tonkin built on the 29-stanza Old English Rune Poem.

## The finding

The site looks abandoned: 262 posts, then nothing after March 2023. It is
not. Its chapters read the Rune Poem inward from **both ends at once**,
pairing stanza *n* with stanza *30−n* — 1+29, 2+28, … 14+16 — which leaves
stanza 15 alone at the centre. The run ends on a post called "The Middle"
because it arrived there. All 29 stanzas, 29 rune castings and 29
translations are present; the work is complete.

The center is chosen, not incidental: stanza 15's rune, *eolhx*, is the one
name in the poem that appears nowhere else in Old English and cannot be
translated. A project organized around translating all 29 stanzas converges
by construction on the single word that resists it.

The author states this plan in the earliest post (2020) and again in the
last (2023). See [`research/structure.md`](research/structure.md).

## The poem itself

The corpus carries Tonkin's translation **twice** — once as the 29
`Stanza N:` posts that close each chapter, and once entire in "O Yes, W.",
posted four days before the run began. Collating them, all 29 Old English
texts agree character-for-character; the translations differ in five places,
two of them real changes of wording. The variants run in *both* directions,
so neither setting is simply the later one. The assembled facing text is
[`book/rune-poem.md`](book/rune-poem.md); the collation is
[`research/edition.md`](research/edition.md).

## The message in the filenames

Every image uploaded for the run is named `N-C-slug.ext` — a position from 1
to 261, then a single character. Sorted by position, the 479 filenames spell
one sentence:

> **LISTEN! COME TO THE MIRROR. SEE? YOU ARE SLIPPING AWAY. MOMENTARY.
> WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR CONSORT AND ONLY IN
> THE MEMORIES OF OTHERS WILL YOU PERSIST. WE ARE EACH OTHER'S ONLY
> IMMORTALITY ON EARTH, OTHERWISE EVERYTHING IS TEMPORARY.**

The numbering is laid down chiastically, like the chapters, but running the
other way: posts 1–130 carry the even positions counting *down* from 260,
and posts 131–261 carry the odd positions counting *up* from 1. The message
is written from the outside in and read from the inside out. The pivot is
post 131, titled "Turn". The last post, "The Middle", carries the full stop.
See [`research/cipher.md`](research/cipher.md).

## The other cipher

Seventeen posts tagged `Rune Code` carry no text at all, only photographs:
**branch runes**, two counts giving the ætt of the futhorc and the position
within it, redrawn from scratch in a new costume every time — fletched arrows,
one tree, a forest of firs, wrapped gifts, faces and skulls, rose thorns,
snowflakes, rowan berries, dominoes and dice, suns, birthday candles, ice cubes
melting on hot paving. Where the futhorc has no letter — V, K, Y — the plate
simply writes the Latin one in among the runes.

All seventeen now read. Sixteen carry a message, fifteen of them whole; the
sixteenth is written in ice and only three of its four lines survive. The
seventeenth, *Loop*, turns out not to be a message at all but Tonkin's
own worked table of the whole cipher, twenty-nine cells in quilled paper, with
rune 15 — *eolhx*, the untranslatable centre — glossed **"Helix"** and given
the only three-dimensional objects on the board. And the *Octave* post states
the key outright in prose, in the clear, in 2022.

The messages answer their own plates. *Arrows*, headed `Par 17.27`, reads
**THE ARROW ONE FORESEES ARRIVES MORE SLOWLY**. *Shh* reads **LISTEN**. *The
Way* reads **THE MAIN ROAD IS SMOOTH YET PEOPLE LOVE TO BE SIDETRACKED** — Tao
Te Ching 53, on notebook page 53. *Present* reads **YOU HAVE NOTHING ELSE**,
and its V, the letter with no rune, is drawn as a present with nothing in it.
*Battle* reads **TO THE DEATH** in dominoes. *Friþ* reads **PEACE** in
snowflakes.

The last one read is the barest — no costume at all, just tally strokes with a
serpentine coiled through them, on notebook page 55. It is the longest message
on any plate, and it is Borges: **YOU WHO READ ME — ARE YOU CERTAIN YOU
UNDERSTAND MY LANGUAGE?** The post is titled *Axaxaxas mlö*, the unreadable
book in *The Library of Babel*, and the sentence is that story's own question,
ciphered in the least legible hand on the site.

The best of them is a GIF. *Everything is Temporary* is drawn in birthday
candles and reads **EVERYTHING IS TEMPORARY** — and over thirty-seven frames
the flames go out, one by one, until the page is nothing but bare candles.

And one plate destroyed itself as it was made. *Soon After it Becomes Water*
is laid out in ice cubes on hot paving, and the sun reached it from the top
down: its first line had melted into one continuous sheet of water before the
shutter opened and cannot be recovered, while the three lines still on dry
stone read **LET US MELT**. See
[`research/rune-code.md`](research/rune-code.md).

## Contents

| Path | What it is |
|---|---|
| `research/structure.md` | The architecture: chiastic pairing, chapter template, cadence |
| `research/cipher.md` | The sentence hidden across the image filenames, and its index |
| `research/rune-code.md` | The branch-rune plates: the system, the key, and all seventeen read |
| `research/relevance.md` | A reflection on the completed work and agent-harness design |
| `research/edition.md` | The poem collated across its two witnesses; a corpus correction |
| `research/archive.md` | What is preserved, what is not, and why |
| `research/bibliography.md` | The 375-entry bibliography, summarized |
| `book/rune-poem.md` | The 29 stanzas: Old English against Tonkin's translation |
| `book/reading-order.md` | The whole work reassembled in book order |
| `book/poem-order.md` | The alternate cut: all 29 stanzas in futhorc order |
| `archive/pages/` | Rendered HTML of all 262 posts |
| `archive/thumbs/` | 300px reference copies of all 479 images |
| `data/corpus.json` | Every post: text, dates, chapters, tags, image and outbound links |
| `data/media.json` | Manifest of the 479 300px archive copies, with SHA-256 |
| `data/media-full.json` | Manifest of the 479 full-resolution originals, with SHA-256 |
| `data/media-code.json` | Subset manifest for 31 full-resolution images from the 17 Rune Code posts |
| `data/bibliography.json` | The bibliography, parsed and classified |

## Tools

The first seven use only the Python standard library and are safe to re-run
(downloads resume, nothing is re-fetched needlessly). `branch.py` and
`tally.py` are reading aids rather than checks, and are the two tools that
need Pillow and numpy.

```sh
python3 tools/harvest.py        # rebuild data/corpus.json from the site's REST API
python3 tools/structure.py      # re-derive the architecture; non-zero exit on mismatch
python3 tools/archive.py        # refresh archive/thumbs, archive/pages, data/media.json
python3 tools/bibliography.py   # reparse the bibliography
python3 tools/book.py           # regenerate book/ from the corpus
python3 tools/edition.py        # collate the poem's two witnesses; write book/rune-poem.md
python3 tools/cipher.py         # recover the filename message; non-zero exit on mismatch
python3 tools/branch.py PLATE   # count the twigs on a branch-rune plate
python3 tools/tally.py PLATE    # read the tally-and-serpentine plate (page 55)
```

The 479 full-resolution images total 742 MB and are deliberately not in git.
`data/media-full.json` carries their checksums, and
`tools/archive.py --variant full` materializes them. See
[`research/archive.md`](research/archive.md).

Note that `data/media.json` is the manifest of what `archive/thumbs/` actually
holds — the 300px copies — so its checksums verify those, not the originals.
`data/media-code.json` remains the smaller full-resolution subset for the 31
images attached to the 17 Rune Code posts; all 31 entries agree exactly with
the full manifest.

## Rights

A research and preservation copy of work by Vern Tonkin. Copyright remains
with the author; every assembled post links back to its source.
