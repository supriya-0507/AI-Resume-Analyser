# AI Resume Analyzer

An AI-powered Resume Analyzer that evaluates resumes against job descriptions, calculates ATS scores, identifies skill gaps, and provides personalized recommendations through an interactive dashboard.

---

## Features

✅ Resume PDF Upload

✅ Automatic Resume Text Extraction

✅ ATS Score Calculation

✅ Resume Quality Score

✅ Skill Match Analysis

✅ Missing Skill Detection

✅ Personalized Recommendations

✅ Interactive Streamlit Dashboard

✅ Visual Analytics using Plotly

✅ Downloadable Analysis Report

---

## Tech Stack

### Backend
- Python
- FastAPI
- PDFPlumber

### Frontend
- Streamlit

### Data Visualization
- Pandas
- Plotly

### Tools & Technologies
- Git
- GitHub
- VS Code

---

## Project Architecture

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Skill Detection Engine
    ↓
Job Description Matching
    ↓
ATS Score Calculation
    ↓
Skill Gap Analysis
    ↓
Recommendation Engine
    ↓
Interactive Dashboard
```

---

## Features Demonstrated

### Resume Analysis
- Extracts text from uploaded PDF resumes
- Detects technical skills from resume content
- Matches skills against job descriptions

### ATS Evaluation
- Calculates ATS compatibility score
- Identifies matched skills
- Highlights missing skills

### Resume Quality Assessment
- Evaluates resume strengths
- Calculates resume quality score
- Generates actionable recommendations

### Dashboard Analytics
- ATS score visualization
- Skill match analysis chart
- Resume overview metrics
- Downloadable analysis report

---


## Installation

Clone the repository:

```bash
git clone https://github.com/supriya-0507/AI-Resume-Analyzer.git
```

Navigate to the project folder:

```bash
cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Running the Frontend

```bash
streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## Sample Output

### ATS Score

```text
28.57%
```

### Resume Score

```text
100
```

### Matched Skills

```text
Python
Git
```

### Missing Skills

```text
SQL
FastAPI
Machine Learning
Docker
AWS
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

- FastAPI API Development
- PDF Processing and Parsing
- Resume Analysis Systems
- ATS Scoring Logic
- Skill Gap Detection
- Streamlit Dashboard Development
- Data Visualization with Plotly
- Git Version Control
- GitHub Project Management

---

## Future Improvements

- AI-Powered Resume Feedback using LLMs
- Gemini/OpenAI Integration
- Resume Summarization
- Industry-Specific ATS Analysis
- Resume Ranking System
- Multi-Resume Comparison
- Skill Learning Roadmap Generator
- Cloud Deployment using AWS or Oracle Cloud
- User Authentication
- Resume History Tracking

---

## Author

### Suvvari Supriya

B.Tech Computer Science and Engineering (Data Analytics)

VIT-AP University

### GitHub

https://github.com/supriya-0507

### LinkedIn

https://www.linkedin.com/in/suvvari-supriya-a74466334

---

## Connect With Me

I am passionate about Data Analytics, Artificial Intelligence, Machine Learning, Software Development, and building impactful technology solutions.

Feel free to connect with me for collaboration, internships, project discussions, and learning opportunities.

### GitHub
https://github.com/supriya-0507

### LinkedIn
https://www.linkedin.com/in/suvvari-supriya-a74466334

---

## License

This project is developed for educational, learning, and portfolio purposes.
