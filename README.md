AI Resume Analyzer
Overview

AI Resume Analyzer is a Python-based web application that evaluates resumes against job descriptions and calculates ATS compatibility scores.

The system extracts text from PDF resumes, identifies technical skills, compares them with job requirements, and provides personalized recommendations for improvement.

Features
Resume PDF Upload
ATS Score Calculation
Skill Gap Analysis
Resume Quality Scoring
Interactive Dashboard
Downloadable Analysis Report
FastAPI Backend
Streamlit Frontend
Tech Stack
Python
FastAPI
Streamlit
PDFPlumber
Pandas
Plotly
Git & GitHub
Installation
pip install -r requirements.txt

Run Backend:

uvicorn backend.main:app --reload

Run Frontend:

streamlit run app.py
Author

Suvvari Supriya
