"""Streamlit web interface for Resume Analyzer."""

import streamlit as st
import json
import os
import tempfile

from .config import load_config
from .core import (
    analyze_resume,
    score_against_jd,
    simulate_ats_score,
    compare_resumes,
    generate_improvement_suggestions,
)
from .utils import get_llm_client


def check_ollama():
    _, _, check_ollama_running = get_llm_client()
    if not check_ollama_running():
        st.error("⚠️ Ollama is not running. Please start it with: `ollama serve`")
        st.stop()


def main():
    st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")
    st.title("📄 Resume Analyzer")
    st.caption("Analyze resumes, score against job descriptions, and simulate ATS evaluation")

    config = load_config()
    check_ollama()

    with st.sidebar:
        st.header("⚙️ Settings")
        st.markdown(f"**Model:** {config['llm']['model']}")
        st.divider()
        st.markdown("### 📋 Instructions")
        st.markdown("1. Upload your resume\n2. Optionally add a job description\n3. Choose an analysis type")

    # File uploads
    col1, col2 = st.columns(2)
    with col1:
        resume_files = st.file_uploader("Upload Resume(s)", type=["txt", "md", "text"], accept_multiple_files=True)
    with col2:
        jd_file = st.file_uploader("Upload Job Description (optional)", type=["txt", "md", "text"])

    jd_text = jd_file.getvalue().decode("utf-8") if jd_file else None

    if not resume_files:
        st.info("👆 Upload a resume to get started.")
        return

    resume_texts = {f.name: f.getvalue().decode("utf-8") for f in resume_files}

    tabs = st.tabs(["📊 Analysis", "🎯 JD Score", "🤖 ATS Score", "💡 Suggestions", "📊 Comparison"])

    # Analysis Tab
    with tabs[0]:
        st.header("General Resume Analysis")
        for name, text in resume_texts.items():
            with st.expander(f"📄 {name}", expanded=len(resume_texts) == 1):
                if st.button(f"Analyze {name}", key=f"analyze_{name}"):
                    with st.spinner("Analyzing resume..."):
                        result = analyze_resume(text, config)

                    score = result.get("overall_score", 0)
                    st.metric("Overall Score", f"{score}/100")
                    st.progress(score / 100)

                    c1, c2 = st.columns(2)
                    with c1:
                        st.subheader("✅ Strengths")
                        for s in result.get("strengths", []):
                            st.markdown(f"- {s}")
                    with c2:
                        st.subheader("⚠️ Weaknesses")
                        for w in result.get("weaknesses", []):
                            st.markdown(f"- {w}")

                    st.subheader("🛠️ Skills")
                    st.write(", ".join(result.get("skills", [])))

    # JD Score Tab
    with tabs[1]:
        st.header("Job Description Scoring")
        if not jd_text:
            st.info("Upload a job description to enable scoring.")
        else:
            for name, text in resume_texts.items():
                if st.button(f"Score {name}", key=f"score_{name}"):
                    with st.spinner("Scoring against JD..."):
                        result = score_against_jd(text, jd_text, config)

                    match_pct = result.get("match_percentage", 0)
                    st.metric("Match Score", f"{match_pct}%")
                    st.progress(match_pct / 100)

                    c1, c2 = st.columns(2)
                    with c1:
                        st.subheader("✅ Matching Skills")
                        for s in result.get("matching_skills", []):
                            st.markdown(f"- {s}")
                    with c2:
                        st.subheader("❌ Missing Skills")
                        for s in result.get("missing_skills", []):
                            st.markdown(f"- {s}")

    # ATS Tab
    with tabs[2]:
        st.header("ATS Score Simulation")
        if not jd_text:
            st.info("Upload a job description to enable ATS simulation.")
        else:
            for name, text in resume_texts.items():
                if st.button(f"ATS Score {name}", key=f"ats_{name}"):
                    with st.spinner("Simulating ATS evaluation..."):
                        result = simulate_ats_score(text, jd_text, config)

                    ats_score = result.get("ats_score", 0)
                    st.metric("ATS Score", f"{ats_score}/100")

                    cols = st.columns(4)
                    for col, (key, label) in zip(cols, [
                        ("keyword_match_score", "Keywords"),
                        ("experience_match_score", "Experience"),
                        ("education_match_score", "Education"),
                        ("formatting_score", "Formatting"),
                    ]):
                        col.metric(label, f"{result.get(key, 0)}%")

    # Suggestions Tab
    with tabs[3]:
        st.header("Improvement Suggestions")
        for name, text in resume_texts.items():
            if st.button(f"Get Suggestions for {name}", key=f"improve_{name}"):
                with st.spinner("Generating suggestions..."):
                    result = generate_improvement_suggestions(text, config)

                for section in ["summary_section", "experience_section", "skills_section", "education_section"]:
                    data = result.get(section, {})
                    if data:
                        with st.expander(section.replace("_", " ").title()):
                            st.markdown(f"**Assessment:** {data.get('current_assessment', 'N/A')}")
                            for s in data.get("suggestions", []):
                                st.markdown(f"- {s}")

    # Comparison Tab
    with tabs[4]:
        st.header("Resume Comparison")
        if len(resume_texts) >= 2:
            if st.button("Compare All Resumes"):
                with st.spinner("Comparing resumes..."):
                    texts_list = [(name, text) for name, text in resume_texts.items()]
                    result = compare_resumes(texts_list, jd_text, config)

                ranking = result.get("ranking", [])
                if ranking:
                    for r in ranking:
                        st.markdown(f"**{r.get('name', 'Unknown')}**: {r.get('score', 0)}/100 — {r.get('summary', '')}")
        else:
            st.info("Upload at least 2 resumes to enable comparison.")


if __name__ == "__main__":
    main()
