#!/usr/bin/env python3
"""Recover the message hidden in the image filenames of Letters for Titles.

Images uploaded for the run are named `N-C-slug.ext`, where N is a position
from 1 to 261 and C is a single character: a letter, or a punctuation mark
spelled out (`period`, `Comma`, `apostrophe`, `exclamation`) because a
filename cannot carry "." or "'" through an upload path. Sorted by N, the
characters spell one continuous sentence. Positions with no numbered image
are the spaces between words.

The numbering is laid down chiastically, the same way the chapters read the
Rune Poem inward from both ends -- but running the other way, so the message
is written from the outside in and read from the inside out:

  posts   1-130   carry the EVEN positions, counting down  260, 258, ... 2
  post      131   is "Turn", and carries position 1: the L of LISTEN
  posts 131-261   carry the ODD  positions, counting up      1, 3, ... 261

The run's last post, "The Middle", carries position 261, the full stop. The
run's fourth post is titled "Decode".

Output:
  research/cipher.md   the message, how it is laid down, and the full index

Exits non-zero if the arms stop being monotonic, if the pivot moves off
"Turn", or if any recovered character contradicts the reading recorded here.

Usage:  python3 tools/cipher.py [--out research/cipher.md]
"""
import argparse, collections, json, re, sys

NUMBER = re.compile(r"^(\d{1,3})-")
TOKEN = re.compile(r"^(\d{1,3})-([^-]+)-")

PUNCT = {
    "period": ".", "Period": ".", ".": ".",
    "Comma": ",", "apostrophe": "'", "exclamation": "!",
}

POSITIONS = 261
PIVOT_TITLE = "Turn"
RUN_START = "2022-03-21"

# The reading, one character per position, gaps included. Verified against
# every recovered filename below; the bracketed positions in NOTES are the
# six characters no surviving filename carries, supplied by context.
MESSAGE = (
    "LISTEN! COME TO THE MIRROR. SEE? YOU ARE SLIPPING AWAY. MOMENTARY. "
    "WRITTEN IN LIGHT. YOU HAVE CHOSEN THE EARTH AS YOUR CONSORT AND ONLY "
    "IN THE MEMORIES OF OTHERS WILL YOU PERSIST. WE ARE EACH OTHER'S ONLY "
    "IMMORTALITY ON EARTH, OTHERWISE EVERYTHING IS TEMPORARY."
)

# Positions where two files disagree. Each stray sits a short distance from
# a position whose letter is missing entirely -- an off-by-N slip in the
# author's own numbering -- so each is resolved by the gap it belongs in.
COLLISIONS = {
    29: ("S", "R", "stray; 'MIRROR. SEE' needs S"),
    79: ("L", "N", "stray N belongs at 77, the N of IN"),
    142: ("E", "M", "stray M belongs at 144, the M of MEMORIES"),
}

# Positions carrying no character: an irregular filename, or none at all.
NOTES = {
    32: "`32-Letters-for-Titles-...gif` names no character because none can be "
        "named — the glyph is `?`, the one mark that cannot sit in a URL, since "
        "it opens the query string. The image *is* the question mark, drawn as "
        "an illuminated interlace initial.",
    39: "no file; context gives R (ARE)",
    69: "no file; context gives R (WRITTEN)",
    77: "no file; context gives N (IN) -- see the stray at 79",
    144: "no file; context gives M (MEMORIES) -- see the stray at 142",
    182: "no file; context gives E (WE)",
    194: "file `194-Twist-...` names the centre chapter where T is due",
}


def load(path="data/corpus.json"):
    with open(path) as f:
        return json.load(f)


def run_posts(recs):
    """The 261 posts of the run itself, in publication order."""
    posts = [r for r in recs if r["date"] >= RUN_START]
    posts.sort(key=lambda r: (r["date"], r["id"]))
    return posts


def scan(posts):
    """Position -> {char or None: [post, ...]} over every numbered filename."""
    out = collections.defaultdict(lambda: collections.defaultdict(list))
    for p in posts:
        for url in p["image_urls"]:
            name = url.rsplit("/", 1)[-1]
            m = NUMBER.match(name)
            if not m:
                continue
            n = int(m.group(1))
            t = TOKEN.match(name)
            tok = t.group(2) if t else None
            if tok in PUNCT:
                ch = PUNCT[tok]
            elif tok and len(tok) == 1:
                ch = tok.upper()
            else:
                ch = None          # bare or irregular filename: a marker only
            out[n][ch].append(p)
    return out


def resolve(found):
    """Position -> single character, applying the documented collisions."""
    out = {}
    for n, byc in found.items():
        chars = sorted(c for c in byc if c)
        if not chars:
            continue
        if len(chars) == 1:
            out[n] = chars[0]
        elif n in COLLISIONS:
            out[n] = COLLISIONS[n][0]
    return out


def expected():
    """MESSAGE as position -> character, gaps dropped."""
    if len(MESSAGE) != POSITIONS:
        raise SystemExit("MESSAGE is %d chars, expected %d"
                         % (len(MESSAGE), POSITIONS))
    return {i: c for i, c in enumerate(MESSAGE, 1) if c != " "}


def arms(posts, found, got):
    """(even, odd, pivot ordinal) as [(post ordinal, position), ...].

    Built from the resolved characters only: a stray file sits at a position
    already spoken for, so counting it would put its own post out of order.
    """
    ordinal = {id(p): i for i, p in enumerate(posts, 1)}
    even, odd = [], []
    for n, ch in got.items():
        i = ordinal[id(found[n][ch][0])]
        (even if n % 2 == 0 else odd).append((i, n))
    even.sort()
    odd.sort()
    return even, odd, min(i for i, _ in odd)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="research/cipher.md")
    args = ap.parse_args()

    posts = run_posts(load())
    found = scan(posts)
    got = resolve(found)
    want = expected()
    even, odd, pivot = arms(posts, found, got)

    print("positions carrying a numbered image: %d/%d" % (len(found), POSITIONS))
    print("characters recovered: %d   supplied from context: %d"
          % (len(got), len(want) - len(got)))

    # Every character we recovered must agree with the reading.
    bad = sorted(n for n, c in got.items() if want.get(n) != c)
    print("recovered characters agreeing with the reading: %d/%d"
          % (len(got) - len(bad), len(got)))
    for n in bad:
        print("  MISMATCH at %d: file says %r, reading says %r"
              % (n, got[n], want.get(n)))

    # The two arms and the post that turns between them.
    ev = [n for _, n in even]
    od = [n for _, n in odd]
    desc = all(a >= b for a, b in zip(ev, ev[1:]))
    asc = all(a <= b for a, b in zip(od, od[1:]))
    pivot_title = posts[pivot - 1]["title"]
    print("even arm: %d images, posts %d-%d, descending %s"
          % (len(even), min(i for i, _ in even), max(i for i, _ in even), desc))
    print("odd  arm: %d images, posts %d-%d, ascending %s"
          % (len(odd), min(i for i, _ in odd), max(i for i, _ in odd), asc))
    print("pivot: post #%d %r (%s)" % (pivot, pivot_title, posts[pivot - 1]["date"]))

    ok = not bad and desc and asc and pivot_title == PIVOT_TITLE
    with open(args.out, "w") as f:
        f.write(report(posts, found, got, want, even, odd, pivot))
    print("wrote", args.out)
    print("\ncipher holds:", ok)
    return 0 if ok else 1


def report(posts, found, got, want, even, odd, pivot):
    L = []
    w = L.append
    w("# The message in the filenames\n")
    w("Every image uploaded for the run is named `N-C-slug.ext`: a position\n"
      "from 1 to %d, then a single character. Punctuation is spelled out\n"
      "(`period`, `Comma`, `apostrophe`, `exclamation`) because a filename\n"
      "cannot carry `.` or `'` through an upload path. Sorted by position the\n"
      "characters spell one sentence; positions with no numbered image are the\n"
      "spaces between the words.\n" % POSITIONS)
    w("\n> **%s**\n" % MESSAGE.strip())
    w("\n%d of the %d positions carry a numbered image and %d characters are\n"
      "recovered directly from filenames. `tools/cipher.py` rebuilds this from\n"
      "`data/corpus.json` and exits non-zero if it stops holding.\n"
      % (len(found), POSITIONS, len(got)))

    w("\n## How it is laid down\n")
    w("The numbering runs chiastically, exactly as the chapters read the Rune\n"
      "Poem inward from both ends — but in the opposite direction, so that the\n"
      "message is *written* from the outside in and *read* from the inside out.\n")
    w("\n| arm | posts | positions | direction |")
    w("|---|---|---|---|")
    w("| even | 1–%d | %d → %d | descending |"
      % (pivot - 1, max(n for _, n in even), min(n for _, n in even)))
    w("| odd | %d–%d | %d → %d | ascending |"
      % (pivot, len(posts), min(n for _, n in odd), max(n for _, n in odd)))
    w("\nNo post carries both parities. The pivot is post #%d, **“%s”** (%s) —\n"
      "the 22-word hinge that sits in the `Hwat` front matter and belongs to no\n"
      "chapter. It carries position 1, the `L` of LISTEN, and its entire text is\n"
      "Dante at the foot of the hill:\n"
      % (pivot, PIVOT_TITLE, posts[pivot - 1]["date"]))
    w("\n> %s\n" % posts[pivot - 1]["text"].strip())
    w("\nThe run's final post, **“The Middle”**, carries position %d: the full\n"
      "stop that closes the sentence. The run's fourth post, three days in, is\n"
      "titled **“Decode”**, has no text at all, and is tagged `Code`.\n"
      % POSITIONS)
    w("\nThe sentence ends on **“EVERYTHING IS TEMPORARY”**, which is the name of\n"
      "the first chapter, and opens on **“LISTEN!”**, the usual rendering of\n"
      "*Hwæt* — the name of the category holding the front matter. The message\n"
      "closes the same loop the chapters do.\n")

    w("\n## Strays and gaps\n")
    w("Three positions carry two files. Each stray sits a short distance from a\n"
      "position whose character is missing entirely — an off-by-N slip in the\n"
      "author's own numbering — so each resolves into the gap it belongs in.\n")
    w("\n| position | kept | stray | resolution |")
    w("|---|---|---|---|")
    for n, (keep, stray, why) in sorted(COLLISIONS.items()):
        w("| %d | `%s` | `%s` | %s |" % (n, keep, stray, why))
    w("\n%d positions carry no character of their own:\n" % len(NOTES))
    for n, note in sorted(NOTES.items()):
        w("- **%d** — %s" % (n, note))

    w("\n## The index\n")
    w("\n| pos | char | source | post | date |")
    w("|---|---|---|---|---|")
    for n in range(1, POSITIONS + 1):
        if n not in want:
            continue
        if n in got:
            p = found[n][got[n]][0]
            src = "filename"
            title, date = p["title"], p["date"]
        else:
            src, title, date = "context", "—", "—"
        w("| %d | `%s` | %s | %s | %s |" % (n, want[n], src, title, date))
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    sys.exit(main())
