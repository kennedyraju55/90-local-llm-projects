"""Streamlit web interface for API Doc Gen."""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import streamlit as st

from .config import load_config
from .core import generate_docs, generate_openapi, export_docs
from .utils import find_python_files, extract_functions, format_extracted_info


def run():
    """Launch the Streamlit web UI."""
    st.set_page_config(page_title="📚 API Doc Generator", page_icon="📚", layout="wide")

    st.markdown("# 📚 API Doc Generator")
    st.markdown("*Generate professional API documentation from Python source code*")
    st.divider()

    config = load_config()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        config.model = st.text_input("Model", value=config.model)
        config.temperature = st.slider("Temperature", 0.0, 1.0, config.temperature, 0.1)
        config.max_tokens = st.number_input("Max Tokens", 512, 8192, config.max_tokens, 256)
        gen_openapi = st.checkbox("Generate OpenAPI Spec", value=False)

    # Input tabs
    tab_upload, tab_path = st.tabs(["📁 Upload Files", "📂 Local Path"])

    source_code = ""
    source_name = "uploaded.py"

    with tab_upload:
        uploaded_files = st.file_uploader(
            "Upload Python files",
            type=["py"],
            accept_multiple_files=True,
        )
        if uploaded_files:
            for uf in uploaded_files:
                code = uf.read().decode("utf-8", errors="replace")
                st.expander(f"📄 {uf.name}").code(code, language="python")
                source_code += f"\n# --- File: {uf.name} ---\n{code}\n"
                source_name = uf.name

    with tab_path:
        source_path = st.text_input("Path to source file or directory:", placeholder="./src")
        if source_path and os.path.exists(source_path):
            files = find_python_files(source_path)
            st.info(f"Found {len(files)} Python file(s)")
            for f in files[:10]:
                st.caption(f"📄 {f}")

    if st.button("📚 Generate Documentation", type="primary", use_container_width=True):
        # Write uploaded code to temp location if needed
        if source_code:
            tmp_dir = os.path.join(os.path.dirname(__file__), "..", "..", ".tmp")
            os.makedirs(tmp_dir, exist_ok=True)
            tmp_path = os.path.join(tmp_dir, source_name)
            with open(tmp_path, "w", encoding="utf-8") as f:
                f.write(source_code)
            actual_path = tmp_path
        elif source_path and os.path.exists(source_path):
            actual_path = source_path
        else:
            st.warning("Please upload files or provide a valid path.")
            return

        try:
            with st.spinner("📚 Generating documentation..."):
                result = generate_docs(actual_path, config)

            col1, col2 = st.columns(2)
            col1.metric("Files Processed", len(result["files"]))
            col2.metric("Items Documented", result["items_count"])

            st.markdown("### 📚 API Documentation")
            st.markdown(result["docs"])

            col_dl1, col_dl2 = st.columns(2)
            with col_dl1:
                st.download_button(
                    "📥 Download as Markdown",
                    data=result["docs"],
                    file_name="api_docs.md",
                    mime="text/markdown",
                )

            if gen_openapi:
                with st.spinner("📄 Generating OpenAPI spec..."):
                    openapi_result = generate_openapi(actual_path, config)
                st.markdown("### 📄 OpenAPI Specification")
                st.code(openapi_result["openapi_yaml"], language="yaml")
                with col_dl2:
                    st.download_button(
                        "📥 Download OpenAPI YAML",
                        data=openapi_result["openapi_yaml"],
                        file_name="openapi.yaml",
                        mime="text/yaml",
                    )
        finally:
            if source_code:
                tmp_path = os.path.join(os.path.dirname(__file__), "..", "..", ".tmp", source_name)
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)


if __name__ == "__main__":
    run()
