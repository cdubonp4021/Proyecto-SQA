# Matriz de pruebas

La matriz resume escenarios representativos de TallerService. La suite completa ejecutada reportó **126 pruebas aprobadas**. Ese resultado está disponible de forma consolidada; no se cuenta con un reporte individual asociado a cada ID de esta matriz.

| ID | Módulo | Tipo | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|---|---|
| TS-01 | Autenticación | Funcional | Usuario sin iniciar sesión intenta acceder al dashboard. | El sistema redirige al formulario de inicio de sesión. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-02 | Autenticación | Funcional | Usuario con credenciales válidas envía el formulario de inicio de sesión. | Se inicia la sesión y se permite acceder al dashboard. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-03 | Propietarios | Funcional | Consulta o registro de propietario con datos requeridos válidos. | El sistema muestra o guarda los datos correctamente. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-04 | Propietarios | Validación | Envío de datos incompletos o inválidos. | El sistema muestra errores y no guarda el registro inválido. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-05 | Vehículos | Integración | Vehículo asociado a un propietario existente. | El vehículo conserva la relación con el propietario y valida sus campos. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-06 | Órdenes de servicio | Funcional | Creación o consulta de una orden vinculada a un vehículo. | La orden se registra y muestra la información correspondiente. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-07 | Mantenimiento | Funcional | Plan de mantenimiento asociado a un vehículo y con fechas programadas. | El sistema valida y muestra el plan y sus fechas. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-08 | Recordatorios | Funcional | Generación o consulta de un recordatorio programado. | El recordatorio conserva su tipo, fecha y estado. | Suite Django aprobada; resultado disponible de forma consolidada. |
| TS-09 | Calidad estática | Análisis | Ejecución de Ruff sobre las aplicaciones del proyecto. | Ruff termina sin errores. | Ruff finalizó sin errores. |
| TS-10 | Cobertura e integración continua | Análisis | Ejecución de pruebas y generación del reporte de cobertura. | Las pruebas pasan y la cobertura supera el mínimo de 60%. | 126 pruebas aprobadas; SonarQube Cloud reportó 93.1% de cobertura y Quality Gate Passed. |

## Evidencia general

- Suite automatizada de Django: **126 pruebas aprobadas**.
- Ruff: **sin errores** en la última ejecución reportada.
- SonarQube Cloud: **93.1% de cobertura** y **Quality Gate Passed**.
- Las evidencias se consultan en las ejecuciones de GitHub Actions y en el proyecto de SonarQube Cloud.