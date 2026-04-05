"""
Lab Results Interpreter - Streamlit Web UI
Professional dark-themed interface for lab result analysis.
"""

import streamlit as st
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.lab_results_interpreter.core import (
    interpret_results,
    identify_abnormalities,
    suggest_followup_tests,
    explain_lab_value,
    display_disclaimer,
    LabSession,
    REFERENCE_RANGES,
    LAB_PANELS,
    DISCLAIMER,
)
from common.llm_client import check_ollama_running

# ─── Page Configuration ─────────────────────────────────────────────

st.set_page_config(
    page_title="Lab Results Interpreter",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Dark Theme CSS ──────────────────────────────────────────────────

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

# ─── Session State ───────────────────────────────────────────────────

if "lab_session" not in st.session_state:
    st.session_state.lab_session = LabSession()

# ─── Sidebar ─────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("## 🏥 Lab Results Interpreter")
    st.markdown("---")

    # Ollama status
    ollama_ok = check_ollama_running()
    if ollama_ok:
        st.success("✅ Ollama is running")
    else:
        st.error("❌ Ollama is not running")
        st.info("Start Ollama: `ollama serve`")

    st.markdown("---")

    # Panel selector
    panel_type = st.selectbox(
        "🧪 Lab Panel Type",
        options=["Auto-Detect"] + LAB_PANELS,
        index=0,
    )
    selected_panel = "" if panel_type == "Auto-Detect" else panel_type

    st.markdown("---")

    # Patient context
    patient_context = st.text_area(
        "👤 Patient Context (optional)",
        placeholder="e.g., 45-year-old male, on metformin, history of diabetes",
        height=100,
    )

    st.markdown("---")

    # Session info
    session = st.session_state.lab_session
    st.markdown(f"**Session Interpretations:** {len(session.get_history())}")

    if st.button("🗑️ Clear Session"):
        st.session_state.lab_session = LabSession()
        st.rerun()

    st.markdown("---")
    st.markdown("🔒 **100% Local Processing**")
    st.markdown("No data leaves your machine")

# ─── Main Content ────────────────────────────────────────────────────

st.markdown("# 🏥 Lab Results Interpreter")
st.markdown("### AI-Powered Laboratory Analysis — 100% HIPAA-Friendly")
st.markdown("---")

# Disclaimer
with st.expander("⚠️ Medical Disclaimer", expanded=False):
    st.warning(DISCLAIMER)

# ─── Tabs ────────────────────────────────────────────────────────────

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔬 Interpret Results",
    "🚨 Find Abnormalities",
    "📋 Follow-Up Tests",
    "📖 Explain Value",
    "📊 Reference Ranges",
])

# ─── Tab 1: Interpret Results ────────────────────────────────────────

with tab1:
    st.markdown("### Enter Lab Results")
    lab_results = st.text_area(
        "Paste your lab results here:",
        height=200,
        placeholder=(
            "e.g.,\n"
            "WBC: 12.5 x10^3/µL\n"
            "RBC: 4.8 x10^6/µL\n"
            "Hemoglobin: 11.2 g/dL\n"
            "Hematocrit: 34.1%\n"
            "Platelets: 180 x10^3/µL"
        ),
        key="interpret_input",
    )

    if st.button("🔬 Interpret Results", key="btn_interpret"):
        if lab_results.strip():
            with st.spinner("Analyzing lab results with Gemma 4..."):
                result = interpret_results(
                    lab_results_text=lab_results,
                    patient_context=patient_context,
                    panel_type=selected_panel,
                    conversation_history=session.conversation_history,
                )
            st.markdown("---")
            st.markdown("### 📋 Interpretation")
            st.markdown(result)

            session.add_interpretation(
                lab_results=lab_results,
                interpretation=result,
                panel_type=selected_panel,
                patient_context=patient_context,
            )
        else:
            st.warning("Please enter lab results to interpret.")

# ─── Tab 2: Abnormalities ───────────────────────────────────────────

with tab2:
    st.markdown("### Identify Abnormal Values")
    abnorm_results = st.text_area(
        "Paste your lab results here:",
        height=200,
        placeholder="Enter lab results to scan for abnormal values...",
        key="abnorm_input",
    )

    if st.button("🚨 Find Abnormalities", key="btn_abnorm"):
        if abnorm_results.strip():
            with st.spinner("Scanning for abnormalities..."):
                result = identify_abnormalities(
                    lab_results_text=abnorm_results,
                    panel_type=selected_panel,
                )
            st.markdown("---")
            st.markdown("### 🚨 Abnormal Values")
            st.markdown(result)
        else:
            st.warning("Please enter lab results to analyze.")

# ─── Tab 3: Follow-Up Tests ─────────────────────────────────────────

with tab3:
    st.markdown("### Suggest Follow-Up Tests")
    followup_results = st.text_area(
        "Paste your lab results here:",
        height=200,
        placeholder="Enter lab results to get follow-up recommendations...",
        key="followup_input",
    )
    clinical_context = st.text_input(
        "Clinical Context (optional)",
        placeholder="e.g., Patient reports fatigue and weight loss",
        key="clinical_ctx",
    )

    if st.button("📋 Get Recommendations", key="btn_followup"):
        if followup_results.strip():
            with st.spinner("Generating follow-up recommendations..."):
                result = suggest_followup_tests(
                    lab_results_text=followup_results,
                    clinical_context=clinical_context,
                )
            st.markdown("---")
            st.markdown("### 📋 Recommended Follow-Up Tests")
            st.markdown(result)
        else:
            st.warning("Please enter lab results to analyze.")

# ─── Tab 4: Explain Value ───────────────────────────────────────────

with tab4:
    st.markdown("### Explain a Lab Value")

    col1, col2, col3 = st.columns(3)
    with col1:
        test_name = st.text_input("Test Name", placeholder="e.g., Hemoglobin")
    with col2:
        test_value = st.text_input("Value", placeholder="e.g., 11.2")
    with col3:
        test_unit = st.text_input("Unit", placeholder="e.g., g/dL")

    if st.button("📖 Explain", key="btn_explain"):
        if test_name and test_value:
            with st.spinner(f"Explaining {test_name}..."):
                result = explain_lab_value(
                    test_name=test_name,
                    value=test_value,
                    unit=test_unit,
                )
            st.markdown("---")
            st.markdown(f"### 📖 {test_name} — {test_value} {test_unit}")
            st.markdown(result)
        else:
            st.warning("Please enter a test name and value.")

# ─── Tab 5: Reference Ranges ────────────────────────────────────────

with tab5:
    st.markdown("### Reference Ranges")

    ref_panel = st.selectbox(
        "Select Panel",
        options=list(REFERENCE_RANGES.keys()),
        key="ref_panel_select",
    )

    if ref_panel:
        st.markdown(f"#### 📊 {ref_panel} Reference Ranges")

        import pandas as pd
        data = []
        for test, info in REFERENCE_RANGES[ref_panel].items():
            data.append({
                "Test": test,
                "Description": info["description"],
                "Reference Range": info["range"],
                "Unit": info["unit"],
            })

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, hide_index=True)

# ─── Session History ─────────────────────────────────────────────────

st.markdown("---")
st.markdown("### 📜 Session History")

history = session.get_history()
if history:
    for i, entry in enumerate(reversed(history), 1):
        with st.expander(
            f"#{len(history) - i + 1} — {entry.get('panel_type', 'General')} "
            f"({entry['timestamp'][:19]})"
        ):
            st.markdown("**Lab Results:**")
            st.code(entry["lab_results"])
            st.markdown("**Interpretation:**")
            st.markdown(entry["interpretation"])
else:
    st.info("No interpretations yet. Enter lab results above to get started.")
