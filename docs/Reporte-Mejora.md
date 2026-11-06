# Reporte de mejora de calidad

## Resumen

Se compararon las métricas del primer análisis de SonarQube Cloud con las del análisis posterior a la integración de Coverage.py. También se registraron los resultados de las pruebas y del análisis con Ruff.

## Comparación de métricas

| Indicador | Antes | Después | Resultado |
|---|---:|---:|---|
| Issues de seguridad | 17 | 14 | Disminuyeron 3; quedan 14 hallazgos de nivel bajo pendientes de revisión. |
| Issues de fiabilidad | 1 | 0 | El análisis final no reportó issues de fiabilidad. |
| Issues de mantenibilidad | 1 | 0 | El análisis final no reportó issues de mantenibilidad. |
| Cobertura | Sin dato | 93.1% | SonarQube recibió el reporte de cobertura. No se calcula una variación porque no había valor inicial. |
| Duplicaciones | 0.0% | 0.0% | Se mantuvo sin duplicación medible. |
| Hotspots revisados | 100% · A | 100% · A | Se mantuvo la revisión completa. |
| Riesgos de dependencias | 0 | 0 | Sin cambios reportados. |
| Quality Gate | No computado | Passed | El análisis final cumplió las condiciones configuradas. |

## Verificaciones del proyecto

- **Pruebas Django:** 126 aprobadas con `config.settings_test`.
- **Ruff:** la revisión terminó con `all checks passed`.
- **Cobertura local:** 93% en el reporte de Coverage.py.
- **Cobertura en SonarQube Cloud:** 93.1%.
- **Umbral configurado en CI:** 60%.

## Interpretación

La integración del reporte de cobertura permitió visualizar la cobertura del código en SonarQube Cloud y obtener un resultado de Quality Gate aprobado. Los issues de fiabilidad y mantenibilidad que aparecían en el primer análisis dejaron de aparecer en el análisis posterior. Los issues de seguridad bajaron de 17 a 14, pero todavía requieren revisión individual.

La cobertura inicial no tenía un valor visible. Por esta razón, no se presenta como 0% ni se calcula un aumento porcentual desde ese punto.

## Evidencias

- Primer análisis y métricas iniciales: `Linea-Base-Calidad.md` y captura del primer análisis de SonarQube Cloud.
- Resultado final de calidad y cobertura: panel de SonarQube Cloud.
- Pruebas y lint: resultados locales y ejecuciones disponibles en GitHub Actions.
- Flujo automatizado: `.github/workflows/tests.yml`.