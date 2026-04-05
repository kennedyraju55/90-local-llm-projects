"""Core business logic for Invoice Extractor."""

import csv
import io
import json
import logging
import os
from typing import Any

from .config import load_config
from .utils import get_llm_client, parse_llm_json, read_invoice_file

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """\
You are an expert invoice parser. Given the raw text of an invoice or receipt,
extract ALL relevant information and return it as a single valid JSON object.

Return ONLY the JSON object — no markdown fences, no commentary.

Use this exact schema:
{
  "vendor": {
    "name": "string",
    "address": "string or null",
    "phone": "string or null",
    "email": "string or null"
  },
  "invoice_number": "string or null",
  "date": "string (ISO 8601 preferred, e.g. 2024-01-15)",
  "due_date": "string or null",
  "line_items": [
    {
      "description": "string",
      "quantity": number,
      "unit_price": number,
      "total": number
    }
  ],
  "subtotal": number,
  "tax": number,
  "grand_total": number,
  "currency": "string (e.g. USD)",
  "payment_terms": "string or null"
}

Rules:
- Use numeric types for all monetary values (no currency symbols).
- If a field cannot be determined, use null.
- Quantities default to 1 when unspecified.
- Compute missing totals from quantity × unit_price when possible.
"""

CATEGORY_PROMPT = """Categorize each line item on this invoice into one of these categories:
{categories}

Return a JSON object with a key "categorized_items" containing a list of objects
with "description" and "category" keys.

Invoice data:
{invoice_json}"""


def extract_invoice_data(text: str, config: dict | None = None) -> dict:
    """Send invoice text to the LLM and parse the structured JSON response."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    messages = [
        {"role": "user", "content": f"Extract all data from this invoice:\n\n{text}"}
    ]

    response = chat(
        messages=messages,
        system_prompt=SYSTEM_PROMPT,
        temperature=cfg["llm"]["temperature"],
        max_tokens=cfg["llm"]["max_tokens"],
    )

    return parse_llm_json(response)


def batch_extract(file_paths: list[str], config: dict | None = None) -> list[dict]:
    """Extract data from multiple invoice files.

    Returns list of dicts with 'file', 'data' or 'error' keys.
    """
    results = []
    for filepath in file_paths:
        try:
            text = read_invoice_file(filepath)
            if not text.strip():
                results.append({"file": filepath, "error": "Empty file"})
                continue
            data = extract_invoice_data(text, config)
            data["_source_file"] = os.path.basename(filepath)
            results.append({"file": filepath, "data": data})
        except Exception as e:
            results.append({"file": filepath, "error": str(e)})
    return results


def detect_duplicates(invoices: list[dict], threshold: float = 0.9) -> list[tuple[int, int, str]]:
    """Detect potential duplicate invoices by invoice number and vendor.

    Returns list of (index1, index2, reason) tuples.
    """
    duplicates = []
    for i in range(len(invoices)):
        for j in range(i + 1, len(invoices)):
            d1 = invoices[i].get("data", {})
            d2 = invoices[j].get("data", {})

            if not d1 or not d2:
                continue

            # Check invoice number match
            inv1 = d1.get("invoice_number", "")
            inv2 = d2.get("invoice_number", "")
            if inv1 and inv2 and inv1 == inv2:
                duplicates.append((i, j, f"Same invoice number: {inv1}"))
                continue

            # Check vendor + total match
            v1 = d1.get("vendor", {}).get("name", "").lower()
            v2 = d2.get("vendor", {}).get("name", "").lower()
            t1 = d1.get("grand_total", 0)
            t2 = d2.get("grand_total", 0)
            if v1 and v2 and v1 == v2 and t1 == t2 and t1 > 0:
                duplicates.append((i, j, f"Same vendor ({v1}) and total ({t1})"))

    return duplicates


def categorize_items(invoice_data: dict, config: dict | None = None) -> dict:
    """Categorize invoice line items using the LLM."""
    cfg = config or load_config()
    chat, _, _ = get_llm_client()

    categories = ", ".join(cfg.get("categories", ["Other"]))
    invoice_json = json.dumps(invoice_data.get("line_items", []), indent=2)

    messages = [
        {"role": "user", "content": CATEGORY_PROMPT.format(
            categories=categories, invoice_json=invoice_json
        )}
    ]

    response = chat(
        messages=messages,
        system_prompt="You are an accounting expert. Categorize invoice items accurately.",
        temperature=0.1, max_tokens=2048,
    )

    return parse_llm_json(response)


def export_to_csv(invoices: list[dict]) -> str:
    """Export extracted invoice data to CSV format string."""
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "Source File", "Vendor", "Invoice #", "Date", "Due Date",
        "Description", "Qty", "Unit Price", "Line Total",
        "Subtotal", "Tax", "Grand Total", "Currency", "Payment Terms"
    ])

    for inv in invoices:
        data = inv.get("data", {})
        if not data:
            continue

        vendor = data.get("vendor", {}).get("name", "N/A")
        for item in data.get("line_items", []):
            writer.writerow([
                data.get("_source_file", ""),
                vendor,
                data.get("invoice_number", ""),
                data.get("date", ""),
                data.get("due_date", ""),
                item.get("description", ""),
                item.get("quantity", ""),
                item.get("unit_price", ""),
                item.get("total", ""),
                data.get("subtotal", ""),
                data.get("tax", ""),
                data.get("grand_total", ""),
                data.get("currency", ""),
                data.get("payment_terms", ""),
            ])

    return output.getvalue()
