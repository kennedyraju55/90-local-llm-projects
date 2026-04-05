"""Tests for Court Filing Generator core module."""

import json
import sys
import os
from unittest.mock import patch, MagicMock

import pytest

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.filing_generator.core import (
    LEGAL_DISCLAIMER,
    SYSTEM_PROMPT,
    FilingType,
    CaseInfo,
    FilingResult,
    FILING_TEMPLATES,
    SAMPLE_CASE_INFO,
    format_filing_header,
    generate_filing,
    generate_motion,
    generate_discovery_request,
    validate_filing,
    _parse_json_response,
)


# ─── Fixtures ────────────────────────────────────────────────────────────────────

@pytest.fixture
def sample_case_info() -> CaseInfo:
    """Provide a sample CaseInfo for testing."""
    return CaseInfo(
        case_number="2025-CV-99999",
        court="United States District Court for the Southern District of New York",
        parties={"plaintiff": "John Smith", "defendant": "BigCorp Inc."},
        judge="Hon. Jane Wilson",
        jurisdiction="federal",
        date_filed="2025-06-01",
    )


@pytest.fixture
def mock_llm_json_response() -> str:
    """Provide a mock JSON response from the LLM."""
    return json.dumps({
        "title": "Motion to Dismiss",
        "content": "IN THE UNITED STATES DISTRICT COURT...\n\nMOTION TO DISMISS\n\n1. Comes now the Defendant...",
        "sections": ["Caption", "Introduction", "Argument", "Conclusion"],
        "warnings": ["Review citations before filing"],
    })


# ─── Test FilingType Enum ────────────────────────────────────────────────────────

class TestFilingType:
    """Tests for the FilingType enum."""

    def test_filing_type_values(self) -> None:
        """All expected filing types exist."""
        expected = [
            "motion_to_dismiss",
            "motion_for_summary_judgment",
            "complaint",
            "answer",
            "motion_to_compel",
            "motion_in_limine",
            "subpoena",
            "discovery_request",
            "appellate_brief",
            "stipulation",
        ]
        actual = [ft.value for ft in FilingType]
        assert set(expected) == set(actual)

    def test_filing_type_is_string_enum(self) -> None:
        """FilingType values are strings."""
        for ft in FilingType:
            assert isinstance(ft.value, str)

    def test_filing_type_lookup(self) -> None:
        """Can look up FilingType by value."""
        ft = FilingType("motion_to_dismiss")
        assert ft == FilingType.MOTION_TO_DISMISS


# ─── Test CaseInfo Dataclass ─────────────────────────────────────────────────────

class TestCaseInfo:
    """Tests for the CaseInfo dataclass."""

    def test_case_info_creation(self, sample_case_info: CaseInfo) -> None:
        """CaseInfo can be created with all fields."""
        assert sample_case_info.case_number == "2025-CV-99999"
        assert sample_case_info.judge == "Hon. Jane Wilson"
        assert sample_case_info.jurisdiction == "federal"

    def test_case_info_parties(self, sample_case_info: CaseInfo) -> None:
        """CaseInfo parties dict is accessible."""
        assert sample_case_info.parties["plaintiff"] == "John Smith"
        assert sample_case_info.parties["defendant"] == "BigCorp Inc."

    def test_case_info_defaults(self) -> None:
        """CaseInfo has proper defaults."""
        ci = CaseInfo(
            case_number="TEST-001",
            court="Test Court",
            parties={"plaintiff": "A", "defendant": "B"},
        )
        assert ci.judge == ""
        assert ci.jurisdiction == "federal"
        assert ci.date_filed  # Should have a default date


# ─── Test format_filing_header ───────────────────────────────────────────────────

class TestFormatFilingHeader:
    """Tests for the format_filing_header function."""

    def test_header_contains_case_number(self, sample_case_info: CaseInfo) -> None:
        """Header contains the case number."""
        header = format_filing_header(sample_case_info)
        assert "2025-CV-99999" in header

    def test_header_contains_parties(self, sample_case_info: CaseInfo) -> None:
        """Header contains party names in uppercase."""
        header = format_filing_header(sample_case_info)
        assert "JOHN SMITH" in header
        assert "BIGCORP INC." in header

    def test_header_contains_court(self, sample_case_info: CaseInfo) -> None:
        """Header contains the court name."""
        header = format_filing_header(sample_case_info)
        assert "UNITED STATES DISTRICT COURT" in header

    def test_header_contains_judge(self, sample_case_info: CaseInfo) -> None:
        """Header contains the judge name."""
        header = format_filing_header(sample_case_info)
        assert "Hon. Jane Wilson" in header

    def test_header_without_judge(self) -> None:
        """Header works without a judge."""
        ci = CaseInfo(
            case_number="TEST-001",
            court="Test Court",
            parties={"plaintiff": "A", "defendant": "B"},
        )
        header = format_filing_header(ci)
        assert "TEST-001" in header


# ─── Test _parse_json_response ───────────────────────────────────────────────────

class TestParseJsonResponse:
    """Tests for the _parse_json_response helper."""

    def test_parse_plain_json(self) -> None:
        """Parse plain JSON string."""
        data = '{"title": "Test", "content": "Hello"}'
        result = _parse_json_response(data)
        assert result["title"] == "Test"

    def test_parse_json_with_code_fences(self) -> None:
        """Parse JSON wrapped in markdown code fences."""
        data = '```json\n{"title": "Test", "content": "Hello"}\n```'
        result = _parse_json_response(data)
        assert result["title"] == "Test"

    def test_parse_json_with_surrounding_text(self) -> None:
        """Parse JSON embedded in surrounding text."""
        data = 'Here is the result:\n{"title": "Test", "score": 85}\nEnd of response.'
        result = _parse_json_response(data)
        assert result["title"] == "Test"
        assert result["score"] == 85

    def test_parse_invalid_json_raises(self) -> None:
        """Invalid JSON raises JSONDecodeError."""
        with pytest.raises(json.JSONDecodeError):
            _parse_json_response("not valid json at all")


# ─── Test generate_filing (mocked) ──────────────────────────────────────────────

class TestGenerateFiling:
    """Tests for the generate_filing function with mocked LLM."""

    @patch("src.filing_generator.core.chat")
    def test_generate_filing_returns_result(
        self, mock_chat: MagicMock, sample_case_info: CaseInfo, mock_llm_json_response: str,
    ) -> None:
        """generate_filing returns a FilingResult."""
        mock_chat.return_value = mock_llm_json_response

        result = generate_filing(
            filing_type="motion_to_dismiss",
            case_info=sample_case_info,
            facts="Defendant failed to respond.",
            arguments="Failure to state a claim under Rule 12(b)(6).",
        )

        assert isinstance(result, FilingResult)
        assert result.filing_type == "motion_to_dismiss"
        assert "Motion to Dismiss" in result.title
        assert result.content  # Should have content
        assert mock_chat.called

    @patch("src.filing_generator.core.chat")
    def test_generate_filing_handles_raw_text(
        self, mock_chat: MagicMock, sample_case_info: CaseInfo,
    ) -> None:
        """generate_filing handles non-JSON responses gracefully."""
        mock_chat.return_value = "This is a plain text response without JSON."

        result = generate_filing(
            filing_type="complaint",
            case_info=sample_case_info,
            facts="Facts here.",
            arguments="Arguments here.",
        )

        assert isinstance(result, FilingResult)
        assert len(result.warnings) > 0  # Should have warnings about parsing


# ─── Test generate_motion (mocked) ──────────────────────────────────────────────

class TestGenerateMotion:
    """Tests for the generate_motion function with mocked LLM."""

    @patch("src.filing_generator.core.chat")
    def test_generate_motion_returns_result(
        self, mock_chat: MagicMock, sample_case_info: CaseInfo, mock_llm_json_response: str,
    ) -> None:
        """generate_motion returns a FilingResult."""
        mock_chat.return_value = mock_llm_json_response

        result = generate_motion(
            motion_type="motion_to_dismiss",
            case_info=sample_case_info,
            grounds="Failure to state a claim.",
        )

        assert isinstance(result, FilingResult)
        assert result.filing_type == "motion_to_dismiss"
        assert result.content
        assert mock_chat.called


# ─── Test generate_discovery_request (mocked) ───────────────────────────────────

class TestGenerateDiscoveryRequest:
    """Tests for the generate_discovery_request function with mocked LLM."""

    @patch("src.filing_generator.core.chat")
    def test_generate_discovery_returns_result(
        self, mock_chat: MagicMock, sample_case_info: CaseInfo,
    ) -> None:
        """generate_discovery_request returns a FilingResult."""
        mock_chat.return_value = json.dumps({
            "title": "Interrogatories",
            "content": "INTERROGATORY NO. 1: ...",
            "sections": ["Definitions", "Instructions", "Interrogatories"],
            "warnings": ["Review before serving"],
        })

        result = generate_discovery_request(
            case_info=sample_case_info,
            discovery_type="interrogatories",
            items=["employment records", "email communications"],
        )

        assert isinstance(result, FilingResult)
        assert result.filing_type == "discovery_request"
        assert result.content
        assert mock_chat.called


# ─── Test validate_filing (mocked) ──────────────────────────────────────────────

class TestValidateFiling:
    """Tests for the validate_filing function with mocked LLM."""

    @patch("src.filing_generator.core.chat")
    def test_validate_filing_returns_dict(self, mock_chat: MagicMock) -> None:
        """validate_filing returns a validation dictionary."""
        mock_chat.return_value = json.dumps({
            "is_valid": True,
            "score": 85,
            "issues": ["Minor formatting issue in paragraph 3"],
            "missing_sections": [],
            "suggestions": ["Add more specific citations"],
            "citation_check": "Citations appear generally correct",
        })

        result = validate_filing("IN THE UNITED STATES DISTRICT COURT...")

        assert isinstance(result, dict)
        assert result["is_valid"] is True
        assert result["score"] == 85
        assert len(result["issues"]) > 0
        assert mock_chat.called

    @patch("src.filing_generator.core.chat")
    def test_validate_filing_handles_parse_failure(self, mock_chat: MagicMock) -> None:
        """validate_filing handles unparseable LLM response."""
        mock_chat.return_value = "I cannot parse this into JSON."

        result = validate_filing("Some filing text...")

        assert isinstance(result, dict)
        assert result["is_valid"] is False
        assert len(result["issues"]) > 0


# ─── Test FILING_TEMPLATES ──────────────────────────────────────────────────────

class TestFilingTemplates:
    """Tests for FILING_TEMPLATES dictionary."""

    def test_all_filing_types_have_templates(self) -> None:
        """Every FilingType has a corresponding template."""
        for ft in FilingType:
            assert ft in FILING_TEMPLATES, f"Missing template for {ft.value}"

    def test_templates_have_required_keys(self) -> None:
        """Each template has title, sections, and description."""
        for ft, template in FILING_TEMPLATES.items():
            assert "title" in template, f"Missing title in {ft.value}"
            assert "sections" in template, f"Missing sections in {ft.value}"
            assert "description" in template, f"Missing description in {ft.value}"
            assert isinstance(template["sections"], list)
            assert len(template["sections"]) > 0

    def test_sample_case_info_exists(self) -> None:
        """SAMPLE_CASE_INFO is properly defined."""
        assert SAMPLE_CASE_INFO.case_number == "2025-CV-01234"
        assert SAMPLE_CASE_INFO.parties["plaintiff"] == "Jane Doe"


# ─── Test Constants ──────────────────────────────────────────────────────────────

class TestConstants:
    """Tests for module constants."""

    def test_legal_disclaimer_not_empty(self) -> None:
        """LEGAL_DISCLAIMER is defined and non-empty."""
        assert LEGAL_DISCLAIMER
        assert "DISCLAIMER" in LEGAL_DISCLAIMER

    def test_system_prompt_not_empty(self) -> None:
        """SYSTEM_PROMPT is defined and non-empty."""
        assert SYSTEM_PROMPT
        assert "legal" in SYSTEM_PROMPT.lower()
