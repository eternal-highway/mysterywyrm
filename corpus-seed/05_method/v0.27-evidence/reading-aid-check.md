# Post-freeze reading-aid check

After freezing the independent observations, ran:

```sh
python tools/tally.py archive/code/2022_05_axaxaxas-mlo-letters-for-titles-vern-tonkin-large-scaled.jpg
```

Source-byte SHA-256:
`6953e91183de5f2365ea68cafc325aa27bd2b1dea3211a01c577d83d3029c14b`.
Observed text output:

```text
JOU WHO READ
ME - ARE JRU
WERTAIN JOU
UNDERXTANL MJ
LANGUAGE [0.1]
```

The printed groups agree with the 10/8/10/12/8 unit structure once the final
`[0.1]` detection is recognized as the visibly drawn question mark. The four
coordinate differences from the independent visual sequence are:

| Location | Tool | Independent visual candidate |
|---|---|---|
| Row 2 unit 7 | 1.5 | 1.4 |
| Row 3 unit 1 | 1.8 | 1.6 |
| Row 4 unit 6 | 2.7 | 2.8 |
| Row 4 unit 10 | 3.5 | 3.8 |

These differences match the known limitations of this counting aid; they were
not silently substituted into the frozen observations. The independent visual
values remain medium-confidence where the coils are dense. The tool's exit 0
means it ran, not that any transcription has passed a correctness test.
