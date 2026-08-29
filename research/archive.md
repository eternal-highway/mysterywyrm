# Preservation archive

*Letters for Titles* turns on a manuscript that no longer exists. The Old
English Rune Poem survived the 1731 Ashburnham House fire only because
George Hickes had printed it in 1705 — as the *Twist* chapter puts it, "the
only copy we have … printed in 1705 from the only surviving manuscript copy,
which burned to ashes in a fire 26 years later." The project's own
Bibliography post carries the caption: *"Copies to be sent if you died to
all the great libraries of the world, including Alexandria."*

The site is currently in the same position the manuscript was: one copy, on
one WordPress host. This archive is the printed edition.

## What is captured

| | |
|---|---|
| `archive/pages/` | rendered HTML of all 262 posts, as served |
| `archive/thumbs/` | 300px reference copy of all 479 images (~17 MB) |
| `data/media.json` | manifest of the **300px** copies above |
| `data/media-full.json` | manifest of the **full-resolution** originals |
| `data/corpus.json` | post text, dates, chapters, tags, image and outbound links |
| `data/bibliography.json` | the 375-entry bibliography, parsed |

## Why the full-resolution images are not in the repo

The 479 originals total **742 MB** — median 1.0 MB, largest 15.9 MB. Putting
that in git would make the repository impractical to clone and would store
image data in a format built for line-oriented diffs.

Instead `data/media-full.json` records, for every original: its URL, exact
byte size, pixel dimensions, **SHA-256 checksum**, and which posts use it.
That is enough to re-fetch the originals and prove they are bit-identical to
what was retrieved on the date in the manifest.

This manifest was missing until now, and the gap ran the length of the
archive's own argument. `data/media.json` was described here and in the README
as the manifest of the originals. It is not: it is written by the default
thumbnail run, carries `variant: "medium"`, totals 15.9 MB, and **not one of
its 479 entries has a side longer than 400px**. Every checksum in it is the
checksum of a 300px copy. Nothing committed could certify the 742 MB, which is
the one thing this archive exists to make certifiable, and the tooling to
produce that certificate was being run into a file the repository ignored.
`data/media-full.json` is now generated, verified 479/479, and committed.

```sh
# materialize the 742 MB of originals wherever you want them
python3 tools/archive.py --variant full --images-dir archive/full --skip-pages \
        --manifest data/media-full.json

# check an existing copy against the manifest
python3 tools/archive.py --verify --variant full --images-dir archive/full \
        --manifest data/media-full.json
```

A full-resolution copy belongs somewhere built for binaries — an external
disk, object storage, Git LFS, or a deposit with a web archive — not in the
git history. The manifest is what makes any of those copies verifiable.

## Retrieval notes

- Source: <https://lettersfortitles.com>, via its public WordPress REST API.
- All 479 images retrieved with 0 failures.
- Several filenames contain non-ASCII characters (`≠`, `þ`, runes); the
  fetcher percent-encodes paths, and on-disk names flatten the upload path.
- Downloads are rate-limited and run six at a time, to stay light on the host.

## Rights

This is a research and preservation copy of work by Vern Tonkin, published
at lettersfortitles.com. Copyright remains with the author. Nothing here is
a republication: every post in the assembled book links back to its source,
and the archive exists so the work is not lost if the host is.
