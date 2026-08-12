import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.schemas.job_analysis import JobAnalysis
from app.schemas.resume_match import ResumeMatch

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0
)

structured_llm = llm.with_structured_output(
    JobAnalysis
)


def analyze_job_description(
    job_description: str
):
    prompt = f"""
    Extract information from this job description.

    Return:
    - role
    - company
    - skills
    - experience required
    - salary range
    - summary

    Job Description:

    {job_description}
    """

    return structured_llm.invoke(prompt)

resume_match_llm = llm.with_structured_output(
    ResumeMatch
)

def match_resume_to_job(
    resume: str,
    job_description: str
):
    prompt = f"""
    Compare the candidate's resume against the job description.

    Evaluate the candidate based on:
    - Required technical skills
    - Relevant experience
    - Technologies
    - Responsibilities
    - Overall suitability

    Give a match score from 0 to 100.

    Do not give a high score simply because some keywords match.
    Consider the overall relevance of the candidate's background.

    Candidate Resume:

    {resume}

    Job Description:

    {job_description}
    """

    return resume_match_llm.invoke(prompt)