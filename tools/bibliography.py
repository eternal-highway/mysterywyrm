#!/usr/bin/env python3
"""Parse the Letters for Titles bibliography into structured data.

The project's "Bibliography" post is ~375 MLA entries in hanging-indent
paragraphs, split into three sections (works cited, image sources, image
caption sources). This parses them and, where it can, links each source to
the chapters that appear to draw on it, by looking for the author's surname
in the corpus text.

Outputs:
  data/bibliography.json   structured entries + chapter linkage
  research/bibliography.md a readable summary

Usage:  python3 tools/bibliography.py
"""
import argparse, collections, html, json, os, re, sys, urllib.request

API = "https://lettersfortitles.com/wp-json/wp/v2"
UA = "letters-for-titles-research/1.0 (bibliography analysis; contact via repo)"

ENTRY_RE = re.compile(
    r'<p style="margin-left: \.5in; text-indent: -\.5in;">(.*?)</p>', re.S)
SECTION_RE = re.compile(r"<(?:strong|b)>(.*?)</(?:strong|b)>", re.S)

# Surnames too common or too generic to use as evidence of citation.
STOPWORD_SURNAMES = {"page", "wright", "green", "young", "white", "king",
                     "cross", "day", "small", "long", "short", "moore"}

# Manuscript shelfmarks and the libraries that hold them.
MS_RE = re.compile(r"\b(MS|Ms\.|Codex|fol\.|f\.\s*\d|Add MS|Cotton|Royal|Sloane|"
                   r"Harley|Laud|Bodley|Rawlinson|Junius|Vitellius|Tiberius)\b")
REPOSITORIES = [
    "British Library", "Bodleian", "British Museum", "Zentralbibliothek",
    "Aberdeen University Library", "Universitätsbibliothek", "Bibliothèque",
    "Parker Library", "Corpus Christi", "Morgan Library", "Metropolitan Museum",
    "Wellcome", "Getty", "National Library", "Royal Library", "Vatican",
    "Heidelberg", "Cambridge University Library", "Trinity College",
]


def text_of(fragment):
    s = re.sub(r"<[^>]+>", "", fragment)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def fetch_bibliography():
    req = urllib.request.Request(f"{API}/posts?slug=bibliography",
                                 headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.load(r)[0]["content"]["rendered"]


def split_sections(body):
    """[(section name, html chunk)] using the <strong>/<b> headers as breaks."""
    marks = [(m.start(), text_of(m.group(1))) for m in SECTION_RE.finditer(body)]
    marks = [(i, n) for i, n in marks if n]
    out, prev, name = [], 0, "Works Cited"
    for pos, n in marks:
        out.append((name, body[prev:pos]))
        prev, name = pos, n
    out.append((name, body[prev:]))
    return out


def parse_entry(fragment, section):
    raw = text_of(fragment)
    if not raw or len(raw) < 12:
        return None
    titles = [text_of(t) for t in re.findall(r"<(?:em|i)>(.*?)</(?:em|i)>", fragment, re.S)]
    titles = [t for t in titles if len(t) > 1]
    links = re.findall(r'href="(https?://[^"]+)"', fragment)
    # "—." continues the previous author (MLA repeat-author dash)
    repeat = raw.startswith("—")
    author = surname = None
    if not repeat:
        m = re.match(r"^([^.]+?),\s+([A-Z][^.,]*?)[.,]", raw)
        if m:                                   # "Surname, Firstname."
            author, surname = f"{m.group(1)}, {m.group(2)}", m.group(1).strip()
        else:                                   # mononym or corporate author
            head = raw.split(".")[0].strip()
            if (head and len(head) < 60 and head[0].isupper()
                    and not titles[:1] == [head] and not MS_RE.search(head)):
                author = surname = head

    if MS_RE.search(raw):
        kind = "manuscript"
    elif "“" in raw or '"' in raw:
        kind = "article"
    else:
        kind = "book"

    years = re.findall(r"\b(1[0-9]\d{2}|20[0-2]\d)\b", raw)
    return {
        "section": section,
        "raw": raw,
        "author": author,
        "surname": surname,
        "titles": titles,
        "kind": kind,
        "repository": next((r for r in REPOSITORIES if r in raw), None),
        "year": years[-1] if years else None,
        "links": links,
        "jstor": [l for l in links if "jstor.org" in l],
        "repeat_author": repeat,
    }


def link_to_chapters(entries, corpus):
    """Map surname -> chapters whose posts mention it (weak but useful evidence)."""
    chap_text = collections.defaultdict(list)
    for r in corpus:
        for c in r["categories"]:
            chap_text[c].append(r["text"])
    blob = {c: " ".join(t) for c, t in chap_text.items()}

    for e in entries:
        s = e["surname"]
        if not s or len(s) < 4 or s.lower() in STOPWORD_SURNAMES:
            e["cited_in"] = []
            continue
        pat = re.compile(r"\b" + re.escape(s) + r"\b")
        e["cited_in"] = sorted(c for c, b in blob.items()
                               if c != "Hwat" and pat.search(b))
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default="data/corpus.json")
    ap.add_argument("--out", default="data/bibliography.json")
    ap.add_argument("--notes", default="research/bibliography.md")
    args = ap.parse_args()

    body = fetch_bibliography()
    entries = []
    for name, chunk in split_sections(body):
        for frag in ENTRY_RE.findall(chunk):
            e = parse_entry(frag, name)
            if e:
                entries.append(e)

    corpus = json.load(open(args.corpus))
    entries = link_to_chapters(entries, corpus)

    by_section = collections.Counter(e["section"] for e in entries)
    jstor = sum(len(e["jstor"]) for e in entries)
    linked = [e for e in entries if e["cited_in"]]

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    json.dump({"source": "https://lettersfortitles.com/bibliography/",
               "count": len(entries),
               "sections": dict(by_section),
               "entries": entries},
              open(args.out, "w"), indent=1, ensure_ascii=False)

    L = ["# Bibliography", "",
         f"{len(entries)} entries parsed from the project's Bibliography post,",
         "in MLA hanging-indent form. Structured data in `data/bibliography.json`;",
         "regenerate with `python3 tools/bibliography.py`.", "",
         "## Sections", ""]
    for s, n in by_section.most_common():
        L.append(f"- **{s}** — {n} entries")
    L += ["", f"- {jstor} JSTOR links across "
              f"{sum(1 for e in entries if e['jstor'])} entries", ""]

    kinds = collections.Counter(e["kind"] for e in entries)
    L += ["## Kinds of source", "", "| Kind | Entries |", "|---|---|"]
    for k, n in kinds.most_common():
        L.append(f"| {k} | {n} |")

    repos = collections.Counter(e["repository"] for e in entries if e["repository"])
    L += ["", "## Manuscript repositories", "",
          f"{sum(repos.values())} entries name a holding institution.", "",
          "| Repository | Entries |", "|---|---|"]
    for r, n in repos.most_common():
        L.append(f"| {r} | {n} |")
    L.append("")

    decades = collections.Counter(
        (int(e["year"]) // 10) * 10 for e in entries if e["year"])
    L += ["## Publication dates", "",
          "| Decade | Entries |", "|---|---|"]
    for d in sorted(decades):
        L.append(f"| {d}s | {decades[d]} |")

    L += ["", "## Sources by chapter", "",
          "Chapters whose text names a cited author's surname. This is",
          "keyword evidence, not the project's own citation marks, so it",
          "under-counts sources used for images and over-counts common names.",
          "", "| Chapter | Sources named |", "|---|---|"]
    per_chap = collections.Counter(c for e in linked for c in e["cited_in"])
    for c, n in per_chap.most_common():
        L.append(f"| {c} | {n} |")

    L += ["", "## Most-cited authors", "",
          "| Author | Entries |", "|---|---|"]
    auth = collections.Counter(e["surname"] for e in entries if e["surname"])
    for a, n in auth.most_common(15):
        L.append(f"| {a} | {n} |")
    L.append("")

    os.makedirs(os.path.dirname(args.notes) or ".", exist_ok=True)
    open(args.notes, "w").write("\n".join(L))
    print(f"parsed {len(entries)} entries "
          f"({len(linked)} linked to chapters) -> {args.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
