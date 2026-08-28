#!/usr/bin/env python3
"""Harvest the Letters for Titles corpus from its WordPress REST API.

Writes data/corpus.json: one normalized record per post, with rendered text
stripped to plain prose, plus category/tag names resolved and image/link counts.

Usage:  python3 tools/harvest.py [--out data/corpus.json]
"""
import argparse, html, json, os, re, sys, time, urllib.request

BASE = "https://lettersfortitles.com/wp-json/wp/v2"
UA = "letters-for-titles-research/1.0 (corpus analysis; contact via repo)"


def get(path, **params):
    """GET one API path, following WP pagination via per_page/page."""
    qs = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{BASE}/{path}?{qs}" if qs else f"{BASE}/{path}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)


def get_all(path, per_page=100):
    """Collect every item from a paginated collection."""
    out, page = [], 1
    while True:
        batch = get(path, per_page=per_page, page=page)
        if not batch:
            break
        out += batch
        if len(batch) < per_page:
            break
        page += 1
        time.sleep(0.5)  # be gentle with the host
    return out


def strip_html(fragment):
    """Rendered HTML -> plain text, dropping scripts and collapsing whitespace."""
    s = re.sub(r"<script.*?</script>", "", fragment, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/corpus.json")
    args = ap.parse_args()

    posts = get_all("posts")
    cats = {c["id"]: c["name"] for c in get_all("categories")}
    tags = {t["id"]: t["name"] for t in get_all("tags")}

    recs = []
    for p in posts:
        body = p["content"]["rendered"]
        recs.append({
            "id": p["id"],
            "slug": p["slug"],
            "title": strip_html(p["title"]["rendered"]),
            "date": p["date"][:10],
            "modified": p["modified"][:10],
            "link": p["link"],
            "categories": [cats[i] for i in p.get("categories", []) if i in cats],
            "tags": [tags[i] for i in p.get("tags", []) if i in tags],
            "words": len(strip_html(body).split()),
            "images": len(re.findall(r"<img", body)),
            "links": re.findall(r'href="(https?://[^"]+)"', body),
            "text": strip_html(body),
        })
    recs.sort(key=lambda r: (r["date"], r["id"]))

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(recs, f, indent=1, ensure_ascii=False)
    print(f"wrote {len(recs)} posts to {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
