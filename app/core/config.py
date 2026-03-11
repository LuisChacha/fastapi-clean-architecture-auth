from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from typing import Optional

class Settings(BaseSettings):
    # --- Configuración General ---
    PROJECT_NAME: str = "Auth Microservice Pro"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # --- Seguridad ---
    # Al no tener valor por defecto, Pydantic lo buscará obligatoriamente en el .env
    SECRET_KEY: str 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # --- Base de Datos (Variables del .env) ---
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str = "5432"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        """
        Construye la URL de conexión dinámicamente.
        Formato: postgresql://user:password@server:port/db
        """
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # --- Configuración de Pydantic ---
    model_config = SettingsConfigDict(
        env_file=".env", 
        case_sensitive=True,
        # Esto permite que si hay variables extra en el .env no explote la app
        extra="ignore" 
    )

# Instancia única (Singleton)
settings = Settings()

