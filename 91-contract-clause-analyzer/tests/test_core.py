"""Tests for the Contract Clause Analyzer core module."""

import pytest
from unittest.mock import patch, MagicMock
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from contract_analyzer.core import (
    analyze_clause,
    analyze_contract,
    compare_clauses,
    get_risk_color,
    get_risk_emoji,
    _parse_json_response,
    ClauseAnalysis,
    ContractAnalysis,
    RiskLevel,
    ClauseType,
    SAMPLE_CLAUSES,
    LEGAL_DISCLAIMER,
)


class TestParseJsonResponse:
    """Tests for JSON response parsing."""

    def test_parse_valid_json(self):
        response = '{"clause_type": "termination", "risk_level": "medium"}'
        result = _parse_json_response(response)
        assert result["clause_type"] == "termination"
        assert result["risk_level"] == "medium"

    def test_parse_json_with_markdown_code_block(self):
        response = '```json\n{"clause_type": "termination"}\n```'
        result = _parse_json_response(response)
        assert result["clause_type"] == "termination"

    def test_parse_json_with_surrounding_text(self):
        response = 'Here is the analysis:\n{"clause_type": "warranty"}\nEnd of analysis.'
        result = _parse_json_response(response)
        assert result["clause_type"] == "warranty"

    def test_parse_invalid_json_returns_error(self):
        response = "This is not JSON at all"
        result = _parse_json_response(response)
        assert "error" in result or "raw_response" in result


class TestRiskHelpers:
    """Tests for risk level helper functions."""

    def test_get_risk_color_low(self):
        assert get_risk_color("low") == "green"

    def test_get_risk_color_medium(self):
        assert get_risk_color("medium") == "yellow"

    def test_get_risk_color_high(self):
        assert get_risk_color("high") == "red"

    def test_get_risk_color_critical(self):
        assert get_risk_color("critical") == "bold red"

    def test_get_risk_color_unknown(self):
        assert get_risk_color("unknown") == "white"

    def test_get_risk_emoji_low(self):
        assert get_risk_emoji("low") == "🟢"

    def test_get_risk_emoji_high(self):
        assert get_risk_emoji("high") == "🔴"

    def test_get_risk_emoji_critical(self):
        assert get_risk_emoji("critical") == "🚨"


class TestAnalyzeClause:
    """Tests for clause analysis with mocked LLM."""

    @patch("contract_analyzer.core.chat")
    def test_analyze_clause_returns_clause_analysis(self, mock_chat):
        mock_chat.return_value = json.dumps({
            "clause_type": "termination",
            "risk_level": "medium",
            "summary": "Standard termination clause with 30-day notice",
            "obligations": ["Provide 30 days written notice"],
            "deadlines": ["30 days notice period"],
            "red_flags": [],
            "recommendations": ["Consider adding cure period"],
            "key_terms": ["termination", "written notice"]
        })
        result = analyze_clause("Either party may terminate upon 30 days notice.")
        assert isinstance(result, ClauseAnalysis)
        assert result.clause_type == "termination"
        assert result.risk_level == "medium"
        assert len(result.obligations) == 1

    @patch("contract_analyzer.core.chat")
    def test_analyze_clause_high_risk(self, mock_chat):
        mock_chat.return_value = json.dumps({
            "clause_type": "non_compete",
            "risk_level": "high",
            "summary": "Overly broad non-compete clause",
            "obligations": ["Cannot compete for 5 years"],
            "deadlines": ["5 year restriction"],
            "red_flags": ["Excessive duration", "Overly broad geographic scope"],
            "recommendations": ["Negotiate shorter duration", "Limit geographic scope"],
            "key_terms": ["non-compete", "restriction"]
        })
        result = analyze_clause("Non-compete for 5 years worldwide.")
        assert result.risk_level == "high"
        assert len(result.red_flags) == 2

    @patch("contract_analyzer.core.chat")
    def test_analyze_clause_handles_malformed_response(self, mock_chat):
        mock_chat.return_value = "Not valid JSON response"
        result = analyze_clause("Some clause text")
        assert isinstance(result, ClauseAnalysis)
        assert result.clause_type == "other"


class TestAnalyzeContract:
    """Tests for full contract analysis with mocked LLM."""

    @patch("contract_analyzer.core.chat")
    def test_analyze_contract_returns_contract_analysis(self, mock_chat):
        mock_chat.return_value = json.dumps({
            "title": "Service Agreement",
            "overall_risk": "medium",
            "summary": "Standard service agreement",
            "clauses": [
                {
                    "clause_type": "termination",
                    "risk_level": "low",
                    "summary": "Standard termination",
                    "obligations": ["30 days notice"],
                    "deadlines": ["30 days"],
                    "red_flags": [],
                    "recommendations": [],
                    "key_terms": []
                },
                {
                    "clause_type": "indemnification",
                    "risk_level": "high",
                    "summary": "Broad indemnification",
                    "obligations": ["Full indemnification"],
                    "deadlines": [],
                    "red_flags": ["One-sided indemnification"],
                    "recommendations": ["Negotiate mutual indemnification"],
                    "key_terms": ["indemnify"]
                }
            ]
        })
        result = analyze_contract("Full contract text here.")
        assert isinstance(result, ContractAnalysis)
        assert result.title == "Service Agreement"
        assert result.total_clauses == 2
        assert result.high_risk_count == 1
        assert result.red_flags_count == 1


class TestCompareClause:
    """Tests for clause comparison with mocked LLM."""

    @patch("contract_analyzer.core.chat")
    def test_compare_clauses_returns_dict(self, mock_chat):
        mock_chat.return_value = json.dumps({
            "differences": ["Duration differs: 1 year vs 2 years"],
            "favorable_to_party_a": ["Shorter restriction period"],
            "favorable_to_party_b": ["Broader protection"],
            "negotiation_points": ["Agree on 18-month term"],
            "recommendation": "Negotiate a middle ground"
        })
        result = compare_clauses("Clause A text", "Clause B text")
        assert "differences" in result
        assert len(result["differences"]) == 1
        assert result["recommendation"] == "Negotiate a middle ground"


class TestDataStructures:
    """Tests for data classes and enums."""

    def test_risk_level_enum(self):
        assert RiskLevel.LOW == "low"
        assert RiskLevel.CRITICAL == "critical"

    def test_clause_type_enum(self):
        assert ClauseType.TERMINATION == "termination"
        assert ClauseType.INDEMNIFICATION == "indemnification"

    def test_clause_analysis_defaults(self):
        ca = ClauseAnalysis(clause_type="other", risk_level="low", summary="Test")
        assert ca.obligations == []
        assert ca.deadlines == []
        assert ca.red_flags == []

    def test_sample_clauses_exist(self):
        assert len(SAMPLE_CLAUSES) >= 3
        assert "indemnification" in SAMPLE_CLAUSES
        assert "termination" in SAMPLE_CLAUSES

    def test_legal_disclaimer_exists(self):
        assert "DISCLAIMER" in LEGAL_DISCLAIMER
        assert "privacy" in LEGAL_DISCLAIMER.lower() or "local" in LEGAL_DISCLAIMER.lower()
