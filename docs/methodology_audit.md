# Benchmark methodology audit

Fecha de generacion: 2026-05-14T11:16:28.689198+00:00

## Veredictos para el pipeline

- Target canonico de benchmark: `event_count` crudo; no `log1p(y)`.
- GLM usa `PoissonRegressor`; XGBoost usa `count:poisson`; RF usa regresion de arboles sobre conteos crudos.
- El split de baseline es cronologico por orden de filas: 70% train, 15% validation, 15% test.
- El panel H3-tiempo actual es observado, no completo: no materializa pares celda-tiempo con cero incidentes.
- La cobertura ICCS debe describirse como cobertura por registros despues de limpieza, no por categorias.
- H3 resolucion 9: area promedio 0.105333 km2; edge length promedio 200.786 m.

## Artefactos generados

- `benchmark_target_model_specification.csv`
- `benchmark_temporal_splits.csv`
- `benchmark_h3_panel_definition.csv`
- `benchmark_iccs_coverage_definition.csv`
- `benchmark_h3_resolution_definition.csv`

## Implicacion para el paper benchmark

No afirmar que todos los modelos usan `log(1+y)`. No afirmar que existe un panel completo H3-tiempo con ceros explicitos. Si se desea un panel completo, eso seria un experimento/pipeline alternativo y requeriria reejecucion de fase 04 en adelante.
