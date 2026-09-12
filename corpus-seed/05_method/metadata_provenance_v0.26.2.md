# v0.26.2 metadata and provenance reconciliation

Date: 2026-09-12
Parent: `letters_for_titles_corpus_seed_v0.26.1.zip`
Parent SHA-256: `ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327`

Version 0.26.2 is a metadata/provenance patch derived from v0.26.1. It corrects Loop and Œ original-media identities/dimensions, registers the Octave image, imports 31 source-byte hash attestations and 262 day-level publication records, updates OQ001/OQ003/OQ007, and corrects the Translating Is canonical URL. It changes no transcription or retained media payload. Nine cross-lineage carrier disputes and the Octave classification question remain for v0.27.

## Source identity

Source hashes below cover exact Git blob bytes at repository commit `23012aceed6b92c0c36f0b315e8ffafb384ec994`, before Windows checkout newline conversion.

| Repository source | SHA-256 |
|---|---|
| `data/media-code.json` | `fd39667b3ec4b429bf53dc71166999b1b0aa2a323dfbad15962e51d96c44e885` |
| `data/media-full.json` | `4821358c1acb0eadb17f0360afc670522f92b9f91a04c88f0b225c9927615717` |
| `data/corpus.json` | `c7031338a251b6d7568b17c05b7ea413f91ac23c0a8d05c4e934202c522499d4` |
| `archive/pages/translating-ice.html` | `7eef1e6be5bd4fa3ddbadfbb0526e5d802b42f4ccc04cef1e7494d095c520304` |

The original 31-row media manifest is bundled verbatim as `01_inventory/rune_code_source_media.json`. All 31 entries agree with the full manifest on URL, SHA-256, byte count, width and height. Its retrieval date is 2026-08-30. No full-resolution source files were available locally or re-fetched in this patch. These are imported source-byte hash attestations, not independent current byte verification. Future interpretation must authenticate actual downloaded bytes first.

The 17 named carriers are matched by normalized media URL, removing only terminal WordPress size/scaled suffixes. Octave is explicitly selected by `2022_04_Octave-Lettersfortitles-VernTonkin.jpg`; it is not inferred from the old page URL. The other 14 records are numbered filename-run assets. Existing visual fingerprints retain their original URL and date in separate fields.

Loop now records the 2062x1528 original; Œ records 2560x2560; Octave records 1083x981. The historical v0.26.0 report retains the actual 1080-pixel derivative URLs and dimensions it read. This patch makes no new image reading.

## Publication metadata and open questions

`01_inventory/harvest_publication_dates.csv` preserves all 262 post IDs, titles, canonical links, publication dates and modification dates from the co-located harvest. Dates have day precision; exact timestamps and revision history are not established. OQ003 becomes publication_dates_available rather than a claim that every chronological research question is solved. OQ001's missing-repository dependency is removed. OQ007 is resolved for hash availability, not local byte possession.

## Canonical URL

For Translating Is, the archived page canonical tag and harvest link agree on `https://lettersfortitles.com/translating-ice/`. Current registers and referring capture links are corrected from `/translating-is/`; the `translating-is` local capture folder remains stable. Original URL provenance is retained in its record and source notes. Today's live page fetch timed out and the REST route was unavailable through the browsing tool; neither establishes a broken live URL.

## Media preservation and interpretation boundary

The pre-existing local AS001 replacement had one 360x360 frame, 28,796 bytes and SHA-256 `d5863af156618640e549dc00eb310e887fd97b73b315b3513a148a976d41a1bc`. It was preserved in the ignored `local-recovery/` folder before restoring the six-frame, 304,353-byte parent GIF with SHA-256 `20fd510698180bc1e36a3bae2ebcf769341e45cd15e7d21f093c9b89ef400910`. Its origin is unknown. The candidate has no media-payload differences from its parent.

Nine carrier transcription disputes and the separate Octave classification question remain open. No Gate 0 key reconstruction or plate adjudication occurs in v0.26.2.
