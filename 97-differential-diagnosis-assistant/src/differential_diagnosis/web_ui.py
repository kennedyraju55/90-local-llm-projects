"""
Differential Diagnosis Assistant - Streamlit Web UI

A browser-based interface for AI-powered diagnostic reasoning with
ranked differentials, workup recommendations, and session tracking.

⚠️ MEDICAL DISCLAIMER: For EDUCATIONAL and INFORMATIONAL purposes ONLY.
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
    print("Then run: streamlit run src/differential_diagnosis/web_ui.py")
    sys.exit(1)

from differential_diagnosis.core import (
    DISCLAIMER,
    BODY_SYSTEMS,
    URGENCY_LABELS,
    assess_urgency,
    get_affected_systems,
    generate_differential,
    get_workup_recommendations,
    compare_diagnoses,
    DiagnosisSession,
    check_ollama_running,
)

# Custom CSS for professional dark theme
st.set_page_config(page_title="Differential Diagnosis Assistant", page_icon="🏥", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stApp { background: linear-gradient(180deg, #0e1117 0%, #1a1a2e 100%); }
    h1 { background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem !important; }
    h2 { color: #667eea !important; }
    h3 { color: #a78bfa !important; }
    .stButton>button { background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; border: none; border-radius: 8px; padding: 0.5rem 2rem; font-weight: 600; transition: transform 0.2s; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4); }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1a1a2e; border: 1px solid #333; color: #e0e0e0; border-radius: 8px; }
    .stSelectbox>div>div { background-color: #1a1a2e; border: 1px solid #333; }
    .stMetric { background: linear-gradient(135deg, #1a1a2e, #16213e); padding: 1rem; border-radius: 10px; border: 1px solid #333; }
    .css-1d391kg { background-color: #1a1a2e; }
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
    st.session_state.session = DiagnosisSession()
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# ---------------------------------------------------------------------------
# Top disclaimer banner
# ---------------------------------------------------------------------------

st.error(
    "⚠️ **MEDICAL DISCLAIMER** — This tool is for **EDUCATIONAL and INFORMATIONAL** "
    "purposes ONLY. It is **NOT** a substitute for professional medical advice, "
    "diagnosis, or treatment. **ALWAYS** consult a qualified healthcare provider. "
    "Call emergency services (911) for medical emergencies."
)

st.title("🏥 Differential Diagnosis Assistant")
st.caption("AI-powered diagnostic reasoning for educational purposes only")

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("⚙️ Options")

    # Body system filter
    selected_system = st.selectbox(
        "Filter by body system",
        options=["All Systems"] + list(BODY_SYSTEMS.keys()),
        format_func=lambda s: s.capitalize() if s != "All Systems" else s,
    )

    st.divider()

    show_history = st.checkbox("Show session history", value=True)

    st.divider()
    st.subheader("📊 Urgency Legend")
    for level in sorted(URGENCY_LABELS.keys()):
        label, advice = URGENCY_LABELS[level]
        st.write(f"**{label}** — {advice}")

    st.divider()
    st.subheader("🏥 Body Systems")
    for system, data in BODY_SYSTEMS.items():
        st.write(f"**{system.capitalize()}** — {data['description']}")

# ---------------------------------------------------------------------------
# Main area — Tabs for different functions
# ---------------------------------------------------------------------------

tab_diagnose, tab_workup, tab_compare = st.tabs([
    "🔍 Differential Diagnosis", "🧪 Workup Recommendations", "⚖️ Compare Diagnoses"
])

# ---------------------------------------------------------------------------
# Tab 1: Differential Diagnosis
# ---------------------------------------------------------------------------

with tab_diagnose:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("💬 Clinical Presentation")

        symptoms_input = st.text_area(
            "Presenting Symptoms:",
            height=100,
            placeholder="e.g., 45-year-old male with sudden onset chest pain radiating to left arm, diaphoresis...",
        )

        patient_info_input = st.text_area(
            "Patient Information (demographics, PMH, medications):",
            height=80,
            placeholder="e.g., 45M, HTN, DM2, smoker, on metformin and lisinopril...",
        )

        exam_findings_input = st.text_area(
            "Examination Findings:",
            height=80,
            placeholder="e.g., BP 160/95, HR 110, diaphoretic, S3 gallop, bilateral rales...",
        )

        combined_text = " ".join(filter(None, [symptoms_input, patient_info_input, exam_findings_input]))

        analyze_clicked = st.button("🔍 Generate Differential", type="primary", disabled=not symptoms_input.strip())

    with col2:
        st.subheader("📊 Urgency Assessment")

        if combined_text.strip():
            level, label, advice = assess_urgency(combined_text)
            systems = get_affected_systems(combined_text)

            st.metric("Urgency Level", label.split(" ", 1)[-1], delta=None)
            st.progress(level / 5)

            if level >= 4:
                st.error(f"**{label}**: {advice}")
            elif level >= 3:
                st.warning(f"**{label}**: {advice}")
            else:
                st.info(f"**{label}**: {advice}")

            st.write("**Affected systems:**")
            for s in systems:
                desc = BODY_SYSTEMS.get(s, {}).get("description", s)
                st.write(f"- 🗺️ **{s.capitalize()}** — {desc}")
        else:
            st.info("Enter symptoms to see urgency assessment")

    # Analysis
    if analyze_clicked and symptoms_input.strip():
        st.divider()
        st.subheader("🩺 AI Differential Diagnosis")

        if not check_ollama_running():
            st.error(
                "❌ **Ollama is not running.** Please start Ollama first with `ollama serve` "
                "and ensure the model is available (`ollama pull gemma4`)."
            )
        else:
            with st.spinner("Generating differential diagnosis with AI..."):
                try:
                    response = generate_differential(
                        symptoms_input, patient_info_input, exam_findings_input,
                        st.session_state.conversation,
                    )
                    st.markdown(response)

                    st.session_state.conversation.append({"role": "user", "content": combined_text})
                    st.session_state.conversation.append({"role": "assistant", "content": response})

                    level, label, advice = assess_urgency(combined_text)
                    systems = get_affected_systems(combined_text)
                    st.session_state.session.add_entry(
                        symptoms_input, patient_info_input, exam_findings_input,
                        level, systems, response,
                    )
                except Exception as exc:
                    st.error(f"❌ Analysis failed: {exc}")

# ---------------------------------------------------------------------------
# Tab 2: Workup Recommendations
# ---------------------------------------------------------------------------

with tab_workup:
    st.subheader("🧪 Workup Recommendations")
    workup_diagnosis = st.text_input(
        "Enter a diagnosis to get workup recommendations:",
        placeholder="e.g., Acute myocardial infarction",
    )
    workup_clicked = st.button("Get Workup", type="primary", disabled=not workup_diagnosis.strip(),
                                key="workup_btn")

    if workup_clicked and workup_diagnosis.strip():
        if not check_ollama_running():
            st.error("❌ **Ollama is not running.** Please start Ollama first.")
        else:
            with st.spinner("Generating workup recommendations..."):
                try:
                    response = get_workup_recommendations(workup_diagnosis)
                    st.markdown(response)
                except Exception as exc:
                    st.error(f"❌ Workup generation failed: {exc}")

# ---------------------------------------------------------------------------
# Tab 3: Compare Diagnoses
# ---------------------------------------------------------------------------

with tab_compare:
    st.subheader("⚖️ Compare Two Diagnoses")
    cmp_col1, cmp_col2 = st.columns(2)
    with cmp_col1:
        cmp_diag1 = st.text_input("Diagnosis 1:", placeholder="e.g., Pulmonary embolism")
    with cmp_col2:
        cmp_diag2 = st.text_input("Diagnosis 2:", placeholder="e.g., Pneumothorax")

    cmp_context = st.text_area(
        "Clinical Context (optional):",
        height=60,
        placeholder="e.g., Young female with sudden dyspnea and pleuritic chest pain...",
    )

    compare_clicked = st.button("Compare", type="primary",
                                 disabled=not (cmp_diag1.strip() and cmp_diag2.strip()),
                                 key="compare_btn")

    if compare_clicked and cmp_diag1.strip() and cmp_diag2.strip():
        if not check_ollama_running():
            st.error("❌ **Ollama is not running.** Please start Ollama first.")
        else:
            with st.spinner("Comparing diagnoses..."):
                try:
                    response = compare_diagnoses(cmp_diag1, cmp_diag2, cmp_context)
                    st.markdown(response)
                except Exception as exc:
                    st.error(f"❌ Comparison failed: {exc}")

# ---------------------------------------------------------------------------
# Session History
# ---------------------------------------------------------------------------

if show_history:
    entries = st.session_state.session.get_history()
    if entries:
        st.divider()
        st.subheader("📋 Session History")
        for i, entry in enumerate(reversed(entries), 1):
            urgency_label = URGENCY_LABELS.get(entry["urgency"], ("?", ""))[0]
            with st.expander(
                f"Consultation #{len(entries) - i + 1} — {urgency_label} — "
                f"{entry['symptoms'][:80]}{'...' if len(entry['symptoms']) > 80 else ''}"
            ):
                st.write(f"**Time:** {entry['timestamp'][:19]}")
                st.write(f"**Urgency:** {urgency_label}")
                st.write(f"**Systems:** {', '.join(entry['systems'])}")
                if entry.get("patient_info"):
                    st.write(f"**Patient Info:** {entry['patient_info']}")
                if entry.get("exam_findings"):
                    st.write(f"**Exam Findings:** {entry['exam_findings']}")
                st.markdown(entry["response"])

# ---------------------------------------------------------------------------
# Bottom disclaimer banner
# ---------------------------------------------------------------------------

st.divider()
st.warning(
    "⚠️ **REMINDER** — All information provided by this tool is for **EDUCATIONAL "
    "purposes ONLY**. Differential diagnoses are AI-generated hypotheses and must NOT "
    "be used for clinical decision-making. Always consult a qualified healthcare "
    "professional. If you are experiencing a medical emergency, "
    "**call emergency services immediately**."
)

st.caption("Part of the 90 Local LLM Projects collection • Powered by Ollama • 100% HIPAA-Friendly")
