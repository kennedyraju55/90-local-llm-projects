"""Streamlit web interface for Meeting Summarizer."""

import streamlit as st
import os
import tempfile

from .config import load_config
from .core import (
    summarize_meeting,
    identify_speakers,
    extract_decision_log,
    generate_followup_reminders,
)
from .utils import get_llm_client, parse_action_items, extract_section


def check_ollama():
    _, _, check_ollama_running = get_llm_client()
    if not check_ollama_running():
        st.error("⚠️ Ollama is not running. Please start it with: `ollama serve`")
        st.stop()


def main():
    st.set_page_config(page_title="Meeting Summarizer", page_icon="📋", layout="wide")
    st.title("📋 Meeting Summarizer")
    st.caption("Extract insights from meeting transcripts using local LLM")

    config = load_config()
    check_ollama()

    with st.sidebar:
        st.header("⚙️ Settings")
        st.markdown(f"**Model:** {config['llm']['model']}")

    uploaded_file = st.file_uploader("Upload meeting transcript", type=["txt", "md", "text"])

    if not uploaded_file:
        st.info("👆 Upload a meeting transcript to get started.")
        return

    transcript = uploaded_file.getvalue().decode("utf-8")
    st.success(f"Loaded transcript: {uploaded_file.name} ({len(transcript)} chars)")

    tabs = st.tabs(["📋 Summary", "👥 Speakers", "✅ Decisions", "📝 Actions", "🔄 Follow-ups"])

    # Summary Tab
    with tabs[0]:
        st.header("Meeting Summary")
        if st.button("Generate Summary", key="gen_summary"):
            with st.spinner("Analyzing transcript..."):
                summary = summarize_meeting(transcript, config)

            st.session_state["summary"] = summary

            overall = extract_section(summary, "SUMMARY")
            st.markdown(f"### Overview\n{overall}")

            attendees = extract_section(summary, "ATTENDEES")
            st.markdown(f"### Attendees\n{attendees}")

            agenda = extract_section(summary, "AGENDA TOPICS")
            st.markdown(f"### Agenda\n{agenda}")

            st.download_button("📥 Download Summary", summary, f"{uploaded_file.name}_summary.md", "text/markdown")

    # Speakers Tab
    with tabs[1]:
        st.header("Speaker Identification")
        if st.button("Identify Speakers", key="gen_speakers"):
            with st.spinner("Identifying speakers..."):
                result = identify_speakers(transcript, config)
            st.markdown(result)

    # Decisions Tab
    with tabs[2]:
        st.header("Decision Log")
        if st.button("Extract Decisions", key="gen_decisions"):
            with st.spinner("Extracting decisions..."):
                result = extract_decision_log(transcript, config)
            st.markdown(result)

    # Actions Tab
    with tabs[3]:
        st.header("Action Items")
        summary = st.session_state.get("summary", "")
        if summary:
            items = parse_action_items(summary)
            if items:
                for item in items:
                    st.markdown(f"- **{item['who']}**: {item['what']} *(Due: {item['when']})*")
            else:
                st.info("No action items found. Generate a summary first.")
        else:
            st.info("Generate a summary first to extract action items.")

    # Follow-ups Tab
    with tabs[4]:
        st.header("Follow-up Reminders")
        if st.button("Generate Follow-ups", key="gen_followups"):
            with st.spinner("Generating follow-up schedule..."):
                result = generate_followup_reminders(transcript, config)
            st.markdown(result)


if __name__ == "__main__":
    main()
