# FastAPI Clean Architecture Auth 🛡️

Este repositorio es un **Showcase de Ingeniería de Software** que implementa un microservicio de autenticación robusto, siguiendo principios de **Clean Architecture** y **SOLID**.

## 🚀 Stack Tecnológico
* **Python 3.12** + **FastAPI** (Alto rendimiento y tipado moderno).
* **SQLAlchemy 2.0** (ORM con soporte asíncrono).
* **Alembic** (Gestión de migraciones de base de datos).
* **PostgreSQL** (Persistencia relacional).
* **Docker & Docker Compose** (Contenerización de infraestructura).
* **JWT & Bcrypt** (Seguridad avanzada para tokens y hashing).

## 🏗️ Arquitectura del Proyecto
El código está organizado en capas para garantizar el desacoplamiento:
- `app/api`: Controladores y definición de rutas.
- `app/core`: Configuraciones globales y lógica de seguridad (JWT).
- `app/infrastructure`: Modelos de base de datos y conexión (SQLAlchemy).
- `app/schemas`: DTOs y validación de datos con Pydantic.
- `app/services`: Lógica de negocio y orquestación.



## 🛠️ Instalación y Uso

1. **Clonar y configurar:**
   ```bash
   git clone https://github.com/LuisChacha/fastapi-clean-architecture-auth.git
   cp .env.example .env
   ```

2. **Levantar infraestructura:**
   ```bash
   docker compose up -d 	
   ```

3. **Ejecutar migraciones y servidor:**
   ```bash
   alembic upgrade head
   uvicorn app.main:app --reload
   ```

4. **Documentación Interactiva:**
   Visita http://localhost:8000/docs para probar los endpoints de Registro, Login y Health Check.

