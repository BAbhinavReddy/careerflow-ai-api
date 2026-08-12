from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth.dependencies import get_current_user

from app.models.user import User
from app.models.application import Application

from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse
)

from app.schemas.resume_match import (
    ResumeMatch,
    ResumeMatchRequest
)

from app.ai.job_analyzer import match_resume_to_job

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
    job_description=application.job_description,
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

@router.post(
    "/applications/{application_id}/match",
    response_model=ResumeMatch
)
def match_application(
    application_id: int,
    request: ResumeMatchRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == current_user.id
    ).first()

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    result = match_resume_to_job(
        request.resume,
        application.job_description
    )

    return result