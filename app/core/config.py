from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # Nombre del Proyecto para la documentación de OpenAPI
    PROJECT_NAME: str = "Auth Microservice Pro"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Seguridad (¡Cámbialas en producción!)
    SECRET_KEY: str = "super_secret_key_para_desarrollo_12345"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Base de Datos (PostgreSQL por defecto)
    DATABASE_URL: Optional[str] = "postgresql://user:pass@localhost:5432/auth_db"

    # Configuración de Pydantic para leer el archivo .env
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

# Instancia única para toda la app (Singleton)
settings = Settings()
