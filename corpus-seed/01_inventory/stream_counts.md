# Stream Inventory Counts

Observed: 2026-08-22  
Primary archive surfaces: `tag/instruction-manual/` and `tag/translation/`

## Resolved in this pass

| Stream | Archive entries | Direct rune/chapter entries | Crossings or exceptions |
|---|---:|---:|---|
| Instruction Manual | 34 | 33 chapter instructions | 1 middle instruction: *How to See the Pair in the Middle* |
| Translation archive snapshot | 34 | 28 direct rune commentaries | 6 auxiliary or cross-rune pages; `ꝥ` is present while *Translating Ear* is not |
| Known translation pages site-wide | 35 | 29 direct rune commentaries | The full rune set plus 6 auxiliary or cross-rune pages |
| Stanzas | 29 | 29 direct rune stanzas | Complete rune set; archive begins at 15 and moves outward |
| Runes / glyph pages | 29 | 29 rune or letter-form pages | Thorn's displayed page title is `Þ` rather than the runic glyph |
| Rune Casting | 31 | 29 direct rune castings | *Translating Feoh* plus *X≠Y≠Z: Rune Casting!* are additional archive entries |
| Alphabet Book | 34 | not normalized to one modern alphabet | Includes runes, archaic letters, ligatures, abbreviations, unfinished titles, and cross-tag pages |

These are counts of entries on the retrieved tag archive pages, not claims about the final size of the site. The gallery exposes additional page imagery, including material not necessarily assigned to either tag.

## Verified-page register hygiene

As of 0.21.0, `verified_page_register.csv` contains 286 evidence rows representing 278 unique URLs. Eight URLs have an early summary row and a later fuller row. Both records remain visible; `supersedes` and `superseded_by` identify which row is current without erasing acquisition lineage. All 263 capture canonical URLs occur in the register. The fifteen registered URLs without capture folders are intentional archive/index surfaces enumerated in `register_capture_reconciliation.csv`; register-row, unique-URL, and capture-folder counts must not be used interchangeably.

## Why the exceptions matter

- The Instruction Manual begins from the middle, then moves outward through the reflected chapter sequence.
- The current Translation archive is not a mechanically complete one-page-per-rune list, although the site-wide page record does include all 29 direct rune commentaries. Its membership also changed between 2026-08-22 and 2026-08-29 when `ꝥ` appeared.
- *Life and Death* crosses Feoh and Mann, which have different reflected partners.
- *I Sing This Wretched Song* binds Mann, Lagu, Ing, and Eþel as a tempo sequence across four chapters.
- *Ing is for Scylding* is simultaneously an alphabet composition and a translation-tag page.
- *Hildegicel* and *A Horrible Wonder* operate as lexical or thematic bridges rather than direct rune-title commentaries.
- *Translating Ear* is recoverable through the *Everything is Temporary* category and its own page; its page carries the Translation tag even though it remains absent from the live Translation archive inspected 2026-08-29. Archive state and page state must therefore be dated separately.
- *Translating Feoh* is present in both the Translation and Rune Casting archives; this is a deliberate archive-state crossing until contrary evidence appears.
- *X≠Y≠Z: Rune Casting!* stages the outer Ear/Feoh pair through three voices and is not one of the 29 direct castings.
- The Alphabet Book archive is not a clean A-to-Z inventory. Its excess and missing complements are evidence.

## Access note

The homepage advertises a WordPress JSON API root, but direct API and robots paths were blocked by the cloud browser during this pass. The registers therefore use the site's public tag archives, their canonical page links, and individually resolved page records. This is an acquisition limitation, not evidence about the work.
