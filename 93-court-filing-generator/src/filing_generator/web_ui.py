"""Streamlit Web UI for Court Filing Generator.

Provides an interactive web interface for generating court filings,
motions, and discovery requests using a local LLM.
"""

import sys
import os

import streamlit as st

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.filing_generator.core import (
    LEGAL_DISCLAIMER,
    CaseInfo,
    FilingType,
    FILING_TEMPLATES,
    generate_filing,
    generate_motion,
    generate_discovery_request,
    validate_filing,
)
from src.filing_generator.config import load_config
from common.llm_client import check_ollama_running

# ─── Page Configuration ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Court Filing Generator",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ──────────────────────────────────────────────────────────────────

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%);
    }
    .main-header {
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(90deg, #1a1a2e, #2d2d44, #1a1a2e);
        border-radius: 10px;
        margin-bottom: 1.5rem;
        border: 1px solid #c9a84c;
    }
    .main-header h1 {
        color: #c9a84c;
        font-size: 2.2rem;
        margin: 0;
    }
    .main-header p {
        color: #a0a0b0;
        font-size: 1rem;
    }
    .privacy-badge {
        display: inline-block;
        background: linear-gradient(90deg, #1b5e20, #2e7d32);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .filing-card {
        background: rgba(30, 30, 50, 0.8);
        border: 1px solid #c9a84c33;
        border-radius: 10px;
        padding: 1.2rem;
        margin: 0.5rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1a1a2e;
        border-radius: 5px;
        color: #c9a84c;
        border: 1px solid #c9a84c33;
    }
    .warning-box {
        background: rgba(201, 168, 76, 0.1);
        border: 1px solid #c9a84c;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ─── Header ──────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="main-header">
    <h1>⚖️ Court Filing Generator</h1>
    <p>AI-Powered Legal Document Drafting with Complete Privacy</p>
    <span class="privacy-badge">🔒 100% Local Processing — No Data Leaves Your Machine</span>
</div>
""", unsafe_allow_html=True)


# ─── Sidebar ─────────────────────────────────────────────────────────────────────

with st.sidebar:
    st.markdown("### ⚙️ Settings")

    config = load_config()

    model = st.selectbox(
        "LLM Model",
        ["gemma4:latest", "gemma4", "gemma3:latest", "llama3:latest"],
        index=0,
    )

    # Check Ollama
    ollama_status = check_ollama_running()
    if ollama_status:
        st.success("✅ Ollama is running")
    else:
        st.error("❌ Ollama is not running. Start with: `ollama serve`")

    st.markdown("---")
    st.markdown("### 📋 Filing Types")

    filing_type_options = {ft.value: FILING_TEMPLATES[ft]["title"] for ft in FilingType}

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color:#666; font-size:0.8rem;">
        <p>⚖️ Court Filing Generator v1.0.0</p>
        <p>🔒 Attorney-Client Privilege Preserved</p>
        <p>Powered by Gemma 4 via Ollama</p>
    </div>
    """, unsafe_allow_html=True)


# ─── Case Information Form ───────────────────────────────────────────────────────

def get_case_info_form(key_prefix: str = "") -> CaseInfo:
    """Render case info form and return CaseInfo."""
    st.markdown("#### 📋 Case Information")
    col1, col2 = st.columns(2)

    with col1:
        case_number = st.text_input("Case Number", value="2025-CV-", key=f"{key_prefix}_case_num")
        court = st.text_input(
            "Court",
            value=config.filing.default_court,
            key=f"{key_prefix}_court",
        )
        judge = st.text_input("Judge", placeholder="Hon. Judge Name", key=f"{key_prefix}_judge")

    with col2:
        plaintiff = st.text_input("Plaintiff", key=f"{key_prefix}_plaintiff")
        defendant = st.text_input("Defendant", key=f"{key_prefix}_defendant")
        jurisdiction = st.selectbox(
            "Jurisdiction",
            ["federal", "state"],
            key=f"{key_prefix}_jurisdiction",
        )

    return CaseInfo(
        case_number=case_number,
        court=court,
        parties={"plaintiff": plaintiff, "defendant": defendant},
        judge=judge,
        jurisdiction=jurisdiction,
    )


# ─── Tabs ────────────────────────────────────────────────────────────────────────

tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Generate Filing",
    "⚖️ Generate Motion",
    "🔍 Discovery Request",
    "✅ Validate Filing",
])


# ─── Tab 1: Generate Filing ─────────────────────────────────────────────────────

with tab1:
    st.markdown("### 📄 Generate Court Filing")

    case_info = get_case_info_form("filing")

    filing_type = st.selectbox(
        "Filing Type",
        options=[ft.value for ft in FilingType],
        format_func=lambda x: FILING_TEMPLATES.get(FilingType(x), {}).get("title", x),
    )

    # Show template info
    selected_template = FILING_TEMPLATES.get(FilingType(filing_type), {})
    if selected_template:
        st.info(f"📋 **Sections:** {', '.join(selected_template.get('sections', []))}")

    facts = st.text_area(
        "Statement of Facts",
        height=150,
        placeholder="Enter the relevant facts of the case...",
        key="filing_facts",
    )

    arguments = st.text_area(
        "Legal Arguments",
        height=150,
        placeholder="Enter your legal arguments and reasoning...",
        key="filing_arguments",
    )

    if st.button("⚖️ Generate Filing", type="primary", key="btn_filing"):
        if not ollama_status:
            st.error("Ollama is not running. Please start it first.")
        elif not case_info.case_number or not case_info.parties.get("plaintiff"):
            st.warning("Please fill in at least the case number and plaintiff.")
        else:
            with st.spinner("Generating filing... This may take a moment."):
                result = generate_filing(filing_type, case_info, facts, arguments, model)

            st.success(f"✅ Generated: {result.title}")

            st.text_area("Generated Document", value=result.content, height=500, key="filing_output")

            if result.warnings:
                st.markdown("#### ⚠️ Warnings")
                for warning in result.warnings:
                    st.warning(warning)

            st.download_button(
                label="📥 Download Filing",
                data=result.content,
                file_name=f"{filing_type}_{case_info.case_number}.txt",
                mime="text/plain",
            )


# ─── Tab 2: Generate Motion ─────────────────────────────────────────────────────

with tab2:
    st.markdown("### ⚖️ Generate Legal Motion")

    case_info_motion = get_case_info_form("motion")

    motion_type = st.selectbox(
        "Motion Type",
        options=[
            "motion_to_dismiss",
            "motion_for_summary_judgment",
            "motion_to_compel",
            "motion_in_limine",
        ],
        format_func=lambda x: x.replace("_", " ").title(),
        key="motion_type_select",
    )

    grounds = st.text_area(
        "Grounds for Motion",
        height=200,
        placeholder="Enter the legal grounds for this motion...",
        key="motion_grounds",
    )

    if st.button("⚖️ Generate Motion", type="primary", key="btn_motion"):
        if not ollama_status:
            st.error("Ollama is not running. Please start it first.")
        elif not grounds:
            st.warning("Please provide the grounds for the motion.")
        else:
            with st.spinner("Generating motion..."):
                result = generate_motion(motion_type, case_info_motion, grounds, model)

            st.success(f"✅ Generated: {result.title}")
            st.text_area("Generated Motion", value=result.content, height=500, key="motion_output")

            if result.warnings:
                for warning in result.warnings:
                    st.warning(warning)

            st.download_button(
                label="📥 Download Motion",
                data=result.content,
                file_name=f"{motion_type}_{case_info_motion.case_number}.txt",
                mime="text/plain",
            )


# ─── Tab 3: Discovery Request ───────────────────────────────────────────────────

with tab3:
    st.markdown("### 🔍 Generate Discovery Requests")

    case_info_disc = get_case_info_form("discovery")

    discovery_type = st.selectbox(
        "Discovery Type",
        ["interrogatories", "rfp", "rfa"],
        format_func=lambda x: {
            "interrogatories": "Interrogatories",
            "rfp": "Requests for Production",
            "rfa": "Requests for Admission",
        }.get(x, x),
        key="disc_type",
    )

    items_text = st.text_area(
        "Discovery Topics (one per line)",
        height=150,
        placeholder="Enter each discovery topic on a separate line...",
        key="disc_items",
    )

    if st.button("🔍 Generate Discovery", type="primary", key="btn_discovery"):
        if not ollama_status:
            st.error("Ollama is not running. Please start it first.")
        elif not items_text.strip():
            st.warning("Please enter at least one discovery topic.")
        else:
            items = [line.strip() for line in items_text.strip().split("\n") if line.strip()]
            with st.spinner("Generating discovery requests..."):
                result = generate_discovery_request(case_info_disc, discovery_type, items, model)

            st.success(f"✅ Generated: {result.title}")
            st.text_area("Generated Discovery", value=result.content, height=500, key="disc_output")

            if result.warnings:
                for warning in result.warnings:
                    st.warning(warning)

            st.download_button(
                label="📥 Download Discovery",
                data=result.content,
                file_name=f"discovery_{discovery_type}_{case_info_disc.case_number}.txt",
                mime="text/plain",
            )


# ─── Tab 4: Validate Filing ─────────────────────────────────────────────────────

with tab4:
    st.markdown("### ✅ Validate Court Filing")

    filing_text = st.text_area(
        "Paste Filing Text to Validate",
        height=300,
        placeholder="Paste the full text of a court filing to validate...",
        key="validate_text",
    )

    uploaded_file = st.file_uploader("Or upload a filing document", type=["txt", "md"], key="validate_upload")
    if uploaded_file is not None:
        filing_text = uploaded_file.getvalue().decode("utf-8")
        st.text_area("Uploaded Content", value=filing_text[:500] + "...", height=100, disabled=True)

    if st.button("✅ Validate Filing", type="primary", key="btn_validate"):
        if not ollama_status:
            st.error("Ollama is not running. Please start it first.")
        elif not filing_text.strip():
            st.warning("Please provide filing text to validate.")
        else:
            with st.spinner("Validating filing..."):
                result = validate_filing(filing_text, model)

            # Display results
            col1, col2, col3 = st.columns(3)
            with col1:
                is_valid = result.get("is_valid", False)
                st.metric("Valid", "✅ Yes" if is_valid else "❌ No")
            with col2:
                st.metric("Score", f"{result.get('score', 0)}/100")
            with col3:
                st.metric("Issues", len(result.get("issues", [])))

            if result.get("issues"):
                st.markdown("#### ❌ Issues Found")
                for issue in result["issues"]:
                    st.error(f"• {issue}")

            if result.get("missing_sections"):
                st.markdown("#### ⚠️ Missing Sections")
                for section in result["missing_sections"]:
                    st.warning(f"• {section}")

            if result.get("suggestions"):
                st.markdown("#### 💡 Suggestions")
                for suggestion in result["suggestions"]:
                    st.info(f"• {suggestion}")

            if result.get("citation_check"):
                st.markdown(f"#### 📚 Citation Check\n{result['citation_check']}")


# ─── Footer ─────────────────────────────────────────────────────────────────────

st.markdown("---")
st.markdown("""
<div style="text-align:center; padding:1rem; color:#666;">
    <p>⚖️ <strong>Court Filing Generator</strong> v1.0.0</p>
    <p>🔒 100% Local Processing — Attorney-Client Privilege Preserved</p>
    <p style="font-size:0.75rem; color:#999;">
        ⚠️ AI-generated documents must be reviewed by a licensed attorney before filing.
        This tool does not constitute legal advice.
    </p>
</div>
""", unsafe_allow_html=True)
