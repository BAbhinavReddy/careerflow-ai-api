````markdown
# CareerFlow AI API

An AI-powered job application tracking and resume matching backend built with Python, FastAPI, PostgreSQL, SQLAlchemy, LangChain, and Google Gemini.

CareerFlow AI API combines traditional backend engineering with LLM-powered job analysis to help users organize job applications and evaluate how well their resume matches a specific job description.

---

## Overview

CareerFlow AI API is a backend-focused application designed around the job application workflow.

The system allows authenticated users to:

- Create an account
- Log in securely using JWT authentication
- Create and track job applications
- Store complete job descriptions
- Retrieve their own applications
- Analyze unstructured job descriptions using Google Gemini
- Extract structured job information using LangChain and Pydantic
- Compare a resume against a job description
- Generate an AI-powered resume-to-job match score from 0–100
- Identify matching and missing skills

The project demonstrates backend API development, relational database integration, authentication, authorization, LLM integration, structured AI outputs, and containerized development.

---

## Key Features

### User Authentication

- User registration
- JWT-based authentication
- Password hashing using bcrypt
- Password verification
- Protected API routes
- User-level authorization

### Job Application Tracking

Each application can contain:

- Company
- Role
- Application status
- Job description
- User ownership

Applications are stored in PostgreSQL and accessed through SQLAlchemy ORM.

### AI Job Description Analysis

The application uses LangChain with Google Gemini to analyze unstructured job descriptions and extract structured information such as:

- Job role
- Company
- Required skills
- Experience requirements
- Salary range
- Job summary

The AI response is validated using Pydantic structured output.

### AI Resume Matching

CareerFlow compares a candidate's resume against a stored job description.

The AI evaluates:

- Technical skills
- Relevant experience
- Technologies
- Job responsibilities
- Overall relevance

It produces:

- Match score from 0–100
- Matching skills
- Missing skills
- Explanation of the match

Example:

```text
Match Score: 92/100

Matching Skills:
- Python
- FastAPI
- PostgreSQL
- Redis
- Docker
- AWS

Missing Skills:
- Kafka
````

---

## Architecture

```text
                         Client
                           |
                           v
                     FastAPI API
                           |
             +-------------+-------------+
             |                           |
             v                           v
       Authentication              Application API
             |                           |
        JWT + bcrypt              CRUD + Authorization
             |                           |
             +-------------+-------------+
                           |
                           v
                     SQLAlchemy ORM
                           |
                           v
                      PostgreSQL
                           |
                           |
             +-------------+-------------+
             |                           |
             v                           v
      Job Description                Resume
             |                           |
             +-------------+-------------+
                           |
                           v
                       LangChain
                           |
                           v
                    Google Gemini
                           |
                           v
                Pydantic Structured Output
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
         Match Score   Matching Skills  Missing Skills
            0-100
```

---

## Application Flow

### Job Application Flow

```text
User
 |
 | POST /applications
 v
FastAPI
 |
 v
Pydantic Validation
 |
 v
Authentication / Authorization
 |
 v
SQLAlchemy
 |
 v
PostgreSQL
```

### AI Job Analysis Flow

```text
Job Description
 |
 v
LangChain
 |
 v
Google Gemini
 |
 v
Structured Pydantic Output
 |
 +----> Role
 +----> Company
 +----> Skills
 +----> Experience
 +----> Salary
 +----> Summary
```

### Resume Matching Flow

```text
Resume
   +
Job Description
   |
   v
LangChain
   |
   v
Google Gemini
   |
   v
Pydantic Validation
   |
   v
Resume Match Result
   |
   +----> Match Score (0-100)
   +----> Matching Skills
   +----> Missing Skills
   +----> Summary
```

---

## Technology Stack

### Backend

* Python 3.11
* FastAPI
* Uvicorn
* REST APIs
* Pydantic
* SQLAlchemy

### Database

* PostgreSQL 16
* SQLAlchemy ORM
* Relational database modeling
* Foreign key relationships

### AI / LLM

* Google Gemini
* Gemini 2.5 Flash
* LangChain
* Structured LLM outputs
* Prompt engineering
* Pydantic-validated AI responses

### Authentication & Security

* JWT
* OAuth2 Bearer Authentication
* bcrypt
* Password hashing
* Password verification
* Protected routes
* User-level authorization

### DevOps / Development

* Docker
* Docker Compose
* Python virtual environments
* Environment variables
* Git

---

## Project Structure

```text
careerflow-ai-api/
│
├── app/
│   ├── api/
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   └── application_routes.py
│   │
│   ├── core/
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── database.py
│   │   └── session.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── application.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── application.py
│   │   └── resume_match.py
│   │
│   ├── services/
│   │
│   ├── ai/
│   │   └── job_analyzer.py
│   │
│   └── main.py
│
├── test_ai.py
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## API Endpoints

The API is documented and testable through FastAPI's automatically generated Swagger/OpenAPI interface.

### Authentication

#### `POST /users`

Creates a new user account.

Example request:

```json
{
  "email": "user@example.com",
  "password": "mypassword"
}
```

The password is hashed before being stored in PostgreSQL.

---

#### `POST /login`

Authenticates an existing user and returns a JWT access token.

Example response:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

#### `GET /me`

Returns information about the currently authenticated user.

Requires a valid JWT bearer token.

---

### Job Applications

#### `POST /applications`

Creates a new job application for the authenticated user.

Example request:

```json
{
  "company": "Google",
  "role": "Backend Engineer",
  "status": "applied",
  "job_description": "We are hiring a Backend Engineer..."
}
```

---

#### `GET /applications`

Retrieves job applications belonging to the authenticated user.

User authorization ensures that users only access their own applications.

---

### AI Resume Matching

#### `POST /applications/{application_id}/match`

Compares a candidate's resume against the job description associated with an application.

Example request:

```json
{
  "resume": "Python backend engineer with experience building REST APIs..."
}
```

Example response:

```json
{
  "match_score": 92,
  "summary": "The candidate is a strong match for the Backend Engineer role...",
  "matching_skills": [
    "Python",
    "FastAPI",
    "PostgreSQL",
    "Redis",
    "Docker",
    "AWS"
  ],
  "missing_skills": [
    "Kafka"
  ]
}
```

---

## AI Structured Output

Instead of relying on free-form LLM responses, the project uses Pydantic models to define the expected structure of AI responses.

Example:

```python
class ResumeMatch(BaseModel):
    match_score: int = Field(
        ge=0,
        le=100
    )
    summary: str
    matching_skills: list[str]
    missing_skills: list[str]
```

This ensures that the AI-generated match score remains within the expected 0–100 range and that the API receives predictable structured data.

---

## Database Design

The application uses PostgreSQL as its relational database.

### Users

```text
users
----------------
id
email
hashed_password
```

### Applications

```text
applications
----------------
id
company
role
status
job_description
user_id
```

The `user_id` field creates a relationship between an application and its owner.

```text
User
 |
 | 1
 |
 | *
 v
Application
```

This allows the API to enforce user-level ownership and authorization.

---

## Authentication Flow

```text
                 Registration
                     |
                     v
                User Password
                     |
                     v
               bcrypt Hashing
                     |
                     v
                PostgreSQL
```

Login:

```text
Email + Password
       |
       v
Find User
       |
       v
Verify bcrypt Hash
       |
       v
Generate JWT
       |
       v
Return Access Token
```

Protected request:

```text
Client
 |
 | Authorization: Bearer <JWT>
 v
FastAPI
 |
 v
Validate JWT
 |
 v
Identify User
 |
 v
Authorize Resource
 |
 v
Process Request
```

---

## Dockerized PostgreSQL

PostgreSQL runs inside a Docker container using Docker Compose.

The database configuration is defined in:

```text
docker-compose.yml
```

Example architecture:

```text
FastAPI Application
       |
       | localhost:5433
       v
Docker Container
       |
       | PostgreSQL:5432
       v
PostgreSQL 16
```

The host uses port `5433` because port `5432` was already unavailable on the local development environment.

---

## Environment Variables

Sensitive configuration is stored in `.env` rather than hardcoded into application code.

Example:

```env
DATABASE_URL=postgresql://admin:password@localhost:5433/careerflow

GEMINI_API_KEY=your_gemini_api_key

SECRET_KEY=your_secret_key
```

The `.env` file should not be committed to Git.

Add it to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd careerflow-ai-api
```

### 2. Create a Virtual Environment

Python 3.11 is used for this project.

```bash
python3.11 -m venv venv
```

Activate the environment:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://admin:password@localhost:5433/careerflow

GEMINI_API_KEY=your_gemini_api_key

SECRET_KEY=your_secret_key
```

Replace the placeholder Gemini API key and secret key with your own values.

---

### 5. Start PostgreSQL

Make sure Docker Desktop is running.

Then:

```bash
docker compose up -d
```

Verify the container:

```bash
docker compose ps
```

Expected:

```text
careerflow_postgres
```

with the container running.

---

### 6. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Swagger can be used to:

* Register users
* Log in
* Authorize using JWT
* Create applications
* Retrieve applications
* Test resume matching

---

## Example End-to-End Workflow

### Step 1 — Create an Account

```http
POST /users
```

```json
{
  "email": "abhinav@example.com",
  "password": "securepassword"
}
```

### Step 2 — Login

```http
POST /login
```

```json
{
  "email": "abhinav@example.com",
  "password": "securepassword"
}
```

Receive:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

### Step 3 — Authorize

Use the JWT access token in Swagger's authorization interface.

```text
Bearer <access_token>
```

### Step 4 — Create a Job Application

```http
POST /applications
```

```json
{
  "company": "Google",
  "role": "Backend Engineer",
  "status": "applied",
  "job_description": "We are hiring a Backend Engineer with experience in Python, FastAPI, PostgreSQL, Redis and Docker. Kafka experience is preferred."
}
```

### Step 5 — Match Resume

```http
POST /applications/1/match
```

```json
{
  "resume": "Software Engineer with experience building Python backend services, REST APIs, PostgreSQL applications, FastAPI services, Docker environments and AI-powered applications using LangChain and Gemini."
}
```

### Step 6 — Receive AI Analysis

```json
{
  "match_score": 92,
  "summary": "The candidate is a strong match...",
  "matching_skills": [
    "Python",
    "FastAPI",
    "PostgreSQL",
    "Docker"
  ],
  "missing_skills": [
    "Kafka"
  ]
}
```

---

## Testing AI Functionality

The AI job analysis and resume matching functionality can also be tested independently using:

```bash
python test_ai.py
```

Example result:

```text
match_score=92

summary="The candidate is a strong match for the Backend Engineer role..."

matching_skills=[
    "Python",
    "FastAPI",
    "PostgreSQL",
    "Redis",
    "Docker",
    "AWS"
]

missing_skills=[
    "Kafka"
]
```

---

## Engineering Concepts Demonstrated

This project demonstrates practical experience with:

* REST API development
* Backend service architecture
* FastAPI application development
* PostgreSQL database integration
* SQLAlchemy ORM
* Relational data modeling
* CRUD operations
* Foreign key relationships
* Pydantic data validation
* Dependency injection
* JWT authentication
* OAuth2 bearer authentication
* Password hashing
* User authorization
* LLM API integration
* LangChain
* Google Gemini
* Prompt engineering
* Structured LLM outputs
* AI response validation
* Resume-to-job matching
* Docker containerization
* Docker Compose
* Environment-based configuration
* Modular Python architecture
* Separation of concerns

---

## Why This Project?

Traditional job trackers primarily store application information.

CareerFlow AI adds an AI-assisted layer that helps analyze job descriptions and evaluate how closely a candidate's resume aligns with a specific position.

The project was designed to combine:

```text
Backend Engineering
        +
Database Engineering
        +
Authentication
        +
LLM Engineering
        =
AI-Powered Backend Application
```

---

## Future Improvements

Potential future improvements include:

* Resume file upload support
* Persistent storage of match results
* Redis caching
* Background AI processing
* Automated job ingestion
* Resume version management
* Application status history
* Email notifications
* Production deployment
* Automated API testing
* Database migrations with Alembic

These features are outside the current project scope.

---

## Project Status

**Status: Completed**

The current version includes the core backend, database, authentication, job application tracking, AI job analysis, and AI-powered resume matching functionality.

---

## Author

**Abhinav Reddy Bobba**

Software Engineer | Python Backend | AI/LLM Engineering

```text
Python • FastAPI • PostgreSQL • SQLAlchemy • LangChain • Gemini
```

```
```
