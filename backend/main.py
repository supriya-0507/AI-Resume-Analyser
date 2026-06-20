from fastapi import FastAPI, UploadFile, File, Form
import shutil
import pdfplumber

app = FastAPI()

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
    "Pandas",
    "NumPy",
    "Oracle",
    "Generative AI",
    "RAG",
    "Cloud Computing",
    "Docker",
    "AWS"
]

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer is Working!"
    }


@app.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Save uploaded file
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # Resume Skills
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Job Description Skills
    job_skills = []

    for skill in SKILLS:
        if skill.lower() in job_description.lower():
            job_skills.append(skill)

    # Matched Skills
    matched_skills = []

    for skill in found_skills:
        if skill in job_skills:
            matched_skills.append(skill)

    # Missing Skills
    missing_skills = []

    for skill in job_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    # ATS Score
    if len(job_skills) > 0:
        ats_score = round(
            (len(matched_skills) / len(job_skills)) * 100,
            2
        )
    else:
        ats_score = 0

    # Recommendations
    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Consider adding {skill} to your resume"
        )

    # Resume Strength Analysis
    strengths = []
    resume_score = 0

    if "project" in text.lower():
        strengths.append("Has Projects")
        resume_score += 25

    if "certification" in text.lower() or "certifications" in text.lower():
        strengths.append("Has Certifications")
        resume_score += 25

    if "education" in text.lower():
        strengths.append("Has Education Section")
        resume_score += 25

    if len(found_skills) >= 5:
        strengths.append("Strong Technical Skills")
        resume_score += 25

    return {
        "filename": file.filename,
        "resume_skills": found_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ats_score": ats_score,
        "resume_score": resume_score,
        "strengths": strengths,
        "recommendations": recommendations
    }