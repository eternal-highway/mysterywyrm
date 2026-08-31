# Claude Review Reconciliation — 0.13.2

Date: 2026-08-26  
Input reviewed: polished 0.13.1  
Canonical parent SHA-256: `69672655b989403d46523681fae6132c15f405c1902c0e52a2c67c6fdc6f6ae1`

This patch accepts Claude's evidence corrections and next-acquisition constraints. No live page was acquired and no chapter was completed.

## Corrections adopted

1. **841/842 resolved.** Combined 0.12.0 contains 842 files. Exactly one is non-text: AS001 `08_assets/mysterywyrm.gif`. Claude verified the 841-file text-bundle scope; its “lossless repack” statement did not establish completeness of the combined release.
2. **Asset boundary recorded.** Claude received a single-frame 364 × 364 JPEG carried as `mysterywyrm.webp`, not canonical six-frame 360 × 360 GIF AS001. Their relation is undetermined. The local GIF currently matches AS001's registered checksum; cross-channel byte identity is not claimed.
3. **Tag claim narrowed.** The eponymous page occupies position 9 in all ten completed paired braids. The *Duets* tag is verified for two of ten only.
4. **Independence counted.** Thirty-six archive-order checks are independent retrochecks. Four *By Land and By Sea* checks are derived from the same category listing.
5. **Middle rescaled.** Ten paired braids are complete. The Middle has two observed paths but remains non-exhaustive and outside the reflected-pair sample.
6. **Invariant bounded.** `2 + 2 + 9 + 2 + 2` is invariant across the ten reconstructed reflected pairs, not fixed across all chapters.
7. **Prediction split.** Axis Mundi's intra-chapter archive-derived order is Prediction A. Bow-to-Os chain contiguity is Prediction B.
8. **Register/capture delta closed.** From 0.12.0 to polished 0.13.1, sixteen newly registered chapter URLs plus five legacy capture backfills yielded +21 unique URLs. Seventeen new capture folders included *Stanza 25: Oak*, already registered in 0.12.0. Thus the headline difference is `21 - 17 = 4`: five legacy backfills offset by one newly captured, already registered page. All 177 capture URLs are registered; 21 registered URLs without folders are enumerated separately.

## Next acquisition constraints adopted

- Direct previous/next link walk first; category archive second.
- One bounded post-date retrieval attempt, then either resolution or “unresolvable by current means.”
- Separate falsification conditions for reversal and chain contiguity.
- No prediction of the nine interior page identities.
- Preserve opaque pages without positional completion.
- Continue with *Axis Mundi* for chain tracing; retain *Everything is Temporary* as the stronger later envelope falsification target.
