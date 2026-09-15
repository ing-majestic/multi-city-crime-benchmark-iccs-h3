#!/usr/bin/env python3
from pathlib import Path
import csv,json,subprocess,sys,re
ROOT=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(ROOT/'scripts/render_public_assets.py'),'--check'],check=True)
d=json.loads((ROOT/'DATA_RELEASE_DECISION.json').read_text()); assert d['raw_municipal_records']['included'] is False and d['processed_record_level_derivatives']['included'] is False and d['final_test_2024']['status']=='CLOSED'
b=json.loads((ROOT/'provenance/RELEASE_SOURCE_BINDING.json').read_text()); assert b['authoritative_english_pdf']['sha256']=='f0fa0f0bb8cf69a0729d0ec5a84499255357e3cbc9e96ab3af7b7c74263f4dab'; assert b['science_lock']['final_test_2024']=='CLOSED'; assert b['science_lock']['m8_results_consumed']==b['science_lock']['m9_results_consumed']==b['science_lock']['m10_results_consumed']==0
with (ROOT/'tables/source/benchmark_macro_mae.csv').open(newline='') as f: rs=list(csv.DictReader(f)); assert len(rs)==35 and all(r['validation_folds']=='2021;2022;2023' for r in rs) and all(r['final_test_status']=='2024 held out; not used' for r in rs)
assert not (ROOT/'CITATION.cff').exists() and not (ROOT/'.zenodo.json').exists()
print('PASS bounded release-candidate verification')
