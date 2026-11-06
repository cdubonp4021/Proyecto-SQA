# Plan de Aseguramiento de Calidad (SQA)

## 1. Propósito

Definir las actividades, herramientas y criterios usados para verificar la calidad de TallerService. El plan busca que los cambios del proyecto pasen por pruebas y análisis automatizados antes de integrarse a la rama principal.

## 2. Alcance

TallerService es una aplicación web para la gestión de un taller automotriz, desarrollada con Django y PostgreSQL. El aseguramiento cubre los módulos de propietarios, vehículos, órdenes de servicio, mantenimiento, recordatorios, mecánicos e historial.

También abarca las pruebas automatizadas, las comprobaciones de Django, el análisis estático con Ruff, la medición de cobertura con Coverage.py, el flujo de GitHub Actions y el análisis de SonarQube Cloud.

## 3. Referencias de calidad

Se toma ISO/IEC 25010 como referencia para observar características del producto como fiabilidad, seguridad y mantenibilidad. Para organizar las pruebas, se consideran conceptos generales de ISO/IEC/IEEE 29119.

Estas referencias sirven como guía para el trabajo; no representan una certificación del proyecto.

## 4. Responsabilidades

| Responsable | Actividad |
|---|---|
| Estudiante | Mantener el código, ejecutar las validaciones, documentar resultados y atender hallazgos. |
| GitHub Actions | Ejecutar automáticamente las etapas de compilación, comprobación, pruebas, lint y cobertura. |
| SonarQube Cloud | Analizar el código e informar métricas y hallazgos de calidad. |

## 5. Actividades de aseguramiento

1. Instalar las dependencias definidas para el proyecto.
2. Compilar los módulos Python y ejecutar las comprobaciones de Django.
3. Ejecutar las pruebas automatizadas con `config.settings_test`.
4. Revisar el código con Ruff.
5. Medir la cobertura con Coverage.py y exigir un mínimo de 60%.
6. Publicar el reporte de cobertura e importarlo en SonarQube Cloud.
7. Revisar los resultados y registrar las acciones de mejora.

## 6. Criterios de aceptación

- Las pruebas automatizadas deben finalizar correctamente.
- Ruff debe terminar sin errores.
- La cobertura total debe ser igual o mayor al 60%.
- El flujo debe completar sus etapas de build, test, analyze y report.
- Los hallazgos de SonarQube deben revisarse y documentarse; no se marcarán como resueltos sin validar el cambio.

## 7. Métricas y línea base actual

| Métrica | Resultado registrado |
|---|---:|
| Pruebas automatizadas | 126 aprobadas |
| Cobertura informada por SonarQube Cloud | 93.1% |
| Quality Gate | Passed |
| Duplicaciones | 0.0% |
| Fiabilidad | A · 0 issues |
| Mantenibilidad | A · 0 issues |
| Seguridad | B · 14 issues de nivel bajo |
| Hotspots | 0 · revisión A |

La cobertura supera el umbral de 60% configurado en el flujo. Los 14 hallazgos de seguridad quedan pendientes de revisión.

## 8. Herramientas

- **Django:** framework de la aplicación y sistema de pruebas.
- **PostgreSQL 17 y Docker Compose:** base de datos del entorno local.
- **GitHub Actions:** integración continua.
- **Ruff:** análisis estático y revisión de imports.
- **Coverage.py:** medición de cobertura.
- **SonarQube Cloud:** análisis de calidad y visualización de métricas.

## 9. Riesgos y acciones

| Riesgo | Acción |
|---|---|
| Un cambio rompe una función existente. | Ejecutar la suite de pruebas antes de integrar cambios. |
| La cobertura cae por debajo del mínimo. | Mantener el umbral de 60% como condición del flujo. |
| Persisten hallazgos de seguridad. | Revisar cada alerta y validar su corrección con nuevas pruebas y análisis. |
| La configuración local difiere de la usada para pruebas rápidas. | Documentar el uso de `config.settings_test` y conservar PostgreSQL para validar el entorno con la base prevista. |

## 10. Control y actualización

Este plan se actualizará cuando cambien los módulos, las herramientas, los criterios de aceptación o las métricas del proyecto. Cada corrección deberá quedar registrada mediante un cambio en el repositorio y una nueva ejecución del flujo de calidad.