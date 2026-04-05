"""Streamlit web interface for Legal Document Summarizer."""

import sys
import os
import tempfile

import streamlit as st

from .config import load_config
from .core import (
    summarize_document,
    extract_clauses,
    score_risks,
    compare_documents,
    generate_export_markdown,
)
from .utils import read_document, get_llm_client


def check_ollama():
    """Check Ollama connectivity and display status."""
    _, _, check_ollama_running = get_llm_client()
    if not check_ollama_running():
        st.error("⚠️ Ollama is not running. Please start it with: `ollama serve`")
        st.stop()


def main():
    """Main Streamlit application."""
    st.set_page_config(page_title="Legal Document Summarizer", page_icon="📜", layout="wide")
    st.title("📜 Legal Document Summarizer")
    st.caption("Analyze legal documents, extract clauses, and assess risks using local LLM")

    config = load_config()
    check_ollama()

    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Settings")
        output_format = st.selectbox("Summary Format", ["bullet", "narrative", "detailed"])
        st.divider()
        st.markdown("**Model:** gemma4 (local via Ollama)")
        st.markdown(f"**Temperature:** {config['llm']['temperature']}")

    # File uploader
    uploaded_files = st.file_uploader(
        "Upload legal documents (PDF or text)",
        type=["txt", "text", "md", "pdf"],
        accept_multiple_files=True,
    )

    if not uploaded_files:
        st.info("👆 Upload one or more legal documents to get started.")
        return

    # Process each uploaded file
    tabs = st.tabs(["📋 Summary", "📄 Clauses", "⚠️ Risk Assessment", "📊 Comparison", "📥 Export"])

    file_texts = {}
    for uploaded_file in uploaded_files:
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        try:
            file_texts[uploaded_file.name] = read_document(tmp_path)
        except Exception as e:
            st.error(f"Error reading {uploaded_file.name}: {e}")
        finally:
            os.unlink(tmp_path)

    if not file_texts:
        return

    # Summary Tab
    with tabs[0]:
        st.header("Document Summary")
        for name, text in file_texts.items():
            with st.expander(f"📄 {name}", expanded=len(file_texts) == 1):
                if st.button(f"Summarize {name}", key=f"sum_{name}"):
                    with st.spinner("Analyzing document..."):
                        summary = summarize_document(text, output_format, config)
                    st.markdown(summary)

    # Clauses Tab
    with tabs[1]:
        st.header("Clause Extraction")
        for name, text in file_texts.items():
            with st.expander(f"📄 {name}", expanded=len(file_texts) == 1):
                if st.button(f"Extract Clauses from {name}", key=f"clause_{name}"):
                    with st.spinner("Extracting clauses..."):
                        result = extract_clauses(text, config)
                    st.markdown(result)

    # Risk Assessment Tab
    with tabs[2]:
        st.header("Risk Assessment")
        for name, text in file_texts.items():
            with st.expander(f"📄 {name}", expanded=len(file_texts) == 1):
                if st.button(f"Assess Risks in {name}", key=f"risk_{name}"):
                    with st.spinner("Analyzing risks..."):
                        result = score_risks(text, config)
                    st.markdown(result)

                    # Risk meter visualization
                    st.subheader("Risk Meter")
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Financial Risk", "See above")
                    col2.metric("Termination Risk", "See above")
                    col3.metric("IP Risk", "See above")

    # Comparison Tab
    with tabs[3]:
        st.header("Document Comparison")
        if len(file_texts) >= 2:
            if st.button("Compare All Documents"):
                temp_paths = []
                try:
                    for name, text in file_texts.items():
                        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as tmp:
                            tmp.write(text)
                            temp_paths.append(tmp.name)

                    with st.spinner("Comparing documents..."):
                        result = compare_documents(temp_paths, config)
                    st.markdown(result)
                finally:
                    for p in temp_paths:
                        os.unlink(p)
        else:
            st.info("Upload at least 2 documents to enable comparison.")

    # Export Tab
    with tabs[4]:
        st.header("Export Report")
        for name, text in file_texts.items():
            if st.button(f"Generate Report for {name}", key=f"export_{name}"):
                with st.spinner("Generating comprehensive report..."):
                    summary = summarize_document(text, "detailed", config)
                    clause_text = extract_clauses(text, config)
                    risk_text = score_risks(text, config)
                    md = generate_export_markdown(summary, clause_text, risk_text, name)

                st.download_button(
                    label=f"📥 Download {name} Report",
                    data=md,
                    file_name=f"{os.path.splitext(name)[0]}_report.md",
                    mime="text/markdown",
                    key=f"dl_{name}",
                )
                st.markdown(md)


if __name__ == "__main__":
    main()
