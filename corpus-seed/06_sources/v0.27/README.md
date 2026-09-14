# Bundled v0.27 evidence

Seventeen original carrier images are authenticated by exact SHA-256, size and
dimensions. Fourteen numbered filename assets from the 31-entry imported media
manifest were outside this acquisition and are not bundled here.

Five archived author pages support the conditional key derivation. Their text
is normalized to LF for portability, checked against the recorded LF hashes.
The original Windows read hashes are retained in the source records. This is
archived source support, not a new live retrieval during packaging.

`bundle-map.json` maps original repository paths to standalone package paths,
with input and bundled hashes. The evidence reports retain their historical
repository path references; resolve those through this map. Repository tool
copies document reproducibility and are intended to run from their original
repository layout. The standalone verifier is `05_method/verify_rune_code_state.py`.
