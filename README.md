# Proyecto DevOps – Entorno Local para Aplicación Flask

Este proyecto implementa un entorno de desarrollo local completo para una aplicación web en Python (Flask) utilizando Docker, Docker Compose y PostgreSQL. 

El objetivo es facilitar la incorporación de nuevos desarrolladores al equipo y permitir pruebas automáticas, contribuciones seguras y despliegue eficiente.

---

## Arquitectura del Software

La aplicación sigue una arquitectura de microservicio simple basada en contenedores:

[ Navegador ]
    --
[ Flask App ]
    --
[ PostgreSQL DB ]

---
### Componentes:
- **Flask App**: Aplicación web desarrollada en Python. Contenida en Docker.
- **PostgreSQL**: Base de datos relacional. También contenida.
- **Docker Compose**: Orquestador que levanta la app y la base de datos.
- **pytest**: Framework para pruebas unitarias.
- **SQLAlchemy**: ORM para conexión y gestión de la base de datos.

---

## Cómo ejecutar el entorno local

Asegúrar de tener Docker y Docker Compose instalados.

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

Construye y levanta los contenedores:
```bash
docker-compose up --build
```

Accede a la app en tu navegador en:
http://localhost:5000

## Cómo ejecutar los tests
# Desde Docker:
```bash
docker-compose run --rm web pytest
```
# Con reporte de cobertura:
```bash
docker-compose run --rm web pytest --cov=app
```
El objetivo es cubrir al menos el 80% del código fuente con tests.

---
Normas de colaboración
Modelo de ramas:
main: versión estable para producción

develop: rama de integración (desarrollo activo)

feature/<nombre>: ramas para nuevas funcionalidades

fix/<nombre>: ramas para corrección de errores.
---
Buenas prácticas:
Hacer pull requests (PR) hacia develop.

Incluir pruebas con cada nueva funcionalidad.

Mantener estilo de código PEP8.

Validar que los tests pasen antes de hacer merge.

---
La base de datos se configura automáticamente con Docker.

Se puede añadir nuevas variables de entorno en docker-compose.yml.
---
