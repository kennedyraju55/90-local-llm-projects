"""Streamlit web interface for Medical Literature Summarizer."""

import streamlit as st
import os

from .config import load_config
from .core import (
    SECTIONS,
    summarize_paper,
    extract_pico,
    rate_evidence_quality,
    format_citation,
)
from .utils import get_llm_client, read_paper


def check_ollama():
    _, _, check_ollama_running = get_llm_client()
    if not check_ollama_running():
        st.error("⚠️ Ollama is not running. Please start it with: `ollama serve`")
        st.stop()


def main():
    st.set_page_config(page_title="Medical Literature Summarizer", page_icon="🔬", layout="wide")
    st.title("🔬 Medical Literature Summarizer")
    st.caption("Analyze medical & scientific papers with PICO framework, evidence rating, and citations")

    config = load_config()
    check_ollama()

    with st.sidebar:
        st.header("⚙️ Settings")
        detail_level = st.selectbox("Detail Level", ["brief", "standard", "comprehensive"])
        citation_style = st.selectbox("Citation Style", ["APA", "MLA", "Chicago", "Vancouver"])
        st.divider()
        st.markdown(f"**Model:** {config['llm']['model']}")

    uploaded_file = st.file_uploader("Upload medical/scientific paper", type=["txt", "md", "text"])

    if not uploaded_file:
        st.info("👆 Upload a paper to get started.")
        return

    paper_text = uploaded_file.getvalue().decode("utf-8")
    st.success(f"Loaded paper: {uploaded_file.name} ({len(paper_text):,} chars)")

    tabs = st.tabs(["📋 Summary", "🔬 PICO", "📊 Evidence", "📚 Citation"])

    # Summary Tab
    with tabs[0]:
        st.header("Structured Summary")
        if st.button("Generate Summary", key="gen_summary"):
            progress = st.progress(0)
            results = {}

            for i, (section_key, section_title, section_prompt) in enumerate(SECTIONS):
                with st.spinner(f"Extracting {section_title}..."):
                    from .core import extract_section
                    try:
                        results[section_key] = extract_section(
                            paper_text, section_key, section_prompt, detail_level, config
                        )
                    except Exception as e:
                        results[section_key] = f"Error: {e}"
                progress.progress((i + 1) / len(SECTIONS))

            for section_key, section_title, _ in SECTIONS:
                content = results.get(section_key, "N/A")
                with st.expander(f"{section_title}", expanded=True):
                    st.markdown(content)

    # PICO Tab
    with tabs[1]:
        st.header("PICO Framework Extraction")
        if st.button("Extract PICO", key="gen_pico"):
            with st.spinner("Extracting PICO elements..."):
                result = extract_pico(paper_text, config)

            for element, label in [("P", "Population"), ("I", "Intervention"),
                                   ("C", "Comparison"), ("O", "Outcome")]:
                st.subheader(f"**{element}** — {label}")

            st.markdown(result)

    # Evidence Tab
    with tabs[2]:
        st.header("Evidence Quality Rating")
        if st.button("Rate Evidence", key="gen_evidence"):
            with st.spinner("Rating evidence quality..."):
                result = rate_evidence_quality(paper_text, config)
            st.markdown(result)

    # Citation Tab
    with tabs[3]:
        st.header("Formatted Citation")
        if st.button(f"Generate {citation_style} Citation", key="gen_citation"):
            with st.spinner(f"Formatting {citation_style} citation..."):
                result = format_citation(paper_text, citation_style, config)
            st.code(result, language=None)
            st.button("📋 Copy", key="copy_citation")


if __name__ == "__main__":
    main()
