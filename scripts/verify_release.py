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

# Scientific scope and data-availability boundaries.
availability = json.loads((ROOT / 'DATA_AVAILABILITY.json').read_text())
assert availability['raw_municipal_records']['included'] is False
assert availability['processed_record_level_derivatives']['included'] is False
assert availability['reviewed_aggregate_outputs']['included'] is True
assert availability['final_test_2024']['status'] == 'CLOSED'
assert availability['final_test_2024']['released_results'] is False

# Stable public artifact identifiers.
index = json.loads((ROOT / 'ARTIFACT_INDEX.json').read_text())
artifacts = {a['id']: a for a in index['artifacts']}
required_ids = {
    'ART01-DATA-001', 'ART01-DATA-002', 'ART01-DATA-003', 'ART01-DATA-004',
    'ART01-TBL-001', 'ART01-TBL-002', 'ART01-TBL-003',
    'ART01-FIG-001', 'ART01-FIG-002', 'ART01-FIG-003',
    'ART01-PROV-001', 'ART01-PROV-002',
    'ART01-REPRO-001', 'ART01-REPRO-002', 'ART01-REPRO-003', 'ART01-REPRO-004',
    'ART01-RIGHTS-001', 'ART01-RIGHTS-002',
}
assert required_ids.issubset(artifacts)
assert len(artifacts) == len({a['id'] for a in index['artifacts']})

# Public provenance and source metadata.
provenance = json.loads((ROOT / 'PROVENANCE.json').read_text())
assert provenance['integrity_manifest'] == 'SHA256SUMS.txt'
assert provenance['generator'] == 'scripts/render_public_assets.py'
assert provenance['artifacts']['ART01-DATA-003']['final_test_2024'] == 'CLOSED'
assert provenance['artifacts']['ART01-DATA-004']['final_test_2024'] == 'CLOSED'

source_manifest = json.loads((ROOT / 'SOURCE_MANIFEST.json').read_text())
sources = {s['id']: s for s in source_manifest['sources']}
assert sources['SRC-CDMX-001']['license_or_terms'] == 'CC-BY-4.0'
assert sources['SRC-CHI-001']['license_or_terms'] == 'CITY_OF_CHICAGO_DATA_PORTAL_TERMS_OF_USE'
assert sources['SRC-CHI-001']['open_license_identifier_asserted'] is False
assert sources['SRC-LON-001']['license_or_terms'] == 'OGL-3.0'
assert sources['SRC-ICCS-001']['license_or_terms'] == 'NO_REUSE_LICENSE_ASSERTED'
assert sources['SRC-CDMX-001']['raw_data_redistributed'] is False
assert sources['SRC-CHI-001']['raw_data_redistributed'] is False
assert sources['SRC-LON-001']['raw_data_redistributed'] is False
assert sources['SRC-ICCS-001']['raw_or_mapping_content_redistributed'] is False

assert (ROOT / 'RIGHTS_AND_LICENSES.md').is_file()
assert (ROOT / 'LICENSE-DATA-DOCS.md').is_file()
assert (ROOT / 'REPRODUCIBILITY.md').is_file()
assert (ROOT / 'PACKAGE_MANIFEST.json').is_file()

# Published validation surface remains bounded to the same folds and excludes 2024.
with (ROOT / 'tables/source/benchmark_macro_mae.csv').open(newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 35
assert all(r['validation_folds'] == '2021;2022;2023' for r in rows)
assert all(r['final_test_status'] == '2024 held out; not used' for r in rows)

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

# Public-facing package excludes incomplete citation metadata and publication-prep files.
for forbidden in (
    'CITATION.cff', '.zenodo.json', 'citation', 'release', 'data_acquisition', 'provenance',
    'DATA_RELEASE_DECISION.json', 'LICENSE_AND_RIGHTS_AUDIT.md',
    'PUBLIC_RELEASE_MANIFEST.json', 'REPRODUCIBILITY_README.md', 'figures/FIGURE_STATUS.json',
    'results', 'mappings', 'splits',
):
    assert not (ROOT / forbidden).exists(), f'non-public package path present: {forbidden}'

print('PASS clean public ART-01 reproducibility package')
