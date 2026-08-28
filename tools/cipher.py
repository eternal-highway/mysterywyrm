#!/usr/bin/env python3
"""Decode the two ciphers hidden in the Letters for Titles corpus.

Cipher 1 — the letter run.  Every post of the year-long run carries a
numbered letter image (`146-M-...jpg`).  The numbers are not publication
order: they are the run folded in half at its centre post, "Turn".  Slot 1
is Turn itself, even slots walk backwards in time, odd slots walk forwards.
Read 1 -> 261 the letters spell one sentence.

Cipher 2 — the rune code.  The artwork on the posts tagged "Rune Code"
writes text in twig runes: a stave with a twigs above and b twigs below
means rune a.b, the b-th rune of the a-th aett.  The "Octave" post is the
key ("Feoh, Wealth is 1.1 ... one octave away ... is 2.1 Haegl").

Usage:  python3 tools/cipher.py            # decode cipher 1, summarize both
        python3 tools/cipher.py --table    # slot-by-slot table for cipher 1
        python3 tools/cipher.py --key      # the aett.position rune key
"""
import json, os, re, sys

RUN_START = "2022-03-21"   # first post of the run; the 2020 seed post is outside it
PIVOT = "turn"             # the post the numbering folds around
SLOTS = 261                # one per post of the run

# a numbered letter image: <slot>-<mark>-<the rest of the filename>
NUMBERED = re.compile(r"/uploads/\d{4}/\d{2}/(\d{1,3})-([^-/]+)-")

MARKS = {"period": ".", "comma": ",", "apostrophe": "'", "exclamation": "!"}

# The sentence the recovered marks spell.  Two slots hold letters the
# harvest did not recover but the sentence fixes; every other blank slot
# is a word space.
INFERRED = {78: "R (of WRITTEN)", 182: "E (of WE)"}
READING = ("LISTEN! COME TO THE MIRROR. SEE[?] YOU ARE SLIPPING AWAY. "
           "MOMENTARY. WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR "
           "CONSORT AND ONLY IN THE MEMORIES OF OTHERS WILL YOU PERSIST. "
           "WE ARE EACH OTHER'S ONLY IMMORTALITY ON EARTH, OTHERWISE "
           "EVERYTHING IS TEMPORARY.")

# The Old English Rune Poem's 29 runes in three octaves (aettir) of eight
# plus the five late vowels the project's own dictionary calls "an amended
# quintet".  Cipher 2 addresses a rune as <aett>.<position>.
FUTHORC = [
    ("Feoh", "F"), ("Ur", "U"), ("Thorn", "TH"), ("Os", "O"),
    ("Rad", "R"), ("Cen", "C"), ("Gifu", "G"), ("Wyn", "W"),
    ("Haegl", "H"), ("Nyd", "N"), ("Is", "I"), ("Ger", "J"),
    ("Eoh", "EO"), ("Peorth", "P"), ("Eolhx", "X"), ("Sigel", "S"),
    ("Tiw", "T"), ("Beorc", "B"), ("Eh", "E"), ("Mann", "M"),
    ("Lagu", "L"), ("Ing", "NG"), ("Ethel", "OE"), ("Daeg", "D"),
    ("Ac", "A"), ("Aesc", "AE"), ("Yr", "Y"), ("Ior", "IO"), ("Ear", "EA"),
]


def load(path="data/corpus.json"):
    with open(path) as f:
        return json.load(f)


def run_posts(recs):
    """The 261 posts of the run, in publication order."""
    return sorted((r for r in recs if r["date"] >= RUN_START),
                  key=lambda r: (r["date"], r["id"]))


def fold(i, pivot):
    """Slot number for the i-th post of the run (0-based), folded at pivot.

    The pivot is slot 1; each step forward in time takes the next odd slot,
    each step backward the next even one.  This is the chiasm of the book
    applied to the run itself: the two halves read inward to the middle.
    """
    if i == pivot:
        return 1
    return 2 * (i - pivot) + 1 if i > pivot else 2 * (pivot - i)


def mark_of(post):
    """(slot number the author wrote on the file, mark, filename) or None.

    The mark is the letter or punctuation the filename names; a numbered
    image whose token is neither (two of them are named for the artwork
    instead) comes back as '?'.
    """
    for url in post["image_urls"]:
        m = NUMBERED.search(url)
        if not m:
            continue
        token = m.group(2)
        if len(token) == 1:
            mark = token.upper()
        else:
            mark = MARKS.get(token.lower(), "?")
        return int(m.group(1)), mark, url.rsplit("/", 1)[-1]
    return None


def decode(recs):
    """slot -> (mark or None, post, written number or None, filename or None)."""
    posts = run_posts(recs)
    pivot = next(i for i, p in enumerate(posts) if p["slug"] == PIVOT)
    table = {}
    for i, p in enumerate(posts):
        got = mark_of(p)
        slot = fold(i, pivot)
        table[slot] = (got[1] if got else None, p,
                       got[0] if got else None, got[2] if got else None)
    return table, posts, pivot


def message(table):
    return "".join(table.get(n, (None,))[0] or "·" for n in range(1, SLOTS + 1))


def main():
    args = sys.argv[1:]
    if "--key" in args:
        print("cipher 2 — twig runes: a twigs above the stave, b twigs below = rune a.b")
        for a in range(4):
            row = [f"{a + 1}.{b + 1} {n:6} {v:2}"
                   for b, (n, v) in enumerate(FUTHORC[a * 8:a * 8 + 8])]
            print("  " + "   ".join(row))
        print("\n  worked example — the plate on 'Arrows' (2022-06-06), headed 'Par 17.27':")
        print("  3.1 2.1 3.3 | 4.1 1.5 1.5 1.4 1.8 | 1.4 2.2 3.3 | ...")
        print("  T   H   E   | A   R   R   O   W   | O   N   E   | ...")
        print("  = THE ARROW ONE FORESEES ARRIVES MORE SLOWLY")
        print("  (Dante, Paradiso XVII.27: 'che saetta previsa vien piu lenta')")
        return 0

    recs = load()
    table, posts, pivot = decode(recs)
    text = message(table)

    ok = len(posts) == SLOTS and pivot * 2 + 1 == SLOTS
    print(f"run posts: {len(posts)}   pivot: {posts[pivot]['title']!r} "
          f"({posts[pivot]['date']}), post {pivot + 1} of {len(posts)}")
    print(f"fold centred: {ok}")

    found = sum(1 for n in range(1, SLOTS + 1) if table.get(n, (None,))[0])
    blank = [n for n in range(1, SLOTS + 1) if not table.get(n, (None,))[0]]
    print(f"marks recovered: {found}/{SLOTS}   "
          f"(· = post carries no numbered image, ? = image not named for a letter)\n")
    print(text)
    print(f"\nreading: {READING}\n")
    print("slots that carry no letter of their own:")
    for n in blank:
        p = table[n][1]
        print(f"  {n:4}  {p['date']}  {p['title']}"
              + ("" if n not in INFERRED else f"   << supplies {INFERRED[n]} >>"))
    print()

    slips = [(n, w, table[n][1]["title"]) for n, (mk, _, w, _) in table.items()
             if w is not None and w != n]
    if slips:
        print("slots whose written number disagrees with the fold "
              "(author's numbering slips; the fold and the sentence agree):")
        for n, written, title in sorted(slips):
            print(f"  slot {n:3}  file says {written:3}  {title}")

    if "--table" in args:
        print("\nslot  mark  date        post")
        for n in range(1, SLOTS + 1):
            mk, p, written, fn = table.get(n, (None, None, None, None))
            flag = "" if written in (None, n) else f"   [file says {written}]"
            print(f"{n:4}  {(mk or '-'):4}  {p['date']}  {p['title']}{flag}")

    return 0 if ok else 1


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.exit(main())
