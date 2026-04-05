"""Tests for Invoice Extractor core logic."""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock
import click

from src.invoice_extractor.core import (
    extract_invoice_data, batch_extract, detect_duplicates, export_to_csv,
)
from src.invoice_extractor.utils import read_invoice_file, parse_llm_json
from src.invoice_extractor.config import load_config

SAMPLE_INVOICE = """\
ACME Corporation
123 Business Ave, New York, NY 10001

Invoice #: INV-2024-0042
Date: 2024-03-15
Due: 2024-04-15

Widget A   2   25.00   50.00
Widget B   5   10.00   50.00

Subtotal:  100.00
Tax (8%):    8.00
Total:     108.00

Payment Terms: Net 30
"""

SAMPLE_LLM_RESPONSE = json.dumps({
    "vendor": {"name": "ACME Corporation", "address": "123 Business Ave", "phone": None, "email": None},
    "invoice_number": "INV-2024-0042",
    "date": "2024-03-15",
    "due_date": "2024-04-15",
    "line_items": [
        {"description": "Widget A", "quantity": 2, "unit_price": 25.00, "total": 50.00},
        {"description": "Widget B", "quantity": 5, "unit_price": 10.00, "total": 50.00},
    ],
    "subtotal": 100.00,
    "tax": 8.00,
    "grand_total": 108.00,
    "currency": "USD",
    "payment_terms": "Net 30",
})


class TestReadInvoiceFile:
    def test_reads_existing(self, tmp_path):
        f = tmp_path / "inv.txt"
        f.write_text(SAMPLE_INVOICE, encoding="utf-8")
        assert "ACME" in read_invoice_file(str(f))

    def test_raises_on_missing(self):
        with pytest.raises(click.ClickException, match="File not found"):
            read_invoice_file("nonexistent.txt")


class TestParseLlmJson:
    def test_parses_clean_json(self):
        data = parse_llm_json(SAMPLE_LLM_RESPONSE)
        assert data["vendor"]["name"] == "ACME Corporation"

    def test_strips_fences(self):
        data = parse_llm_json(f"```json\n{SAMPLE_LLM_RESPONSE}\n```")
        assert data["grand_total"] == 108.00

    def test_raises_on_invalid(self):
        with pytest.raises(click.ClickException, match="Failed to parse"):
            parse_llm_json("not json")


class TestExtractInvoiceData:
    @patch("src.invoice_extractor.core.get_llm_client")
    def test_returns_structured_data(self, mock_get):
        mock_chat = MagicMock(return_value=SAMPLE_LLM_RESPONSE)
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        data = extract_invoice_data(SAMPLE_INVOICE)
        assert data["vendor"]["name"] == "ACME Corporation"
        assert data["grand_total"] == 108.00
        mock_chat.assert_called_once()

    @patch("src.invoice_extractor.core.get_llm_client")
    def test_low_temperature(self, mock_get):
        mock_chat = MagicMock(return_value=SAMPLE_LLM_RESPONSE)
        mock_get.return_value = (mock_chat, MagicMock(), MagicMock())

        extract_invoice_data("text")
        assert mock_chat.call_args.kwargs["temperature"] == 0.1


class TestDetectDuplicates:
    def test_detects_same_invoice_number(self):
        invoices = [
            {"file": "a.txt", "data": {"invoice_number": "INV-001", "vendor": {"name": "A"}, "grand_total": 100}},
            {"file": "b.txt", "data": {"invoice_number": "INV-001", "vendor": {"name": "A"}, "grand_total": 100}},
        ]
        dups = detect_duplicates(invoices)
        assert len(dups) == 1
        assert "INV-001" in dups[0][2]

    def test_no_duplicates(self):
        invoices = [
            {"file": "a.txt", "data": {"invoice_number": "INV-001", "vendor": {"name": "A"}, "grand_total": 100}},
            {"file": "b.txt", "data": {"invoice_number": "INV-002", "vendor": {"name": "B"}, "grand_total": 200}},
        ]
        assert detect_duplicates(invoices) == []


class TestExportToCsv:
    def test_export_format(self):
        invoices = [{"file": "test.txt", "data": json.loads(SAMPLE_LLM_RESPONSE)}]
        invoices[0]["data"]["_source_file"] = "test.txt"
        csv_data = export_to_csv(invoices)
        assert "ACME Corporation" in csv_data
        assert "Widget A" in csv_data


class TestConfig:
    def test_default_config(self):
        assert load_config()["llm"]["temperature"] == 0.1

    @patch.dict(os.environ, {"INVOICE_EXTRACTOR_MODEL": "llama3"})
    def test_env_override(self):
        assert load_config()["llm"]["model"] == "llama3"
