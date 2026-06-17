from pydantic import BaseModel
from typing import List, Optional


class JobAnalysis(BaseModel):
    role: str
    company: str
    skills: List[str]
    experience_required: Optional[str] = None
    salary_range: Optional[str] = None
    summary: str