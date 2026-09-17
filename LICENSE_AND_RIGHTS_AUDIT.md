# License and rights audit — CURRENT release candidate

State: **REMEDIATED_PENDING_BOUNDED_R06_5_REAUDIT**

Audit scope: the allowlist-bounded CURRENT release surface for ART-01. This record does not authorize publication, a GitHub Release, Zenodo deposit, DOI, or venue submission. R06.5 remains the independent authority for closure of finding R06.5-F001.

## 1. Artifact-class rights conclusion

| Artifact class | Current examples | Ownership / copyright position | Applicable license / reuse basis | Attribution / restrictions | Redistribution status |
|---|---|---|---|---|---|
| Original software/code | `scripts/*.py` | Repository-authored software | MIT, root `LICENSE` | Preserve MIT copyright and permission notice | Included |
| Original documentation / release metadata | `README.md`, reproducibility/release/provenance documentation and JSON metadata | Repository-authored text/metadata to the extent copyrightable | CC BY 4.0 under `LICENSE-DATA-DOCS.md` | Attribute repository authors; third-party source terms remain separate | Included |
| Original schematic/vector figure artwork | `benchmark_workflow.svg`, `temporal_validation.svg` and editable text sources | Repository-authored schematic presentation | CC BY 4.0 under `LICENSE-DATA-DOCS.md` | Attribute repository authors; no third-party logos/trademarks included | Included |
| Aggregate reviewed analytical outputs | `tables/source/*.csv`, deterministic table exports, `h3_boundary_support.svg` | Researcher-produced aggregate measurements/model results and their repository-authored selection/arrangement/presentation | CC BY 4.0 only for rights held by repository authors; underlying source facts/data are **not relicensed** and remain subject to the source-specific instruments below | Preserve source attribution and source-specific restrictions; do not imply source endorsement | Included as aggregate-only outputs |
| Raw municipal source material | CDMX, Chicago, London incident-level source snapshots | Third-party/source-publisher material | Original source terms only | Source-specific; no repository sublicensing | **NOT INCLUDED / DO NOT REDISTRIBUTE** |
| Processed record-level derivatives | Private cleaned/geospatial panels | Derived from third-party source records | No public redistribution conclusion asserted here | Held private | **NOT INCLUDED / HOLD_NOT_RELEASED** |
| UNODC ICCS publication/taxonomy/mapping snapshot | ICCS PDF/private mapping catalog | UN/UNODC third-party material | No reuse license or permission is asserted by this repository | No taxonomy rows, mapping table, PDF pages, logos, or other ICCS publication content are redistributed | **NOT INCLUDED** |

The root MIT license is a software license and **does not automatically extend to municipal data, UNODC material, or other third-party content**.

## 2. Source-by-source evidence and obligations

### Mexico City — FGJ open-data source

- Dataset: `Carpetas de investigación FGJ`.
- Publisher/source: Fiscalía General de Justicia de la Ciudad de México via Portal de Datos Abiertos CDMX.
- Official evidence URL: https://datos.cdmx.gob.mx/dataset/carpetas-de-investigacion-fgj-de-la-ciudad-de-mexico
- License shown by the official dataset page: Creative Commons Attribution 4.0.
- License URL: https://creativecommons.org/licenses/by/4.0/
- Reuse basis: CC BY 4.0 permits reuse/adaptation subject to attribution and license conditions.
- Release treatment: raw and record-level data are not redistributed; only aggregate research outputs are included. Source attribution is required.

### Chicago — City of Chicago crime data

- Dataset: `Crimes - 2001 to Present` / City of Chicago crime data.
- Publisher/data owner: Chicago Police Department / City of Chicago Data Portal.
- Official dataset URL: https://data.cityofchicago.org/d/ijzp-q8t2
- Federal catalog mirror used for durable source discovery: https://catalog.data.gov/dataset/crimes-2001-to-present
- The City dataset metadata identifies the license as `See Terms of Use`; no CC/ODC/open-license identifier is asserted here.
- Canonical City terms URL: https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html
- Additional official City-hosted terms evidence: https://webapps1.chicago.gov/ChicagoTif/disclaimer.html
- Reuse basis recorded conservatively: City of Chicago Terms of Use govern secondary/derivative use and require source/disclaimer compliance; this repository does **not** relicense City data.
- Release treatment: no Chicago raw records or processed record-level panels are included. Only researcher-produced aggregate results are included. Users reacquiring or reusing Chicago source data must follow the then-current City terms and dataset-specific notices. The City/CPD is not represented as endorsing this repository or its transformed outputs.

### London / England-Wales police open data

- Source: data.police.uk archive / street-level crime data.
- Official source URL: https://data.police.uk/data/archive/
- Official licensing evidence: https://data.police.uk/ and https://data.police.uk/about/
- Catalog metadata: https://www.data.gov.uk/dataset/bb2c3b16-6719-4e00-ae75-48dd462cb915/england-national-crime-mapping
- License: Open Government Licence v3.0.
- License URL: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- Reuse basis: OGL v3.0, subject to its attribution and other conditions.
- Release treatment: raw and record-level data are not redistributed; only aggregate research outputs are included. Required source/OGL attribution must be preserved.

### UNODC ICCS framework

- Framework source URL: https://www.unodc.org/documents/data-and-analysis/statistics/crime/ICCS/ICCS_English_2016_web.pdf
- Public reuse license for the ICCS publication/taxonomy was **not demonstrated by the audited release evidence**, therefore none is asserted.
- Release treatment is deliberately non-redistributive: the ICCS PDF, private mapping catalog, taxonomy rows, and mapping tables remain excluded. Public files may report aggregate counts/percentages resulting from private application of the classification, but do not reproduce ICCS taxonomy content.
- Attribution/provenance: identify UNODC ICCS as the classification framework and link to the official framework source; do not imply UNODC endorsement.

## 3. Aggregate-output compatibility boundary

The CURRENT aggregate CSV/TEX/SVG outputs contain city-level counts, coverage percentages, H3 support counts, benchmark MAE values, validation-status labels, and deterministic presentations of those research outputs. They do not contain incident-level records, addresses, coordinates, municipal source rows, ICCS mapping rows, publisher templates, source logos, or source documents.

The repository's CC BY 4.0 grant applies only to repository-authored copyrightable expression/selection/arrangement. It does not grant rights in underlying third-party data. Independent reacquisition of source data must occur from the official URLs under the source terms recorded above.

## 4. Redistribution decisions

- Raw municipal records: `DO_NOT_REDISTRIBUTE`.
- Processed record-level derivatives: `HOLD_NOT_RELEASED`.
- Aggregate reviewed outputs: included in the release candidate under the scoped rights boundary above, pending independent R06.5 re-audit.
- ICCS mapping/catalog material: excluded; provenance/framework URL only.
- Publisher templates, logos, and venue-facing manuscript binaries: excluded from this public package.

## 5. Release and science locks

Release lock remains active: no `v1.0.0` tag, GitHub Release, Zenodo deposit, DOI, venue selection, author-order inference, or corresponding-author inference is authorized by this remediation.

Science lock remains unchanged: `science_changed=false`; `claims_promoted=0`; `2024=CLOSED`; M8/M9/M10 consumed by ART-01 = `0/0/0`.
