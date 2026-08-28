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

## Contents

| Path | What it is |
|---|---|
| `research/structure.md` | The architecture: chiastic pairing, chapter template, cadence |
| `research/archive.md` | What is preserved, what is not, and why |
| `research/bibliography.md` | The 375-entry bibliography, summarized |
| `book/reading-order.md` | The whole work reassembled in book order |
| `book/poem-order.md` | The alternate cut: all 29 stanzas in futhorc order |
| `archive/pages/` | Rendered HTML of all 262 posts |
| `archive/thumbs/` | 300px reference copies of all 479 images |
| `data/corpus.json` | Every post: text, dates, chapters, tags, image and outbound links |
| `data/media.json` | Manifest of the full-resolution originals, with SHA-256 |
| `data/bibliography.json` | The bibliography, parsed and classified |

## Tools

All four use only the Python standard library and are safe to re-run
(downloads resume, nothing is re-fetched needlessly).

```sh
python3 tools/harvest.py        # rebuild data/corpus.json from the site's REST API
python3 tools/structure.py      # re-derive the architecture; non-zero exit on mismatch
python3 tools/archive.py        # refresh archive/thumbs, archive/pages, data/media.json
python3 tools/bibliography.py   # reparse the bibliography
python3 tools/book.py           # regenerate book/ from the corpus
```

The 479 full-resolution images total 742 MB and are deliberately not in git.
`data/media.json` carries their checksums so any copy can be verified;
`tools/archive.py --variant full` materializes them. See
[`research/archive.md`](research/archive.md).

## Rights

A research and preservation copy of work by Vern Tonkin. Copyright remains
with the author; every assembled post links back to its source.
