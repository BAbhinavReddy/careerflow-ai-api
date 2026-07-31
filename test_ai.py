from app.ai.job_analyzer import analyze_job_description

jd = """
Google is hiring a Backend Engineer.

Requirements:
Python
FastAPI
Redis
PostgreSQL

Salary:
120k-150k
"""

result = analyze_job_description(jd)
print(result)