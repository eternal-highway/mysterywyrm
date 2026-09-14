#!/usr/bin/env python3
"""Validate and render the bounded v0.27 comparison, without editing the seed."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re

from archive import pixel_size

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "research/v0.27"
FROZEN_OBSERVATIONS = "41cc3a03b6cb2c899e431fedd69897f7a8fbf084c1204dc204091eca19cedce9"
FROZEN_KEY = "721dccd4d07b4691f8820aeca8c2d4b9817a48bc2bb806f549007f5ac5a9ebde"
PAGES = {"P241", "P161", "P055", "P209", "P229", "P046", "P109", "P189", "P125", "P261"}
PROVISIONAL = {"2.6", "2.7", "2.8", "3.7"}


def frozen(path, digest):
    blob = path.read_bytes().replace(b"\r\n", b"\n")
    if hashlib.sha256(blob).hexdigest() != digest:
        raise ValueError(f"Frozen input changed: {path.name}")
    return blob.decode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check reproducibility without writing")
    args = parser.parse_args()
    observations = json.loads(frozen(WORK / "independent-observations.json", FROZEN_OBSERVATIONS))
    key_rows = list(csv.DictReader(frozen(WORK / "loop-candidate-key.csv", FROZEN_KEY).splitlines()))
    key = {r["coordinate"]: r["transliteration"].upper() for r in key_rows}
    decisions = json.loads((WORK / "comparison-decisions.json").read_text(encoding="utf-8"))
    sources = json.loads((WORK / "source-authentication.json").read_text(encoding="utf-8"))
    if len(observations["carriers"]) != 10 or {r["page"] for r in observations["carriers"]} != PAGES:
        raise ValueError("Expected all nine disputes and Octave exactly once")
    if set(decisions) != PAGES:
        raise ValueError("Decision coverage differs from required carriers")
    manifest_blob = (ROOT / "data/media-code.json").read_bytes()
    if hashlib.sha256(manifest_blob.replace(b"\r\n", b"\n")).hexdigest() != sources["manifest_lf_sha256"]:
        raise ValueError("Source manifest changed")
    corroboration = json.loads((WORK / "key-corroboration-sources.json").read_text(encoding="utf-8"))
    expected_urls = {
        "https://lettersfortitles.com/octave/", "https://lettersfortitles.com/the-game/",
        "https://lettersfortitles.com/stanza-15-helix/", "https://lettersfortitles.com/sun/",
        "https://lettersfortitles.com/stanza-23-home/",
    }
    if len(corroboration) != 5 or {r["canonical_url"] for r in corroboration} != expected_urls:
        raise ValueError("Missing conditional-key source support")
    for source in corroboration:
        blob = (ROOT / source["page"]).read_bytes()
        if hashlib.sha256(blob.replace(b"\r\n", b"\n")).hexdigest() != source["lf_sha256"]:
            raise ValueError("Corroborating source changed")
    lines = [
        "# v0.27 bounded comparative pass", "",
        "Completed and verified 2026-09-13 under the user-authorized conditional-key exception.",
        "**Research comparison only: no canonical release or silent lineage overwrite.**", "",
        "All nine disputed carriers and the separate Octave classification were examined.",
        "The original independent observations were frozen before detailed lineage-coordinate",
        "comparison. Candidate phrases and reading-aid descriptions were already known;",
        "this is not a blind semantic experiment.", "",
        "## Results", "",
        "| Page | Carrier | Disposition | Scope |", "|---|---|---|---|",
    ]
    for row in observations["carriers"]:
        d = decisions[row["page"]]
        if d["disposition"] not in {"seed", "harvest", "neither", "unresolved"}:
            raise ValueError("Invalid disposition")
        if d["disposition"] == "unresolved" and not d["unresolved_reason"]:
            raise ValueError("Unresolved disposition needs a reason")
        lines.append(f"| {row['page']} | {row['title']} | {d['disposition']} | {d['scope']} |")
    lines += ["", "## Interpretation rules", "",
        "Rows below preserve spatial order. Plaintext is mechanically concatenated within",
        "each row; word spacing and alternative traversals appear only in interpretation.",
        "`†` marks assignments supported through the separately documented authored-source",
        "derivation in [key-corroboration.md](key-corroboration.md), not directly exposed",
        "Loop inscriptions. These occur at 2.6, 2.7, 2.8 and 3.7. Alternatives remain in",
        "braces; an invalid coordinate stays visible rather than being repaired.",
        "Ger renders as Y under the frozen candidate convention; TH, AE, OE and NG are",
        "multi-character transliterations of single runes. `[unknown]` is not punctuation.", "",
        "Gate 0 Outcome B is not asserted. Separate primary-source corroboration supports",
        "use of the provisional assignments under the approved exception. It does not",
        "resolve ambiguous plate features or traversal. Dispositions are recommendations",
        "for the future release; the standing ledger remains unreleased.", "",
    ]
    for row in observations["carriers"]:
        d = decisions[row["page"]]
        matches = [s for s in sources["carriers"] if row["post"] in s["posts"]]
        if len(matches) != 1:
            raise ValueError(f"Ambiguous source association: {row['page']}")
        source = matches[0]
        blob = (ROOT / "archive/code" / source["file"]).read_bytes()
        if (hashlib.sha256(blob).hexdigest() != source["sha256"] or len(blob) != source["bytes"]
                or pixel_size(blob) != (source["width"], source["height"])):
            raise ValueError(f"Evidence bytes changed: {row['page']}")
        lines += [f"## {row['page']} — {row['title']}", "",
            f"Disposition: **{d['disposition']}**. Scope: {d['scope']}.", "",
            f"Evidence: `archive/code/{source['file']}`; {source['width']} × {source['height']};",
            f"{source['bytes']:,} bytes; [canonical media]({source['url']}).", "",
            f"SHA-256: `{source['sha256']}`.", "",
            f"Confidence: {row['confidence']}", "", row["observation"], ""]
        if not row["rows"]:
            if row["page"] != "P261":
                raise ValueError("Only classification-only Octave may omit coordinates")
            lines += ["Independent coordinates: not extracted (classification-only scope).",
                "Mechanical plaintext: not extracted (classification does not authorize transcription).", ""]
        else:
            lines += ["| Spatial row | Independent coordinates / literal marks | Mechanical plaintext |",
                      "|---|---|---|"]
            for i, cells in enumerate(row["rows"], 1):
                def decode(token):
                    if token == "?" and row["page"] == "P109" and i == 7:
                        return "[unknown]"
                    alternatives = token.split("|")
                    values = []
                    for t in alternatives:
                        if t in key:
                            values.append(key[t] + ("†" if t in PROVISIONAL else ""))
                        elif re.fullmatch(r"\d+\.\d+", t):
                            values.append(f"[invalid:{t}]")
                        elif t in {"K", "Y", "V", "?", "—"}:
                            values.append(t)
                        else:
                            raise ValueError(f"Unknown token: {t}")
                    return "{" + "/".join(values) + "}" if len(values) > 1 else values[0]
                coord = " ".join(cells).replace("|", "/")
                text = "".join(decode(t) for t in cells)
                lines.append(f"| {i} | `{coord}` | `{text}` |")
            lines.append("")
        lines += ["Comparison: " + d["reason"], "",
                  "Semantic interpretation: " + d["semantic_interpretation"], ""]
        if d["unresolved_reason"]:
            lines += ["Remaining uncertainty: " + d["unresolved_reason"], ""]
    lines += ["## Verification and release boundary", "",
        "The renderer checks the frozen observation/key hashes, all ten carrier byte",
        "identities, the source-manifest content hash, the five corroborating HTML",
        "identities, complete carrier/decision coverage and unresolved reasons. It can",
        "validate record consistency and evidence identity; it cannot certify visual",
        "correctness. Text-source checks normalize CRLF to LF for portable Git checkouts;",
        "the retained source records also preserve the exact bytes/hashes originally read.",
        "Image-byte hashes are never normalized. The two source tables remain intact.", "",
        "The earlier complete-source authentication covers 17/17 named carriers.",
        "This pass does not reclassify the seven agreeing carriers, publish a corpus ZIP,",
        "or transcribe Octave. Packaging a release must retain the unresolved findings",
        "and this conditional-key provenance, not flatten them into nine complete readings.", ""]
    rendered = "\n".join(lines)
    target = WORK / "comparative-pass.md"
    if args.check:
        if target.read_text(encoding="utf-8") != rendered:
            raise ValueError("Rendered report differs from inputs")
    else:
        target.write_text(rendered, encoding="utf-8")
    print("PASS: 10/10 carrier records; source bytes and frozen inputs verified; report consistent")


if __name__ == "__main__":
    main()
