# Independent Audit of v0.12.0 — Claude Branch

Date: 2026-08-26
Scope: full ingest of the CORE and CAPTURE bundles, mechanical register audit, live-site verification, and one chapter reconstruction.
Nothing in the canonical corpus has been altered. Everything below is a proposal.

## 1. Ingest and integrity

- 841 files unpacked from the two bundles. **All 841 SHA-256 checksums verified.** The repack is lossless.
- Directory structure matches the README's map. All files named in the briefing are present.

## 2. Mechanical register audit

Checks run and passed:

- `core_stream_alignment.csv` — 29 rows, no duplicate URLs across the four stream columns.
- Reflected partners — every row satisfies `n + partner = 30`. No exceptions.
- `runic_pair_matrix.csv` — 15 rows, consistent with the alignment.
- Archive positions contiguous and gapless in all six stream registers. The single non-numeric value is TR034 (*Translating Ear*), which is documented as absent from the retrieved Translation snapshot.
- Counts match the prose: 29 stanzas, 29 glyphs, 31 castings (29 direct + 2 crossings), 34 translations, 34 instruction manual, 34 alphabet book.

**One hygiene finding.** `verified_page_register.csv` has 183 rows but 177 unique URLs. Six pages appear twice — `l-is-for-letters-for-titles`, `rune-casting-nyd`, `rune-casting-wyn`, `stanza-10-need`, `hail`, `translating-ing`. In each case an early P0xx row recorded from a search result was later re-recorded as a P1xx row with fuller direct evidence. No factual conflict. But the register now double-counts, and any future count drawn from it will be wrong by six. Proposed repair: keep both rows, add a `supersedes` / `superseded_by` column so the lineage stays visible, and state the unique-page count separately.

## 3. Structural finding: the braid order is the reverse of the category archive

This is the most consequential thing I found, and it is mechanical rather than interpretive.

**Claim.** For every reconstructed chapter, the previous/next braid order is exactly the reverse of that chapter's category-archive listing order, and each stream's within-chapter order is exactly the reverse of that stream's tag-archive order.

**Warrant.**

- Retrieved `category/war-and-peace/` live. It lists seventeen posts. Reversed, that listing is character-for-character the braid in `war_and_peace_path.md`, including the interior.
- Retrieved `category/by-land-and-by-sea/` live. Reversed, it produced a seventeen-page braid whose two boundary seams and one interior adjacency were then independently confirmed by direct previous/next links on three separate pages.
- Checked all nine v0.12.0 chapters against the four stream registers. In 36 of 36 cases (9 chapters × 4 streams), the recorded braid order is the reverse of the register's archive positions. No exceptions.

**Most likely explanation.** WordPress tag and category archives list newest first; previous/next links run oldest to newest. The braid is therefore publication order, and the archives are its mirror. The site says as much in its own voice: *L is for Letters for Titles* describes a book written forward and linked backward.

**What this changes.**

The corpus currently records each chapter's "partner-order mutation" as a per-chapter discovery — Ger → Beorc here, Cen → Dæg there — and `chapter_braid_comparison.md` concludes that "no stream consistently supplies the reversal." That observation is accurate but the framing implies more contingency than the evidence supports. There is one generative fact, not nine independent mutations: the order in which Tonkin wrote the pages. The partner order in each stream follows from composition sequence.

This does not deflate the work. It relocates the question. "Why is the glyph pair in this order?" becomes "why did he write these pages in this order?" — which is a question about composition, and a better one.

**What this does not change.** The envelope itself is still a real and non-trivial result. Publication order explains why partner order varies; it does not explain why the pages happen to have been written in a glyph-glyph, casting-casting, nine-page interior, translation-translation, stanza-stanza sequence, ten times.

**Falsification route.** Post dates would settle this outright. They were not exposed in the retrieved markdown. Image upload paths are weakly corroborative — the *By Land and By Sea* pages carry 2022/07 and 2022/08 upload paths while *War and Peace* pages carry 2022/12, matching the chain direction — but upload date is not post date and should not be treated as proof.

## 4. Structural finding: the chapter is folded like the book

Every reconstructed braid is 2 + 2 + 9 + 2 + 2. And in **all ten** chapters, position 9 of 17 — the exact centre, eight pages either side — is the eponymous chapter page, the one tagged *Duets*:

| Chapter | Position 9 |
|---|---|
| Sitting to Battle | Sitting to Battle |
| Trust | Trust |
| The Future | The Future |
| War and Peace | War and Peace |
| Fate | Fate |
| The Water Cycle | The Water Cycle |
| Prosperity | Prosperity |
| You Have Nothing Else | You Have Nothing Else |
| Light | Light |
| By Land and By Sea | By Land and By Sea |

The corpus records this implicitly — every path file has it — but does not state it. It should. A seventeen-page braid folded around its ninth page has the same shape as a twenty-nine-rune poem folded around its fifteenth stanza. The chapter is a scale model of the book, which is the site's own "mirror within a mirror," and it means the *Duets* page is not an introduction to a chapter but its hinge.

This also gives a sharp falsification test for every remaining chapter: if a chapter's *Duets* page is not at position 9, the model breaks.

## 5. Reinterpretation candidate: the Trust ↔ Sitting to Battle circuit

Recorded as a fact, offered as a reinterpretation, not a correction.

The glyph archive places *Sitting to Battle* nearer the newest end than *Trust*. Under the reversal result, *Sitting to Battle* was written after *Trust*. So of the two edges in the "34-page circuit":

- `Stanza 17: Tiw → ᛋ` is a forward link, consistent with every other seam in the chain.
- `Stanza 14: The Game → ᛇ` is a **backward** link.

If that is right, the circuit is not a symmetrical loop but the chain plus one retrospective link — precisely the "written forward, linked backward" behaviour the site describes, occurring at the point where composition turns toward the middle. The Middle cluster, whose pages sit at archive position 1 in every stream, was written last.

The corpus's circuit claim is not wrong about the links. The proposal is that the two edges are of different kinds and should be labelled as such. This should be tested against post dates before adoption, and the existing claim preserved either way.

## 6. Reconstruction delivered

*By Land and By Sea* (Ac–Rad) is reconstructed in `02_structure/by_land_and_by_sea_path.md`. Summary:

- Seventeen pages, envelope intact, tenth instance.
- Partner order Ac → Rad / Rad → Ac / Ac → Rad / Rad → Ac. Strict alternation; precedent in *The Water Cycle*.
- **New verified seam: `Stanza 4: God → ᚪ`.** *Axis Mundi* enters *By Land and By Sea*. Direct previous-page link on the Ac glyph.
- Outgoing seam `Stanza 25: Oak → ᛞ` retained unchanged.
- No second circuit.

**Four pages are new to the corpus** — absent from every register and every capture folder:

| Page | URL | Stream |
|---|---|---|
| By Land and By Sea | `/by-land-and-by-sea/` | chapter orientation (Duets) |
| X≠Y≠Z: Are we there yet? | `/x≠y≠z-are-we-there-yet/` | dialogue |
| The Way | `/the-way/` | code (opaque) |
| Crann Bethadh | `/crann-bethadh/` | auxiliary / etymology |

Two alphabet entries can now be assigned a chapter: AB025 *R is for Riddle* and AB026 *A is for Golem Aleph* both belong to *By Land and By Sea*. By elimination AB027 *Æ is for George William Russell* is a candidate for *Axis Mundi*, but that is inference, not observation.

## 7. Predictions, recorded before testing

From the reversal result, *Axis Mundi* should be:

`ᚩ → ᚫ → Rune Casting: Os → Rune Casting: Æsc → [nine interior pages, with Axis Mundi at position 9] → Translating Os → Translating Æsc → Stanza 26: Ash → Stanza 4: God → ᚪ`

and its incoming seam should be `Stanza 27: Bow → ᚩ` from *They'll Cut You*.

These are stated in advance so that a mismatch counts as evidence against the model rather than being absorbed into it. If *Axis Mundi* comes back in any other order, the reversal result is wrong or incomplete and this audit should be revised, not the observation.

## 8. Where I think v0.12.0 is over-confident

- **"No stream consistently supplies the reversal."** True as stated, misleading as framed. See §3.
- **The nine partner-order mutations recorded one per changelog entry.** These are nine records of one fact.
- **"Only Trust ↔ Sitting to Battle forms a verified reciprocal circuit."** Accurate, but the two edges may not be the same kind of edge. See §5.
- **The envelope described as "not a universal law."** The corpus's caution is right in principle, but it now has ten instances, a fixed 2/2/9/2/2 partition, and a fixed position-9 hinge. The honest statement is stronger than the current one: it is a well-supported regularity with a specific shape and a clear falsification test, not merely a recurring tendency.

## 9. Proposed version

A v0.13.0 carrying: the *By Land and By Sea* braid; four new page records; the `Stanza 4: God → ᚪ` seam; the extended chain; the reversal result and the position-9 result as new structural claims with their warrants and limits; the register de-duplication; and the circuit reinterpretation held as a candidate pending post dates. The v0.12.0 statements it revises should be preserved in the lineage log, not overwritten.
