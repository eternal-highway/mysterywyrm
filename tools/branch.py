#!/usr/bin/env python3
"""Read a branch-rune plate from Letters for Titles.

The `Rune Code` posts carry photographs of a notebook in which each rune is
drawn as a stem with twigs: the count above the stem gives the aett of the
futhorc, the count below gives the position inside it. The arrow's tail V is
not decoration -- its upper arm is the first twig above and its lower arm the
first twig below, which is why every rune has at least aett 1, position 1.

This finds the rows, the stem of each row, and the arrowheads (a head is a
closed triangle, the only shape on the page enclosing white; the shaft
crossing it splits that hole in two, so nearby holes are merged), then counts
the twigs on each side of every arrow at a range of distances from the stem.

It is a READING AID, not a verifier. Hand-drawn twigs are uneven: short ones
are missed at large offsets and merge with their neighbours at small ones, so
the count per offset is reported and the reader adjudicates. Counts marked
stable (the same at every offset) can be trusted; the rest need an eye.

Unlike the rest of tools/, this needs Pillow and numpy.

Usage:
  python3 tools/branch.py PLATE.jpg          # every row
  python3 tools/branch.py PLATE.jpg --row 1  # one row
"""
import argparse, collections, sys
from collections import deque

try:
    from PIL import Image
    import numpy as np
except ImportError:
    sys.exit("branch.py needs Pillow and numpy: pip install pillow numpy")

# The 29 runes in futhorc order, split into aetts of 8, 8, 8 and 5.
AETT = [["F", "U", "TH", "O", "R", "C", "G", "W"],
        ["H", "N", "I", "J", "EO", "P", "X", "S"],
        ["T", "B", "E", "M", "L", "NG", "OE", "D"],
        ["A", "AE", "Y", "IO", "EA"]]


def letter(a, p):
    if 1 <= a <= 4 and 1 <= p <= len(AETT[a - 1]):
        return AETT[a - 1][p - 1]
    return "[%d.%d]" % (a, p)


def inkmask(path):
    """The green pen, separated from paper and the printed rule."""
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    return (G - R > 18) & (G - B > 5) & (R < 170)


def hruns(mask, minlen):
    """Pixels inside a horizontal ink run at least minlen long: the shafts."""
    out = np.zeros_like(mask)
    for y in range(mask.shape[0]):
        row = mask[y]
        x = 0
        while x < len(row):
            if not row[x]:
                x += 1
                continue
            s = x
            while x < len(row) and row[x]:
                x += 1
            if x - s >= minlen:
                out[y, s:x] = True
    return out


def bands(mask, minink=8, gap=6):
    """Rows of writing, as (y0, y1) bands of inked scanlines."""
    rows = mask.sum(axis=1)
    ys = [i for i, v in enumerate(rows) if v > minink]
    if not ys:
        return []
    out, cur = [], [ys[0]]
    for y in ys[1:]:
        if y - cur[-1] <= gap:
            cur.append(y)
        else:
            out.append((cur[0], cur[-1]))
            cur = [y]
    out.append((cur[0], cur[-1]))
    return out


def stemline(shaft):
    """The stem's y at every x, interpolated across the gaps."""
    W = shaft.shape[1]
    s = np.full(W, -1.0)
    for x in range(W):
        ys = np.nonzero(shaft[:, x])[0]
        if len(ys):
            s[x] = ys.mean()
    k = np.nonzero(s >= 0)[0]
    return np.interp(np.arange(W), k, s[k]) if len(k) >= 2 else None


def holes(sub, minarea=4):
    """Enclosed white: one per arrowhead, or two where the shaft splits it."""
    H, W = sub.shape
    bg = ~sub
    seen = np.zeros((H, W), bool)
    q = deque()
    for x in range(W):
        for y in (0, H - 1):
            if bg[y, x] and not seen[y, x]:
                seen[y, x] = True
                q.append((y, x))
    for y in range(H):
        for x in (0, W - 1):
            if bg[y, x] and not seen[y, x]:
                seen[y, x] = True
                q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W and bg[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True
                q.append((ny, nx))
    enc = bg & ~seen
    done = np.zeros((H, W), bool)
    out = []
    for y in range(H):
        for x in range(W):
            if enc[y, x] and not done[y, x]:
                q = deque([(y, x)])
                done[y, x] = True
                px = [(y, x)]
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if (0 <= ny < H and 0 <= nx < W and enc[ny, nx]
                                and not done[ny, nx]):
                            done[ny, nx] = True
                            q.append((ny, nx))
                            px.append((ny, nx))
                if len(px) >= minarea:
                    xs = [b for _, b in px]
                    out.append((min(xs), max(xs)))
    return sorted(out)


def merge(spans, gap=10):
    out = []
    for s in spans:
        if out and s[0] - out[-1][1] <= gap:
            out[-1] = (out[-1][0], max(out[-1][1], s[1]))
        else:
            out.append(s)
    return out


def crossings(sub, stem, off):
    """Columns where ink sits on the line parallel to the stem at `off`."""
    H, W = sub.shape
    b = np.zeros(W, bool)
    for x in range(W):
        y = int(round(stem[x] + off))
        if 0 <= y < H:
            b[x] = sub[y, x]
    return b


def centres(b, gap=1):
    xs = np.nonzero(b)[0]
    if len(xs) == 0:
        return []
    out, cur = [], [xs[0]]
    for x in xs[1:]:
        if x - cur[-1] <= gap:
            cur.append(x)
        else:
            out.append((cur[0] + cur[-1]) // 2)
            cur = [x]
    out.append((cur[0] + cur[-1]) // 2)
    return out


def read_row(mask, shaft, y0, y1, offs):
    sub = mask[y0:y1 + 1]
    stem = stemline(shaft[y0:y1 + 1])
    if stem is None:
        return None
    heads = merge(holes(sub))
    inhead = lambda x: any(h[0] - 5 <= x <= h[1] + 5 for h in heads)
    up = {o: centres(crossings(sub, stem, -o)) for o in offs}
    dn = {o: centres(crossings(sub, stem, o)) for o in offs}
    arrows, prev = [], -1
    for h0, h1 in heads:
        ca = [len([x for x in up[o] if prev < x < h0 and not inhead(x)])
              for o in offs]
        cp = [len([x for x in dn[o] if prev < x < h0 and not inhead(x)])
              for o in offs]
        a = collections.Counter(ca).most_common(1)[0][0]
        p = collections.Counter(cp).most_common(1)[0][0]
        arrows.append({"head": (h0 + h1) // 2, "up": ca, "dn": cp,
                       "aett": a, "pos": p, "letter": letter(a, p),
                       "stable": len(set(ca)) == 1 and len(set(cp)) == 1})
        prev = h1
    return arrows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plate")
    ap.add_argument("--row", type=int, help="read only this row (1-based)")
    ap.add_argument("--offsets", default="6:15",
                    help="distances from the stem to sample, START:STOP")
    args = ap.parse_args()

    lo, hi = (int(v) for v in args.offsets.split(":"))
    offs = range(lo, hi)
    mask = inkmask(args.plate)
    shaft = hruns(mask, 12)
    rows = bands(mask)
    print("%s: %d rows" % (args.plate, len(rows)))
    for i, (y0, y1) in enumerate(rows, 1):
        if args.row and i != args.row:
            continue
        arrows = read_row(mask, shaft, y0, y1, offs)
        if not arrows:
            print("row %d: no stem found" % i)
            continue
        reading = "".join(a["letter"] for a in arrows)
        firm = sum(a["stable"] for a in arrows)
        print("\nrow %d: %-24s (%d of %d arrows stable)"
              % (i, reading, firm, len(arrows)))
        for a in arrows:
            print("   head x%-5d %-6s %d.%-3d %s  up %s  dn %s"
                  % (a["head"], a["letter"], a["aett"], a["pos"],
                     "  " if a["stable"] else "~?", a["up"], a["dn"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
