from fastapi import FastAPI, UploadFile, File
import shutil
import pdfplumber

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
    "Cloud Computing"
]

JOB_SKILLS = [
    "Python",
    "SQL",
    "Power BI",
    "Machine Learning",
    "Data Analytics",
    "Git",
    "GitHub",
    "Excel"
]

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My Resume Analyzer is Working!"}


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

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

    # Find skills in resume
    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # Match with job requirements
    matched_skills = []

    for skill in JOB_SKILLS:
        if skill in found_skills:
            matched_skills.append(skill)

    # Find missing skills
    missing_skills = []

    for skill in JOB_SKILLS:
        if skill not in matched_skills:
            missing_skills.append(skill)

    # ATS Score
    ats_score = round((len(matched_skills) / len(JOB_SKILLS)) * 100, 2)

    return {
        "filename": file.filename,
        "skills_found": found_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "ats_score": ats_score
    }