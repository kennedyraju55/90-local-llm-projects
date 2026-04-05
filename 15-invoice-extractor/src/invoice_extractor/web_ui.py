"""Streamlit web interface for Invoice Extractor."""

import streamlit as st
import json
import os
import tempfile

from .config import load_config
from .core import (
    extract_invoice_data,
    batch_extract,
    detect_duplicates,
    categorize_items,
    export_to_csv,
)
from .utils import get_llm_client, read_invoice_file


def check_ollama():
    _, _, check_ollama_running = get_llm_client()
    if not check_ollama_running():
        st.error("⚠️ Ollama is not running. Please start it with: `ollama serve`")
        st.stop()


def main():
    st.set_page_config(page_title="Invoice Extractor", page_icon="🧾", layout="wide")
    st.title("🧾 Invoice Extractor")
    st.caption("Extract structured data from invoices and receipts using local LLM")

    config = load_config()
    check_ollama()

    with st.sidebar:
        st.header("⚙️ Settings")
        output_format = st.selectbox("Output Format", ["Table", "JSON", "CSV"])
        st.divider()
        st.markdown(f"**Model:** {config['llm']['model']}")

    # Multi-file uploader
    uploaded_files = st.file_uploader(
        "Upload invoices", type=["txt", "text", "md"],
        accept_multiple_files=True,
    )

    if not uploaded_files:
        st.info("👆 Upload one or more invoice files to get started.")
        return

    tabs = st.tabs(["📊 Extracted Data", "🔍 Duplicates", "📁 Categories", "📥 Export"])

    # Process files
    if "invoice_results" not in st.session_state:
        st.session_state["invoice_results"] = {}

    # Extracted Data Tab
    with tabs[0]:
        st.header("Extracted Invoice Data")
        if st.button("Extract All", key="extract_all"):
            results = []
            for uploaded_file in uploaded_files:
                text = uploaded_file.getvalue().decode("utf-8")
                with st.spinner(f"Extracting {uploaded_file.name}..."):
                    try:
                        data = extract_invoice_data(text, config)
                        data["_source_file"] = uploaded_file.name
                        results.append({"file": uploaded_file.name, "data": data})
                        st.success(f"✓ {uploaded_file.name}")
                    except Exception as e:
                        results.append({"file": uploaded_file.name, "error": str(e)})
                        st.error(f"✗ {uploaded_file.name}: {e}")

            st.session_state["invoice_results"] = results

        results = st.session_state.get("invoice_results", [])
        for result in results:
            if "data" in result:
                data = result["data"]
                with st.expander(f"📄 {result['file']}", expanded=True):
                    vendor = data.get("vendor", {}).get("name", "Unknown")
                    total = data.get("grand_total", 0)
                    currency = data.get("currency", "USD")

                    c1, c2, c3 = st.columns(3)
                    c1.metric("Vendor", vendor)
                    c2.metric("Total", f"{total:.2f} {currency}")
                    c3.metric("Invoice #", data.get("invoice_number", "N/A"))

                    if data.get("line_items"):
                        st.table([
                            {
                                "Description": item.get("description", ""),
                                "Qty": item.get("quantity", 0),
                                "Unit Price": f"{item.get('unit_price', 0):.2f}",
                                "Total": f"{item.get('total', 0):.2f}",
                            }
                            for item in data["line_items"]
                        ])

    # Duplicates Tab
    with tabs[1]:
        st.header("Duplicate Detection")
        results = st.session_state.get("invoice_results", [])
        if results:
            duplicates = detect_duplicates(results)
            if duplicates:
                for i, j, reason in duplicates:
                    st.warning(f"⚠️ {results[i]['file']} ↔ {results[j]['file']}: {reason}")
            else:
                st.success("No duplicates detected!")
        else:
            st.info("Extract invoices first to check for duplicates.")

    # Categories Tab
    with tabs[2]:
        st.header("Category Tagging")
        results = st.session_state.get("invoice_results", [])
        for result in results:
            if "data" in result:
                if st.button(f"Categorize {result['file']}", key=f"cat_{result['file']}"):
                    with st.spinner("Categorizing..."):
                        cat_result = categorize_items(result["data"], config)
                    items = cat_result.get("categorized_items", [])
                    if items:
                        st.table(items)

    # Export Tab
    with tabs[3]:
        st.header("Export Data")
        results = st.session_state.get("invoice_results", [])
        if results:
            csv_data = export_to_csv(results)
            st.download_button("📥 Download CSV", csv_data, "invoices.csv", "text/csv")

            json_data = json.dumps([r.get("data", {}) for r in results if "data" in r], indent=2)
            st.download_button("📥 Download JSON", json_data, "invoices.json", "application/json")
        else:
            st.info("Extract invoices first to enable export.")


if __name__ == "__main__":
    main()
