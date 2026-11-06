# Manual técnico

## 1. Arquitectura general

TallerService utiliza Django para atender las solicitudes del usuario, validar la información y aplicar la lógica de la aplicación. PostgreSQL almacena los datos. En el entorno local, Docker Compose permite iniciar la base de datos.

El flujo de calidad automatizado se ejecuta con GitHub Actions. Ruff revisa el código, Coverage.py mide la cobertura y SonarQube Cloud presenta el análisis de calidad.

## 2. Componentes principales

| Componente | Función |
|---|---|
| Django | Aplicación web, rutas, vistas, formularios, modelos y pruebas. |
| PostgreSQL 17 | Base de datos del entorno local. |
| Docker Compose | Inicio de PostgreSQL en el equipo local. |
| GitHub Actions | Automatización de las verificaciones del repositorio. |
| Ruff | Análisis estático y revisión de imports. |
| Coverage.py | Medición y generación del reporte de cobertura. |
| SonarQube Cloud | Análisis de métricas e issues de calidad. |

## 3. Flujo de integración continua

El flujo está definido en `.github/workflows/tests.yml` y se ejecuta cuando hay cambios en `main` o una solicitud de integración dirigida a esa rama.

1. **Build:** instala las dependencias, compila los módulos Python y ejecuta las comprobaciones de Django.
2. **Test:** ejecuta las pruebas con `config.settings_test` y genera datos de cobertura.
3. **Analyze:** ejecuta Ruff y comprueba que la cobertura alcance el mínimo de 60%.
4. **Report:** publica el resumen de cobertura y genera `coverage.xml` para el análisis de SonarQube Cloud.

## 4. Archivos importantes

| Archivo | Uso |
|---|---|
| `requirements.txt` | Dependencias principales de la aplicación. |
| `requirements-dev.txt` | Dependencias para desarrollo, pruebas y análisis. |
| `config/settings_test.py` | Configuración rápida usada por la suite automatizada. |
| `.github/workflows/tests.yml` | Definición del flujo de calidad de GitHub Actions. |
| `sonar-project.properties` | Configuración del proyecto para SonarQube Cloud. |
| `.env.example` | Ejemplo de las variables necesarias; no debe contener secretos reales. |

## 5. Ejecución local

Desde PowerShell, en la carpeta principal del proyecto:

```powershell
# Instalar las dependencias
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt

# Ejecutar las pruebas automatizadas
.\.venv\Scripts\python.exe manage.py test --settings=config.settings_test

# Revisar el código con Ruff
.\.venv\Scripts\python.exe -m ruff check core owners vehicles service_orders maintenance reminders