"""Streamlit web interface for Commit Gen."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import streamlit as st

from .config import load_config, COMMIT_TYPES, COMMIT_EMOJIS
from .core import generate_commit_messages
from .utils import get_git_diff, get_git_stat, get_git_branch


def run():
    """Launch the Streamlit web UI."""
    st.set_page_config(page_title="📝 Commit Message Generator", page_icon="📝", layout="wide")

    st.markdown("# 📝 Commit Message Generator")
    st.markdown("*AI-powered conventional commit messages from git diffs*")
    st.divider()

    config = load_config()

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        config.model = st.text_input("Model", value=config.model)
        config.temperature = st.slider("Temperature", 0.0, 1.0, config.temperature, 0.1)
        config.num_suggestions = st.number_input("Number of Suggestions", 1, 10, config.num_suggestions)
        config.use_emoji = st.checkbox("Use Emoji Prefixes", value=config.use_emoji)

        st.subheader("Commit Type (optional)")
        msg_type = st.selectbox("Type", ["auto"] + COMMIT_TYPES)
        if msg_type == "auto":
            msg_type = ""

        st.subheader("🎨 Emoji Reference")
        for k, v in COMMIT_EMOJIS.items():
            st.text(f"{v}  {k}")

    # Input tabs
    tab_paste, tab_git = st.tabs(["📋 Paste Diff", "🔀 Git Integration"])

    diff_text = ""

    with tab_paste:
        diff_text = st.text_area(
            "Paste your git diff here:",
            height=350,
            placeholder="diff --git a/file.py b/file.py\n--- a/file.py\n+++ b/file.py\n@@ -1,3 +1,3 @@\n-old line\n+new line",
        )

    with tab_git:
        st.info("💡 Git integration reads from the repository where this app is running.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📥 Read Staged Changes"):
                diff_text = get_git_diff(staged_only=True)
                if diff_text:
                    st.text_area("Staged Diff:", value=diff_text, height=250, disabled=True)
                else:
                    st.warning("No staged changes found.")
        with col2:
            if st.button("📥 Read All Changes"):
                diff_text = get_git_diff(staged_only=False)
                if diff_text:
                    st.text_area("All Changes:", value=diff_text, height=250, disabled=True)
                else:
                    st.warning("No changes found.")

        branch = get_git_branch()
        stat = get_git_stat()
        if branch:
            st.caption(f"Branch: `{branch}`")
        if stat:
            st.code(stat)

    if st.button("✨ Generate Commit Messages", type="primary", use_container_width=True):
        if not diff_text.strip():
            st.warning("Please provide a diff (paste or read from git).")
            return

        with st.spinner("✨ Generating commit messages..."):
            result = generate_commit_messages(diff_text, msg_type, config)

        st.success("Generated!")
        st.markdown("### 💡 Suggested Commit Messages")
        st.markdown(result)

        st.download_button(
            "📥 Download Messages",
            data=result,
            file_name="commit_messages.txt",
            mime="text/plain",
        )


if __name__ == "__main__":
    run()
