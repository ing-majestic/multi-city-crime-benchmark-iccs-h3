#!/usr/bin/env python3
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

subprocess.run(
    [sys.executable, str(ROOT / 'scripts/render_public_assets.py'), '--check'],
    check=True,
)

# Scientific/release guards.
d = json.loads((ROOT / 'DATA_RELEASE_DECISION.json').read_text())
assert d['raw_municipal_records']['included'] is False
assert d['processed_record_level_derivatives']['included'] is False
assert d['final_test_2024']['status'] == 'CLOSED'
assert d['release_lock']['active'] is True
assert d['release_lock']['tag_v1_0_0_created'] is False
assert d['release_lock']['github_release_created'] is False
assert d['release_lock']['zenodo_deposit_created'] is False
assert d['release_lock']['doi_assigned'] is False

b = json.loads((ROOT / 'provenance/RELEASE_SOURCE_BINDING.json').read_text())
assert b['authoritative_english_pdf']['sha256'] == 'f0fa0f0bb8cf69a0729d0ec5a84499255357e3cbc9e96ab3af7b7c74263f4dab'
assert b['science_lock']['science_changed'] is False
assert b['science_lock']['final_test_2024'] == 'CLOSED'
assert b['science_lock']['m8_results_consumed'] == 0
assert b['science_lock']['m9_results_consumed'] == 0
assert b['science_lock']['m10_results_consumed'] == 0

with (ROOT / 'tables/source/benchmark_macro_mae.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 35
assert all(r['validation_folds'] == '2021;2022;2023' for r in rows)
assert all(r['final_test_status'] == '2024 held out; not used' for r in rows)

# Rights/licensing remediation guards.
rights = (ROOT / 'LICENSE_AND_RIGHTS_AUDIT.md').read_text()
assert 'REMEDIATED_PENDING_BOUNDED_R06_5_REAUDIT' in rights
assert (ROOT / 'LICENSE-DATA-DOCS.md').is_file()
acq = json.loads((ROOT / 'data_acquisition/SOURCE_ACQUISITION_MANIFEST.json').read_text())
sources = {s['id']: s for s in acq['sources']}
assert sources['cdmx_raw']['license_or_terms'] == 'CC-BY-4.0'
assert sources['chicago_raw']['license_or_terms'] == 'CITY_OF_CHICAGO_DATA_PORTAL_TERMS_OF_USE'
assert sources['chicago_raw']['license_identifier_asserted'] is False
assert sources['london_raw']['license_or_terms'] == 'OGL-3.0'
assert sources['iccs_mapping_catalog_private_snapshot']['license_or_terms'] == 'NO_REUSE_LICENSE_ASSERTED'
assert all(s['redistributed'] is False for s in sources.values())

# Allowlist and SHA-256 manifest must agree exactly, except that the checksum
# file cannot checksum itself.
allowlist = [
    line.strip()
    for line in (ROOT / 'PUBLIC_ALLOWLIST.txt').read_text().splitlines()
    if line.strip()
]
assert len(allowlist) == len(set(allowlist))
assert 'SHA256SUMS.txt' in allowlist
for rel in allowlist:
    assert (ROOT / rel).is_file(), f'missing allowlisted file: {rel}'

manifest = {}
for line in (ROOT / 'SHA256SUMS.txt').read_text().splitlines():
    if not line.strip():
        continue
    digest, rel = line.split(None, 1)
    rel = rel.strip()
    assert len(digest) == 64 and all(c in '0123456789abcdef' for c in digest)
    assert rel not in manifest
    manifest[rel] = digest

expected_manifest_paths = set(allowlist) - {'SHA256SUMS.txt'}
assert set(manifest) == expected_manifest_paths, 'SHA256SUMS paths differ from PUBLIC_ALLOWLIST'
for rel, expected in manifest.items():
    actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
    assert actual == expected, f'SHA-256 mismatch: {rel}'

# CURRENT release surface hygiene.
for forbidden in ('CITATION.cff', '.zenodo.json', 'results', 'mappings', 'splits'):
    assert not (ROOT / forbidden).exists(), f'forbidden current-surface path present: {forbidden}'
assert not any(ROOT.glob('.ws07_sync*'))
assert not any(ROOT.rglob('.ws07_sync*'))

print('PASS bounded release-candidate verification including SHA-256 and rights remediation')
