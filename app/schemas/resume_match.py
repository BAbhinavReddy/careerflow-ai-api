from pydantic import BaseModel, Field


class ResumeMatch(BaseModel):
    match_score: int = Field(
        ge=0,
        le=100
    )
    summary: str
    matching_skills: list[str]
    missing_skills: list[str]


class ResumeMatchRequest(BaseModel):
    resume: str