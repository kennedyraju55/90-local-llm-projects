"""
Patient Intake Summarizer - Streamlit Web UI

A browser-based interface for patient intake form summarization with
categorized history extraction, risk factor identification, and session tracking.

⚠️ DISCLAIMER: AI-generated summaries require physician review before clinical use.
"""

import sys
import os

# Path setup for common module
_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

try:
    import streamlit as st
except ImportError:
    print("ERROR: Streamlit is not installed. Install it with: pip install streamlit")
    print("Then run: streamlit run src/patient_intake_summarizer/web_ui.py")
    sys.exit(1)

from patient_intake_summarizer.core import (
    DISCLAIMER,
    INTAKE_CATEGORIES,
    summarize_intake,
    extract_medical_history,
    generate_pre_visit_summary,
    identify_risk_factors,
    flag_missing_info,
    IntakeSession,
    check_ollama_running,
)

# Page config
st.set_page_config(page_title="Patient Intake Summarizer", page_icon="🏥", layout="wide")

# Custom CSS for professional dark theme
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%); }
    .stButton>button { background: linear-gradient(90deg, #667eea, #764ba2); color: white; border: none; border-radius: 25px; padding: 0.5rem 2rem; font-weight: bold; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(102,126,234,0.4); }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1e1e2e; color: #cdd6f4; border: 1px solid #45475a; }
    h1, h2, h3 { color: #cdd6f4 !important; }
    .stMarkdown { color: #bac2de; }
    .stSelectbox>div>div { background-color: #1e1e2e; border: 1px solid #45475a; }
    .stMetric { background: linear-gradient(135deg, #1a1a2e, #16213e); padding: 1rem; border-radius: 10px; border: 1px solid #45475a; }
    div[data-testid="stSidebar"] { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); }
    .stSuccess { background-color: rgba(102, 126, 234, 0.1); border: 1px solid #667eea; }
    footer { visibility: hidden; }
    .block-container { padding-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------

if "session" not in st.session_state:
    st.session_state.session = IntakeSession()
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# ---------------------------------------------------------------------------
# Top disclaimer banner
# ---------------------------------------------------------------------------

st.error(
    "⚠️ **CLINICAL DISCLAIMER** — AI-generated summaries are for **CLINICAL DECISION "
    "SUPPORT** only. All output **MUST** be reviewed and verified by a licensed physician. "
    "This tool runs **100% locally** — no patient data leaves this machine (HIPAA-friendly)."
)

st.title("🏥 Patient Intake Summarizer")
st.caption("AI-powered intake form summarization — 100% local, HIPAA-friendly")

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("⚙️ Options")

    summary_format = st.selectbox(
        "Summary Format",
        options=["structured", "brief", "detailed"],
        format_func=lambda x: {
            "structured": "📋 Structured (with headers)",
            "brief": "📝 Brief (3-5 sentences)",
            "detailed": "📖 Detailed (comprehensive)",
        }[x],
    )

    st.divider()

    st.subheader("🎯 Focus Areas")
    focus_areas: list[str] = []
    for cat_key, cat_desc in INTAKE_CATEGORIES.items():
        if st.checkbox(cat_desc.split("(")[0].strip(), key=f"focus_{cat_key}"):
            focus_areas.append(cat_key)

    st.divider()

    appointment_type = st.selectbox(
        "Appointment Type (for pre-visit)",
        options=["general", "follow-up", "specialist", "annual_physical", "urgent"],
        format_func=lambda x: x.replace("_", " ").title(),
    )

    st.divider()

    show_history = st.checkbox("Show session history", value=True)

    st.divider()
    st.subheader("📊 Intake Categories")
    for key, desc in INTAKE_CATEGORIES.items():
        st.write(f"**{key}** — {desc}")

# ---------------------------------------------------------------------------
# Main area
# ---------------------------------------------------------------------------

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📄 Patient Intake Form")

    intake_text = st.text_area(
        "Paste or type the patient intake form text:",
        height=250,
        placeholder=(
            "e.g., Patient: Jane Doe, 52F. Chief Complaint: Persistent lower back "
            "pain for 3 weeks. Medical History: Type 2 diabetes (diagnosed 2018), "
            "hypertension. Medications: Metformin 500mg BID, Lisinopril 10mg daily. "
            "Allergies: Penicillin (rash). Family History: Father — MI at age 60, "
            "Mother — breast cancer. Social: Non-smoker, occasional alcohol, works "
            "as an office manager..."
        ),
    )

with col2:
    st.subheader("📊 Quick Stats")

    if intake_text.strip():
        word_count = len(intake_text.split())
        char_count = len(intake_text)
        st.metric("Word Count", word_count)
        st.metric("Character Count", char_count)
        st.metric("Focus Areas", len(focus_areas) if focus_areas else "All")
        st.metric("Format", summary_format.title())
    else:
        st.info("Enter intake form text to see stats")

# ---------------------------------------------------------------------------
# Action buttons
# ---------------------------------------------------------------------------

st.divider()

btn_col1, btn_col2, btn_col3, btn_col4, btn_col5 = st.columns(5)

with btn_col1:
    summarize_clicked = st.button("📋 Summarize", type="primary", disabled=not intake_text.strip())
with btn_col2:
    extract_clicked = st.button("🔍 Extract History", disabled=not intake_text.strip())
with btn_col3:
    previsit_clicked = st.button("🩺 Pre-Visit", disabled=not intake_text.strip())
with btn_col4:
    risks_clicked = st.button("⚠️ Risk Factors", disabled=not intake_text.strip())
with btn_col5:
    missing_clicked = st.button("❓ Missing Info", disabled=not intake_text.strip())

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

if summarize_clicked and intake_text.strip():
    st.divider()
    st.subheader("📋 Clinical Summary")

    if not check_ollama_running():
        st.error(
            "❌ **Ollama is not running.** Please start Ollama first with `ollama serve` "
            "and ensure the model is available (`ollama pull gemma4`)."
        )
    else:
        with st.spinner("Generating clinical summary with AI..."):
            try:
                result = summarize_intake(
                    intake_text,
                    summary_format,
                    focus_areas or None,
                    st.session_state.conversation,
                )
                st.markdown(result)
                st.session_state.conversation.append({"role": "user", "content": intake_text})
                st.session_state.conversation.append({"role": "assistant", "content": result})
                st.session_state.session.add_summary(intake_text, result, summary_format, focus_areas)
            except Exception as exc:
                st.error(f"❌ Summarization failed: {exc}")

if extract_clicked and intake_text.strip():
    st.divider()
    st.subheader("🔍 Extracted Medical History")

    if not check_ollama_running():
        st.error("❌ **Ollama is not running.** Start with `ollama serve`.")
    else:
        with st.spinner("Extracting medical history categories..."):
            try:
                result = extract_medical_history(intake_text)
                for category, content in result.items():
                    with st.expander(f"📂 {category.replace('_', ' ').title()}", expanded=True):
                        st.write(str(content))
            except Exception as exc:
                st.error(f"❌ Extraction failed: {exc}")

if previsit_clicked and intake_text.strip():
    st.divider()
    st.subheader("🩺 Pre-Visit Summary")

    if not check_ollama_running():
        st.error("❌ **Ollama is not running.** Start with `ollama serve`.")
    else:
        with st.spinner("Generating pre-visit summary..."):
            try:
                intake_data = extract_medical_history(intake_text)
                result = generate_pre_visit_summary(intake_data, appointment_type)
                st.markdown(result)
            except Exception as exc:
                st.error(f"❌ Pre-visit summary failed: {exc}")

if risks_clicked and intake_text.strip():
    st.divider()
    st.subheader("⚠️ Risk Factors")

    if not check_ollama_running():
        st.error("❌ **Ollama is not running.** Start with `ollama serve`.")
    else:
        with st.spinner("Identifying risk factors..."):
            try:
                result = identify_risk_factors(intake_text)
                if result:
                    for r in result:
                        st.warning(f"⚠️ {r}")
                else:
                    st.success("No significant risk factors identified.")
            except Exception as exc:
                st.error(f"❌ Risk analysis failed: {exc}")

if missing_clicked and intake_text.strip():
    st.divider()
    st.subheader("❓ Missing Information")

    if not check_ollama_running():
        st.error("❌ **Ollama is not running.** Start with `ollama serve`.")
    else:
        with st.spinner("Checking for missing information..."):
            try:
                result = flag_missing_info(intake_text)
                if result:
                    for item in result:
                        st.info(f"❓ {item}")
                else:
                    st.success("✅ All standard intake categories appear complete.")
            except Exception as exc:
                st.error(f"❌ Missing info check failed: {exc}")

# ---------------------------------------------------------------------------
# Session history
# ---------------------------------------------------------------------------

if show_history:
    entries = st.session_state.session.get_summaries()
    if entries:
        st.divider()
        st.subheader("📋 Session History")
        for i, entry in enumerate(reversed(entries), 1):
            with st.expander(
                f"Summary #{len(entries) - i + 1} — {entry['summary_format']} — "
                f"{entry['intake_text'][:80]}{'...' if len(entry['intake_text']) > 80 else ''}"
            ):
                st.write(f"**Time:** {entry['timestamp'][:19]}")
                st.write(f"**Format:** {entry['summary_format']}")
                st.write(f"**Focus Areas:** {', '.join(entry['focus_areas']) if entry['focus_areas'] else 'All'}")
                st.markdown(entry["summary"])

# ---------------------------------------------------------------------------
# Bottom disclaimer
# ---------------------------------------------------------------------------

st.divider()
st.warning(
    "⚠️ **REMINDER** — All summaries generated by this tool are for **CLINICAL DECISION "
    "SUPPORT** only. They **MUST** be reviewed by a licensed physician. No patient data "
    "leaves this machine. If you have concerns about a patient, **consult with the "
    "attending physician immediately**."
)

st.caption("Part of the 90 Local LLM Projects collection • Powered by Ollama • 100% HIPAA-friendly")
