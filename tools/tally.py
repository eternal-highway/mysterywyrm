#!/usr/bin/env python3
"""Read a tally-and-serpentine plate from Letters for Titles.

The Axaxaxas mlo plate (notebook page 55) drops the costume entirely: every
rune is a bare group of vertical strokes in blue ballpoint with a serpentine
coiled through them. As everywhere in the Rune Code, a rune is two counts:

    aett     = the number of UPRIGHTS
    position = the number of ARMS the serpentine makes across them

and the arms are what the eye actually has to count. Counting them directly
fails -- the arms are curved and the ink runs together -- but the uprights and
the arms together weave a lattice, and each gap between two consecutive arms
encloses a cell of white paper. So the arms can be counted through the holes
they leave:

    position = (cells enclosed in the coil's LEFT-hand column) + 1

which is what this does. Holes are the same trick branch.py uses for
arrowheads: enclosed white is the one thing on the page that is unambiguous.

Calibrated against the seven runes of WHO and READ in row 1, whose values are
fixed independently by the working note on the facing page (`READ` written
over `1.5 3.3 4.1 3.8`); it reads all seven correctly, and 44 of the plate's
48 runes come out stable under every threshold tried. The other four are dense
and want an eye, so the per-rune counts are printed too.

Like branch.py this is a READING AID, not a verifier: it does not check
itself and does not exit non-zero. Unlike the rest of tools/ it needs Pillow
and numpy.

Usage:
  python3 tools/tally.py PLATE.jpg
"""
import argparse, sys
from collections import deque

try:
    from PIL import Image
    import numpy as np
except ImportError:
    sys.exit("tally.py needs Pillow and numpy: pip install pillow numpy")

AETT = [["F", "U", "TH", "O", "R", "C", "G", "W"],
        ["H", "N", "I", "J", "EO", "P", "X", "S"],
        ["T", "B", "E", "M", "L", "NG", "OE", "D"],
        ["A", "AE", "Y", "IO", "EA"]]


def letter(a, p):
    if 1 <= a <= 4 and 1 <= p <= len(AETT[a - 1]):
        return AETT[a - 1][p - 1]
    return "[%d.%d]" % (a, p)


def boxmean(a, r):
    """Mean of a over a (2r+1) square, via an integral image."""
    a = a.astype(np.float64)
    H, W = a.shape
    ii = np.zeros((H + 1, W + 1))
    ii[1:, 1:] = a.cumsum(0).cumsum(1)
    y0, y1 = np.clip(np.arange(H) - r, 0, H), np.clip(np.arange(H) + r + 1, 0, H)
    x0, x1 = np.clip(np.arange(W) - r, 0, W), np.clip(np.arange(W) + r + 1, 0, W)
    s = (ii[np.ix_(y1, x1)] - ii[np.ix_(y0, x1)]
         - ii[np.ix_(y1, x0)] + ii[np.ix_(y0, x0)])
    return s / np.outer(y1 - y0, x1 - x0)


def luminance(path):
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    return 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]


def onpaper(lum, x0, x1, y0, y1, pad=15, floor=110):
    """True if this mark sits on the lit page rather than on the desk.

    The notebook's edge and the dark wood beyond it clear every ink test --
    they are as dark as the pen and as thick -- but they are not on paper, and
    the paper around a rune is bright even where the light has fallen off, so
    the MEDIAN of the neighbourhood separates them cleanly (about 190 around a
    rune against about 23 off the page) where a brighter percentile does not:
    the desk carries specular highlights as bright as paper, just not many.
    """
    H, W = lum.shape
    win = lum[max(0, y0 - pad):min(H, y1 + pad),
              max(0, x0 - pad):min(W, x1 + pad)]
    return win.size > 0 and np.median(win) > floor


def inkmask(path, dark=40):
    """The ballpoint, less the paper, the printed rule and the red margin.

    The light falls across the page, so "dark" is measured against a local
    background rather than a fixed threshold -- the same fix branch.py needed.
    Colour is no use here: at the foot of the page the light goes warm enough
    to drag the blue ink's B-R below any usable cut, so only the red margin
    line is excluded by colour. The printed rule survives that test but is
    thinner than the pen, so it goes by stroke thickness instead.
    """
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    lum = 0.299 * R + 0.587 * G + 0.114 * B
    m = (boxmean(lum, 60) - lum > dark) & (R - B < 25)
    return thick(m, 3)


def thick(m, minrun):
    """Drop ink in vertical runs shorter than minrun: the printed rule."""
    H, W = m.shape
    out = np.zeros_like(m)
    for x in range(W):
        col = m[:, x]
        y = 0
        while y < H:
            if not col[y]:
                y += 1
                continue
            s = y
            while y < H and col[y]:
                y += 1
            if y - s >= minrun:
                out[s:y, x] = True
    return out


def close(m, r=2):
    """Bridge the gaps the camera left in the strokes, so holes stay holes."""
    def dil(a):
        o = a.copy()
        for dy in range(-r, r + 1):
            for dx in range(-r, r + 1):
                if dy * dy + dx * dx <= r * r:
                    o |= np.roll(np.roll(a, dy, 0), dx, 1)
        return o
    return ~dil(~dil(m))


def blobs(m, minpx=120):
    lab = np.zeros(m.shape, np.int32)
    out = []
    n = 0
    ys, xs = np.nonzero(m)
    for y, x in zip(ys, xs):
        if lab[y, x]:
            continue
        n += 1
        q = deque([(y, x)])
        lab[y, x] = n
        P = [(y, x)]
        while q:
            cy, cx = q.popleft()
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = cy + dy, cx + dx
                    if (0 <= ny < m.shape[0] and 0 <= nx < m.shape[1]
                            and m[ny, nx] and not lab[ny, nx]):
                        lab[ny, nx] = n
                        q.append((ny, nx))
                        P.append((ny, nx))
        Y = [p[0] for p in P]
        X = [p[1] for p in P]
        if len(P) >= minpx:
            out.append((min(X), max(X), min(Y), max(Y)))
    return sorted(out)


def rows(m, minink=120, gap=25, lo=60, hi=220, pad=45):
    """Bands of writing. The page texture and the objects lying around the
    notebook keep a floor of ink at every y, so the cut is well above zero;
    what survives it is either a row of runes or something far too tall to be
    one (the facing page at the top, the book at the foot), so bands are kept
    by height and then padded back out to catch the descenders."""
    prof = m.sum(axis=1)
    ys = [y for y, v in enumerate(prof) if v > minink]
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
    H = m.shape[0]
    return [(max(0, a - pad), min(H - 1, b + pad))
            for a, b in out if lo <= b - a <= hi]


def uprights(sub, frac=0.55, merge=5):
    """Near-vertical strokes running most of the rune's height."""
    h, w = sub.shape
    best = np.zeros(w, int)
    for s in [i * 0.04 for i in range(-5, 6)]:
        for x0 in range(w):
            cur = 0
            for y in range(h):
                x = int(round(x0 + s * (y - h / 2)))
                if 0 <= x < w and sub[y, x]:
                    cur += 1
                    if cur > best[x0]:
                        best[x0] = cur
                else:
                    cur = 0
    cols = [x for x in range(w) if best[x] >= frac * h]
    out, cur = [], []
    for x in cols:
        if cur and x - cur[-1] > merge:
            out.append((cur[0] + cur[-1]) // 2)
            cur = []
        cur.append(x)
    if cur:
        out.append((cur[0] + cur[-1]) // 2)
    return out


def holes(sub, minarea=30):
    """Enclosed white: one per cell of the lattice."""
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
                P = [(y, x)]
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if (0 <= ny < H and 0 <= nx < W and enc[ny, nx]
                                and not done[ny, nx]):
                            done[ny, nx] = True
                            q.append((ny, nx))
                            P.append((ny, nx))
                if len(P) >= minarea:
                    out.append((sum(p[0] for p in P) / len(P),
                                sum(p[1] for p in P) / len(P)))
    return out


def position(sub, ups):
    """Arms across the uprights = cells in the coil's left column, plus one."""
    hs = holes(sub)
    if not hs or not ups:
        return 1, len(hs)
    cys = sorted(cy for cy, cx in hs if cx < min(ups) - 2)
    if not cys:
        return 1, len(hs)
    tol = max(8, sub.shape[0] * 0.06)
    levels = 1
    for i in range(1, len(cys)):
        if cys[i] - cys[i - 1] > tol:
            levels += 1
    return levels + 1, len(hs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plate")
    ap.add_argument("--pad", type=int, default=7)
    ap.add_argument("--wordgap", type=int, default=60)
    ap.add_argument("--margin", type=int, default=250,
                    help="ink this far past the last rune is the "
                         "notebook edge, not writing")
    args = ap.parse_args()

    m = close(inkmask(args.plate))
    lum = luminance(args.plate)
    text, detail = [], []
    for i, (y0, y1) in enumerate(rows(m), 1):
        band = np.zeros_like(m)
        band[y0:y1 + 1] = m[y0:y1 + 1]
        gs = blobs(band)
        if not gs:
            continue
        line, prev = "", None
        for (x0, x1, gy0, gy1) in gs:
            w, h = x1 - x0, gy1 - gy0
            if h < 15 and w >= 40:          # the drawn dash between two words
                line += " - "
                prev = x1
                continue
            if h < 30 or w < 35:            # specks, and the printed rule's ends
                continue
            if not onpaper(lum, x0, x1, gy0, gy1):
                continue
            if prev is not None and x0 - prev > args.margin:
                break
            if prev is not None and x0 - prev > args.wordgap:
                line += " "
            prev = x1
            p = args.pad
            sub = m[max(0, gy0 - p):gy1 + p, max(0, x0 - p):x1 + p]
            ups = uprights(sub)
            pos, nh = position(sub, ups)
            L = letter(len(ups), pos)
            line += L
            detail.append((i, x0, len(ups), pos, L, nh))
        text.append(" ".join(line.split()))
    print("\n".join(text))
    print()
    for d in detail:
        print("  row %d  x%-5d  %d.%d = %-4s (%d cells)" % d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
