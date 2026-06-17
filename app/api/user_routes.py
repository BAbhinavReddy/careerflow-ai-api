from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.models.user import User
from app.db.session import get_db

from app.core.security import hash_password
from app.auth.dependencies import get_current_user

router = APIRouter()


@router.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user