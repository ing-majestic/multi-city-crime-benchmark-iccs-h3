# Rights and licenses

This repository separates rights by artifact class. Repository licenses do not override or relicense third-party source material.

## Software

Original software code in this repository is covered by the root `LICENSE` (MIT License).

## Repository-authored documentation and figures

Repository-authored documentation and schematic figures are covered by the terms stated in `LICENSE-DATA-DOCS.md`.

## Reviewed aggregate outputs

The public CSV tables contain reviewed aggregate measurements used to regenerate the tables and figures associated with the article. The repository's license applies only to copyrightable repository-authored expression, selection, and arrangement to the extent rights are held by the authors. Underlying facts and third-party source material remain subject to their original source terms.

## Crime-record and classification sources

- **Mexico City crime records**: the official open-data source is identified in `SOURCE_MANIFEST.json` with CC BY 4.0 terms. Raw records are not redistributed.
- **Chicago crime records**: the official dataset and City of Chicago terms are identified in `SOURCE_MANIFEST.json`. No open-license identifier is asserted by this repository. Raw records are not redistributed.
- **London police records**: data.police.uk material is identified in `SOURCE_MANIFEST.json` with Open Government Licence v3.0 terms. Raw records are not redistributed.
- **ICCS / UNODC**: no reuse license is asserted here for the ICCS publication or taxonomy. ICCS publication content, taxonomy rows, mapping rows, and the private mapping snapshot are not redistributed.

## Official boundary sources used for H3 support

The public H3-support summaries and downstream benchmark surfaces depend on official city-boundary inputs. Those geometries are not redistributed by this repository; only source/provenance metadata and aggregate analytical outputs are public.

- **Mexico City boundary — INEGI Marco Geoestadístico 2024**: governed by the *Términos de Libre Uso de la Información del INEGI*. Required attribution recorded for this package: “Fuente: INEGI, Marco Geoestadístico, 2024.” Official source and terms URLs, retrieval identity and SHA-256 are recorded under `SRC-CDMX-BOUNDARY-001` in `SOURCE_MANIFEST.json`.
- **Chicago boundary — City of Chicago, Boundaries - City, qqq8-j68g**: governed by the City of Chicago Data Terms of Use. No open-license identifier is asserted. Attribution recorded for this package: “City of Chicago Data Portal, Boundaries - City, dataset qqq8-j68g.” Source identity and terms are recorded under `SRC-CHI-BOUNDARY-001`.
- **London boundary — Greater London Authority**: source licensing record identifies the Open Government Licence together with the Ordnance Survey OpenData Licence. Required attribution recorded for this package: “Contains National Statistics data © Crown copyright and database right; Contains Ordnance Survey data © Crown copyright and database right.” Source identity and licensing document are recorded under `SRC-LON-BOUNDARY-001`.

## Material not redistributed

This repository does not distribute raw municipal crime records, processed record-level panels, official city-boundary geometries, or the private ICCS mapping snapshot. Readers should obtain upstream material from the official source portals listed in `SOURCE_MANIFEST.json` and comply with the applicable source terms.

Repository-authored aggregate outputs do not transfer or supersede rights in the underlying third-party data, boundary files, publications, names, logos, or trademarks.
