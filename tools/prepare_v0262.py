"""Build the bounded v0.26.2 metadata patch from the verified v0.26.1 parent.

Run once on an integration branch. Packaging/verification is a separate step.
"""
from pathlib import Path
import csv
import hashlib
import io
import json
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SEED = ROOT / 'corpus-seed'
PARENT = ROOT / 'letters_for_titles_corpus_seed_v0.26.1.zip'
PARENT_HASH = 'ae30b2eead39ee43667d8098281d03a17577d19a044bab277d02ea965a837327'
DATE = '2026-09-12'

def sha(b):
    return hashlib.sha256(b).hexdigest()

def source_bytes(rel):
    return subprocess.check_output(['git', 'show', '23012aceed6b92c0c36f0b315e8ffafb384ec994:' + rel], cwd=ROOT)

def write(rel, text):
    (SEED / rel).write_text(text, encoding='utf-8', newline='\n')

def replace(rel, old, new):
    p = SEED / rel
    text = p.read_text(encoding='utf-8')
    assert old in text, (rel, old)
    write(rel, text.replace(old, new))

def read_csv(rel):
    with (SEED / rel).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def write_csv(rel, rows):
    with (SEED / rel).open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

assert sha(PARENT.read_bytes()) == PARENT_HASH
assert not (ROOT / 'dist/letters_for_titles_corpus_seed_v0.26.2.zip').exists()
assert 'Version: 0.26.1' in (SEED / 'README.md').read_text(encoding='utf-8')
with zipfile.ZipFile(PARENT) as z:
    assert z.testzip() is None
    prefix = 'letters_for_titles_corpus_seed/'
    parent = {n[len(prefix):]: z.read(n) for n in z.namelist() if not n.endswith('/')}
    manifest = parent['MANIFEST.sha256'].decode().splitlines()
    for line in manifest:
        digest, rel = line.split('  ', 1)
        assert sha(parent[rel.removeprefix('./')]) == digest

# Preserve the pre-existing local change before restoring the release artifact.
gif = SEED / '08_assets/mysterywyrm.gif'
recovery = ROOT / 'local-recovery'
recovery.mkdir(exist_ok=True)
(recovery / '.gitignore').write_text('*\n', encoding='utf-8')
local = gif.read_bytes()
backup = recovery / f'mysterywyrm-{sha(local)}.gif'
if backup.exists():
    assert backup.read_bytes() == local
else:
    backup.write_bytes(local)
(recovery / 'README.md').write_text(
    f'# Local GIF preservation\n\nSaved {DATE} before restoring AS001 from v0.26.1.\n'
    f'Local SHA-256: {sha(local)}\nLocal bytes: {len(local)}\n'
    'The local GIF has one 360x360 frame; the release GIF has six 360x360 frames.\n'
    'The origin of the local replacement is unknown. This backup is not release evidence.\n',
    encoding='utf-8')
gif.write_bytes(parent['08_assets/mysterywyrm.gif'])

media = json.loads((ROOT / 'data/media-code.json').read_text(encoding='utf-8'))
full = json.loads((ROOT / 'data/media-full.json').read_text(encoding='utf-8'))
full_by_url = {r['url']: r for r in full['images']}
assert len(media['images']) == 31
for r in media['images']:
    for key in ('sha256', 'bytes', 'width', 'height'):
        assert r[key] == full_by_url[r['url']][key]

# Bundle the original manifest verbatim; these are imported hash attestations,
# not a claim to have downloaded/rehashed the full-resolution media today.
(SEED / '01_inventory/rune_code_source_media.json').write_bytes(source_bytes('data/media-code.json'))
def norm(url):
    return re.sub(r'-(?:\d+x\d+|scaled)(?=\.[^.]+$)', '', url)

rows = read_csv('01_inventory/rune_code_carrier_fingerprints.csv')
for row in rows:
    old_url = row['source_url']
    if row['page_id'] == 'P261':
        matches = [r for r in media['images'] if r['file'] == '2022_04_Octave-Lettersfortitles-VernTonkin.jpg']
    else:
        matches = [r for r in media['images'] if norm(r['url']) == norm(old_url)]
    assert len(matches) == 1, row['page_id']
    m = matches[0]
    if row['source_sha256']:
        assert row['source_sha256'] == m['sha256']
    row['source_url'] = m['url']
    row['natural_dimensions'] = f"{m['width']}x{m['height']}"
    row['source_sha256'] = m['sha256']
    row['visual_source_url'] = old_url if row['visual_fingerprint_sha256'] else ''
    row['source_hash_provenance'] = 'Imported from rune_code_source_media.json; agrees with repository data/media-full.json; bytes not re-fetched in v0.26.2'
    row['source_retrieved_on'] = media['retrieved']
    if row['page_id'] == 'P261':
        row['limitations'] = 'Image carrier registered in v0.26.2; textual-key classification preserved, image inscription/classification deferred to v0.27. No new visual inspection.'
    else:
        row['limitations'] += ' Source hash is a harvest-manifest attestation imported in v0.26.2. Historical visual fingerprint refers to visual_source_url and captured_on, not a new full-resolution inspection.'
write_csv('01_inventory/rune_code_carrier_fingerprints.csv', rows)

corpus = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
chronology = [dict(post_id=p['id'], title=p['title'], url=p['link'], publication_date=p['date'], modified_date=p['modified'], provenance='repository data/corpus.json; WordPress REST API harvest; day precision') for p in corpus]
assert len(chronology) == 262 and all(re.fullmatch(r'\d{4}-\d{2}-\d{2}', p['publication_date']) for p in chronology)
write_csv('01_inventory/harvest_publication_dates.csv', chronology)

questions = read_csv('01_inventory/open_questions.csv')
for q in questions:
    if q['id'] == 'OQ001':
        q.update(status='resolved_by_colocated_harvest', blocking_condition='none; repository data/corpus.json and tools/cipher.py are available', allowed_next_action='Rerun tools/cipher.py from repository root; retain distinction between directly recovered and context-filled slots', not_a_fix_because='The former missing-repository dependency is removed; this does not adjudicate Rune Code plates')
    elif q['id'] == 'OQ003':
        q.update(status='publication_dates_available', blocking_condition='none for day-level chronology; imported harvest dates do not establish exact timestamps or revision history', allowed_next_action='Use harvest_publication_dates.csv for day-level chronology; retrieve authoritative timestamps only if a finer-grained question requires them', not_a_fix_because='Publication and modification dates are separately preserved from WordPress metadata; do not substitute modification dates for publication')
    elif q['id'] == 'OQ007':
        q.update(status='resolved_by_harvest_hash_manifest', blocking_condition='none for hash availability; full-resolution files are not bundled or re-fetched in v0.26.2', allowed_next_action='Authenticate any future downloaded carrier against rune_code_source_media.json before interpreting it', not_a_fix_because='All 31 source-byte hashes are imported from the harvest and cross-checked against its full manifest; visual fingerprints remain distinct')
write_csv('01_inventory/open_questions.csv', questions)

old_url = 'https://lettersfortitles.com/translating-is/'
new_url = 'https://lettersfortitles.com/translating-ice/'
post = next(p for p in corpus if p['slug'] == 'translating-ice')
assert post['title'] == 'Translating Is' and post['link'] == new_url
html = (ROOT / 'archive/pages/translating-ice.html').read_text(encoding='utf-8')
assert f'<link rel="canonical" href="{new_url}"' in html
for rel in ('01_inventory/verified_page_register.csv', '01_inventory/translation_register.csv', '02_structure/core_stream_alignment.csv', '07_capture/stanza-11-ice/links.csv', '07_capture/translating-eh/links.csv', '07_capture/translating-is/record.md'):
    replace(rel, old_url, new_url)
with (SEED / '07_capture/translating-is/record.md').open('a', encoding='utf-8') as f:
    f.write('\n## v0.26.2 URL provenance correction — 2026-09-12\n\nThe earlier register URL was `https://lettersfortitles.com/translating-is/`. The archived page canonical tag and WordPress-derived harvest link agree on `/translating-ice/`. The capture folder and original capture date remain unchanged. Live retrieval in this pass failed; this correction is archive-backed, not a new page capture.\n')
with (SEED / '06_sources/source_notes.md').open('a', encoding='utf-8') as f:
    f.write('\n## v0.26.2 canonical URL correction\n\nHistorical references to `https://lettersfortitles.com/translating-is/` above are retained as acquisition history. Current canonical URL: `https://lettersfortitles.com/translating-ice/`, supported by the archived canonical tag and harvest record; see `05_method/metadata_provenance_v0.26.2.md`.\n')

replace('05_method/rune_code_plate_reconciliation_v0.26.0.md', 'were inspected at their live full available source resolution.', 'were inspected at the live served resolutions recorded below. Correction in v0.26.2: these were not the largest available originals for Loop or Œ; the 1080-pixel derivatives remain the evidence actually read in this historical report.')

summary = 'Version 0.26.2 is a metadata/provenance patch derived from v0.26.1. It corrects Loop and Œ original-media identities/dimensions, registers the Octave image, imports 31 source-byte hash attestations and 262 day-level publication records, updates OQ001/OQ003/OQ007, and corrects the Translating Is canonical URL. It changes no transcription or retained media payload. Nine cross-lineage carrier disputes and the Octave classification question remain for v0.27.'
scope = '\n\n## Cross-lineage boundary — v0.26.2\n\nThe plate readings below remain the seed lineage’s readings, not adjudicated repository-wide findings. Nine carriers disagree with the harvest lineage; Octave has a separate classification question. See the repository `CROSS-LINEAGE-FINDINGS.md` and `V0.27-ADJUDICATION-PACKET.md`. Metadata completion does not pass Gate 0 or authorize a reading change.\n'
replace('README.md', 'Version: 0.26.1', 'Version: 0.26.2')
replace('README.md', 'Version 0.26.1 is a Rune Code quality-assurance patch.', summary + scope + '\nVersion 0.26.1 is a Rune Code quality-assurance patch.')
for rel in ('CODEX_HANDOFF.md', 'CLAUDE_HANDOFF.md'):
    replace(rel, 'Corpus 0.26.1', 'Corpus 0.26.2')
    replace(rel, 'Date: 2026-08-30', f'Date: {DATE}')
    text = (SEED / rel).read_text(encoding='utf-8')
    first, rest = text.split('\n', 1)
    write(rel, first + '\n\n' + summary + scope + rest)
replace('CODEX_HANDOFF.md', 'Parent: `letters_for_titles_corpus_seed_v0.26.0.zip`', 'Parent: `letters_for_titles_corpus_seed_v0.26.1.zip`')
replace('CODEX_HANDOFF.md', 'Parent SHA-256: `3f9b2c307b4763d97bfdfcbb801cf9ee575242595bf3eaf7bfbbac1a09f814a0`', f'Parent SHA-256: `{PARENT_HASH}`')
replace('CODEX_HANDOFF.md', "Claude's absent full harvest repository still prevents an end-to-end rerun of all 216 numbered tokens.", 'The full harvest is now co-located in the repository; tools/cipher.py reproduces the complete filename-run derivation, with recovered characters distinguished from context-filled positions.')
replace('CLAUDE_HANDOFF.md', 'your absent complete harvest repository still prevents an independent rerun of all 216 numbered slots.', 'the complete harvest is now co-located and its filename verifier is runnable from the repository root.')
replace('05_method/reentry_capsule.md', "This is substantial local confirmation, not a substitute for Claude's absent 216-token harvest repository.", 'The complete harvest is now co-located in the repository, where tools/cipher.py independently reproduces the filename-run derivation. Preserve direct recovery versus context-filled positions.')
replace('05_method/reentry_capsule.md', 'The current canonical release is `letters_for_titles_corpus_seed_v0.26.1.zip`, a quality-assurance patch derived from supplied canonical 0.26.0 SHA-256 `3f9b2c307b4763d97bfdfcbb801cf9ee575242595bf3eaf7bfbbac1a09f814a0`.', f'This v0.26.2 candidate derives from canonical `letters_for_titles_corpus_seed_v0.26.1.zip`, SHA-256 `{PARENT_HASH}`. Publication status must be checked in the repository release record.')
replace('05_method/reentry_capsule.md', "A future bounded pass may rerun the complete 261-slot verification if Claude's harvest repository is supplied,", 'The full harvest is co-located and its filename verification is available. A future bounded pass may')
with (SEED / '05_method/reentry_capsule.md').open('a', encoding='utf-8') as f:
    f.write(scope + '\n' + summary + '\nPublication dates have day precision; imported source hashes are harvest attestations, not newly authenticated bytes. v0.27 begins only after this patch lands and requires independent Loop authentication and 29-cell key reconstruction.\n')
replace('05_method/version_control_protocol.md', '→ 0.26.1 (Rune Code QA correction)`', '→ 0.26.1 (Rune Code QA correction) → 0.26.2 (metadata/provenance patch candidate)`')
changelog = (SEED / 'CHANGELOG.md').read_text(encoding='utf-8')
write('CHANGELOG.md', changelog.replace('# Changelog\n', f'# Changelog\n\n## 0.26.2 — {DATE}\n\n{summary}\n\nSource hashes are imported from the 2026-08-30 harvest manifest and agree with the full manifest; full-resolution bytes were not re-fetched. Historical rendered fingerprints and actual read resolutions are preserved. Canonical AS001 bytes match v0.26.1.\n', 1))
with (SEED / '05_method/lineage_log.md').open('a', encoding='utf-8') as f:
    f.write(f'\n## {DATE} — v0.26.2 metadata/provenance patch\n\n- Canonical parent: `{PARENT.name}`; SHA-256 `{PARENT_HASH}`.\n- {summary}\n- Existing historical reports and readings remain historical; the v0.26.0 resolution overclaim receives an explicit correction.\n- AS001 restored to parent bytes after preserving a pre-existing local one-frame replacement outside the release.\n')

sources = {}
for rel in ('data/media-code.json', 'data/media-full.json', 'data/corpus.json', 'archive/pages/translating-ice.html'):
    sources[rel] = sha(source_bytes(rel))
source_table = '\n'.join(f'| `{p}` | `{h}` |' for p, h in sources.items())
write('05_method/metadata_provenance_v0.26.2.md', f'''# v0.26.2 metadata and provenance reconciliation

Date: {DATE}
Parent: `{PARENT.name}`
Parent SHA-256: `{PARENT_HASH}`

{summary}

## Source identity

Source hashes below cover the exact Git blob bytes at repository commit `23012aceed6b92c0c36f0b315e8ffafb384ec994`, before any Windows checkout newline conversion.

| Repository source | SHA-256 |
|---|---|
{source_table}

The original 31-row media manifest is bundled verbatim as `01_inventory/rune_code_source_media.json`. All 31 entries agree with the full manifest on URL, SHA-256, byte count, width and height. Its retrieval date is 2026-08-30. No full-resolution source files were available locally or re-fetched in this patch. These are imported source-byte hash attestations, not independent current byte verification. Future interpretation must authenticate actual downloaded bytes first.

The 17 named carriers are matched by normalized media URL, removing only terminal WordPress size/scaled suffixes. Octave is explicitly selected by `2022_04_Octave-Lettersfortitles-VernTonkin.jpg`; it is not inferred from the old page URL. The other 14 records are numbered filename-run assets. Existing visual fingerprints retain their original URL and date in separate fields.

Loop now records the 2062x1528 original; Œ records 2560x2560; Octave records 1083x981. The historical v0.26.0 report retains the actual 1080-pixel derivative URLs and dimensions it read. This patch makes no new image reading.

## Publication metadata and open questions

`01_inventory/harvest_publication_dates.csv` preserves all 262 post IDs, titles, canonical links, publication dates and modification dates from the co-located harvest. Dates have day precision; exact timestamps and revision history are not established. OQ003 becomes publication_dates_available rather than a claim that every chronological research question is solved. OQ001's missing-repository dependency is removed. OQ007 is resolved for hash availability, not local byte possession.

## Canonical URL

For Translating Is, the archived page canonical tag and harvest link agree on `https://lettersfortitles.com/translating-ice/`. Current registers and referring capture links are corrected from `/translating-is/`; the `translating-is` local capture folder remains stable. Original URL provenance is retained in its record and source notes. Today's live page fetch timed out and the REST route was unavailable through the browsing tool; neither establishes a broken live URL.

## Media preservation and interpretation boundary

The pre-existing local AS001 replacement had one 360x360 frame, 28,796 bytes and SHA-256 `{sha(local)}`. It was preserved in the ignored `local-recovery/` folder before restoring the six-frame, 304,353-byte parent GIF with SHA-256 `{sha(parent['08_assets/mysterywyrm.gif'])}`. Its origin is unknown. The candidate has no media-payload differences from its parent.

Nine carrier transcription disputes and the separate Octave classification question remain open. No Gate 0 key reconstruction or plate adjudication occurs in v0.26.2.
''')
print('Prepared v0.26.2 metadata patch; local GIF backed up:', backup)
