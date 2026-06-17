import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.schemas.job_analysis import JobAnalysis

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