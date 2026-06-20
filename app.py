import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.warning("Please upload a PDF resume")
        st.stop()

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    data = {
        "job_description": job_description
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/upload",
            files=files,
            data=data
        )

        result = response.json()

        st.success("Analysis Complete")

        # ATS SCORE
        st.subheader("ATS Score")
        st.metric("ATS Score", f"{result['ats_score']}%")

        st.progress(min(int(result["ats_score"]), 100))

        # RESUME RATING
        if result["ats_score"] >= 80:
            st.success("🏆 Excellent Resume Match")
        elif result["ats_score"] >= 60:
            st.info("👍 Good Resume Match")
        elif result["ats_score"] >= 40:
            st.warning("⚠️ Average Resume Match")
        else:
            st.error("❌ Poor Resume Match")

        # RESUME SCORE
        st.subheader("Resume Score")
        st.metric("Resume Score", result["resume_score"])

        # OVERVIEW
        st.subheader("📊 Resume Overview")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Skills Found",
            len(result["skills_found"])
        )

        c2.metric(
            "Matched Skills",
            len(result["matched_skills"])
        )

        c3.metric(
            "Missing Skills",
            len(result["missing_skills"])
        )

        # PIE CHART
        st.subheader("Skill Match Analysis")

        chart_df = pd.DataFrame({
            "Category": ["Matched", "Missing"],
            "Count": [
                len(result["matched_skills"]),
                len(result["missing_skills"])
            ]
        })

        fig = px.pie(
            chart_df,
            values="Count",
            names="Category",
            hole=0.5
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # SKILLS SECTION
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")

            for skill in result["matched_skills"]:
                st.success(skill)

        with col2:
            st.subheader("❌ Missing Skills")

            for skill in result["missing_skills"]:
                st.error(skill)

        # TOP SKILLS TO LEARN
        st.subheader("🔥 Top Skills To Learn")

        for skill in result["missing_skills"][:5]:
            st.write("•", skill)

        # STRENGTHS
        st.subheader("💪 Strengths")

        for strength in result["strengths"]:
            st.info(strength)

        # RECOMMENDATIONS
        st.subheader("📌 Recommendations")

        for rec in result["recommendations"]:
            st.warning(rec)

        # DOWNLOAD REPORT
        report = f"""
AI Resume Analyzer Report

ATS Score: {result['ats_score']}%

Resume Score: {result['resume_score']}

Matched Skills:
{', '.join(result['matched_skills'])}

Missing Skills:
{', '.join(result['missing_skills'])}

Strengths:
{', '.join(result['strengths'])}

Recommendations:
{chr(10).join(result['recommendations'])}
"""

        st.download_button(
            "📥 Download Report",
            report,
            file_name="resume_report.txt"
        )

    except Exception as e:
        st.error(f"Error: {e}")