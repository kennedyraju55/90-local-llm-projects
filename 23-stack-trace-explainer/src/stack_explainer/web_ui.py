"""Streamlit web interface for Stack Explainer."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import streamlit as st

from .config import load_config, SUPPORTED_LANGUAGES
from .core import explain_trace, generate_fix_code, find_similar_errors
from .utils import detect_language, extract_error_type, COMMON_ERRORS


def run():
    """Launch the Streamlit web UI."""
    st.set_page_config(page_title="🔥 Stack Trace Explainer", page_icon="🔥", layout="wide")

    st.markdown("# 🔥 Stack Trace Explainer")
    st.markdown("*Understand stack traces and errors in plain English — with fix suggestions*")
    st.divider()

    config = load_config()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        config.model = st.text_input("Model", value=config.model)
        config.temperature = st.slider("Temperature", 0.0, 1.0, config.temperature, 0.1)
        config.max_tokens = st.number_input("Max Tokens", 512, 8192, config.max_tokens, 256)

        language_hint = st.selectbox("Language Hint", ["auto"] + SUPPORTED_LANGUAGES)
        if language_hint == "auto":
            language_hint = ""

        show_fix = st.checkbox("Generate Fix Code", value=True)
        show_similar = st.checkbox("Find Similar Errors", value=False)

        st.subheader("📚 Common Error Reference")
        ref_lang = st.selectbox("Language", list(COMMON_ERRORS.keys()))
        for err, desc in COMMON_ERRORS.get(ref_lang, {}).items():
            st.caption(f"**{err}**: {desc}")

    # Input
    tab_paste, tab_upload = st.tabs(["📋 Paste Trace", "📁 Upload File"])

    trace_text = ""

    with tab_paste:
        trace_text = st.text_area(
            "Paste your stack trace here:",
            height=300,
            placeholder='Traceback (most recent call last):\n  File "app.py", line 42, in main\n    result = process(data)\nKeyError: \'key\'',
        )

    with tab_upload:
        uploaded = st.file_uploader("Upload a file containing the stack trace", type=["txt", "log", "err"])
        if uploaded:
            trace_text = uploaded.read().decode("utf-8", errors="replace")
            st.code(trace_text[:2000])

    if st.button("🔥 Explain Error", type="primary", use_container_width=True):
        if not trace_text.strip():
            st.warning("Please paste or upload a stack trace first.")
            return

        # Quick analysis
        detected = detect_language(trace_text) if not language_hint else language_hint
        error_type = extract_error_type(trace_text)

        col1, col2 = st.columns(2)
        col1.metric("Language", detected if detected != "unknown" else "auto-detect")
        col2.metric("Error Type", error_type[:50] if error_type else "Unknown")

        with st.spinner("🔥 Analyzing stack trace..."):
            result = explain_trace(trace_text, language_hint, config)

        st.success("Analysis complete!")
        st.markdown("### 💡 Explanation")
        st.markdown(result["explanation"])

        if show_fix:
            with st.spinner("🔧 Generating fix code..."):
                fix = generate_fix_code(trace_text, result["explanation"], config)
            st.markdown("### 🔧 Suggested Fix")
            st.markdown(fix)

        if show_similar:
            with st.spinner("🔗 Finding similar errors..."):
                similar = find_similar_errors(trace_text, config)
            st.markdown("### 🔗 Related Errors")
            st.markdown(similar)

        st.download_button(
            "📥 Download Explanation",
            data=result["explanation"],
            file_name="error_explanation.md",
            mime="text/markdown",
        )


if __name__ == "__main__":
    run()
