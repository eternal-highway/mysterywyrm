# Acquisition Protocol

## Unit of acquisition

One page, acquired as a relation-bearing record rather than isolated prose.

## Required fields

1. Canonical URL and access date.
2. Exact displayed title and slug.
3. Publication and modification dates when available.
4. Page mode(s) and chapter assignment(s).
5. Full heading structure.
6. Rights-respecting text record or local source capture where authorized.
7. Every image in page order: URL/file identity, alt text, caption, quoted source, artist/manuscript/work, and relation to adjacent text.
8. All internal links with anchor text and destination.
9. Previous and next page links.
10. Categories and tags.
11. Rune/letter/glyph/sound fields where explicit.
12. Codes, substitutions, unusual punctuation, spacing, lineation, and typographic anomalies.
13. Claims copied into the claims/evidence register.
14. Uncertainties copied without premature repair.

## Three records, never silently merged

- **Observed:** what the page visibly contains.
- **Site-authored:** what Tonkin explicitly claims or instructs.
- **Working inference:** a relation proposed during study.

## Order of work

1. Inventory and capture.
2. Reconstruct link and sequence graphs.
3. Populate the 29-rune and 15-chapter matrix.
4. Align compositional streams within each chapter.
5. Only then undertake interpretive synthesis.

## Chapter reconstruction order

For every unreconstructed chapter:

1. Walk direct previous/next navigation first and record each observed adjacency.
2. Do not generate the path by reversing a category archive.
3. After the link walk, retrieve the category archive only as a completeness and order cross-check.
4. Record navigation evidence and archive evidence separately, including whether a comparison is independent or derived from the same source.
5. Leave the interior unpredicted. Opaque code, riddles, and cross-stream pages remain unresolved unless the site supplies their resolution.

For *Axis Mundi*, test `02_structure/axis_mundi_prediction.md` as two separate predictions: intra-chapter form/order and outer chain contiguity.

## Bounded publication-date attempt

Before the next chapter acquisition, make one bounded attempt to recover exact post dates through the WordPress REST posts endpoint, `wp-sitemap.xml` last-modification values, and relevant category feeds. Keep these evidence types distinct: modification time is not necessarily publication time. If all routes are inaccessible or non-decisive, record both temporal interpretations as **unresolvable by current means** rather than indefinitely pending.

## Failure handling

A timeout or inaccessible page is a capture-state fact, not absence. Keep the page in the register, mark the failed attempt, and return later without inventing its content.
