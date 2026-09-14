#!/usr/bin/env python3
"""Verify the approved v0.27 ZIP against the canonical working tree and Git ref."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

from preflight_v027_release import CANDIDATE_SHA, ROOT, manifest, package, require, tree


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--zip", type=Path, default=ROOT / "dist/letters_for_titles_corpus_seed_v0.27.0.zip")
    parser.add_argument("--ref", help="Also verify every committed seed blob at this Git ref")
    args = parser.parse_args()
    files = package(args.zip, CANDIDATE_SHA)
    require(tree(ROOT / "corpus-seed") == files, "canonical working tree differs from approved ZIP")
    if args.ref:
        fmt = subprocess.check_output(["git", "rev-parse", "--show-object-format"], cwd=ROOT, text=True).strip()
        raw = subprocess.check_output(["git", "ls-tree", "-r", "-z", args.ref, "--", "corpus-seed/"], cwd=ROOT)
        blobs = {}
        for item in raw.split(b"\0"):
            if not item:
                continue
            metadata, path = item.split(b"\t", 1)
            mode, kind, oid = metadata.split()
            require(mode == b"100644" and kind == b"blob", "unexpected Git entry type")
            name = path.decode("utf-8").removeprefix("corpus-seed/")
            blobs[name] = oid.decode("ascii")
        expected = {p: hashlib.new(fmt, b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()
                    for p, b in files.items()}
        require(blobs == expected, "committed seed path set or blob bytes differ from approved ZIP")
        print(f"Git {args.ref}: all {len(blobs)} seed blobs equal approved ZIP bytes")
    for name in ("verify_rune_code_state.py", "verify_cipher_letter_run.py"):
        subprocess.run([sys.executable, "-X", "utf8", "-B", str(ROOT / "corpus-seed/05_method" / name)],
                       cwd=ROOT / "corpus-seed", check=True)
    require(tree(ROOT / "corpus-seed") == files, "state verification changed seed bytes")
    print(f"PASS: {len(files)} files; {manifest(files)} hashes; ZIP CRC and sidecar; exact seed equality")
    print("ZIP SHA-256: " + CANDIDATE_SHA)


if __name__ == "__main__":
    main()
