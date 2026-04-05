"""Streamlit web interface for Code Reviewer."""

import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import streamlit as st

from .config import load_config
from .core import review_single_file, generate_autofix
from .utils import detect_language, SEVERITY_COLORS, CATEGORY_ICONS


def run():
    """Launch the Streamlit web UI."""
    st.set_page_config(page_title="🔍 Code Review Bot", page_icon="🔍", layout="wide")

    st.markdown("# 🔍 Code Review Bot")
    st.markdown("*AI-powered code review with severity scoring & auto-fix suggestions*")
    st.divider()

    config = load_config()

    # Sidebar settings
    with st.sidebar:
        st.header("⚙️ Settings")
        config.model = st.text_input("Model", value=config.model)
        config.temperature = st.slider("Temperature", 0.0, 1.0, config.temperature, 0.1)
        config.max_tokens = st.number_input("Max Tokens", 512, 8192, config.max_tokens, 256)
        focus_options = st.multiselect(
            "Focus Areas",
            ["BUG", "STYLE", "SECURITY", "PERFORMANCE", "BEST_PRACTICE"],
            default=[],
        )
        show_autofix = st.checkbox("Generate Auto-Fix", value=False)

    # Input tabs
    tab_editor, tab_upload = st.tabs(["📝 Code Editor", "📁 File Upload"])

    code_text = ""
    filename = "code.py"

    with tab_editor:
        language = st.selectbox("Language", ["python", "javascript", "typescript", "java", "go", "rust", "cpp", "ruby"])
        filename = st.text_input("Filename", value=f"example.{language[:2] if language != 'python' else 'py'}")
        code_text = st.text_area("Paste your code here:", height=400, placeholder="def hello():\n    print('world')")

    with tab_upload:
        uploaded = st.file_uploader("Upload a code file", type=["py", "js", "ts", "java", "go", "rs", "cpp", "c", "rb"])
        if uploaded:
            code_text = uploaded.read().decode("utf-8", errors="replace")
            filename = uploaded.name
            st.code(code_text, language=detect_language(filename))

    if st.button("🔍 Review Code", type="primary", use_container_width=True):
        if not code_text.strip():
            st.warning("Please paste or upload some code first.")
            return

        # Write to temp file for processing
        tmp_dir = os.path.join(os.path.dirname(__file__), "..", "..", ".tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        tmp_path = os.path.join(tmp_dir, filename)
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(code_text)

        try:
            with st.spinner("🔍 Analyzing code..."):
                result = review_single_file(tmp_path, focus_options, config)

            if result.get("error"):
                st.error(f"Error: {result['error']}")
                return

            # Display results
            st.success("Review complete!")
            col1, col2, col3 = st.columns(3)
            col1.metric("Language", result.get("language", "unknown"))
            col2.metric("Lines", result.get("lines", 0))
            col3.metric("Status", "✅ Reviewed")

            st.markdown("### 📋 Review Results")
            st.markdown(result["review"])

            if show_autofix:
                with st.spinner("🔧 Generating auto-fix..."):
                    fix = generate_autofix(tmp_path, result["review"], config)
                st.markdown("### 🔧 Auto-Fix Suggestions")
                st.markdown(fix)

            # Export
            st.download_button(
                "📥 Download Review Report",
                data=result["review"],
                file_name=f"review_{filename}.md",
                mime="text/markdown",
            )
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


if __name__ == "__main__":
    run()
