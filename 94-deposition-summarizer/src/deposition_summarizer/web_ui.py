"""Streamlit web interface for Deposition Summarizer."""

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from common.llm_client import check_ollama_running

from .config import load_config
from .core import (
    LEGAL_DISCLAIMER,
    SAMPLE_TRANSCRIPT,
    summarize_deposition,
    find_admissions,
    find_contradictions,
    extract_testimony,
    generate_follow_up_questions,
    get_significance_emoji,
)


def check_ollama():
    """Check Ollama connectivity and display status."""
    if not check_ollama_running():
        st.error("⚠️ Ollama is not running. Please start it with: `ollama serve`")
        st.stop()


def main():
    """Main Streamlit application."""
    st.set_page_config(page_title="Deposition Summarizer", page_icon="⚖️", layout="wide")

    # Custom CSS — dark theme with legal gold accents
    st.markdown("""
    <style>
        .main { background-color: #0e1117; }
        .stApp { background: linear-gradient(180deg, #0e1117 0%, #1a1a2e 100%); }
        h1 {
            background: linear-gradient(90deg, #d4a843 0%, #c49b3a 50%, #b8860b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem !important;
        }
        h2 { color: #d4a843 !important; }
        h3 { color: #c49b3a !important; }
        .stButton>button {
            background: linear-gradient(90deg, #d4a843 0%, #b8860b 100%);
            color: #1a1a2e;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 2rem;
            font-weight: 600;
            transition: transform 0.2s;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(212, 168, 67, 0.4);
        }
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #1a1a2e;
            border: 1px solid #333;
            color: #e0e0e0;
            border-radius: 8px;
        }
        .stSelectbox>div>div { background-color: #1a1a2e; border: 1px solid #333; }
        div[data-testid="stSidebar"] { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); }
        footer { visibility: hidden; }
        .block-container { padding-top: 2rem; }
        .admission-card {
            background: rgba(255, 193, 7, 0.1);
            border-left: 4px solid #ffc107;
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 0 8px 8px 0;
        }
        .contradiction-card {
            background: rgba(244, 67, 54, 0.1);
            border-left: 4px solid #f44336;
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 0 8px 8px 0;
        }
        .testimony-card {
            background: rgba(76, 175, 80, 0.1);
            border-left: 4px solid #4caf50;
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 0 8px 8px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.title("⚖️ Deposition Summarizer")
    st.caption("AI-powered deposition transcript analysis • 100% local processing • Attorney-client privilege protected")

    config = load_config()
    check_ollama()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        model = st.text_input("Model", value=config["llm"]["model"])
        witness_name = st.text_input("Witness Name (optional)", value="")
        st.divider()
        st.markdown("🔒 **100% Local Processing**")
        st.markdown("No data leaves your machine")
        st.markdown(f"**Model:** {model}")
        st.markdown(f"**Temperature:** {config['llm']['temperature']}")
        st.divider()
        if st.button("📋 Load Sample Transcript"):
            st.session_state["transcript_text"] = SAMPLE_TRANSCRIPT
        if st.button("⚖️ Legal Disclaimer"):
            st.session_state["show_disclaimer"] = True

    # Show disclaimer if requested
    if st.session_state.get("show_disclaimer"):
        st.warning(LEGAL_DISCLAIMER)
        if st.button("Dismiss"):
            st.session_state["show_disclaimer"] = False
            st.rerun()

    # Transcript input
    st.subheader("📄 Deposition Transcript")

    col1, col2 = st.columns([1, 1])
    with col1:
        uploaded_file = st.file_uploader("Upload transcript file", type=["txt", "text", "md"])
    with col2:
        st.markdown("**Or paste transcript below:**")

    transcript_text = ""
    if uploaded_file:
        transcript_text = uploaded_file.getvalue().decode("utf-8")
    else:
        transcript_text = st.text_area(
            "Paste deposition transcript",
            value=st.session_state.get("transcript_text", ""),
            height=200,
            placeholder="Paste the deposition transcript here...",
        )

    if not transcript_text.strip():
        st.info("👆 Upload a transcript file or paste text to get started. Use 'Load Sample' in the sidebar for a demo.")
        return

    st.success(f"✅ Transcript loaded: {len(transcript_text):,} characters")

    # Analysis tabs
    tabs = st.tabs([
        "📋 Full Summary",
        "🎯 Key Admissions",
        "⚡ Contradictions",
        "📄 Testimony",
        "❓ Follow-up Questions",
    ])

    # Full Summary tab
    with tabs[0]:
        st.header("Full Deposition Summary")
        if st.button("🔍 Generate Full Summary", key="btn_summary"):
            with st.spinner("Analyzing deposition with AI..."):
                summary = summarize_deposition(transcript_text, model)

            if summary.witness:
                st.markdown(f"**Witness:** {summary.witness}")
            if summary.date:
                st.markdown(f"**Date:** {summary.date}")

            if summary.overall_summary:
                st.subheader("Overview")
                st.markdown(summary.overall_summary)

            if summary.key_admissions:
                st.subheader("Key Admissions")
                for adm in summary.key_admissions:
                    emoji = get_significance_emoji(adm.significance)
                    st.markdown(
                        f'<div class="admission-card">{emoji} <strong>{adm.speaker}:</strong> '
                        f'{adm.statement} <em>[{adm.page_line}]</em> — {adm.significance}</div>',
                        unsafe_allow_html=True,
                    )

            if summary.contradictions:
                st.subheader("Contradictions")
                for con in summary.contradictions:
                    st.markdown(
                        f'<div class="contradiction-card">⚡ <strong>A:</strong> {con.statement_a}<br>'
                        f'<strong>B:</strong> {con.statement_b}<br>'
                        f'<em>{con.explanation}</em></div>',
                        unsafe_allow_html=True,
                    )

            if summary.topics_covered:
                st.subheader("Topics Covered")
                st.write(", ".join(summary.topics_covered))

            if summary.follow_up_questions:
                st.subheader("Suggested Follow-up Questions")
                for i, q in enumerate(summary.follow_up_questions, 1):
                    st.markdown(f"{i}. {q}")

    # Key Admissions tab
    with tabs[1]:
        st.header("Key Admissions")
        if st.button("🎯 Find Admissions", key="btn_admissions"):
            with st.spinner("Extracting key admissions..."):
                admissions = find_admissions(transcript_text, model)

            if not admissions:
                st.warning("No key admissions found.")
            else:
                for adm in admissions:
                    emoji = get_significance_emoji(adm.significance)
                    st.markdown(
                        f'<div class="admission-card">{emoji} <strong>{adm.speaker}:</strong> '
                        f'{adm.statement}<br><em>Ref: {adm.page_line} | '
                        f'Significance: {adm.significance}</em></div>',
                        unsafe_allow_html=True,
                    )

    # Contradictions tab
    with tabs[2]:
        st.header("Contradiction Detection")
        if st.button("⚡ Find Contradictions", key="btn_contradictions"):
            with st.spinner("Detecting contradictions..."):
                contras = find_contradictions(transcript_text, model)

            if not contras:
                st.warning("No contradictions found.")
            else:
                for i, con in enumerate(contras, 1):
                    st.markdown(
                        f'<div class="contradiction-card">'
                        f'<strong>Contradiction #{i}</strong><br>'
                        f'<strong>Statement A [{con.page_line_a}]:</strong> {con.statement_a}<br>'
                        f'<strong>Statement B [{con.page_line_b}]:</strong> {con.statement_b}<br>'
                        f'<em>Explanation: {con.explanation}</em></div>',
                        unsafe_allow_html=True,
                    )

    # Testimony tab
    with tabs[3]:
        st.header("Testimony Extraction")
        topic = st.text_input("Enter topic to search for:", placeholder="e.g., safety valve, pressure readings")
        if topic and st.button("📄 Extract Testimony", key="btn_testimony"):
            with st.spinner(f"Extracting testimony on '{topic}'..."):
                testimony_list = extract_testimony(transcript_text, topic, model)

            if not testimony_list:
                st.warning(f"No testimony found on topic: {topic}")
            else:
                for t in testimony_list:
                    emoji = get_significance_emoji(t.relevance)
                    st.markdown(
                        f'<div class="testimony-card">{emoji} <strong>{t.speaker}:</strong> '
                        f'{t.summary}<br><em>Ref: {t.page_line} | '
                        f'Relevance: {t.relevance}</em></div>',
                        unsafe_allow_html=True,
                    )

    # Follow-up Questions tab
    with tabs[4]:
        st.header("Follow-up Questions")
        if st.button("❓ Generate Questions", key="btn_followup"):
            with st.spinner("Generating follow-up questions..."):
                questions = generate_follow_up_questions(transcript_text, model)

            if not questions:
                st.warning("No follow-up questions generated.")
            else:
                for i, q in enumerate(questions, 1):
                    st.markdown(f"**{i}.** {q}")


if __name__ == "__main__":
    main()
