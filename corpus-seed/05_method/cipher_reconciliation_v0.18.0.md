# Cipher Reconciliation — 0.18.0

Date: 2026-08-28  
Scope: page-local decoding of *IO is for I/O*, *COW*, and *Night Riddle*; frame-level negative control for canonical AS001

## Result

Three previously unresolved page objects yield exact plaintext, but they do so through three different mechanisms. No shared alphabet, shared byte encoding, shared execution model, or positional key was found. The warranted conclusion is plural and local: identify the medium on each page, obtain its explicit or historical key, and preserve exact output before interpretation.

## 1. IO is for I/O — 8-bit ASCII

Primary page: https://lettersfortitles.com/io-is-for-i-o/

- Input: the visible page binary, retaining displayed byte order.
- Normalization: collapse whitespace between bits; regroup as consecutive 8-bit bytes; no reversal, padding, or character substitution.
- Length: 79 bytes.
- Normalized bitstream SHA-256: `0efe29f4532adfb38a48db45a2f981594fb26487de449fdd028c2e0de45130b8`.
- Exact decoded bytes, shown with the final space before the closing code mark: `If Zeus had turned Io into a beaver instead of a cow she could have swum home. `

The plaintext supplies a direct local hinge among Ovid's Io, cow, beaver, swimming, and home. It is evidence for that composition, not a binary key for other pages.

## 2. COW — bounded interpreter

Primary page: https://lettersfortitles.com/cow/

The long object was treated as program data. A small interpreter implemented only the twelve three-letter commands defined on the page. It performed integer tape/cell operations, balanced-loop jumps, character output, and the documented register operation. It did not evaluate host-language source, touch the filesystem or network, accept user input, or implement unlisted behavior. Execution stopped on normal program completion with a 10,000,000-step cap in place.

### Mechanical record

- Normalized program length: 18,258 characters.
- Token count: 6,086.
- Matched loop pairs: 317 / 317.
- Steps to halt: 83,144.
- Normalized program SHA-256: `026626cdde6af5359789dd24c2bfea44a30682db8d789a98855f49695ffb4708`.
- Input commands (`oom`): 0.
- Integer-output commands (`OOM`): 0.
- Dynamic-execution commands (`mOO`): 0.
- Exact text output: `Is the labyrinth a paradise of solitude? is the labyrinth a balance between selection and exclusion? Is a labyrinth a prison of repetitions and dead ends?\n\n`

### Command histogram

| Command | Count |
|---|---:|
| `moo` | 317 |
| `mOo` | 1,194 |
| `moO` | 1,198 |
| `mOO` | 0 |
| `Moo` | 156 |
| `MOo` | 317 |
| `MoO` | 1,634 |
| `MOO` | 317 |
| `OOO` | 313 |
| `MMM` | 640 |
| `OOM` | 0 |
| `oom` | 0 |

The output holds three competing accounts of the labyrinth: solitude as paradise; selection/exclusion as balance; and repetition/dead ends as prison. This is a local thematic relation to the site's labyrinth and traversal language. It is not proof that the COW output encodes the chapter braid or that all code pages should be executed.

## 3. Night Riddle — Nyctographic Square Alphabet

Primary page: https://lettersfortitles.com/night-riddle/  
Historical key: https://schnark.github.io/lewis-carroll/html/magazines/nyctograph.html  
Contextual cross-check: https://www.lewiscarroll.org/2012/02/07/alices-adventures-in-carrolls-own-square-alphabet/

The page tags identify nictography and a square alphabet. Each handwritten symbol in the lead image was compared with Lewis Carroll's Nyctographic Square Alphabet, preserving the page's five line breaks. The transcription is:

```text
CAN YOU READ
WHAT WAS
WRITTEN
IN THE
DARK?
```

Normalized sentence: `Can you read what was written in the dark?`

The result is self-referential: a writing-in-the-dark system asks whether the reader can read what was written in the dark. The mechanism is historically local and visibly signaled. It is not a key for Rune Code, Pitman shorthand, or other image ciphers.

## 4. Canonical mysterywyrm.gif — negative control

Project artifact AS001 has SHA-256 `20fd510698180bc1e36a3bae2ebcf769341e45cd15e7d21f093c9b89ef400910`, a 360 × 360 canvas, six frames at 10 centiseconds each, and an infinite loop. Coalesced frame inspection shows a stable large upper form, an interlaced wyrm, a lower knot, and a right-hand threefold form. The animation cycles a blink/closure in the wyrm and rotation in the threefold form. No textual metadata, discrete symbol stream, privileged frame, or reproducible plaintext was recovered.

AS001 is user-supplied project evidence, not a site-authored asset. Visual resemblance does not establish a rune identity, an alphabet, or a cipher.

## Stop conditions

- Do not use plaintext semantics to back-fill undecoded symbols.
- Do not transfer a page-local key to another page without direct medium or key evidence.
- Do not run opaque code in a host evaluator; only bounded emulation of a documented instruction set is represented here.
- Do not count thematic resonance as an independent structural proof.
- Leave *Shh*, *The Way*, *Bright Fruits*, *Friþ*, *Soon After it Becomes Water*, and other unresolved objects unresolved until page-specific evidence appears.
