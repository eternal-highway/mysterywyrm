"""Validate the v0.26.2 delta, create its manifest and verify a clean ZIP extraction."""
from pathlib import Path
import csv
import hashlib
import io
import json
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / 'corpus-seed'
DIST = ROOT / 'dist'
PARENT = ROOT / 'letters_for_titles_corpus_seed_v0.26.1.zip'
PREFIX = 'letters_for_titles_corpus_seed/'
sha = lambda data: hashlib.sha256(data).hexdigest()
assert sha(PARENT.read_bytes()) == 'ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327'
with zipfile.ZipFile(PARENT) as z:
    assert z.testzip() is None
    parent = {n[len(PREFIX):]: z.read(n) for n in z.namelist() if not n.endswith('/')}

# Restore checkout-only newline conversions to the exact parent bytes.
# Any semantic difference remains for the allowlisted delta review below.
for rel, original in parent.items():
    p = SEED / rel
    assert p.exists(), f'Unexpected deletion: {rel}'
    current = p.read_bytes()
    if current != original and current.replace(b'\r\n', b'\n') == original.replace(b'\r\n', b'\n'):
        p.write_bytes(original)

allowed = {
    'README.md', 'CHANGELOG.md', 'CODEX_HANDOFF.md', 'CLAUDE_HANDOFF.md',
    '01_inventory/open_questions.csv', '01_inventory/rune_code_carrier_fingerprints.csv',
    '01_inventory/translation_register.csv', '01_inventory/verified_page_register.csv',
    '02_structure/core_stream_alignment.csv', '05_method/lineage_log.md',
    '05_method/reentry_capsule.md', '05_method/rune_code_plate_reconciliation_v0.26.0.md',
    '05_method/verify_rune_code_state.py', '05_method/version_control_protocol.md',
    '06_sources/source_notes.md', '07_capture/stanza-11-ice/links.csv',
    '07_capture/translating-eh/links.csv', '07_capture/translating-is/record.md',
    '01_inventory/rune_code_source_media.json', '01_inventory/harvest_publication_dates.csv',
    '05_method/metadata_provenance_v0.26.2.md', '05_method/release_validation_v0.26.2.md',
    'MANIFEST.sha256',
}
def payload():
    return {p.relative_to(SEED).as_posix(): p.read_bytes() for p in SEED.rglob('*') if p.is_file()}

files = payload()
delta = sorted(r for r in files if files[r] != parent.get(r))
assert set(delta) <= allowed, f'Unscoped changes: {set(delta) - allowed}'
for rel in delta:
    if Path(rel).suffix in {'.md', '.csv', '.py', '.json'}:
        (SEED / rel).write_bytes(files[rel].replace(b'\r\n', b'\n'))
files = payload()
assert files['01_inventory/code_register.csv'] == parent['01_inventory/code_register.csv']
assert all(files[r] == b for r, b in parent.items() if Path(r).suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp'})
source_manifest = subprocess.check_output(['git', 'show', '23012aceed6b92c0c36f0b315e8ffafb384ec994:data/media-code.json'], cwd=ROOT)
assert files['01_inventory/rune_code_source_media.json'] == source_manifest
full = json.loads((ROOT / 'data/media-full.json').read_text(encoding='utf-8'))
full_by_url = {r['url']: r for r in full['images']}
for row in json.loads(source_manifest)['images']:
    assert all(row[k] == full_by_url[row['url']][k] for k in ('sha256', 'bytes', 'width', 'height'))
with (SEED / '01_inventory/harvest_publication_dates.csv').open(encoding='utf-8', newline='') as f:
    dates = list(csv.DictReader(f))
corpus = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
assert len(dates) == len(corpus) == 262
for exported, original in zip(dates, corpus):
    assert (exported['post_id'], exported['title'], exported['url'], exported['publication_date'], exported['modified_date']) == (str(original['id']), original['title'], original['link'], original['date'], original['modified'])
csv_count = 0
for rel, b in files.items():
    if rel.endswith('.csv'):
        rows = [r for r in csv.reader(io.StringIO(b.decode('utf-8-sig'), newline='')) if r]
        assert rows and all(len(r) == len(rows[0]) for r in rows), f'Nonrectangular CSV: {rel}'
        csv_count += 1

def run_verifiers(tree):
    logs = []
    for script in ('verify_rune_code_state.py', 'verify_cipher_letter_run.py'):
        result = subprocess.run([sys.executable, '-X', 'utf8', str(tree / '05_method' / script)], check=True, capture_output=True, text=True, encoding='utf-8')
        logs.append(result.stdout)
    return '\n'.join(logs)

logs = run_verifiers(SEED)
report = f'''# Release validation — v0.26.2

Date: 2026-09-12
Scope: metadata/provenance patch candidate; no transcription adjudication.
Parent: `letters_for_titles_corpus_seed_v0.26.1.zip`
Parent SHA-256: `{sha(PARENT.read_bytes())}`

## Checks

- Parent ZIP CRC and exact SHA-256 verified; parent payload is the comparison baseline.
- Candidate modifications are restricted to the declared metadata, provenance, guidance and verifier paths.
- `code_register.csv` is byte-identical to the parent. Every retained image/GIF payload is byte-identical to the parent.
- {csv_count} CSV files parse as rectangular tables.
- All 31 imported media hash records agree with the co-located full-resolution manifest; no new download verification is claimed.
- Harvest publication-date export preserves 262 records at day precision.
- Source-URL correction agrees with archived canonical tag and harvest metadata; live retrieval did not succeed in this pass.
- Repository filename derivation passes: 211/211 directly recovered characters; seven characters supplied from context.
- Repository structure verifier passes in Python UTF-8 mode: all 29 stanzas, castings and translations; reflected pairs and central chapter confirmed.

## Seed verifier output

```text
{logs.strip()}
```

## Packaging

The regenerated manifest excludes only itself. `tools/package_v0262.py` verifies ZIP CRC, a single safe root, every manifest hash, exact path-set equality and both seed verifiers in a clean extraction. The candidate ZIP checksum and resulting counts are recorded outside this payload in `RELEASE-v0.26.2.md`, avoiding a self-referential hash.

## Boundaries

Historical visual fingerprints keep their original identity/date. Original-media hash availability does not authenticate any future downloaded bytes. Nine carrier transcription disputes and the Octave classification question remain open; Gate 0 has not been performed. The published release remains v0.26.1 until this candidate is integrated and published.
'''
(SEED / '05_method/release_validation_v0.26.2.md').write_text(report, encoding='utf-8', newline='\n')
files = payload()
manifest = ''.join(f'{sha(b)}  ./{r}\n' for r, b in sorted(files.items()) if r != 'MANIFEST.sha256')
(SEED / 'MANIFEST.sha256').write_text(manifest, encoding='utf-8', newline='\n')
files = payload()
DIST.mkdir(exist_ok=True)
target = DIST / 'letters_for_titles_corpus_seed_v0.26.2.zip'
assert not target.exists(), 'Candidate ZIP already exists; do not overwrite a versioned package'
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for rel, b in sorted(files.items()):
        info = zipfile.ZipInfo(PREFIX + rel, date_time=(2026, 9, 12, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, b)
with tempfile.TemporaryDirectory(prefix='v0262-verify-', dir=DIST) as tmp:
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {PREFIX + r for r in files}
        assert all('..' not in Path(n).parts and n.startswith(PREFIX) for n in z.namelist())
        for rel, b in files.items():
            assert z.read(PREFIX + rel) == b
        z.extractall(tmp)
    tree = Path(tmp) / PREFIX.rstrip('/')
    actual = {p.relative_to(tree).as_posix() for p in tree.rglob('*') if p.is_file()}
    expected = set()
    for line in (tree / 'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
        digest, rel = line.split('  ', 1)
        rel = rel.removeprefix('./')
        assert rel not in expected
        expected.add(rel)
        assert sha((tree / rel).read_bytes()) == digest
    assert actual == expected | {'MANIFEST.sha256'}
    run_verifiers(tree)

digest = sha(target.read_bytes())
(DIST / (target.name + '.sha256')).write_text(f'{digest}  {target.name}\n', encoding='utf-8')
delta = sorted(r for r in files if files[r] != parent.get(r))
release = f'''# v0.26.2 release candidate

Prepared and validated: 2026-09-12
Branch: `corpus-v0.26.2-integration`
Status: local candidate; not merged, tagged or published. Published v0.26.1 remains unchanged.

Candidate: `dist/{target.name}`
SHA-256: `{digest}`
Parent SHA-256: `{sha(PARENT.read_bytes())}`

## Result

The candidate corrects Loop/Œ source dimensions and media URLs, registers Octave's image, imports all 31 source-byte hash attestations, adds 262 day-level publication records, updates OQ001/OQ003/OQ007 and corrects Translating Is to `/translating-ice/`. Its readings and retained media are unchanged from v0.26.1.

The pre-existing one-frame local GIF is preserved under ignored `local-recovery/`; canonical AS001 was restored from the parent ZIP and again has six frames. Its source is unknown.

## Verification

- {len(files)} files; {len(files)-1} payload hashes; complete path-set agreement.
- ZIP CRC, single root, all extracted bytes, manifest hashes, and clean-extraction seed verifiers: pass.
- {csv_count} rectangular CSVs; code register and every retained media file identical to parent.
- Seed filename check: 74/74; full harvest: 211/211 direct characters, seven context-supplied characters.
- Site structure derivation: pass under Python UTF-8 mode. Initial Windows default-codepage execution failed; no source change was needed.
- 31 imported hash identities agree with the full harvest manifest; full-resolution media not present locally or re-fetched.
- Canonical URL supported by archived canonical tag and harvest. Live retrieval failed; no new live capture claimed.

## Candidate delta ({len(delta)} files)

''' + '\n'.join(f'- `corpus-seed/{r}`' for r in delta) + '''

## Remaining release steps

Review and merge the dedicated integration branch, then attach the ZIP and checksum to a release tagged at the import commit. v0.27 remains deferred until v0.26.2 lands. Gate 0 and the nine disputed readings have not been adjudicated.
'''
(ROOT / 'RELEASE-v0.26.2.md').write_text(release, encoding='utf-8', newline='\n')
print(f'PASS: {len(files)} files; {len(files)-1} hashes; {len(delta)} changed/added files; {csv_count} CSVs')
print(f'ZIP SHA-256: {digest}')
