"""
Contract Clause Analyzer - Streamlit Web UI.

⚖️ LEGAL DISCLAIMER: This tool provides AI-assisted contract analysis for
informational purposes only. It is NOT legal advice.

🔒 PRIVACY: All processing happens locally. No data ever leaves your machine.
"""

import streamlit as st

st.set_page_config(page_title="Contract Clause Analyzer", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stApp { background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%); }
    h1 { background: linear-gradient(90deg, #d4a574 0%, #c9956c 50%, #b8860b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.5rem !important; }
    h2 { color: #d4a574 !important; }
    h3 { color: #c9956c !important; }
    .stButton>button { background: linear-gradient(90deg, #667eea, #764ba2); color: white; border: none; border-radius: 25px; padding: 0.5rem 2rem; font-weight: bold; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(102,126,234,0.4); }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1e1e2e; color: #cdd6f4; border: 1px solid #45475a; }
    h1, h2, h3 { color: #cdd6f4 !important; }
    .stMarkdown { color: #bac2de; }
    div[data-testid="stSidebar"] { background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%); }
    footer { visibility: hidden; }
    .risk-low { color: #a6e3a1; font-weight: bold; }
    .risk-medium { color: #f9e2af; font-weight: bold; }
    .risk-high { color: #f38ba8; font-weight: bold; }
    .risk-critical { color: #ff0000; font-weight: bold; animation: blink 1s infinite; }
    @keyframes blink { 50% { opacity: 0.5; } }
</style>
""", unsafe_allow_html=True)

from contract_analyzer.core import (
    LEGAL_DISCLAIMER,
    SAMPLE_CLAUSES,
    analyze_clause,
    analyze_contract,
    compare_clauses,
    get_risk_emoji,
    check_ollama_running,
)

st.title("⚖️ Contract Clause Analyzer")
st.markdown("**🔒 100% Local Processing • Zero Data Leakage • Attorney-Client Privilege Protected**")

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    model = st.selectbox("LLM Model", ["gemma4:latest", "gemma4", "llama3", "mistral"], index=0)
    
    st.markdown("---")
    st.markdown("### 📋 Sample Clauses")
    sample_choice = st.selectbox("Load a sample", ["(none)"] + list(SAMPLE_CLAUSES.keys()))
    
    st.markdown("---")
    st.markdown(
        "⚖️ **Legal Disclaimer**\n\n"
        "This tool is for informational purposes only. "
        "It is NOT legal advice."
    )
    st.markdown("🔒 **Privacy**: All data stays on your machine.")

# Check Ollama
if not check_ollama_running():
    st.error("⚠️ Ollama is not running. Start it with: `ollama serve`")
    st.stop()

tab1, tab2, tab3 = st.tabs(["📋 Clause Analysis", "📄 Full Contract", "🔍 Compare Clauses"])

with tab1:
    st.header("Analyze a Contract Clause")
    
    default_text = SAMPLE_CLAUSES.get(sample_choice, "") if sample_choice != "(none)" else ""
    clause_text = st.text_area("Paste contract clause here:", value=default_text, height=200, key="clause_input")
    
    if st.button("🔍 Analyze Clause", key="analyze_btn"):
        if clause_text.strip():
            with st.spinner("Analyzing clause..."):
                result = analyze_clause(clause_text, model=model)
            
            risk_emoji = get_risk_emoji(result.risk_level)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Clause Type", result.clause_type.replace("_", " ").title())
            with col2:
                st.metric("Risk Level", f"{risk_emoji} {result.risk_level.upper()}")
            with col3:
                st.metric("Red Flags", len(result.red_flags))
            
            st.markdown(f"**Summary:** {result.summary}")
            
            if result.obligations:
                st.markdown("#### 📌 Obligations")
                for ob in result.obligations:
                    st.markdown(f"- {ob}")
            
            if result.deadlines:
                st.markdown("#### ⏰ Deadlines")
                for dl in result.deadlines:
                    st.markdown(f"- {dl}")
            
            if result.red_flags:
                st.markdown("#### 🚩 Red Flags")
                for rf in result.red_flags:
                    st.error(rf)
            
            if result.recommendations:
                st.markdown("#### 💡 Recommendations")
                for rec in result.recommendations:
                    st.success(rec)
        else:
            st.warning("Please paste a contract clause to analyze.")

with tab2:
    st.header("Full Contract Analysis")
    contract_text = st.text_area("Paste full contract text:", height=300, key="contract_input")
    uploaded_file = st.file_uploader("Or upload a text file:", type=["txt"], key="contract_upload")
    
    if uploaded_file:
        contract_text = uploaded_file.read().decode("utf-8")
    
    if st.button("📄 Analyze Full Contract", key="full_btn"):
        if contract_text.strip():
            with st.spinner("Analyzing full contract..."):
                result = analyze_contract(contract_text, model=model)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Overall Risk", f"{get_risk_emoji(result.overall_risk)} {result.overall_risk.upper()}")
            with col2:
                st.metric("Total Clauses", result.total_clauses)
            with col3:
                st.metric("High Risk", result.high_risk_count)
            with col4:
                st.metric("Red Flags", result.red_flags_count)
            
            st.markdown(f"**{result.summary}**")
            
            for i, clause in enumerate(result.clause_analyses, 1):
                with st.expander(f"{get_risk_emoji(clause.risk_level)} Clause {i}: {clause.clause_type.replace('_', ' ').title()}"):
                    st.markdown(f"**Risk:** {clause.risk_level.upper()}")
                    st.markdown(f"**Summary:** {clause.summary}")
                    if clause.red_flags:
                        for rf in clause.red_flags:
                            st.error(rf)
                    if clause.recommendations:
                        for rec in clause.recommendations:
                            st.success(rec)
        else:
            st.warning("Please provide contract text.")

with tab3:
    st.header("Compare Two Clauses")
    col1, col2 = st.columns(2)
    with col1:
        clause_a = st.text_area("Clause A:", height=200, key="compare_a")
    with col2:
        clause_b = st.text_area("Clause B:", height=200, key="compare_b")
    
    if st.button("🔍 Compare", key="compare_btn"):
        if clause_a.strip() and clause_b.strip():
            with st.spinner("Comparing clauses..."):
                result = compare_clauses(clause_a, clause_b, model=model)
            
            if "differences" in result:
                st.markdown("#### 🔍 Key Differences")
                for diff in result.get("differences", []):
                    st.info(diff)
            
            if result.get("recommendation"):
                st.success(f"💡 **Recommendation:** {result['recommendation']}")
        else:
            st.warning("Please provide both clauses.")

st.markdown("---")
st.markdown("⚖️ *This tool is for informational purposes only. Not legal advice. Consult a qualified attorney.*")
