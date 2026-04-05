"""Streamlit Web UI for Legal Brief Writer."""

import streamlit as st
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.brief_writer.core import (
    BriefType,
    CaseDetails,
    LEGAL_DISCLAIMER,
    BRIEF_TEMPLATES,
    write_brief,
    write_memorandum,
    write_irac_analysis,
    improve_legal_writing,
    format_brief_text,
    format_irac_text,
    display_brief_types,
)
from src.brief_writer.config import load_config
from common.llm_client import check_ollama_running

# ---------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="⚖️ Legal Brief Writer",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------------------------

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        color: #e0e0e0;
    }
    .main-header {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(90deg, #1a1a2e, #2d1b4e);
        border-radius: 12px;
        margin-bottom: 2rem;
        border: 1px solid #c9a84c;
    }
    .main-header h1 {
        color: #c9a84c;
        font-size: 2.2rem;
        margin-bottom: 0.3rem;
    }
    .main-header p {
        color: #a0a0b0;
        font-size: 1rem;
    }
    .privacy-badge {
        display: inline-block;
        background: #1b5e20;
        color: #a5d6a7;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }
    .stTextArea textarea {
        background-color: #1e1e2f;
        color: #e0e0e0;
        border: 1px solid #3a3a5c;
    }
    .section-output {
        background-color: #1e1e2f;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #c9a84c;
        margin-bottom: 1rem;
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #0f3460 100%);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.markdown("""
<div class="main-header">
    <h1>⚖️ Legal Brief Writer</h1>
    <p>AI-powered legal brief and memoranda generation</p>
    <span class="privacy-badge">🔒 100% Local • No Data Leaves Your Machine</span>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("⚙️ Settings")

    # Ollama status
    ollama_ok = check_ollama_running()
    if ollama_ok:
        st.success("✅ Ollama is running")
    else:
        st.error("❌ Ollama is not running. Start it with: `ollama serve`")

    config = load_config()

    model = st.text_input("Model", value=config.llm.model)
    temperature = st.slider("Temperature", 0.0, 1.0, config.llm.temperature, 0.1)
    max_tokens = st.number_input("Max Tokens", 1024, 16384, config.llm.max_tokens, 512)

    st.divider()
    st.header("📋 Case Details")
    case_name = st.text_input("Case Name", "Smith v. Jones")
    case_number = st.text_input("Case Number", "")
    court = st.text_input("Court", "")
    jurisdiction = st.text_input("Jurisdiction", "")
    client_position = st.selectbox("Client Position", ["Plaintiff", "Defendant", "Appellant", "Appellee", "Petitioner", "Respondent", ""])
    opposing_party = st.text_input("Opposing Party", "")

    st.divider()
    st.caption("⚖️ Legal Brief Writer v1.0.0")
    st.caption("All processing is 100% local")

case_details = CaseDetails(
    case_name=case_name,
    case_number=case_number,
    court=court,
    jurisdiction=jurisdiction,
    client_position=client_position,
    opposing_party=opposing_party,
)

# ---------------------------------------------------------------------------
# Main Content Tabs
# ---------------------------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "📝 Write Brief",
    "📋 Memorandum",
    "🔍 IRAC Analysis",
    "✍️ Improve Writing",
])

# ---------------------------------------------------------------------------
# Tab 1: Write Brief
# ---------------------------------------------------------------------------

with tab1:
    st.subheader("📝 Write a Legal Brief")

    col1, col2 = st.columns([1, 2])

    with col1:
        brief_type = st.selectbox(
            "Brief Type",
            [bt.value for bt in BriefType],
            format_func=lambda x: x.replace("_", " ").title(),
        )

        try:
            bt = BriefType(brief_type)
            template = BRIEF_TEMPLATES.get(bt, {})
            st.info(template.get("description", ""))
            st.caption(f"Sections: {', '.join(template.get('sections', []))}")
        except ValueError:
            pass

    with col2:
        facts = st.text_area(
            "Statement of Facts",
            height=200,
            placeholder="Enter the factual background of the case...",
        )
        issues = st.text_area(
            "Legal Issues",
            height=150,
            placeholder="Enter the legal issues to address...",
        )
        arguments = st.text_area(
            "Key Arguments",
            height=150,
            placeholder="Enter the key arguments to make...",
        )

    if st.button("⚖️ Generate Brief", type="primary", use_container_width=True):
        if not facts or not issues:
            st.warning("Please provide at least facts and issues.")
        else:
            with st.spinner("Generating brief with local LLM..."):
                result = write_brief(
                    brief_type=brief_type,
                    case_details=case_details,
                    facts=facts,
                    issues=issues,
                    arguments=arguments,
                    model=model,
                )

            st.success(f"✅ Brief generated! Word count: {result.word_count}")

            output_text = format_brief_text(result)

            for section in sorted(result.sections, key=lambda s: s.order):
                with st.expander(f"📄 {section.title}", expanded=True):
                    st.markdown(section.content)

            if result.legal_issues:
                st.subheader("Legal Issues Analysis")
                for i, li in enumerate(result.legal_issues, 1):
                    with st.expander(f"Issue {i}: {li.issue}"):
                        st.markdown(f"**Rule:** {li.rule}")
                        st.markdown(f"**Analysis:** {li.analysis}")
                        st.markdown(f"**Conclusion:** {li.conclusion}")

            if result.table_of_authorities:
                with st.expander("📚 Table of Authorities"):
                    for auth in result.table_of_authorities:
                        st.markdown(f"- {auth}")

            if result.warnings:
                st.warning("⚠️ Areas for Attorney Review:")
                for w in result.warnings:
                    st.markdown(f"- {w}")

            st.download_button(
                "📥 Download Brief",
                data=output_text,
                file_name=f"{brief_type}_brief.txt",
                mime="text/plain",
                use_container_width=True,
            )

# ---------------------------------------------------------------------------
# Tab 2: Memorandum
# ---------------------------------------------------------------------------

with tab2:
    st.subheader("📋 Write a Legal Memorandum")
    st.caption("Objective internal memo analyzing legal issues")

    question = st.text_area(
        "Question Presented",
        height=100,
        placeholder="State the legal question to be analyzed...",
    )
    memo_facts = st.text_area(
        "Statement of Facts",
        height=200,
        placeholder="Enter the relevant facts...",
        key="memo_facts",
    )

    if st.button("📋 Generate Memorandum", type="primary", use_container_width=True):
        if not question or not memo_facts:
            st.warning("Please provide the question presented and facts.")
        else:
            with st.spinner("Generating memorandum with local LLM..."):
                result = write_memorandum(
                    case_details=case_details,
                    question_presented=question,
                    facts=memo_facts,
                    model=model,
                )

            st.success(f"✅ Memorandum generated! Word count: {result.word_count}")

            output_text = format_brief_text(result)

            for section in sorted(result.sections, key=lambda s: s.order):
                with st.expander(f"📄 {section.title}", expanded=True):
                    st.markdown(section.content)

            st.download_button(
                "📥 Download Memorandum",
                data=output_text,
                file_name="legal_memorandum.txt",
                mime="text/plain",
                use_container_width=True,
            )

# ---------------------------------------------------------------------------
# Tab 3: IRAC Analysis
# ---------------------------------------------------------------------------

with tab3:
    st.subheader("🔍 IRAC Analysis")
    st.caption("Issue → Rule → Application → Conclusion")

    irac_issue = st.text_area(
        "Legal Issue",
        height=100,
        placeholder="State the legal issue to analyze...",
        key="irac_issue",
    )
    irac_facts = st.text_area(
        "Relevant Facts",
        height=200,
        placeholder="Enter the relevant facts...",
        key="irac_facts",
    )

    if st.button("🔍 Perform IRAC Analysis", type="primary", use_container_width=True):
        if not irac_issue or not irac_facts:
            st.warning("Please provide both the issue and facts.")
        else:
            with st.spinner("Performing IRAC analysis with local LLM..."):
                result = write_irac_analysis(
                    issue=irac_issue,
                    facts=irac_facts,
                    model=model,
                )

            st.success("✅ IRAC analysis complete!")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Issue")
                st.markdown(result.issue)
                st.markdown("### Rule")
                st.markdown(result.rule)
            with col2:
                st.markdown("### Application")
                st.markdown(result.analysis)
                st.markdown("### Conclusion")
                st.markdown(result.conclusion)

            output_text = format_irac_text(result)
            st.download_button(
                "📥 Download IRAC Analysis",
                data=output_text,
                file_name="irac_analysis.txt",
                mime="text/plain",
                use_container_width=True,
            )

# ---------------------------------------------------------------------------
# Tab 4: Improve Writing
# ---------------------------------------------------------------------------

with tab4:
    st.subheader("✍️ Improve Legal Writing")
    st.caption("Get AI-powered suggestions to improve your legal writing")

    writing_text = st.text_area(
        "Legal Text to Improve",
        height=300,
        placeholder="Paste your legal text here for improvement suggestions...",
        key="improve_text",
    )

    if st.button("✍️ Improve Writing", type="primary", use_container_width=True):
        if not writing_text:
            st.warning("Please provide text to improve.")
        else:
            with st.spinner("Analyzing and improving legal writing..."):
                result = improve_legal_writing(text=writing_text, model=model)

            st.success("✅ Writing improvement complete!")

            st.markdown("### Improved Text")
            st.markdown(result["improved_text"])

            col1, col2 = st.columns(2)

            with col1:
                if result.get("changes"):
                    st.markdown("### Changes Made")
                    for change in result["changes"]:
                        st.markdown(f"- {change}")

            with col2:
                if result.get("suggestions"):
                    st.markdown("### Suggestions")
                    for suggestion in result["suggestions"]:
                        st.markdown(f"- {suggestion}")

            st.metric("Readability Score", result.get("readability_score", "N/A"))

            if result.get("legal_accuracy_notes"):
                st.info(f"📝 Legal Accuracy Notes: {result['legal_accuracy_notes']}")

            st.download_button(
                "📥 Download Improved Text",
                data=result["improved_text"],
                file_name="improved_legal_text.txt",
                mime="text/plain",
                use_container_width=True,
            )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    <p>⚖️ Legal Brief Writer v1.0.0 | 🔒 100% Local Processing | Powered by Gemma 4 via Ollama</p>
    <p><strong>Disclaimer:</strong> This tool is for drafting assistance only. 
    All output must be reviewed by a licensed attorney.</p>
</div>
""", unsafe_allow_html=True)
