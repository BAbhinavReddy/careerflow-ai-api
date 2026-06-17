from fastapi import FastAPI

from app.db.database import engine, Base

from app.models.user import User
from app.models.application import Application

from app.api.user_routes import router as user_router

from app.api.auth_routes import router as auth_router

from app.api.application_routes import (
    router as application_router
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(application_router)

@app.get("/")
def root():
    return {"message": "CareerFlow AI API is running"}