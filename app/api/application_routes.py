from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth.dependencies import get_current_user

from app.models.user import User
from app.models.application import Application

from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse
)

router = APIRouter()


@router.post(
    "/applications",
    response_model=ApplicationResponse
)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_application = Application(
        company=application.company,
        role=application.role,
        status=application.status,
        user_id=current_user.id
    )

    db.add(db_application)
    db.commit()
    db.refresh(db_application)

    return db_application


@router.get(
    "/applications",
    response_model=list[ApplicationResponse]
)
def get_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    applications = (
        db.query(Application)
        .filter(Application.user_id == current_user.id)
        .all()
    )

    return applications