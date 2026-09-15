#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,html,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/'tables/source'
FAMS=['cdmx_daily','chicago_daily','cdmx_monthly_view','chicago_monthly_view','london_monthly_native']
MODELS=['zero','persistence_lag_1','seasonal_naive','poisson','negative_binomial','random_forest_poisson','xgboost_count_poisson']
FL={'cdmx_daily':'CDMX daily','chicago_daily':'Chicago daily','cdmx_monthly_view':'CDMX monthly view','chicago_monthly_view':'Chicago monthly view','london_monthly_native':'London monthly native'}
ML={'zero':'Zero predictor','persistence_lag_1':'Lag-1 persistence','seasonal_naive':'Seasonal naive','poisson':'Poisson GLM','negative_binomial':'Negative Binomial NB2','random_forest_poisson':'Random Forest (Poisson)','xgboost_count_poisson':'XGBoost (count:poisson)'}
def rows(n):
 with (SRC/n).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def fmt(v):
 v=float(v); a=abs(v)
 return (f'{v:.4e}'.replace('e+0','e+').replace('e-0','e-')) if a>=1e5 or (0<a<1e-4) else f'{v:.6f}'.rstrip('0').rstrip('.')
def wr(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8',newline='\n')
def svg(lines,w,h):
 body=''.join(f'<text x="60" y="{80+55*i}" font-family="sans-serif" font-size="24">{html.escape(t)}</text>' for i,t in enumerate(lines))
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white" stroke="black"/>{body}</svg>\n'
def render(out):
 c=rows('data_coverage.csv'); l=[r'\begin{table*}[!t]',r'\centering',r'\caption{Data coverage and resolution-9 H3 support. Processed-record ICCS mapping coverage and raw-record criminal-eligibility coverage use distinct denominators and must not be combined. H3 uses the center-containment policy.}',r'\label{tab:art01-data-coverage}',r'\scriptsize',r'\resizebox{\textwidth}{!}{%',r'\begin{tabular}{lrrrrrrr}',r'\toprule',r'City & Processed records & ICCS mapped & Mapping (\%) & Raw records & Criminal eligible & Eligibility (\%) & H3 r9 center \\',r'\midrule']
 for r in c:l.append(f'{r["city"]} & {int(r["processed_records"]):,} & {int(r["iccs_mapped_records"]):,} & {float(r["iccs_mapping_percent"]):.3f} & {int(r["raw_records"]):,} & {int(r["criminal_eligible_records"]):,} & {float(r["criminal_eligibility_percent"]):.3f} & {int(r["h3_r9_center_cells"]):,} \\\\')
 l += [r'\bottomrule',r'\end{tabular}%',r'}',r'\end{table*}','']; wr(out/'tables/export/tab_art01_data_coverage.tex','\n'.join(l))
 b=rows('benchmark_macro_mae.csv'); d={(r['benchmark_family'],r['comparator']):r for r in b}; l=[r'\begin{table*}[!t]',r'\centering',r'\caption{Macro mean MAE over the 2021--2023 validation folds. Values are descriptive within each benchmark family; the 2024 held-out final-test period is not used.}',r'\label{tab:art01-benchmark}',r'\scriptsize',r'\begin{tabular}{llr}',r'\toprule',r'Benchmark family & Comparator & Macro MAE \\',r'\midrule']
 for f in FAMS:
  first=True
  for m in MODELS:l.append(f'{FL[f] if first else ""} & {ML[m]} & {fmt(d[(f,m)]["macro_mae"])} \\\\'); first=False
  l.append(r'\addlinespace')
 l += [r'\bottomrule',r'\end{tabular}',r'\end{table*}','']; wr(out/'tables/export/tab_art01_benchmark.tex','\n'.join(l))
 lp={r['benchmark_family']:r for r in rows('local_performance.csv')}; l=[r'\begin{table*}[!t]',r'\centering',r'\caption{Learned-model performance with the lowest-MAE mandatory naive control shown for context. Values are descriptive within each benchmark family and support within-family comparison only.}',r'\label{tab:art01-local-performance}',r'\scriptsize',r'\begin{tabular}{lrrrrr}',r'\toprule',r'Benchmark family & Naive floor & Poisson & NB2 & RF-Poisson & XGB-Poisson \\',r'\midrule']
 for f in FAMS:
  r=lp[f]; vals=[fmt(r[x]) for x in ('naive_floor_mae','poisson_mae','nb2_mae','rf_poisson_mae','xgb_poisson_mae')];l.append(FL[f]+' & '+' & '.join(vals)+r' \\')
 l += [r'\bottomrule',r'\end{tabular}',r'\end{table*}','']; wr(out/'tables/export/tab_art01_local_performance.tex','\n'.join(l))
 h=rows('h3_boundary_support.csv'); wr(out/'figures/export/h3_boundary_support.svg',svg(['Resolution-9 H3 boundary-policy support','City | Full | Center (selected) | Overlap']+[f'{r["city"]} | {int(r["full_cells"]):,} | {int(r["center_cells"]):,} | {int(r["overlap_cells"]):,}' for r in h],1000,360))
 wf=(ROOT/'figures/source/benchmark_workflow.txt').read_text().strip().split(' -> '); wr(out/'figures/export/benchmark_workflow.svg',svg(['Benchmark construction and evaluation flow']+[' -> '.join(wf[i:i+2]) for i in range(0,len(wf),2)],1400,420))
 tp=(ROOT/'figures/source/temporal_validation.txt').read_text().strip().splitlines(); wr(out/'figures/export/temporal_validation.svg',svg(['Rolling-origin validation boundary']+tp,1400,260))
def check():
 with tempfile.TemporaryDirectory() as td:
  t=Path(td);render(t)
  rel=['tables/export/tab_art01_data_coverage.tex','tables/export/tab_art01_benchmark.tex','tables/export/tab_art01_local_performance.tex','figures/export/h3_boundary_support.svg','figures/export/benchmark_workflow.svg','figures/export/temporal_validation.svg']
  bad=[p for p in rel if (ROOT/p).read_bytes()!=(t/p).read_bytes()]
  if bad:raise SystemExit('STALE_OR_NONDETERMINISTIC: '+', '.join(bad))
  print('PASS deterministic regeneration')
if __name__=='__main__':
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--write',action='store_true');g.add_argument('--check',action='store_true');a=p.parse_args();render(ROOT) if a.write else check()
