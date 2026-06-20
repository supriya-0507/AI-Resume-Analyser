from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil
import pdfplumber
import os

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SKILLS = [
    "Python",
    "SQL",
    "Git",
    "GitHub",
    "FastAPI",
    "Machine Learning",
    "Data Analytics",
    "Power BI",
    "Excel",
    "Java",
    "C++",
    "Docker",
    "AWS",
    "Oracle",
    "RAG"
]

os.makedirs("uploads", exist_ok=True)


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API Running"}


@app.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form("")
):

    # Save uploaded file
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

    text_lower = text.lower()

    # Skills found in resume
    found_skills = [
        skill for skill in SKILLS
        if skill.lower() in text_lower
    ]

    # Job skills from job description
    if job_description.strip():

        job_skills = [
            skill for skill in SKILLS
            if skill.lower() in job_description.lower()
        ]

    else:
        job_skills = found_skills

    # Matched skills
    matched_skills = [
        skill for skill in job_skills
        if skill in found_skills
    ]

    # Missing skills
    missing_skills = [
        skill for skill in job_skills
        if skill not in found_skills
    ]

    # ATS Score
    ats_score = 0

    if len(job_skills) > 0:
        ats_score = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )

    # Resume Quality Score
    resume_score = 0
    strengths = []

    if "project" in text_lower:
        resume_score += 25
        strengths.append("Has Projects")

    if "certification" in text_lower or "certificate" in text_lower:
        resume_score += 25
        strengths.append("Has Certifications")

    if "education" in text_lower:
        resume_score += 25
        strengths.append("Has Education Section")

    if len(found_skills) >= 5:
        resume_score += 25
        strengths.append("Strong Technical Skills")

    # Recommendations
    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Consider adding {skill} to your resume"
        )

    return {
        "filename": file.filename,
        "skills_found": found_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ats_score": ats_score,
        "resume_score": resume_score,
        "strengths": strengths,
        "recommendations": recommendations
    }