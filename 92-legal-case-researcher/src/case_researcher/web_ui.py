"""Streamlit Web UI for Legal Case Researcher.

Provides an interactive browser-based interface for legal research tasks.
All processing happens locally — no data leaves the machine.
"""

import os
import sys
import streamlit as st

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from common.llm_client import check_ollama_running, list_models
from src.case_researcher.core import (
    research_case_law,
    find_precedents,
    analyze_legal_argument,
    extract_citations,
    summarize_case,
    LEGAL_DISCLAIMER,
    SAMPLE_SCENARIOS,
    get_strength_emoji,
)

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Legal Case Researcher",
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
    }
    .main-header {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(90deg, #d4a574 0%, #c9956b 50%, #d4a574 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .privacy-badge {
        background: linear-gradient(135deg, #1b5e20, #2e7d32);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        text-align: center;
        font-size: 0.85rem;
        margin: 0.5rem 0;
    }
    .case-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(212, 165, 116, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .strength-strong { color: #4caf50; font-weight: bold; }
    .strength-moderate { color: #ff9800; font-weight: bold; }
    .strength-weak { color: #f44336; font-weight: bold; }
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(212, 165, 116, 0.2);
    }
    .disclaimer-box {
        background: rgba(244, 67, 54, 0.1);
        border: 1px solid rgba(244, 67, 54, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin-top: 1rem;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.markdown('<p class="main-header">⚖️ Legal Case Researcher</p>', unsafe_allow_html=True)
st.markdown(
    '<div style="text-align:center; color: #aaa; margin-bottom: 1.5rem;">'
    '🔒 100% Local • Zero Data Leakage • Attorney-Client Privilege Protected'
    '</div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("## ⚙️ Settings")

    # Connection status
    ollama_ok = check_ollama_running()
    if ollama_ok:
        st.success("✅ Ollama is running")
        available_models = list_models()
    else:
        st.error("❌ Ollama is not running")
        st.info("Start Ollama with: `ollama serve`")
        available_models = []

    model = st.selectbox(
        "🤖 Model",
        options=available_models if available_models else ["gemma4:latest"],
        index=0,
    )

    jurisdiction = st.selectbox(
        "📍 Jurisdiction",
        ["federal", "state", "all", "international"],
        index=0,
    )

    st.markdown("---")
    st.markdown(
        '<div class="privacy-badge">🔒 All data stays on your machine</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### 📚 Sample Scenarios")
    selected_sample = st.selectbox(
        "Load a sample",
        ["(none)"] + list(SAMPLE_SCENARIOS.keys()),
    )

    st.markdown("---")
    st.markdown(
        f'<div class="disclaimer-box">{LEGAL_DISCLAIMER}</div>',
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------

tab_research, tab_precedents, tab_analyze, tab_summarize = st.tabs([
    "🔍 Case Research",
    "📚 Find Precedents",
    "📋 Analyze Argument",
    "📄 Summarize Case",
])

# ---- Tab 1: Case Research --------------------------------------------------
with tab_research:
    st.subheader("🔍 Research Case Law")

    default_query = ""
    if selected_sample != "(none)" and selected_sample in SAMPLE_SCENARIOS:
        default_query = SAMPLE_SCENARIOS[selected_sample]["query"]

    query = st.text_area(
        "Enter your legal research question:",
        value=default_query,
        height=100,
        placeholder="e.g., What constitutes a material breach of contract?",
    )

    if st.button("🔍 Research", key="btn_research", type="primary"):
        if not query.strip():
            st.warning("Please enter a research question.")
        elif not ollama_ok:
            st.error("Ollama must be running to perform research.")
        else:
            with st.spinner("Researching case law..."):
                result = research_case_law(query, jurisdiction=jurisdiction, model=model)

            st.markdown("### 📋 Summary")
            st.info(result.summary)

            if result.relevant_cases:
                st.markdown("### 📚 Relevant Cases")
                for case in result.relevant_cases:
                    with st.expander(f"📖 {case.case_name} ({case.year})"):
                        col1, col2 = st.columns(2)
                        col1.markdown(f"**Citation:** {case.citation}")
                        col2.markdown(f"**Court:** {case.court}")
                        st.markdown(f"**Key Holding:** {case.key_holding}")
                        st.markdown(f"**Relevance:** {case.relevance}")

            if result.key_legal_principles:
                st.markdown("### ⚖️ Key Legal Principles")
                for p in result.key_legal_principles:
                    st.markdown(f"- {p}")

            if result.analysis:
                st.markdown("### 📝 Analysis")
                st.write(result.analysis)

            if result.suggested_search_terms:
                st.markdown("### 🔎 Suggested Search Terms")
                st.write(", ".join(result.suggested_search_terms))

# ---- Tab 2: Find Precedents ------------------------------------------------
with tab_precedents:
    st.subheader("📚 Find Legal Precedents")

    default_facts = ""
    default_issue = ""
    if selected_sample != "(none)" and selected_sample in SAMPLE_SCENARIOS:
        default_facts = SAMPLE_SCENARIOS[selected_sample].get("facts", "")
        default_issue = SAMPLE_SCENARIOS[selected_sample].get("query", "")

    case_facts = st.text_area(
        "Describe the case facts:",
        value=default_facts,
        height=120,
        placeholder="Describe the factual scenario...",
    )
    legal_issue = st.text_input(
        "Legal issue to research:",
        value=default_issue,
        placeholder="e.g., Breach of fiduciary duty",
    )

    if st.button("📚 Find Precedents", key="btn_precedents", type="primary"):
        if not case_facts.strip() or not legal_issue.strip():
            st.warning("Please provide both case facts and a legal issue.")
        elif not ollama_ok:
            st.error("Ollama must be running.")
        else:
            with st.spinner("Searching for precedents..."):
                results = find_precedents(case_facts, legal_issue, model=model)

            if not results:
                st.warning("No precedents found. Try rephrasing your query.")
            else:
                for p in results:
                    score_pct = f"{p.relevance_score:.0%}"
                    with st.expander(f"📖 {p.case_name} — Relevance: {score_pct}"):
                        st.markdown(f"**Citation:** {p.citation}")
                        st.markdown(f"**Factual Similarity:** {p.factual_similarity}")
                        st.markdown(f"**Legal Similarity:** {p.legal_similarity}")
                        st.markdown(f"**Recommendation:** {p.recommendation}")
                        if p.distinguishing_factors:
                            st.markdown("**Distinguishing Factors:**")
                            for df in p.distinguishing_factors:
                                st.markdown(f"- {df}")
                        if p.applicable_holdings:
                            st.markdown("**Applicable Holdings:**")
                            for ah in p.applicable_holdings:
                                st.markdown(f"- {ah}")

# ---- Tab 3: Analyze Argument -----------------------------------------------
with tab_analyze:
    st.subheader("📋 Analyze Legal Argument")

    argument_text = st.text_area(
        "Enter the legal argument to analyze:",
        height=150,
        placeholder="Paste or type a legal argument...",
    )

    if st.button("📋 Analyze", key="btn_analyze", type="primary"):
        if not argument_text.strip():
            st.warning("Please enter an argument to analyze.")
        elif not ollama_ok:
            st.error("Ollama must be running.")
        else:
            with st.spinner("Analyzing argument..."):
                result = analyze_legal_argument(argument_text, model=model)

            emoji = get_strength_emoji(result.strength)
            col1, col2, col3 = st.columns(3)
            col1.metric("Strength", f"{emoji} {result.strength.upper()}")
            col2.metric("Confidence", f"{result.confidence_score:.0%}")
            col3.metric("Doctrines", str(len(result.relevant_doctrines)))

            st.markdown("### Summary")
            st.write(result.argument_summary)

            left, right = st.columns(2)
            with left:
                if result.supporting_points:
                    st.markdown("### ✅ Supporting Points")
                    for sp in result.supporting_points:
                        st.markdown(f"- {sp}")
                if result.suggested_improvements:
                    st.markdown("### 💡 Improvements")
                    for si in result.suggested_improvements:
                        st.markdown(f"- {si}")
            with right:
                if result.weaknesses:
                    st.markdown("### ❌ Weaknesses")
                    for w in result.weaknesses:
                        st.markdown(f"- {w}")
                if result.counter_arguments:
                    st.markdown("### ⚔️ Counter Arguments")
                    for ca in result.counter_arguments:
                        st.markdown(f"- {ca}")

            if result.relevant_doctrines:
                st.markdown("### 📖 Relevant Legal Doctrines")
                for d in result.relevant_doctrines:
                    st.markdown(f"- {d}")

# ---- Tab 4: Summarize Case -------------------------------------------------
with tab_summarize:
    st.subheader("📄 Summarize Case Document")

    upload_method = st.radio("Input method:", ["📝 Paste text", "📁 Upload file"], horizontal=True)

    case_text = ""
    if upload_method == "📁 Upload file":
        uploaded = st.file_uploader("Upload a case document", type=["txt", "md", "pdf"])
        if uploaded is not None:
            case_text = uploaded.read().decode("utf-8", errors="replace")
            st.text_area("Preview:", value=case_text[:2000], height=150, disabled=True)
    else:
        case_text = st.text_area(
            "Paste the case text:",
            height=200,
            placeholder="Paste the full case text or a relevant excerpt...",
        )

    if st.button("📄 Summarize", key="btn_summarize", type="primary"):
        if not case_text.strip():
            st.warning("Please provide case text to summarize.")
        elif not ollama_ok:
            st.error("Ollama must be running.")
        else:
            with st.spinner("Summarizing case..."):
                result = summarize_case(case_text, model=model)

            if result.get("parse_error"):
                st.write(result.get("summary", ""))
            else:
                st.markdown("### 📋 Case Information")
                info_cols = st.columns(3)
                info_cols[0].markdown(f"**Case:** {result.get('case_name', 'N/A')}")
                info_cols[1].markdown(f"**Citation:** {result.get('citation', 'N/A')}")
                info_cols[2].markdown(f"**Date:** {result.get('date_decided', 'N/A')}")

                info_cols2 = st.columns(3)
                info_cols2[0].markdown(f"**Court:** {result.get('court', 'N/A')}")
                info_cols2[1].markdown(f"**Judge:** {result.get('judge', 'N/A')}")
                parties = result.get("parties", {})
                info_cols2[2].markdown(
                    f"**Plaintiff:** {parties.get('plaintiff', 'N/A')} vs "
                    f"**Defendant:** {parties.get('defendant', 'N/A')}"
                )

                for section, title, icon in [
                    ("facts", "Facts", "📝"),
                    ("holding", "Holding", "🔨"),
                    ("reasoning", "Reasoning", "💭"),
                    ("rule_of_law", "Rule of Law", "📖"),
                    ("significance", "Significance", "⭐"),
                    ("procedural_history", "Procedural History", "📜"),
                ]:
                    if result.get(section):
                        st.markdown(f"### {icon} {title}")
                        st.write(result[section])

                if result.get("issues"):
                    st.markdown("### ⚖️ Legal Issues")
                    for issue in result["issues"]:
                        st.markdown(f"- {issue}")

                if result.get("key_quotes"):
                    st.markdown("### 💬 Key Quotes")
                    for q in result["key_quotes"]:
                        st.markdown(f'> "{q}"')

                if result.get("dissent_summary"):
                    st.markdown("### 👎 Dissenting Opinion")
                    st.write(result["dissent_summary"])

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

st.markdown("---")
st.markdown(
    f'<div class="disclaimer-box">{LEGAL_DISCLAIMER}</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div style="text-align:center; color:#666; padding:1rem;">'
    '⚖️ Legal Case Researcher v1.0.0 • Powered by Gemma 4 via Ollama • 100% Local'
    '</div>',
    unsafe_allow_html=True,
)
