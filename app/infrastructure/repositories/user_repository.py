from sqlalchemy.orm import Session
from sqlalchemy import select
from app.infrastructure.models import User
from app.schemas.user import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()

    def create(self, obj_in: UserCreate, hashed_password: str) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=hashed_password,
            full_name=obj_in.full_name,
            is_active=obj_in.is_active
        )
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
