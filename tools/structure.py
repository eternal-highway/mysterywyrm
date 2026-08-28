#!/usr/bin/env python3
"""Derive the structural skeleton of the Letters for Titles corpus.

Reads data/corpus.json and reports the chapter/stanza architecture:
which Rune Poem stanzas each chapter covers, whether the chiastic
pairing n + (30-n) holds, and whether the per-rune series are complete.

Usage:  python3 tools/structure.py
"""
import collections, datetime, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book import role_of  # noqa: E402  (shared post-role classifier)

ROLES = ["glyph", "casting", "translating", "stanza", "howto", "isfor", "xyz", "other"]

STANZAS = 29
PAIR_SUM = STANZAS + 1  # 30: stanza n is chaptered with stanza 30-n


def load(path="data/corpus.json"):
    with open(path) as f:
        return json.load(f)


def chapters(recs):
    """Chapter -> sorted post list, ordered by the chapter's first publication."""
    by = collections.defaultdict(list)
    for r in recs:
        for c in r["categories"]:
            by[c].append(r)
    for c in by:
        by[c].sort(key=lambda r: r["date"])
    return dict(sorted(by.items(), key=lambda kv: kv[1][0]["date"]))


def stanza_index(recs):
    """Stanza number -> (gloss, chapter, date), parsed from 'Stanza N: Gloss'."""
    out = {}
    for r in recs:
        m = re.match(r"^Stanza (\d+):\s*(.+)$", r["title"])
        if m:
            chap = r["categories"][0] if r["categories"] else "?"
            out[int(m.group(1))] = (m.group(2), chap, r["date"])
    return out


def main():
    recs = load()
    st = stanza_index(recs)
    chaps = chapters(recs)

    missing = [n for n in range(1, STANZAS + 1) if n not in st]
    print(f"posts: {len(recs)}   words: {sum(r['words'] for r in recs)}   "
          f"images: {sum(r['images'] for r in recs)}")
    print(f"span: {recs[0]['date']} -> {recs[-1]['date']}")
    print(f"stanza posts: {len(st)}/{STANZAS}"
          + (f"   MISSING {missing}" if missing else "   (complete)"))

    for series in ("Rune Casting", "Translating"):
        n = sum(1 for r in recs if r["title"].startswith(series))
        print(f"{series!r} posts: {n}/{STANZAS}"
              + ("   (complete)" if n == STANZAS else "   INCOMPLETE"))

    print("\nchapter architecture (stanza pairs sum to %d):" % PAIR_SUM)
    by_chap = collections.defaultdict(list)
    for n, (gloss, chap, _) in st.items():
        by_chap[chap].append((n, gloss))

    ok = True
    for chap, posts in chaps.items():
        pair = sorted(by_chap.get(chap, []))
        if not pair:
            print(f"  {chap:26} {len(posts):3} posts   (front matter, no stanza)")
        elif len(pair) == 2:
            total = pair[0][0] + pair[1][0]
            ok &= total == PAIR_SUM
            flag = "" if total == PAIR_SUM else f"  <-- sum {total}, expected {PAIR_SUM}"
            print(f"  {chap:26} {len(posts):3} posts   "
                  f"stanza {pair[0][0]:2} ({pair[0][1]}) + stanza {pair[1][0]:2} ({pair[1][1]}){flag}")
        else:
            (n, gloss), = pair
            print(f"  {chap:26} {len(posts):3} posts   "
                  f"stanza {n} ({gloss})   << unpaired center >>")

    print("\nchiastic pairing holds:", ok)

    print("\nchapter composition by post role:")
    header = f"  {'chapter':26}" + "".join(f"{r[:6]:>8}" for r in ROLES) + "   tot"
    print(header)
    for chap, posts in chaps.items():
        c = collections.Counter(role_of(p["title"]) for p in posts)
        print(f"  {chap:26}" + "".join(f"{c.get(r, 0):>8}" for r in ROLES)
              + f"{len(posts):>6}")

    days = sorted({r["date"] for r in recs if r["date"] >= "2022-03-25"})
    wd = collections.Counter(
        datetime.date.fromisoformat(d).strftime("%a") for d in days)
    print(f"publication days: {len(days)}   weekday spread: {dict(wd)}")
    return 0 if ok and not missing else 1


if __name__ == "__main__":
    sys.exit(main())
