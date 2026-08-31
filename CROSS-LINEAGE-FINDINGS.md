# Cross-lineage findings — corpus-seed v0.26.1 against the harvest/research layer

Reviewer: Claude (bounded review role, `LINEAGES.md` § Model roles)
Date: 2026-08-31
State reviewed: `main` at `aad614d`, fast-forward only, working tree clean

> Sections 1–4 below preserve the bounded review snapshot examined on 2026-08-31 at `aad614d`; § 5 records subsequent disposition and current repository state.

This document **records** disagreements. It does not resolve them. Under
`LINEAGES.md` § Authority rule, neither lineage may be silently overwritten;
every item below marked *contradiction* needs explicit adjudication by the
owner of the corpus lineage before either record changes.

It is an **evidence ledger**: entries are added when a conflict is found and
struck only when a release adjudicates them. § 5 records the dispositions
ruled so far and what remains open.

Nothing in `corpus-seed/` was modified. Any edit inside that tree invalidates
its 1,415-file `MANIFEST.sha256`, so corrections belong either outside the
tree (as here) or in a new Codex release with a regenerated manifest.

---

## 1. Validation results

### Checkout

| Check | Result |
|---|---|
| `git pull --ff-only origin main` | Already up to date; no merge commit created |
| `HEAD` | `aad614d` = `origin/main` |
| Working tree | clean |

### Corpus seed integrity

| Check | Result |
|---|---|
| `sha256sum -c MANIFEST.sha256` | **1,415 / 1,415 OK**, 0 failures |
| Files in `corpus-seed/` | 1,416 |
| Files present but not covered by manifest | 1 — `MANIFEST.sha256` itself, as documented |
| Files in manifest but absent from tree | 0 |
| `05_method/verify_rune_code_state.py` | **pass** — 17/17 classified (14 ordered + 1 rebus + 2 key carriers); stale phrases 0; fingerprints 17/17, exact source-byte hashes 3 |
| `05_method/verify_cipher_letter_run.py` | **pass** — message length 261, local tokens 74/74, failures 0 |

Verifiers were run in the order `CODEX_HANDOFF.md` specifies (Rune Code state
before the filename verifier). Every figure in
`05_method/release_validation_v0.26.1.md` that is locally checkable reproduces.

### Independent harvest-layer checks (re-run for cross-comparison)

| Check | Result |
|---|---|
| `tools/cipher.py` | exit 0, `cipher holds: True`, 211/211 recovered characters agree; regenerated `research/cipher.md` **byte-identical** to the committed file |
| `tools/structure.py` | exit 0; chapter sizes 23 / 19 / 12 × 17 / 10 |
| Tracked-file changes from running either tool | none |

---

## 2. Namespace and provenance boundary

**Coherent as built; unenforced as policy.**

Coherent:

- `aad614d` is 1,418 additions, 1 modification, 0 deletions. The only paths
  touched outside `corpus-seed/` are `LINEAGES.md` (new) and `README.md`
  (+9 lines, additive pointer). `archive/`, `data/`, `book/`, `research/`
  and `tools/` are untouched.
- Path namespaces are disjoint. `.gitignore` excludes nothing under
  `corpus-seed/`.
- The imported tree reproduces the release payload exactly (§ 1).

Unenforced — two gaps, both outside the seed tree:

- **No release tag.** `LINEAGES.md` § Update rule: "Each merged corpus release
  receives a Git tag of the form `corpus-vX.Y.Z`." `git tag -l` is empty.
  `corpus-v0.26.1` was never applied to `aad614d`.
- **No manifest guard.** Nothing mechanically detects an edit inside
  `corpus-seed/`. The seed's own two verifiers check Rune Code state and the
  filename run; neither verifies `MANIFEST.sha256`. A stray edit would pass
  both while silently breaking the release payload.

A third, softer gap: `README.md` and `research/rune-code.md` state Rune Code
readings as the repository's settled findings, with no cross-reference to the
seed's differing readings. That presents one lineage's result as the
repository's result, which is what the authority rule forbids.

### Provenance cross-check (mechanical, no decoding)

- **14 of 16** plate carriers cited in the seed's reconciliations appear in
  `data/media-code.json` at the **identical source URL and identical pixel
  dimensions**. The two lineages read the same assets. Every reading conflict
  in § 3 is therefore a dispute about counting, not about evidence state.
- All **3** exact source-byte SHA-256 values the seed holds (*Arrows*,
  *The Way*, *Present*) **match** `data/media-code.json` byte-for-byte. Hard
  integrity confirmation across the boundary.
- **2 exceptions — the seed read downscaled derivatives:**

  | Plate | Seed `natural_dimensions` / cited source | Harvest manifest holds |
  |---|---|---|
  | *Œ is for Œdipean Riddle* | 1080 × 1080 (`…-1080x1080.jpg`) | **2560 × 2560** (`…-scaled.jpg`) |
  | *Loop* | 1080 × 800 (`…-1080x800.jpg`) | **2062 × 1528** (`Loop.lettersfortitles-verntonkin.jpg`) |

  `rune_code_plate_reconciliation_v0.26.0.md` states both were "inspected at
  their live full available source resolution". For these two rows that is
  factually wrong, and `01_inventory/rune_code_carrier_fingerprints.csv`
  records the derivative sizes under the column `natural_dimensions`.
  This matters twice over: *Œdipean* is one of the contested readings, and
  *Loop* is the **key carrier** the whole cipher rests on.

---

## 3. Substantive contradictions

### 3a. Rune Code readings

Seven carriers agree exactly, coordinate for coordinate: *Arrows*, *Present*,
*Battle*, *Friþ*, *Bright Fruits*, *Everything is Temporary*, and *Loop*
(both classify it as key, not plaintext). Those are not listed below.

| Plate | corpus-seed v0.26.1 | harvest / `research/rune-code.md` | Status |
|---|---|---|---|
| **Shh** | `SILENT` | `LISTEN` | **order only** |
| **Axaxaxas mlö** | `CAN YOU READ ME — ARE YOU READING THE BEGINNING OF SOMETHING?` (47 units) | `YOU WHO READ ME — ARE YOU CERTAIN YOU UNDERSTAND MY LANGUAGE?` (48 units) | **contradiction** |
| **It Never Deceives** | `WHAT DID` (7 staves, 4+3) | `GUARDIAN` (8 glyphs, 4+4) | **contradiction** |
| **Always** | `BEING ENDLESS` (12 staves, 2 clusters) | `I KEEP U AND KILL U` (12 coords + 2 Roman `K`, 6 rows) | **contradiction** |
| **Œ is for Œdipean Riddle** | `A TWIN / SUN / DAY` | `NIGHT AND DAY` | **contradiction** |
| **You Knew it Beforehand** | upper `WHAT DO YOU KNOW?`; lower `AFTER / NO / LIFE / DEATH` | upper `WHAT IS OUR FATE?`; lower unresolved | **contradiction** |
| **The Way** | `…IS **LEVEL** YET…` | `…IS **SMOOTH** YET…` | **contradiction (one word)** |
| **Soon After it Becomes Water** | `SO LET US MELT`, 11 units, complete | `… LET US MELT`, line 1 melted and unrecoverable | **contradiction (evidence state)** |
| **For Anybody Who Rests With Them** | complete: `HOW UNCOMFORTABLE DO YOU WANT TO BE?` | `HOW UNCOMFORTABLE … BE?`, middle unresolved | **mostly convergent, one conflict** |
| **Octave** | prose key carrier; **no image carrier registered** | reads a plate: `CODE` + `WHERE / THE / BE·THE / HELL ?` | **registration gap** |

Detail on the sharpest cases:

**Shh — pure ordering dispute.** Both records read the *same six coordinates
on the same six boughs*: 2.8 S, 2.3 I, 3.5 L, 3.3 E, 2.2 N, 3.1 T. Even the
crown agrees at 3.1 = T (the seed by above/below, the harvest by right/left on
a vertical stem). The seed traverses left boughs top-down, right boughs
top-down, crown last → `SILENT`. The harvest traverses left boughs bottom-up,
crown, right boughs top-down → `LISTEN`. `research/rune-code.md` explicitly
names `SILENT` as the alternative and argues for `LISTEN` on path continuity;
the seed does not acknowledge `LISTEN` at all. No mechanical decider exists in
either record.

**Axaxaxas mlö — the gap is one row wide.** Both read five rows, a drawn dash
after `ME`, and a drawn `?` at the end. Row unit-counts agree on rows 1, 2, 3
and 5 (10 / 8 / 10 / 8) and word segmentation agrees throughout. Units 7–15
are *coordinate-identical* in both records (`READ` 1.5 3.3 4.1 3.8, `ME` 3.4
3.3, `ARE` 4.1 1.5 3.3). The entire 47-vs-48 discrepancy is **row 4**: seed 11
units (`BEGINNING OF`), harvest 12 (`UNDERSTAND MJ`). That is a single,
bounded, mechanically testable question — how many stave units are in row 4 —
and the harvest side has a re-runnable tool (`tools/tally.py`) whose raw output
is quoted in `research/rune-code.md`. The seed read the same 1694 × 2560 asset.

**Œdipean — the harvest's own re-count matches the seed.** Both read 11 faces
in rows of 5 / 3 / 3, and row 3 is coordinate-identical (3.8 4.1 4.3 = `DAY`).
`research/rune-code.md` flags that the second face from the left "reads three
yellow points over one flame, which is 3.1 (T) rather than the 2.1 (H) the
word needs" — 3.1 is exactly the seed's value at that position. The harvest's
own anomaly note is evidence *against* its own `NIGHT`. Weigh this together
with § 2: the seed decoded this plate at 1080 × 1080 when a 2560 × 2560
original exists.

**For Anybody — largely convergent, but not adoptable yet.** Rows 1, 2, 3 and
7 are coordinate-identical. The seed supplies firm values exactly where the
harvest prints uncertainty ranges, and the two are compatible at row 4 glyph 2
(seed 3.8; harvest "3 up / 7–8 down"). But **one genuine coordinate conflict
remains**: row 4 glyph 3, seed `1.4` (O) against harvest `1.3` (TH). The seed
is the more complete record and its sentence is grammatical, which is
suggestive but is not adjudication — a completion that reads well is exactly
the kind of evidence this review is meant to hold at arm's length. This plate
therefore stays on the contested list and is settled with the other eight, not
adopted ahead of them.

**Systematic convention difference.** The harvest writes English *y* with Ger
(2.4) — `JOU`, `MJ` — arguing it is the /j/ rune. The seed uses Yr (4.3) for
the same slot (`YOU` on *Axaxaxas mlö* and *You Knew it Beforehand*). This
propagates into several of the conflicts above and should be adjudicated once,
not per plate.

**Aggregate count.** Seed: 14 ordered + 1 rebus + 2 key carriers = 17. Harvest:
16 message plates + 1 key (*Loop*). The whole delta is *Octave*: the seed's
fingerprint register carries `not applicable` and a page URL for P261 and never
registers the `Octave-Lettersfortitles-VernTonkin.jpg` carrier (1083 × 981),
which the harvest holds in `data/media-code.json` with a SHA-256 and reads as
an inscription.

### 3b. Corpus-level agreements worth recording

- **Filename cipher: complete agreement.** Same 261-character message, same
  fold at post 131 (*Turn*), same slot 32 = `?`, same 142→144 author slip.
  Seed 74/74 local tokens; harvest 211/211 recovered characters.
- **Page coverage reconciles exactly.** Seed 263 registered content URLs vs
  harvest 262 posts. The single difference is
  `https://lettersfortitles.com/` — the site home page, which the seed
  registers (folder `home`) and a WordPress REST post harvest does not return.
  **No coverage gap in either direction.**
- **Structure agrees.** Chapter braid sizes match the seed's model exactly
  (23 / 19 / twelve × 17 / 10). The seed's ten-page Middle path and the
  harvest's `Twist` category are the **same ten pages in the same order**.
- **Tag sets agree.** 17 Rune Code, 25 Code, on both sides.

### 3c. Smaller discrepancies

| Item | Seed | Harvest | Note |
|---|---|---|---|
| Canonical URL of *Translating Is* | `/translating-is/` | `/translating-ice/` | Harvest slug comes from the WordPress REST API and is authoritative for the site's own permalink. Likely a title-derived value in the seed. |
| Numbered images in the filename run | "216" (attributed to Claude's packet) | 213 positions carry a numbered image; 211 characters recovered | Attributed figure appears to predate the harvester's text-fidelity fix. Plaintext is unaffected. |
| Capture folder naming | ASCII-normalized (`ac-glyph`, `x-y-z-1984`) | live percent-encoded slugs (`%e1%9a%aa`, `x-%e2%89%a0-y-%e2%89%a0-z-1984`) | Not a defect, but slug-level joins between the lineages are impossible; join on canonical URL. |

---

## 4. Open questions the harvest layer now unblocks

Three entries in `01_inventory/open_questions.csv` are blocked on evidence that
is now in this same repository:

| ID | Seed status | What the harvest layer holds |
|---|---|---|
| **OQ001** | `blocked_external_evidence` — "Claude harvest repository absent" | The harvest **is** this repository: `data/corpus.json` (262 posts), `data/media.json` (479), `tools/cipher.py`. Verifier runs clean end to end. |
| **OQ003** | `unresolvable_by_current_means` — "Exact post dates unavailable" | `data/corpus.json` carries a per-post `date` from the REST API. 257 publication days, weekday-only spread. The Middle path dates 2023-03-07 → 2023-03-20. This also bears on the *Trust* ↔ *Sitting to Battle* seam the capsule leaves "pending exact post dates". |
| **OQ007** | `blocked_media_bytes` — exact bytes for *Arrows*, *The Way*, *Present* only | `data/media-code.json` carries exact source-byte SHA-256 for **all 31** full-resolution Rune Code images, and the seed's 3 match it exactly. |

These are reported as available evidence. Closing them is the corpus owner's
call, not this review's.

---

## 5. Disposition

Ruled 2026-08-31 by the repository owner. The findings above are preserved as
an evidence ledger; the resolutions proposed in the first draft of this
document are **not** adopted wholesale.

### Adopted and applied

| # | Ruling | State |
|---|---|---|
| 1 | Findings document becomes an evidence ledger on `main` | **merged** — PR #4, merge commit `586e06d` |
| 2 | Annotated `corpus-v0.26.1` tag pointing at `aad614d` | **published** — annotated tag and GitHub Release |
| 3 | Manifest guard + CI enforcement, outside `corpus-seed/` | **done** — `tools/verify-corpus-seed.sh`, `.github/workflows/lineage-integrity.yml` |
| 4 | Cross-links from `README.md`, `LINEAGES.md`, `research/rune-code.md` | **done** |

The annotated `corpus-v0.26.1` tag is published as a proper tag object and
peels to the import commit
`aad614d8a873e3da3f91c16d935814f7e05d1d6d`. Its annotation records the
canonical ZIP and parent hashes and the verification results. The
[Canonical corpus seed v0.26.1 GitHub Release](https://github.com/eternal-highway/mysterywyrm/releases/tag/corpus-v0.26.1)
publishes the original `letters_for_titles_corpus_seed_v0.26.1.zip` asset. A
fresh download of the published 1,320,822-byte asset verified as SHA-256
`ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327`.
`LINEAGES.md`'s release-tag and original-artifact rule is now satisfied.

The guard derives the expected path set from `MANIFEST.sha256` and the tree at
run time. No payload count is hardcoded, so a future release of a different
size still passes. It verifies every hash, asserts that the manifest's path set
equals the tree's except for the manifest itself, and then runs both state
verifiers. Confirmed to fail on a stray added file, a single changed byte, and
a deleted payload file.

### Release scope

Two releases, deliberately separated so that provenance repair does not travel
under cover of transcription change:

**v0.26.2 — factual metadata and provenance only. Changes no reading.**

1. Correct the two `natural_dimensions` rows in
   `01_inventory/rune_code_carrier_fingerprints.csv` — *Œ is for Œdipean
   Riddle* 2560 × 2560, *Loop* 2062 × 1528 — and soften the "full available
   source resolution" claim in `rune_code_plate_reconciliation_v0.26.0.md`.
2. Register the *Octave* image carrier for P261
   (`Octave-Lettersfortitles-VernTonkin.jpg`, 1083 × 981). Registration only;
   whether it bears an inscription is a v0.27.0 question.
3. Import the 31 exact source-byte SHA-256 values from `data/media-code.json`,
   resolving **OQ007**.
4. Re-status **OQ001** and **OQ003**: the harvest repository and per-post
   publication dates are now co-located in this repository.
5. Adjudicate the canonical URL of *Translating Is* — seed `/translating-is/`
   against the harvest's `/translating-ice/`, the latter taken from the
   WordPress REST API.

**v0.27.0 — transcription adjudication.** One bounded comparative pass over all
nine contested carriers together, not an iterative exchange. Suggested order,
cheapest decisive test first:

1. *Axaxaxas mlö* row 4 unit count — the single row that produces the whole
   47-vs-48 divergence.
2. The Y-rune convention, Ger (2.4) against Yr (4.3). Settled once, it
   propagates through several plates.
3. *Œ is for Œdipean Riddle*, re-read at 2560 × 2560 rather than 1080 × 1080.
4. *It Never Deceives* — does the lower row carry three groups or four?
5. *Shh* — traversal order only; the six coordinates already agree.
6. *For Anybody Who Rests With Them* — row 4 glyph 3, `1.4` against `1.3`.
7. *Always*.
8. *You Knew it Beforehand*, upper field.
9. *The Way*, word 5 — `LEVEL` against `SMOOTH`.
10. *Soon After it Becomes Water* — an evidence-state question (is line 1
    recoverable?) rather than a counting one.

Do this once, comparatively, on the largest available source bytes. The failure
mode being avoided is a resumed one-plate-at-a-time Claude↔Codex loop.

### Standing constraint

`All seventeen are read` remains a **lineage-specific** claim. It is no longer
stated as a repository-level finding anywhere in the tree: `README.md` and
`research/rune-code.md` now attribute it to the harvest layer and point here.
Eight readings conflict outright and a ninth (*For Anybody*) retains one
coordinate conflict; several of these disputes concern counting **identical
source bytes**, which makes them a reproducibility problem rather than an
evidence-availability one. That is the substantive result of importing both
lineages: apparent closure was concealing it.
