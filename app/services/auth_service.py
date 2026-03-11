from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.infrastructure.repositories.user_repository import UserRepository
from app.core import security
from app.schemas.user import UserCreate
from app.infrastructure.models import User

class AuthService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register_user(self, user_in: UserCreate) -> User:
        # 1. Verificar si el usuario ya existe
        user = self.repository.get_by_email(user_in.email)
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El usuario con este email ya existe en el sistema.",
            )
        
        # 2. Hashear la contraseña
        hashed_password = security.get_password_hash(user_in.password)
        
        # 3. Crear el usuario en la DB
        return self.repository.create(user_in, hashed_password)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.repository.get_by_email(email)
        if not user:
            return None
        if not security.verify_password(password, user.hashed_password):
            return None
        return user
