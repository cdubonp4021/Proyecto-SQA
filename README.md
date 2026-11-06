# Sistema de control de servicios — TallerService

[![Pruebas y calidad](https://github.com/cdubonp4021/Proyecto-SQA/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/cdubonp4021/Proyecto-SQA/actions/workflows/tests.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=cdubonp4021_Proyecto-SQA&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cdubonp4021_Proyecto-SQA)
[![Cobertura](https://sonarcloud.io/api/project_badges/measure?project=cdubonp4021_Proyecto-SQA&metric=coverage)](https://sonarcloud.io/summary/new_code?id=cdubonp4021_Proyecto-SQA)

TallerService es una aplicación web para apoyar la operación de un taller automotriz. Permite gestionar propietarios, vehículos, órdenes de servicio, mantenimiento preventivo, recordatorios, mecánicos e historial.

Esta guía explica cómo preparar y ejecutar el proyecto en una computadora nueva con Windows.

## Tecnologías

- Python y Django
- PostgreSQL 17
- Docker Compose
- GitHub Actions
- Ruff
- Coverage.py
- SonarQube Cloud

## Requisitos

Instala estas herramientas antes de continuar:

- [Git](https://git-scm.com/downloads)
- [Python 3.10 o superior](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Durante la instalación de Python, habilita la opción **Add Python to PATH**. Al terminar, abre Docker Desktop y espera a que indique que está iniciado.

## Descargar el proyecto

Abre PowerShell y ejecuta:

```powershell
git clone https://github.com/cdubonp4021/Proyecto-SQA.git
cd Proyecto-SQA