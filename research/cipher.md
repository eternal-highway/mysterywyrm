# The message in the filenames

Every image uploaded for the run is named `N-C-slug.ext`: a position
from 1 to 261, then a single character. Punctuation is spelled out
(`period`, `Comma`, `apostrophe`, `exclamation`) because a filename
cannot carry `.` or `'` through an upload path. Sorted by position the
characters spell one sentence; positions with no numbered image are the
spaces between the words.


> **LISTEN! COME TO THE MIRROR. SEE? YOU ARE SLIPPING AWAY. MOMENTARY. WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR CONSORT AND ONLY IN THE MEMORIES OF OTHERS WILL YOU PERSIST. WE ARE EACH OTHER'S ONLY IMMORTALITY ON EARTH, OTHERWISE EVERYTHING IS TEMPORARY.**


213 of the 261 positions carry a numbered image and 211 characters are
recovered directly from filenames. `tools/cipher.py` rebuilds this from
`data/corpus.json` and exits non-zero if it stops holding.


## How it is laid down

The numbering runs chiastically, exactly as the chapters read the Rune
Poem inward from both ends — but in the opposite direction, so that the
message is *written* from the outside in and *read* from the inside out.


| arm | posts | positions | direction |
|---|---|---|---|
| even | 1–130 | 260 → 2 | descending |
| odd | 131–261 | 1 → 261 | ascending |

No post carries both parities. The pivot is post #131, **“Turn”** (2022-09-19) —
the 22-word hinge that sits in the `Hwat` front matter and belongs to no
chapter. It carries position 1, the `L` of LISTEN, and its entire text is
Dante at the foot of the hill:


> He did not disappear from sight, but stayed; indeed he so impeded my ascent that I had often to turn back again.


The run's final post, **“The Middle”**, carries position 261: the full
stop that closes the sentence. The run's fourth post, three days in, is
titled **“Decode”**, has no text at all, and is tagged `Code`.


The sentence ends on **“EVERYTHING IS TEMPORARY”**, which is the name of
the first chapter, and opens on **“LISTEN!”**, the usual rendering of
*Hwæt* — the name of the category holding the front matter. The message
closes the same loop the chapters do.


## Strays and gaps

Three positions carry two files. Each stray sits a short distance from a
position whose character is missing entirely — an off-by-N slip in the
author's own numbering — so each resolves into the gap it belongs in.


| position | kept | stray | resolution |
|---|---|---|---|
| 29 | `S` | `R` | stray; 'MIRROR. SEE' needs S |
| 79 | `L` | `N` | stray N belongs at 77, the N of IN |
| 142 | `E` | `M` | stray M belongs at 144, the M of MEMORIES |

7 positions carry no character of their own:

- **32** — `32-Letters-for-Titles-...gif` names no character because none can be named — the glyph is `?`, the one mark that cannot sit in a URL, since it opens the query string. The image *is* the question mark, drawn as an illuminated interlace initial.
- **39** — no file; context gives R (ARE)
- **69** — no file; context gives R (WRITTEN)
- **77** — no file; context gives N (IN) -- see the stray at 79
- **144** — no file; context gives M (MEMORIES) -- see the stray at 142
- **182** — no file; context gives E (WE)
- **194** — file `194-Twist-...` names the centre chapter where T is due

## The index


| pos | char | source | post | date |
|---|---|---|---|---|
| 1 | `L` | filename | Turn | 2022-09-19 |
| 2 | `I` | filename | Stanza 7: Gift | 2022-09-16 |
| 3 | `S` | filename | Stanza 23: Home | 2022-09-20 |
| 4 | `T` | filename | Translating Gifu | 2022-09-15 |
| 5 | `E` | filename | ᛝ | 2022-09-21 |
| 6 | `N` | filename | Translating Eþel | 2022-09-14 |
| 7 | `!` | filename | ᚹ | 2022-09-22 |
| 9 | `C` | filename | Rune Casting: Ing | 2022-09-23 |
| 10 | `O` | filename | Œ is for Œdipean Riddle | 2022-09-12 |
| 11 | `M` | filename | Rune Casting: Wyn | 2022-09-26 |
| 12 | `E` | filename | Gift Riddle | 2022-09-09 |
| 14 | `T` | filename | X≠Y≠Z: Z’s Lament | 2022-09-08 |
| 15 | `O` | filename | Ing is for Scylding | 2022-09-28 |
| 17 | `T` | filename | W is for Ƿ | 2022-09-29 |
| 18 | `H` | filename | I Sing This Wretched Song | 2022-09-06 |
| 19 | `E` | filename | X≠Y≠Z: No Z | 2022-09-30 |
| 21 | `M` | filename | Prosperity | 2022-10-03 |
| 22 | `I` | filename | G is for Go | 2022-09-02 |
| 23 | `R` | filename | Bliss | 2022-10-04 |
| 24 | `R` | filename | How to Summon an Angel | 2022-09-01 |
| 25 | `O` | filename | All in All | 2022-10-05 |
| 26 | `R` | filename | Rune Casting: Eþel | 2022-08-31 |
| 27 | `.` | filename | Ing is for Nerþus | 2022-10-06 |
| 29 | `S` | filename | How to be Happy | 2022-10-07 |
| 30 | `E` | filename | ᛟ | 2022-08-29 |
| 31 | `E` | filename | Translating Wyn | 2022-10-10 |
| 32 | `?` | context | — | — |
| 34 | `Y` | filename | Stanza 6: Torch | 2022-08-25 |
| 35 | `O` | filename | Stanza 22: Ing | 2022-10-12 |
| 36 | `U` | filename | Stanza 24: Day | 2022-08-24 |
| 38 | `A` | filename | Translating Dæg | 2022-08-23 |
| 39 | `R` | context | — | — |
| 40 | `E` | filename | Translating Cen | 2022-08-22 |
| 42 | `S` | filename | How to Burn the Cotton Library | 2022-08-19 |
| 43 | `L` | filename | Rune Casting: Hægl | 2022-10-18 |
| 44 | `I` | filename | D is for Dark | 2022-08-18 |
| 45 | `P` | filename | Rune Casting: Lagu | 2022-10-19 |
| 46 | `P` | filename | How to make a Torch | 2022-08-17 |
| 47 | `I` | filename | How to Survive a Tornado | 2022-10-20 |
| 48 | `N` | filename | Or are you both? | 2022-08-16 |
| 49 | `G` | filename | H is for Hægl | 2022-10-21 |
| 51 | `A` | filename | X≠Y≠Z: (X+Y)-Z=(X-Y)÷Z | 2022-10-24 |
| 52 | `W` | filename | Night Riddle | 2022-08-12 |
| 53 | `A` | filename | A Horrible Wonder | 2022-10-25 |
| 54 | `Y` | filename | X≠Y≠Z: Contraries and Negations | 2022-08-11 |
| 55 | `.` | filename | The Water Cycle | 2022-10-26 |
| 57 | `M` | filename | Soon After it Becomes Water | 2022-10-27 |
| 58 | `O` | filename | How to Burn it All Down | 2022-08-09 |
| 59 | `M` | filename | H is for Hwat is it | 2022-10-28 |
| 60 | `E` | filename | Rune Casting: Dæg | 2022-08-08 |
| 61 | `N` | filename | L is for Letters for Titles | 2022-10-31 |
| 62 | `T` | filename | Rune Casting: Cen | 2022-08-05 |
| 63 | `A` | filename | How to Go Overboard | 2022-11-01 |
| 64 | `R` | filename | ᚳ | 2022-08-04 |
| 65 | `Y` | filename | Translating Lagu | 2022-11-02 |
| 66 | `.` | filename | ᛞ | 2022-08-03 |
| 68 | `W` | filename | Stanza 25: Oak | 2022-08-02 |
| 69 | `R` | context | — | — |
| 70 | `I` | filename | Stanza 5: The Ride | 2022-08-01 |
| 71 | `T` | filename | Stanza 21: The Sea | 2022-11-07 |
| 72 | `T` | filename | Translating Rad | 2022-07-29 |
| 73 | `E` | filename | ᛗ | 2022-11-08 |
| 74 | `N` | filename | Translating Ac | 2022-07-28 |
| 76 | `I` | filename | How to Make Ink | 2022-07-27 |
| 77 | `N` | context | — | — |
| 79 | `L` | filename | Rune Casting: Nyd | 2022-11-11 |
| 80 | `I` | filename | Crann Bethadh | 2022-07-25 |
| 81 | `G` | filename | How to Hold it Together | 2022-11-14 |
| 82 | `H` | filename | How to Bathe a Gannet | 2022-07-22 |
| 83 | `T` | filename | N is for ‘N | 2022-11-15 |
| 84 | `.` | filename | By Land and By Sea | 2022-07-21 |
| 86 | `Y` | filename | X≠Y≠Z: Are we there yet? | 2022-07-20 |
| 87 | `O` | filename | Life and Death | 2022-11-17 |
| 88 | `U` | filename | The Way | 2022-07-19 |
| 90 | `H` | filename | A is for Golem Aleph | 2022-07-18 |
| 91 | `A` | filename | ꝥ | 2022-11-21 |
| 92 | `V` | filename | How to Measure a Mile | 2022-07-15 |
| 93 | `E` | filename | You Knew it Beforehand | 2022-11-22 |
| 95 | `C` | filename | M is for Mortality | 2022-11-23 |
| 96 | `H` | filename | Rune Casting: Rad | 2022-07-13 |
| 97 | `O` | filename | How to Listen Beforehand | 2022-11-24 |
| 98 | `S` | filename | ᚱ | 2022-07-12 |
| 99 | `E` | filename | Translating Nyd | 2022-11-25 |
| 100 | `N` | filename | ᚪ | 2022-07-11 |
| 102 | `T` | filename | Stanza 4: God | 2022-07-08 |
| 103 | `H` | filename | Stanza 20: Human | 2022-11-29 |
| 104 | `E` | filename | Stanza 26: Ash | 2022-07-07 |
| 106 | `E` | filename | Translating Æsc | 2022-07-06 |
| 107 | `A` | filename | ᛖ | 2022-12-01 |
| 108 | `R` | filename | Translating Os | 2022-07-05 |
| 109 | `T` | filename | ᛁ | 2022-12-02 |
| 110 | `H` | filename | How to Talk to God | 2022-07-04 |
| 112 | `A` | filename | Æ is for George William Russell | 2022-07-01 |
| 113 | `S` | filename | Rune Casting: Is | 2022-12-06 |
| 115 | `Y` | filename | How to Listen to a Horse | 2022-12-07 |
| 116 | `O` | filename | Truth | 2022-06-29 |
| 117 | `U` | filename | I is for Iceland Spar | 2022-12-08 |
| 118 | `R` | filename | Axis Mundi | 2022-06-28 |
| 120 | `C` | filename | The Ogam Ash Tree | 2022-06-27 |
| 121 | `O` | filename | How to Stab Somebody with an Icicle | 2022-12-12 |
| 122 | `N` | filename | Shh | 2022-06-24 |
| 123 | `S` | filename | War and Peace | 2022-12-13 |
| 124 | `O` | filename | O is for Apostrophe | 2022-06-23 |
| 125 | `R` | filename | Hildegicel | 2022-12-14 |
| 126 | `T` | filename | X≠Y≠Z: How to Punch a Tree | 2022-06-22 |
| 128 | `A` | filename | Rune Casting: Æsc | 2022-06-21 |
| 129 | `N` | filename | E is for ⁊ | 2022-12-16 |
| 130 | `D` | filename | Rune Casting: Os | 2022-06-20 |
| 132 | `O` | filename | ᚫ | 2022-06-17 |
| 133 | `N` | filename | Translating Eh | 2022-12-20 |
| 134 | `L` | filename | ᚩ | 2022-06-16 |
| 135 | `Y` | filename | Translating Is | 2022-12-21 |
| 137 | `I` | filename | Stanza 11: Ice | 2022-12-22 |
| 138 | `N` | filename | Stanza 3: Thorn | 2022-06-14 |
| 140 | `T` | filename | Translating Thorn | 2022-06-13 |
| 141 | `H` | filename | ᛄ | 2022-12-26 |
| 142 | `E` | filename | Translating Yr | 2022-06-10 |
| 144 | `M` | context | — | — |
| 145 | `E` | filename | Rune Casting: Ger | 2022-12-28 |
| 146 | `M` | filename | UI is for User Interface | 2022-06-08 |
| 147 | `O` | filename | Rune Casting: Beorc | 2022-12-29 |
| 148 | `R` | filename | For Anybody Who Rests With Them | 2022-06-07 |
| 149 | `I` | filename | How to Calculate a New Year | 2022-12-30 |
| 150 | `E` | filename | Arrows | 2022-06-06 |
| 151 | `S` | filename | B is for Beginning | 2023-01-02 |
| 153 | `O` | filename | Bright Fruits | 2023-01-03 |
| 154 | `F` | filename | How to do Archery | 2022-06-02 |
| 156 | `O` | filename | X≠Y≠Z: Three Body Problem | 2022-06-01 |
| 157 | `T` | filename | The Future | 2023-01-05 |
| 158 | `H` | filename | Th is for Ye | 2022-05-31 |
| 159 | `E` | filename | X≠Y≠Z: Divination | 2023-01-06 |
| 160 | `R` | filename | How to Grab a Thorn | 2022-05-30 |
| 161 | `S` | filename | Ge is for Prefix | 2023-01-09 |
| 163 | `W` | filename | Y is for Year’s Mind | 2023-01-10 |
| 164 | `I` | filename | Rune Casting: Yr | 2022-05-26 |
| 165 | `L` | filename | How to Eat a Birch Tree | 2023-01-11 |
| 166 | `L` | filename | ᚣ | 2022-05-25 |
| 168 | `Y` | filename | Þ | 2022-05-24 |
| 169 | `O` | filename | Translating Beorc | 2023-01-13 |
| 170 | `U` | filename | Stanza 2: Aurochs | 2022-05-23 |
| 172 | `P` | filename | Stanza 28: Beaver | 2022-05-20 |
| 173 | `E` | filename | Stanza 12: Year | 2023-01-17 |
| 174 | `R` | filename | Translating Ior | 2022-05-19 |
| 175 | `S` | filename | ᛇ | 2023-01-18 |
| 176 | `I` | filename | Translating Ur | 2022-05-18 |
| 177 | `S` | filename | ᛏ | 2023-01-19 |
| 178 | `T` | filename | How to Look Joyful | 2022-05-17 |
| 179 | `.` | filename | Rune Casting: Tiw | 2023-01-20 |
| 181 | `W` | filename | Rune Casting: Eoh | 2023-01-23 |
| 182 | `E` | context | — | — |
| 184 | `A` | filename | The Aurochs and the Beaver | 2022-05-12 |
| 185 | `R` | filename | Eo is for Eorl | 2023-01-25 |
| 186 | `E` | filename | Bad Idea | 2022-05-11 |
| 188 | `E` | filename | Moody Joy | 2022-05-10 |
| 189 | `A` | filename | ♂︎ | 2023-01-27 |
| 190 | `C` | filename | How to go Extinct | 2022-05-09 |
| 191 | `H` | filename | Trust | 2023-01-30 |
| 193 | `O` | filename | Kings | 2023-01-31 |
| 194 | `T` | context | — | — |
| 195 | `H` | filename | X≠Y≠Z: A Joy in the Home | 2023-02-01 |
| 196 | `E` | filename | IO is for I/O | 2022-05-04 |
| 197 | `R` | filename | T is for Thincso | 2023-02-02 |
| 198 | `'` | filename | How to Milk a Beaver | 2022-05-03 |
| 199 | `S` | filename | How to Make Poison | 2023-02-03 |
| 201 | `O` | filename | Translating Tiw | 2023-02-06 |
| 202 | `N` | filename | Rune Casting: Ur | 2022-04-29 |
| 203 | `L` | filename | Translating Eoh | 2023-02-07 |
| 204 | `Y` | filename | ᛡ | 2022-04-28 |
| 206 | `I` | filename | ᚢ | 2022-04-27 |
| 207 | `M` | filename | Stanza 17: Tiw | 2023-02-09 |
| 208 | `M` | filename | Stanza 29: The Grave | 2022-04-26 |
| 209 | `O` | filename | ᛋ | 2023-02-10 |
| 210 | `R` | filename | Stanza 1: Wealth | 2022-04-25 |
| 211 | `T` | filename | ᛈ | 2023-02-13 |
| 212 | `A` | filename | Translating Feoh | 2022-04-22 |
| 213 | `L` | filename | Rune Casting: Sigel | 2023-02-14 |
| 214 | `I` | filename | Translating Ear | 2022-04-21 |
| 215 | `T` | filename | Rune Casting: Peorþ | 2023-02-15 |
| 216 | `Y` | filename | Byþ | 2022-04-20 |
| 218 | `O` | filename | How to Dig my Grave | 2022-04-19 |
| 219 | `N` | filename | P is for Poetry | 2023-02-17 |
| 221 | `E` | filename | Always | 2023-02-20 |
| 222 | `A` | filename | X is not Y and Neither is Z | 2022-04-15 |
| 223 | `R` | filename | X≠Y≠Z: Settlers | 2023-02-21 |
| 224 | `T` | filename | COW | 2022-04-14 |
| 225 | `H` | filename | Sitting to Battle | 2023-02-22 |
| 226 | `,` | filename | F is for Fee | 2022-04-13 |
| 228 | `O` | filename | X≠Y≠Z: 1984 | 2022-04-12 |
| 229 | `T` | filename | Battle | 2023-02-24 |
| 230 | `H` | filename | Everything is Temporary | 2022-04-11 |
| 231 | `E` | filename | S is for Saxon | 2023-02-27 |
| 232 | `R` | filename | The Oxen of the Sun | 2022-04-08 |
| 233 | `W` | filename | How to Navigate by the Sun | 2023-02-28 |
| 234 | `I` | filename | How to Die | 2022-04-07 |
| 235 | `S` | filename | Translating Peorð | 2023-03-01 |
| 236 | `E` | filename | Octave | 2022-04-06 |
| 238 | `E` | filename | X≠Y≠Z: Rune Casting! | 2022-04-05 |
| 239 | `V` | filename | Stanza 16: Sun | 2023-03-03 |
| 240 | `E` | filename | F is for Finis | 2022-04-04 |
| 241 | `R` | filename | Stanza 14: The Game | 2023-03-06 |
| 242 | `Y` | filename | How to Move a Cow | 2022-04-01 |
| 243 | `T` | filename | ᛉ | 2023-03-07 |
| 244 | `H` | filename | Against every Evil Rune Poem | 2022-03-31 |
| 245 | `I` | filename | Rune Casting: Eolhx | 2023-03-08 |
| 246 | `N` | filename | Rune Casting: Feoh | 2022-03-30 |
| 247 | `G` | filename | X is for | 2023-03-09 |
| 249 | `I` | filename | Fen | 2023-03-10 |
| 250 | `S` | filename | ᚠ | 2022-03-28 |
| 252 | `T` | filename | ᛠ | 2022-03-25 |
| 253 | `E` | filename | Loop | 2023-03-14 |
| 254 | `M` | filename | Decode | 2022-03-24 |
| 255 | `P` | filename | How to See the Pair in the Middle | 2023-03-15 |
| 256 | `O` | filename | Bibliography | 2022-03-23 |
| 257 | `R` | filename | Translating Eolhx | 2023-03-16 |
| 258 | `A` | filename | Vern Tonkin | 2022-03-22 |
| 259 | `R` | filename | Stanza 15: Helix | 2023-03-17 |
| 260 | `Y` | filename | O Yes, W. | 2022-03-21 |
| 261 | `.` | filename | The Middle | 2023-03-20 |
