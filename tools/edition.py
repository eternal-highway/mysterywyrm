#!/usr/bin/env python3
"""Assemble and collate Tonkin's translation of the Old English Rune Poem.

The corpus carries the poem twice, independently:

  witness A  the 29 `Stanza N:` posts, one per rune, each closing its chapter
  witness B  "O Yes, W." (2022-03-21), the whole poem in a single post

Neither is a copy of the other in the corpus, so they can be collated. This
reads both, checks they agree, and writes the facing-text edition.

Output:
  book/rune-poem.md   all 29 stanzas, Old English against the translation,
                      in futhorc order, with every variant recorded

Exits non-zero if either witness stops parsing as 29 stanzas in futhorc
order, each with Old English and a translation.

Usage:  python3 tools/edition.py [--out book/rune-poem.md]
"""
import argparse, difflib, json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book import FUTHORC  # noqa: E402  (shared rune order)

COLLECTED = "o-yes-w"          # the single-post witness
TERMINATOR = "᛬᛫"              # the punctus that closes every stanza's Old English
STANZAS = 29
PAIR_SUM = STANZAS + 1         # stanza n is chaptered with stanza 30-n
NON_CHAPTER = {"Hwat", "Uncategorized"}


def load(path="data/corpus.json"):
    with open(path) as f:
        return json.load(f)


def split_stanza(paras):
    """Paragraphs -> (Old English lines, translation lines).

    Every stanza sets its Old English first and closes it with the manuscript
    punctus ᛬᛫; the facing translation follows. The split is that mark.
    """
    lines = [p.strip() for p in paras if p.strip()]
    ends = [i for i, p in enumerate(lines) if TERMINATOR in p]
    if not ends:
        return None, None
    cut = ends[-1]
    return lines[:cut + 1], lines[cut + 1:]


def parse_collected(recs):
    """"O Yes, W." -> {stanza number: (glyph, Old English, translation)}.

    The post sets each stanza's rune on a line of its own; those glyph lines
    are the stanza boundaries.
    """
    post = next((r for r in recs if r["slug"] == COLLECTED), None)
    if post is None:
        sys.exit(f"edition: no post with slug {COLLECTED!r}")
    paras = post["paragraphs"]
    marks = [i for i, p in enumerate(paras) if len(p.strip()) <= 3]
    out = {}
    for n, i in enumerate(marks, start=1):
        end = marks[n] if n < len(marks) else len(paras)
        oe, en = split_stanza(paras[i + 1:end])
        out[n] = (paras[i].strip(), oe, en)
    return post, out


def parse_stanza_posts(recs):
    """The 29 `Stanza N:` posts -> {stanza number: (post, Old English, translation)}."""
    out = {}
    for r in recs:
        m = re.match(r"^Stanza (\d+):\s*(.+)$", r["title"])
        if m:
            oe, en = split_stanza(r["paragraphs"])
            out[int(m.group(1))] = (r, oe, en)
    return out


def norm(lines, glyphs):
    """Comparable form: one line, NFC, straight quotes, no leading rune."""
    s = unicodedata.normalize("NFC", " ".join(lines))
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"^[" + glyphs + r"]\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def wording(s):
    """The same text with punctuation discarded, to tell wording from pointing."""
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", "", s)).strip()


def diff_spans(a, b):
    """The words that actually differ, so a variant note points rather than repeats."""
    aw, bw = a.split(), b.split()
    spans = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw).get_opcodes():
        if tag != "equal":
            spans.append((" ".join(aw[i1:i2]), " ".join(bw[j1:j2])))
    return spans


def collate(A, B, glyphs):
    """Compare the witnesses stanza by stanza; return one record per variant."""
    variants = []
    for n in range(1, STANZAS + 1):
        for side, ia, ib in (("Old English", 1, 1), ("Translation", 2, 2)):
            a, b = norm(A[n][ia], glyphs), norm(B[n][ib], glyphs)
            if a != b:
                variants.append({
                    "stanza": n, "side": side, "stanza_post": a, "collected": b,
                    "kind": "wording" if wording(a) != wording(b) else "pointing",
                    "spans": diff_spans(a, b),
                })
    return variants


def check(A, B):
    """Fail loudly if either witness stops being 29 stanzas in futhorc order."""
    problems = []
    for label, w in (("stanza posts", A), ("collected poem", B)):
        missing = [n for n in range(1, STANZAS + 1) if n not in w]
        if missing:
            problems.append(f"{label}: missing stanza(s) {missing}")
        for n, entry in sorted(w.items()):
            if not entry[1] or not entry[2]:
                problems.append(f"{label}: stanza {n} has no Old English or no translation")
    for n, (name, glyph) in enumerate(FUTHORC, start=1):
        if n in B and B[n][0] != glyph:
            problems.append(f"collected poem: stanza {n} marked {B[n][0]!r}, expected {glyph!r} ({name})")
    return problems


def reading(was, now):
    """One variant, phrased as an apparatus entry."""
    if not now:
        return f"omits “{was}”"
    if not was:
        return f"adds “{now}”"
    return f"reads “{now}” for “{was}”"


def verse(lines):
    """Verse block: a blockquote whose line breaks survive rendering."""
    return "\n".join("> " + l + ("  " if i < len(lines) - 1 else "")
                     for i, l in enumerate(lines))


def render(A, collected, variants):
    kinds = {k: sum(1 for v in variants if v["kind"] == k) for k in ("wording", "pointing")}
    by_stanza = {}
    for v in variants:
        by_stanza.setdefault(v["stanza"], []).append(v)

    out = ["# The Rune Poem — Old English and Tonkin's translation", "",
           "All 29 stanzas, in futhorc order, Old English against the facing",
           "translation. Generated and collated by `tools/edition.py`.", "",
           "## The two witnesses", "",
           "The corpus carries the poem twice. The 29 `Stanza N:` posts each close",
           "a chapter with one stanza; **“O Yes, W.”** "
           f"({collected['date']}) sets the whole", "poem in a single post. "
           "Collating them:", "",
           "- All 29 Old English texts agree" if not any(v["side"] == "Old English" for v in variants)
           else f"- {sum(1 for v in variants if v['side'] == 'Old English')} Old English variant(s)",
           f"- {kinds['wording']} translation variant(s) of wording",
           f"- {kinds['pointing']} of punctuation only", "",
           "The stanza posts are the copy-text below: they carry the terminal",
           "punctuation the collected setting drops, and each stanza stands in the",
           "chapter that argued it out. That is an editorial choice, not a verdict:",
           "neither witness is uniformly the later text, and at least one variant",
           "below is better in the collected setting. Every disagreement is recorded",
           "at the stanza where it falls; which reading to prefer, and why, is",
           "argued in `research/edition.md`.", ""]

    for n, (name, glyph) in enumerate(FUTHORC, start=1):
        post, oe, en = A[n]
        gloss = re.match(r"^Stanza \d+:\s*(.+)$", post["title"]).group(1)
        chapter = next((c for c in post["categories"] if c not in NON_CHAPTER), "—")
        pair = PAIR_SUM - n
        pairing = (f"paired with stanza {pair}" if pair != n
                   else "**unpaired — the poem's midpoint and the book's end**")
        out += [f"## {n}. {glyph} {name} — {gloss}", "",
                f"*{chapter}* · {pairing} · [source]({post['link']})", "",
                verse(oe), "", verse(en), ""]
        for v in by_stanza.get(n, []):
            note = "; ".join(reading(was, now) for was, now in v["spans"])
            out += [f"> **Variant** ({v['side']}, {v['kind']}). “O Yes, W.” "
                    + note + ("" if note.endswith((".”", "?”", "!”")) else "."), ""]

    out += ["---", "",
            "Old English text as Tonkin sets it, following the 1705 Hickes printing —",
            "the only witness to the burned manuscript. Translation © Vern Tonkin;",
            "reproduced here for research, with each stanza linked to its source.", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="book/rune-poem.md")
    ap.add_argument("--corpus", default="data/corpus.json")
    args = ap.parse_args()

    recs = load(args.corpus)
    glyphs = "".join(g for _, g in FUTHORC)
    collected, B = parse_collected(recs)
    A = parse_stanza_posts(recs)

    problems = check(A, B)
    if problems:
        for p in problems:
            print("FAIL " + p, file=sys.stderr)
        sys.exit(1)

    variants = collate(A, B, glyphs)
    print(f"both witnesses parse: {STANZAS} stanzas, futhorc order, "
          "Old English and translation present")
    if not any(v["side"] == "Old English" for v in variants):
        print("Old English: all 29 stanzas agree between witnesses")
    for v in variants:
        print(f"  variant  stanza {v['stanza']:>2}  {v['side']:<11} {v['kind']}")
        print(f"      stanza post: {v['stanza_post']}")
        print(f"      collected  : {v['collected']}")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        f.write(render(A, collected, variants))
    print(f"wrote {args.out} ({len(variants)} variants recorded)", file=sys.stderr)


if __name__ == "__main__":
    main()
