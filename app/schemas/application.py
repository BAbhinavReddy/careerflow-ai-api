from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"
    job_description: str


class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    job_description: str
    class Config:
        from_attributes = True