# Línea base de calidad

## Propósito

Registrar las métricas del primer análisis disponible en SonarQube Cloud, antes de integrar el reporte de cobertura y aplicar las mejoras documentadas.

## Métricas iniciales

| Indicador | Resultado inicial | Observación |
|---|---:|---|
| Issues de seguridad | 17 | Hallazgos identificados por el análisis inicial. |
| Issues de fiabilidad | 1 | Un problema reportado inicialmente. |
| Issues de mantenibilidad | 1 | Un problema reportado inicialmente. |
| Hotspots revisados | 100% · A | El panel mostró revisión completa. |
| Riesgos de dependencias | 0 | No se mostraron riesgos. |
| Cobertura | Sin dato (`—`) | El reporte de cobertura aún no estaba disponible en SonarQube. No equivale a 0%. |
| Duplicaciones | 0.0% | El análisis inicial no mostró duplicación medible. |
| Quality Gate | No computado | El panel inicial todavía no presentaba un resultado calculado. |

## Fuente de la medición

Los datos corresponden al primer análisis visible del proyecto **Proyecto-SQA** en SonarQube Cloud, antes de que se importara `coverage.xml`. La captura del análisis inicial sirve como evidencia de esta línea base.

## Alcance y limitaciones

Esta línea base refleja las métricas disponibles en ese primer análisis. La cobertura y el Quality Gate no tenían un valor inicial visible, por lo que no deben compararse como si hubieran partido de 0% o de un resultado fallido. La comparación con las métricas posteriores se documentará en `Reporte-Mejora.md`.