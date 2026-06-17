from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"


class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str

    class Config:
        from_attributes = True