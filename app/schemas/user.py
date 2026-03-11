from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, Field

# Esquema para LEER (lo que la API devuelve)
class User(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)

# Esquema para CREAR (lo que la API recibe)
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=72)
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
