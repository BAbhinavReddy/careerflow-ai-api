from app.ai.job_analyzer import match_resume_to_job


resume = """
Abhinav Reddy Bobba

Backend / AI Engineer

Skills:
Python, FastAPI, PostgreSQL, SQLAlchemy,
Redis, Docker, LangChain, Gemini, AWS

Experience:
Built backend APIs using FastAPI and PostgreSQL.
Developed AI applications using LangChain and Gemini.
Implemented authentication, database integration,
and structured LLM outputs.
"""


job_description = """
We are hiring a Backend Engineer.

Requirements:
Python
FastAPI
PostgreSQL
Redis
Docker

Experience building REST APIs is required.

Experience with Kafka is preferred.
AWS experience is a plus.
"""


result = match_resume_to_job(
    resume,
    job_description
)

print(result)