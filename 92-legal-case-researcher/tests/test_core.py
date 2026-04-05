"""Tests for Legal Case Researcher core module."""

import json
import pytest
from unittest.mock import patch, MagicMock
from dataclasses import asdict

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.case_researcher.core import (
    _parse_json_response,
    research_case_law,
    find_precedents,
    analyze_legal_argument,
    extract_citations,
    summarize_case,
    get_strength_color,
    get_strength_emoji,
    CaseReference,
    LegalArgument,
    ResearchResult,
    PrecedentAnalysis,
    LEGAL_DISCLAIMER,
    SAMPLE_SCENARIOS,
)


# ---------------------------------------------------------------------------
# JSON parsing tests
# ---------------------------------------------------------------------------

class TestParseJsonResponse:
    def test_valid_json(self):
        raw = '{"key": "value", "count": 42}'
        result = _parse_json_response(raw)
        assert result == {"key": "value", "count": 42}

    def test_json_with_code_fence(self):
        raw = '```json\n{"key": "value"}\n```'
        result = _parse_json_response(raw)
        assert result == {"key": "value"}

    def test_json_with_plain_code_fence(self):
        raw = '```\n{"key": "value"}\n```'
        result = _parse_json_response(raw)
        assert result == {"key": "value"}

    def test_invalid_json_fallback_to_brace(self):
        raw = 'Here is the result: {"key": "value"} and some extra text.'
        result = _parse_json_response(raw)
        assert result == {"key": "value"}

    def test_completely_invalid_json(self):
        raw = "This is not JSON at all."
        result = _parse_json_response(raw)
        assert result.get("parse_error") is True
        assert "raw_response" in result


# ---------------------------------------------------------------------------
# Helper function tests
# ---------------------------------------------------------------------------

class TestHelpers:
    def test_get_strength_color_strong(self):
        assert get_strength_color("strong") == "green"

    def test_get_strength_color_moderate(self):
        assert get_strength_color("moderate") == "yellow"

    def test_get_strength_color_weak(self):
        assert get_strength_color("weak") == "red"

    def test_get_strength_color_unknown(self):
        assert get_strength_color("unknown") == "white"

    def test_get_strength_emoji_strong(self):
        assert get_strength_emoji("strong") == "💪"

    def test_get_strength_emoji_moderate(self):
        assert get_strength_emoji("moderate") == "⚖️"

    def test_get_strength_emoji_weak(self):
        assert get_strength_emoji("weak") == "⚠️"

    def test_get_strength_emoji_unknown(self):
        assert get_strength_emoji("unknown") == "❓"


# ---------------------------------------------------------------------------
# Data structure tests
# ---------------------------------------------------------------------------

class TestDataStructures:
    def test_case_reference_defaults(self):
        ref = CaseReference()
        assert ref.case_name == ""
        assert ref.citation == ""
        assert ref.year == ""

    def test_legal_argument_defaults(self):
        arg = LegalArgument()
        assert arg.strength == "moderate"
        assert arg.confidence_score == 0.0
        assert arg.supporting_points == []

    def test_research_result_defaults(self):
        result = ResearchResult()
        assert result.query == ""
        assert result.relevant_cases == []

    def test_precedent_analysis_defaults(self):
        pa = PrecedentAnalysis()
        assert pa.relevance_score == 0.0
        assert pa.distinguishing_factors == []

    def test_case_reference_asdict(self):
        ref = CaseReference(case_name="Test v. Case", citation="123 U.S. 456")
        d = asdict(ref)
        assert d["case_name"] == "Test v. Case"
        assert d["citation"] == "123 U.S. 456"


# ---------------------------------------------------------------------------
# Mocked LLM research tests
# ---------------------------------------------------------------------------

MOCK_RESEARCH_RESPONSE = json.dumps({
    "summary": "Test summary",
    "relevant_cases": [
        {
            "case_name": "Smith v. Jones",
            "citation": "123 U.S. 456 (2020)",
            "year": "2020",
            "court": "Supreme Court",
            "jurisdiction": "federal",
            "relevance": "Directly on point",
            "key_holding": "Test holding",
        }
    ],
    "key_legal_principles": ["Principle A"],
    "suggested_search_terms": ["term1"],
    "analysis": "Test analysis",
})

MOCK_PRECEDENT_RESPONSE = json.dumps({
    "precedents": [
        {
            "case_name": "Alpha v. Beta",
            "citation": "789 F.2d 101",
            "relevance_score": 0.92,
            "factual_similarity": "Very similar facts",
            "legal_similarity": "Same legal issue",
            "distinguishing_factors": ["Factor X"],
            "applicable_holdings": ["Holding Y"],
            "recommendation": "Cite this case",
        }
    ]
})

MOCK_ANALYZE_RESPONSE = json.dumps({
    "argument_summary": "A strong argument",
    "strength": "strong",
    "supporting_points": ["Good point"],
    "weaknesses": ["Minor weakness"],
    "counter_arguments": ["Counter A"],
    "suggested_improvements": ["Improve X"],
    "relevant_doctrines": ["Res judicata"],
    "confidence_score": 0.85,
})

MOCK_CITATIONS_RESPONSE = json.dumps({
    "citations": [
        {
            "case_name": "Doe v. Roe",
            "citation": "456 U.S. 789",
            "year": "2019",
            "court": "Circuit Court",
            "jurisdiction": "federal",
            "relevance": "Cited for standard of review",
            "key_holding": "Established test",
        }
    ]
})

MOCK_SUMMARIZE_RESPONSE = json.dumps({
    "case_name": "Test v. Summary",
    "citation": "999 U.S. 1",
    "court": "Supreme Court",
    "date_decided": "2023-01-01",
    "judge": "Justice Test",
    "parties": {"plaintiff": "Test", "defendant": "Summary"},
    "procedural_history": "Appealed from district court",
    "facts": "Key facts here",
    "issues": ["Issue 1"],
    "holding": "Court held X",
    "reasoning": "Because of Y",
    "rule_of_law": "Rule Z",
    "significance": "Landmark decision",
    "key_quotes": ["Notable quote"],
    "dissent_summary": None,
})


class TestResearchCaseLaw:
    @patch("src.case_researcher.core.chat", return_value=MOCK_RESEARCH_RESPONSE)
    def test_research_returns_result(self, mock_chat):
        result = research_case_law("breach of contract")
        assert isinstance(result, ResearchResult)
        assert result.summary == "Test summary"
        assert len(result.relevant_cases) == 1
        assert result.relevant_cases[0].case_name == "Smith v. Jones"
        assert result.analysis == "Test analysis"
        mock_chat.assert_called_once()

    @patch("src.case_researcher.core.chat", return_value="Not valid JSON at all")
    def test_research_handles_bad_json(self, mock_chat):
        result = research_case_law("test query")
        assert isinstance(result, ResearchResult)
        assert "Not valid JSON" in result.summary


class TestFindPrecedents:
    @patch("src.case_researcher.core.chat", return_value=MOCK_PRECEDENT_RESPONSE)
    def test_find_precedents_returns_list(self, mock_chat):
        results = find_precedents("some facts", "legal issue")
        assert isinstance(results, list)
        assert len(results) == 1
        assert results[0].case_name == "Alpha v. Beta"
        assert results[0].relevance_score == 0.92

    @patch("src.case_researcher.core.chat", return_value="invalid")
    def test_find_precedents_handles_bad_json(self, mock_chat):
        results = find_precedents("facts", "issue")
        assert results == []


class TestAnalyzeLegalArgument:
    @patch("src.case_researcher.core.chat", return_value=MOCK_ANALYZE_RESPONSE)
    def test_analyze_returns_argument(self, mock_chat):
        result = analyze_legal_argument("test argument")
        assert isinstance(result, LegalArgument)
        assert result.strength == "strong"
        assert result.confidence_score == 0.85
        assert "Res judicata" in result.relevant_doctrines

    @patch("src.case_researcher.core.chat", return_value="not json")
    def test_analyze_handles_bad_json(self, mock_chat):
        result = analyze_legal_argument("test")
        assert isinstance(result, LegalArgument)


class TestExtractCitations:
    @patch("src.case_researcher.core.chat", return_value=MOCK_CITATIONS_RESPONSE)
    def test_extract_returns_citations(self, mock_chat):
        results = extract_citations("In Doe v. Roe, 456 U.S. 789...")
        assert isinstance(results, list)
        assert len(results) == 1
        assert results[0].case_name == "Doe v. Roe"

    @patch("src.case_researcher.core.chat", return_value="bad response")
    def test_extract_handles_bad_json(self, mock_chat):
        results = extract_citations("text")
        assert results == []


class TestSummarizeCase:
    @patch("src.case_researcher.core.chat", return_value=MOCK_SUMMARIZE_RESPONSE)
    def test_summarize_returns_dict(self, mock_chat):
        result = summarize_case("Full case text here...")
        assert isinstance(result, dict)
        assert result["case_name"] == "Test v. Summary"
        assert result["court"] == "Supreme Court"
        assert "Issue 1" in result["issues"]

    @patch("src.case_researcher.core.chat", return_value="not json")
    def test_summarize_handles_bad_json(self, mock_chat):
        result = summarize_case("text")
        assert result.get("parse_error") is True


# ---------------------------------------------------------------------------
# Constants / samples tests
# ---------------------------------------------------------------------------

class TestConstants:
    def test_disclaimer_not_empty(self):
        assert len(LEGAL_DISCLAIMER) > 0
        assert "DISCLAIMER" in LEGAL_DISCLAIMER

    def test_sample_scenarios_exist(self):
        assert len(SAMPLE_SCENARIOS) >= 3
        assert "contract_breach" in SAMPLE_SCENARIOS

    def test_sample_scenario_structure(self):
        for key, scenario in SAMPLE_SCENARIOS.items():
            assert "title" in scenario
            assert "query" in scenario
            assert "jurisdiction" in scenario
            assert "facts" in scenario
