# Separate source support for the conditional key

This support was identified after the independent observations were frozen.
It is not retroactive evidence that hidden Loop inscriptions were directly read.
Gate 0 remains conditional; Outcome B is not asserted.

The author's [Octave prose](https://lettersfortitles.com/octave/) explicitly
describes three successive groups of eight, followed by the remaining vowels,
and explains indexing by group and position. This is an independent authored
statement of the grouping rule, rather than an inference solely from visible
Loop cells or the harvest's transcription table.

The site's numbered stanza pages independently associate ordinals, rune names
in their tags, and the corresponding poem text. Applying that stated rule to
these source ordinals gives:

| Source | Ordinal | Rune identification | Derived coordinate |
|---|---:|---|---|
| [Stanza 14: The Game](https://lettersfortitles.com/the-game/) | 14 | Peorð / P (normalized Peorth) | 2.6 |
| [Stanza 15: Helix](https://lettersfortitles.com/stanza-15-helix/) | 15 | Eolhx / X | 2.7 |
| [Stanza 16: Sun](https://lettersfortitles.com/sun/) | 16 | Sigel / S | 2.8 |
| [Stanza 23: Home](https://lettersfortitles.com/stanza-23-home/) | 23 | Eþel / Œ (normalized Ethel) | 3.7 |

Calculation: `group = floor((ordinal - 1) / 8) + 1` and
`position = ((ordinal - 1) mod 8) + 1`. The identification is source-based;
the coordinate is an explicitly disclosed deduction from the author's rule.
This meets the approved exception's requirement for separately identified
source support. It does not establish whether an individual plate uses a
particular glyph or traversal, and cannot repair an uncertain count.

The five archived HTML sources were checked against canonical URLs, displayed
titles, and unique body anchors. Their exact hashes, sizes, and retained tags
are in `key-corroboration-sources.json`. `data/corpus.json` was used to locate
the pages; the source HTML was then checked. These are retained historical
captures, not new live captures. The sources come from the same author/site:
this is separate authored evidence, not independent authorship.

All decoded occurrences of these four coordinates retain a marker in the
results. The marker now means **supported by this explicit source derivation**,
rather than silently promoted to a directly observed Loop cell.
