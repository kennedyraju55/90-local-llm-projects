"""
Clinical Note Generator - Streamlit Web UI

Browser-based interface for generating SOAP notes from encounter descriptions.

⚠️ MEDICAL DISCLAIMER: For EDUCATIONAL and INFORMATIONAL purposes ONLY.
"""

import sys
import os

_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

try:
    import streamlit as st
except ImportError:
    print("ERROR: Streamlit is not installed. Install with: pip install streamlit")
    sys.exit(1)

from clinical_note_generator.core import (
    DISCLAIMER,
    NOTE_TEMPLATES,
    SPECIALTY_PROMPTS,
    generate_soap_note,
    generate_note_section,
    refine_note,
    NoteSession,
)
from common.llm_client import check_ollama_running

st.set_page_config(page_title="Clinical Note Generator", page_icon="🏥", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%); }
    .stButton>button { background: linear-gradient(90deg, #667eea, #764ba2); color: white; border: none; border-radius: 25px; padding: 0.5rem 2rem; font-weight: bold; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(102,126,234,0.4); }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1e1e2e; color: #cdd6f4; border: 1px solid #45475a; }
    h1, h2, h3 { color: #cdd6f4 !important; }
    .stMarkdown { color: #bac2de; }
</style>
""", unsafe_allow_html=True)

if "note_session" not in st.session_state:
    st.session_state.note_session = NoteSession()

st.error(
    "⚠️ **MEDICAL DISCLAIMER** — This tool generates AI-assisted clinical note drafts for "
    "**EDUCATIONAL and INFORMATIONAL** purposes ONLY. All generated notes **MUST** be reviewed "
    "and approved by the treating physician before use in clinical documentation."
)

st.title("🏥 Clinical Note Generator")
st.caption("AI-Powered SOAP Note Generation • 100% Local • HIPAA-Friendly")

with st.sidebar:
    st.header("⚙️ Configuration")
    note_type = st.selectbox("Note Type", list(NOTE_TEMPLATES.keys()), format_func=lambda x: NOTE_TEMPLATES[x])
    specialty = st.selectbox("Specialty", list(SPECIALTY_PROMPTS.keys()), format_func=lambda x: x.replace("_", " ").title())

    st.divider()
    st.subheader("👤 Patient Demographics")
    patient_age = st.text_input("Age", placeholder="e.g., 45")
    patient_sex = st.selectbox("Sex", ["", "Male", "Female", "Other"])

    st.divider()
    st.subheader("📊 Session Stats")
    summary = st.session_state.note_session.get_summary()
    st.metric("Notes Generated", summary["total_notes"])

col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("📝 Encounter Description")
    encounter = st.text_area(
        "Describe the patient encounter:",
        height=200,
        placeholder="e.g., 55-year-old male presents with 3-day history of progressive chest pain, "
                    "worse with deep inspiration. Reports mild shortness of breath. No fever. "
                    "PMH: HTN, DM2. Vitals: BP 145/90, HR 88, RR 18, SpO2 96%...",
    )

    col_gen, col_section = st.columns(2)
    with col_gen:
        generate_full = st.button("📋 Generate Full SOAP Note", type="primary", disabled=not encounter)
    with col_section:
        section_choice = st.selectbox("Section", ["S", "O", "A", "P"], format_func=lambda x: {"S": "Subjective", "O": "Objective", "A": "Assessment", "P": "Plan"}[x])
        generate_section = st.button("📄 Generate Section", disabled=not encounter)

with col2:
    st.subheader("🏥 SOAP Reference")
    st.markdown("""
    **S - Subjective:** Chief complaint, HPI, ROS, PMH/PSH/FH/SH
    
    **O - Objective:** Vitals, PE findings, labs, imaging
    
    **A - Assessment:** Diagnosis, differentials, clinical reasoning
    
    **P - Plan:** Treatment, meds, follow-up, education, referrals
    """)

if generate_full and encounter:
    st.divider()
    st.subheader("📋 Generated SOAP Note")

    if not check_ollama_running():
        st.error("❌ Ollama is not running. Start with `ollama serve`.")
    else:
        demographics = {}
        if patient_age:
            demographics["age"] = patient_age
        if patient_sex:
            demographics["sex"] = patient_sex

        with st.spinner("Generating SOAP note..."):
            try:
                note = generate_soap_note(
                    encounter_description=encounter,
                    patient_demographics=demographics or None,
                    note_type=note_type,
                    specialty=specialty,
                )
                st.markdown(note)
                st.session_state.note_session.add_note(encounter, note, note_type, specialty)
                st.session_state.last_note = note
            except Exception as exc:
                st.error(f"❌ Generation failed: {exc}")

if generate_section and encounter:
    st.divider()
    section_names = {"S": "Subjective", "O": "Objective", "A": "Assessment", "P": "Plan"}
    st.subheader(f"📄 {section_names[section_choice]} Section")

    if not check_ollama_running():
        st.error("❌ Ollama is not running.")
    else:
        with st.spinner(f"Generating {section_names[section_choice]}..."):
            try:
                result = generate_note_section(encounter, section_choice)
                st.markdown(result)
            except Exception as exc:
                st.error(f"❌ Generation failed: {exc}")

if hasattr(st.session_state, "last_note") and st.session_state.last_note:
    st.divider()
    st.subheader("✏️ Refine Note")
    feedback = st.text_area("Enter feedback to refine the note:", height=100, placeholder="Add more detail to the Plan section...")
    if st.button("🔄 Refine Note") and feedback:
        with st.spinner("Refining note..."):
            try:
                refined = refine_note(st.session_state.last_note, feedback)
                st.markdown(refined)
                st.session_state.last_note = refined
            except Exception as exc:
                st.error(f"❌ Refinement failed: {exc}")

st.divider()
st.warning(
    "⚠️ **REMINDER** — All generated notes are AI-assisted drafts and **MUST** be reviewed by "
    "the treating physician. This tool does NOT replace clinical judgment. Never use AI-generated "
    "notes as final documentation without physician review and approval."
)
st.caption("Part of the 90 Local LLM Projects collection • 100% Local Processing • HIPAA-Friendly")
