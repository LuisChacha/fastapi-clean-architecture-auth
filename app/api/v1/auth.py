from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db
from app.services.auth_service import AuthService
from app.schemas.user import User, UserCreate
from app.schemas.auth_token import Token
# AQUÍ ESTÁ EL IMPORT QUE TE COMENTABA:
from app.core import security 

router = APIRouter()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en el sistema.
    """
    auth_service = AuthService(db)
    return auth_service.register_user(user_in)

@router.post("/login", response_model=Token)
def login(
    db: Session = Depends(get_db), 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    Endpoint de login compatible con OAuth2.
    """
    auth_service = AuthService(db)
    user = auth_service.authenticate(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Ahora 'security' ya está definido y funcionará:
    access_token = security.create_access_token(subject=user.id)
    
    return {
        "access_token": access_token, 
        "token_type": "bearer"
    }
