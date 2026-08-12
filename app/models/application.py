from sqlalchemy import Column, Integer, String, ForeignKey, Text

from app.db.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String, nullable=False)

    role = Column(String, nullable=False)

    status = Column(String, default="applied")

    job_description = Column(Text, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))