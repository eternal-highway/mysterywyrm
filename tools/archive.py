#!/usr/bin/env python3
"""Archive Letters for Titles: rendered pages and every image.

The Rune Poem survives only because one copy was printed before the
manuscript burned. This does the same for the site.

The full-resolution images total ~742 MB, too much to keep in git, so the
split is:

  archive/thumbs/   300px reference copies of all 479 images (~17 MB, in repo)
  archive/pages/    rendered HTML of every post and page (in repo)
  data/media.json   manifest of the FULL-RESOLUTION originals - URL, byte
                    size, dimensions, SHA-256, and which posts use them

`--variant full --images-dir archive/full` materializes the 742 MB originals
anywhere you like; `--verify` re-hashes them against the manifest.

Usage:
  python3 tools/archive.py                      # thumbs + pages + manifest
  python3 tools/archive.py --variant full --images-dir archive/full
  python3 tools/archive.py --verify --variant full --images-dir archive/full
  python3 tools/archive.py --tag "Rune Code" --variant full \
          --images-dir archive/code --manifest data/media-code.json --skip-pages
"""
import argparse, concurrent.futures as cf, hashlib, json, os, sys, time
import urllib.parse, urllib.request

API = "https://lettersfortitles.com/wp-json/wp/v2"
UA = "letters-for-titles-research/1.0 (preservation archive; contact via repo)"


def _safe(url):
    """Percent-encode non-ASCII path characters (several titles use ≠, þ, runes)."""
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (p.scheme, p.netloc, urllib.parse.quote(p.path, safe="/%"), p.query, p.fragment))


def fetch(url, timeout=120):
    req = urllib.request.Request(_safe(url), headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_json(url):
    return json.loads(fetch(url).decode("utf-8"))


def media_index():
    """Full-resolution source_url -> {size name: variant url}, from the media API."""
    out, page = {}, 1
    while True:
        batch = fetch_json(f"{API}/media?per_page=100&page={page}")
        if not batch:
            break
        for m in batch:
            su = m.get("source_url")
            if not su:
                continue
            sizes = m.get("media_details", {}).get("sizes", {})
            out[su] = {k: v["source_url"] for k, v in sizes.items() if v.get("source_url")}
        if len(batch) < 100:
            break
        page += 1
    return out


def local_name(url):
    """Stable on-disk filename: the upload path, flattened."""
    path = urllib.parse.urlsplit(url).path
    return path.replace("/wp-content/uploads/", "").replace("/", "_")


def pixel_size(b):
    """Dimensions from raw bytes for JPEG/PNG/GIF, without an image library."""
    if b[:8] == b"\x89PNG\r\n\x1a\n":
        return int.from_bytes(b[16:20], "big"), int.from_bytes(b[20:24], "big")
    if b[:3] == b"GIF":
        return int.from_bytes(b[6:8], "little"), int.from_bytes(b[8:10], "little")
    if b[:2] == b"\xff\xd8":
        i = 2
        while i < len(b) - 9:
            if b[i] != 0xFF:
                i += 1
                continue
            m = b[i + 1]
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                return (int.from_bytes(b[i + 7:i + 9], "big"),
                        int.from_bytes(b[i + 5:i + 7], "big"))
            i += 2 + int.from_bytes(b[i + 2:i + 4], "big")
    return None, None


def grab(url, dest):
    """Download to dest unless already present; return the bytes."""
    if os.path.exists(dest):
        return open(dest, "rb").read()
    data = fetch(url)
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    with open(dest, "wb") as f:
        f.write(data)
    time.sleep(0.15)  # be gentle with the host
    return data


def run_pool(items, fn, workers=6, label=""):
    ok, failed = [], []
    with cf.ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(fn, it): it for it in items}
        for i, fu in enumerate(cf.as_completed(futs), 1):
            try:
                ok.append(fu.result())
            except Exception as e:
                failed.append({"item": str(futs[fu]), "error": str(e)})
            if i % 50 == 0:
                print(f"  {label} {i}/{len(futs)}", file=sys.stderr)
    return ok, failed


def archive_images(corpus, out_dir, variant, index):
    """Download one variant of every image the corpus references."""
    refs = {}
    for r in corpus:
        for u in r["image_urls"]:
            refs.setdefault(u, []).append(r["slug"])

    def one(full_url):
        src = full_url if variant == "full" else index.get(full_url, {}).get(variant, full_url)
        name = local_name(src)
        data = grab(src, os.path.join(out_dir, name))
        w, h = pixel_size(data)
        return {
            "url": full_url, "fetched": src, "file": name,
            "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "width": w, "height": h, "posts": sorted(refs[full_url]),
        }

    entries, failed = run_pool(sorted(refs), one, label="img")
    entries.sort(key=lambda e: e["url"])
    return entries, failed


def archive_pages(corpus, out_dir):
    """Save each post's rendered HTML under its slug."""
    def one(rec):
        data = grab(rec["link"], os.path.join(out_dir, rec["slug"] + ".html"))
        return {"slug": rec["slug"], "url": rec["link"], "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest()}
    return run_pool(corpus, one, label="page")


def verify(manifest_path, images_dir):
    man = json.load(open(manifest_path))
    bad = []
    for e in man["images"]:
        p = os.path.join(images_dir, e["file"])
        if not os.path.exists(p):
            bad.append((e["file"], "missing"))
        elif hashlib.sha256(open(p, "rb").read()).hexdigest() != e["sha256"]:
            bad.append((e["file"], "checksum mismatch"))
    print(f"verified {len(man['images'])} images against {manifest_path}: "
          f"{len(bad)} problem(s)")
    for f, why in bad:
        print(f"  {why}: {f}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default="data/corpus.json")
    ap.add_argument("--variant", default="medium", choices=["medium", "large", "full"],
                    help="image resolution to download (default: medium, the in-repo set)")
    ap.add_argument("--images-dir", default="archive/thumbs")
    ap.add_argument("--pages-dir", default="archive/pages")
    ap.add_argument("--manifest", default="data/media.json")
    ap.add_argument("--skip-pages", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--tag", action="append", default=[], metavar="TAG",
                    help="restrict to posts carrying this tag (repeatable); "
                         "useful for pulling one series at full resolution")
    args = ap.parse_args()

    if args.verify:
        return verify(args.manifest, args.images_dir)

    corpus = json.load(open(args.corpus))
    if args.tag:
        want = set(args.tag)
        corpus = [r for r in corpus if want & set(r["tags"])]
        if not corpus:
            print(f"no posts tagged {', '.join(sorted(want))}", file=sys.stderr)
            return 1
    index = {} if args.variant == "full" else media_index()
    print(f"archiving {args.variant} images for {len(corpus)} posts", file=sys.stderr)
    imgs, img_fail = archive_images(corpus, args.images_dir, args.variant, index)

    pages, page_fail = ([], [])
    if not args.skip_pages:
        pages, page_fail = archive_pages(corpus, args.pages_dir)

    total = sum(e["bytes"] for e in imgs)
    manifest = {
        "source": "https://lettersfortitles.com",
        "retrieved": time.strftime("%Y-%m-%d"),
        "variant": args.variant,
        "count": len(imgs),
        "total_bytes": total,
        "failures": img_fail + page_fail,
        "pages": sorted(pages, key=lambda p: p["slug"]),
        "images": imgs,
    }
    os.makedirs(os.path.dirname(args.manifest) or ".", exist_ok=True)
    with open(args.manifest, "w") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    print(f"{len(imgs)} images ({total/1e6:.1f} MB), {len(pages)} pages, "
          f"{len(img_fail)+len(page_fail)} failure(s) -> {args.manifest}", file=sys.stderr)
    return 1 if (img_fail or page_fail) else 0


if __name__ == "__main__":
    sys.exit(main())
