from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.auth import router as auth_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/health", tags=["system"])
async def health_check():
    """Endpoint para monitoreo de salud del servicio"""
    return {
        "status": "available",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION
    }

# En el futuro aquí incluiremos los routers de la API
# app.include_router(api_router, prefix=settings.API_V1_STR)

# Registrar el router de autenticación
app.include_router(auth_router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])

