from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# Motor de conexión
# Usamos pool_pre_ping para que SQLAlchemy verifique si la conexión sigue viva
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para todos los modelos (Estilo SQLAlchemy 2.0)
class Base(DeclarativeBase):
    pass

# Dependencia para obtener la DB en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
