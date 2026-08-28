# mysterywyrm

Research on **Letters for Titles** — <https://www.lettersfortitles.com> — an
alphabet book by Vern Tonkin built on the 29-stanza Old English Rune Poem.

## Contents

| Path | What it is |
|---|---|
| `research/structure.md` | Findings: the corpus's chiastic architecture and chapter template |
| `data/corpus.json` | All 262 posts, normalized (text, dates, chapters, tags, links) |
| `tools/harvest.py` | Rebuilds `data/corpus.json` from the site's WordPress REST API |
| `tools/structure.py` | Re-derives and checks every structural claim; non-zero exit on mismatch |

## Reproducing

```sh
python3 tools/harvest.py      # refetch the corpus  -> data/corpus.json
python3 tools/structure.py    # verify the architecture
```

Both use only the Python standard library.

## Headline finding

The site looks abandoned — posts stop in March 2023 — but it is complete.
Its chapters pair the Rune Poem's stanzas from both ends inward, every pair
summing to 30 (1+29, 2+28, … 14+16), leaving stanza 15 unpaired at the
center. The work ends on a post called "The Middle" because it arrived
there. See `research/structure.md`.
