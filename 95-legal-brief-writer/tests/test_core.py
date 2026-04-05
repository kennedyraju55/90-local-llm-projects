"""Tests for Legal Brief Writer core module."""

import json
import pytest
from unittest.mock import patch, MagicMock

from src.brief_writer.core import (
    BriefType,
    BriefSection,
    LegalIssue,
    BriefResult,
    CaseDetails,
    LEGAL_DISCLAIMER,
    SYSTEM_PROMPT,
    BRIEF_TEMPLATES,
    SAMPLE_CASE_DETAILS,
    _parse_json_response,
    write_brief,
    write_memorandum,
    write_irac_analysis,
    generate_table_of_authorities,
    improve_legal_writing,
    format_brief_text,
    format_irac_text,
    display_brief_types,
)


# ---------------------------------------------------------------------------
# Test Data
# ---------------------------------------------------------------------------

SAMPLE_BRIEF_RESPONSE = json.dumps({
    "title": "Memorandum of Law in Support of Plaintiff's Motion",
    "sections": [
        {"title": "Caption", "content": "Smith v. Acme Corp, Case No. 2024-CV-01234", "order": 1},
        {"title": "Statement of Facts", "content": "The plaintiff alleges that...", "order": 2},
        {"title": "Argument", "content": "Under the applicable standard...", "order": 3},
        {"title": "Conclusion", "content": "For the foregoing reasons...", "order": 4},
    ],
    "legal_issues": [
        {
            "issue": "Whether defendant breached the duty of care",
            "rule": "A duty of care exists when...",
            "analysis": "Applying the facts here...",
            "conclusion": "The defendant breached the duty of care.",
        }
    ],
    "warnings": ["Verify citation accuracy", "Check jurisdiction-specific rules"],
    "table_of_authorities": [
        "Palsgraf v. Long Island R.R. Co., 248 N.Y. 339 (1928)",
        "Terry v. Ohio, 392 U.S. 1 (1968)",
    ],
})

SAMPLE_IRAC_RESPONSE = json.dumps({
    "issue": "Whether the defendant owed a duty of care to the plaintiff",
    "rule": "Under the Restatement (Third) of Torts, a duty of care exists...",
    "analysis": "In this case, the defendant was in a position to foresee...",
    "conclusion": "The defendant owed a duty of care to the plaintiff.",
})

SAMPLE_TOA_RESPONSE = json.dumps({
    "authorities": [
        "Marbury v. Madison, 5 U.S. 137 (1803)",
        "Brown v. Board of Education, 347 U.S. 483 (1954)",
    ]
})

SAMPLE_IMPROVE_RESPONSE = json.dumps({
    "improved_text": "The defendant negligently failed to maintain the premises.",
    "changes": ["Removed passive voice", "Added specificity"],
    "suggestions": ["Consider adding a citation for the standard"],
    "readability_score": "Good",
    "legal_accuracy_notes": "Verify the negligence standard applies in this jurisdiction.",
})


# ---------------------------------------------------------------------------
# Test _parse_json_response
# ---------------------------------------------------------------------------

class TestParseJsonResponse:
    def test_parse_clean_json(self):
        result = _parse_json_response('{"key": "value"}')
        assert result == {"key": "value"}

    def test_parse_json_with_markdown_fences(self):
        result = _parse_json_response('```json\n{"key": "value"}\n```')
        assert result == {"key": "value"}

    def test_parse_json_with_generic_fences(self):
        result = _parse_json_response('```\n{"key": "value"}\n```')
        assert result == {"key": "value"}

    def test_parse_json_with_surrounding_text(self):
        result = _parse_json_response('Here is the result: {"key": "value"} end.')
        assert result == {"key": "value"}

    def test_parse_json_array(self):
        result = _parse_json_response('Some text then ["a", "b", "c"] end')
        assert result == {"items": ["a", "b", "c"]}

    def test_parse_invalid_json_returns_raw(self):
        result = _parse_json_response("not json at all")
        assert "raw_text" in result
        assert result["raw_text"] == "not json at all"


# ---------------------------------------------------------------------------
# Test BriefType Enum
# ---------------------------------------------------------------------------

class TestBriefType:
    def test_all_brief_types_exist(self):
        expected = [
            "trial_brief", "appellate_brief", "amicus_brief",
            "memorandum_of_law", "memorandum_in_support",
            "memorandum_in_opposition", "reply_brief",
            "legal_memorandum", "case_summary",
        ]
        actual = [bt.value for bt in BriefType]
        assert actual == expected

    def test_brief_type_from_string(self):
        bt = BriefType("trial_brief")
        assert bt == BriefType.TRIAL_BRIEF

    def test_invalid_brief_type(self):
        with pytest.raises(ValueError):
            BriefType("invalid_type")


# ---------------------------------------------------------------------------
# Test Data Structures
# ---------------------------------------------------------------------------

class TestDataStructures:
    def test_brief_section(self):
        section = BriefSection(title="Introduction", content="This brief...", order=1)
        assert section.title == "Introduction"
        assert section.content == "This brief..."
        assert section.order == 1

    def test_legal_issue(self):
        issue = LegalIssue(
            issue="Whether duty exists",
            rule="Under common law...",
            analysis="Applying the rule...",
            conclusion="Duty exists.",
        )
        assert issue.issue == "Whether duty exists"

    def test_case_details(self):
        cd = CaseDetails(
            case_name="Doe v. Roe",
            case_number="2024-001",
            court="District Court",
        )
        assert cd.case_name == "Doe v. Roe"
        assert cd.jurisdiction == ""

    def test_brief_result_defaults(self):
        result = BriefResult(brief_type="trial_brief", title="Test Brief")
        assert result.sections == []
        assert result.legal_issues == []
        assert result.word_count == 0
        assert result.warnings == []
        assert result.table_of_authorities == []

    def test_sample_case_details(self):
        assert SAMPLE_CASE_DETAILS.case_name == "Smith v. Acme Corporation"
        assert SAMPLE_CASE_DETAILS.client_position == "Plaintiff"


# ---------------------------------------------------------------------------
# Test BRIEF_TEMPLATES
# ---------------------------------------------------------------------------

class TestBriefTemplates:
    def test_all_types_have_templates(self):
        for bt in BriefType:
            assert bt in BRIEF_TEMPLATES, f"Missing template for {bt.value}"

    def test_templates_have_sections(self):
        for bt, template in BRIEF_TEMPLATES.items():
            assert "sections" in template
            assert len(template["sections"]) > 0

    def test_templates_have_description(self):
        for bt, template in BRIEF_TEMPLATES.items():
            assert "description" in template
            assert len(template["description"]) > 10


# ---------------------------------------------------------------------------
# Test write_brief with mock
# ---------------------------------------------------------------------------

class TestWriteBrief:
    @patch("src.brief_writer.core.chat")
    def test_write_brief_success(self, mock_chat):
        mock_chat.return_value = SAMPLE_BRIEF_RESPONSE

        case_details = CaseDetails(case_name="Test v. Case", case_number="001")
        result = write_brief(
            brief_type="memorandum_of_law",
            case_details=case_details,
            facts="The plaintiff was injured.",
            issues="Negligence and duty of care.",
            arguments="Defendant breached duty.",
            model="gemma4:latest",
        )

        assert isinstance(result, BriefResult)
        assert result.brief_type == "memorandum_of_law"
        assert len(result.sections) == 4
        assert len(result.legal_issues) == 1
        assert result.word_count > 0
        mock_chat.assert_called_once()

    @patch("src.brief_writer.core.chat")
    def test_write_brief_invalid_type_defaults(self, mock_chat):
        mock_chat.return_value = SAMPLE_BRIEF_RESPONSE

        case_details = CaseDetails(case_name="Test v. Case")
        result = write_brief(
            brief_type="nonexistent_type",
            case_details=case_details,
            facts="Facts",
            issues="Issues",
            arguments="Args",
        )

        assert result.brief_type == "memorandum_of_law"


# ---------------------------------------------------------------------------
# Test write_memorandum with mock
# ---------------------------------------------------------------------------

class TestWriteMemorandum:
    @patch("src.brief_writer.core.chat")
    def test_write_memorandum_success(self, mock_chat):
        mock_chat.return_value = SAMPLE_BRIEF_RESPONSE

        case_details = CaseDetails(case_name="Test v. Case")
        result = write_memorandum(
            case_details=case_details,
            question_presented="Does a duty of care exist?",
            facts="The plaintiff was injured at the defendant's property.",
            model="gemma4:latest",
        )

        assert isinstance(result, BriefResult)
        assert result.brief_type == "legal_memorandum"
        assert len(result.sections) > 0
        mock_chat.assert_called_once()


# ---------------------------------------------------------------------------
# Test write_irac_analysis with mock
# ---------------------------------------------------------------------------

class TestWriteIRAC:
    @patch("src.brief_writer.core.chat")
    def test_write_irac_success(self, mock_chat):
        mock_chat.return_value = SAMPLE_IRAC_RESPONSE

        result = write_irac_analysis(
            issue="Does a duty of care exist?",
            facts="Plaintiff was injured on premises.",
            model="gemma4:latest",
        )

        assert isinstance(result, LegalIssue)
        assert "duty" in result.issue.lower()
        assert len(result.rule) > 0
        assert len(result.analysis) > 0
        assert len(result.conclusion) > 0
        mock_chat.assert_called_once()


# ---------------------------------------------------------------------------
# Test generate_table_of_authorities with mock
# ---------------------------------------------------------------------------

class TestGenerateTOA:
    @patch("src.brief_writer.core.chat")
    def test_generate_toa_success(self, mock_chat):
        mock_chat.return_value = SAMPLE_TOA_RESPONSE

        result = generate_table_of_authorities(
            brief_text="In Marbury v. Madison, the court held...",
            model="gemma4:latest",
        )

        assert isinstance(result, list)
        assert len(result) == 2
        assert "Marbury" in result[0]
        mock_chat.assert_called_once()


# ---------------------------------------------------------------------------
# Test improve_legal_writing with mock
# ---------------------------------------------------------------------------

class TestImproveLegalWriting:
    @patch("src.brief_writer.core.chat")
    def test_improve_writing_success(self, mock_chat):
        mock_chat.return_value = SAMPLE_IMPROVE_RESPONSE

        result = improve_legal_writing(
            text="The defendant failed to maintain premises properly.",
            model="gemma4:latest",
        )

        assert isinstance(result, dict)
        assert "improved_text" in result
        assert "changes" in result
        assert "suggestions" in result
        assert "readability_score" in result
        assert len(result["changes"]) > 0
        mock_chat.assert_called_once()


# ---------------------------------------------------------------------------
# Test Display Helpers
# ---------------------------------------------------------------------------

class TestDisplayHelpers:
    def test_format_brief_text(self):
        result = BriefResult(
            brief_type="trial_brief",
            title="Test Brief",
            sections=[
                BriefSection(title="Introduction", content="This is the intro.", order=1),
                BriefSection(title="Argument", content="The argument is...", order=2),
            ],
            word_count=10,
            warnings=["Check citations"],
            table_of_authorities=["Case v. Case, 123 F.3d 456 (2020)"],
        )
        text = format_brief_text(result)
        assert "Test Brief" in text
        assert "INTRODUCTION" in text
        assert "ARGUMENT" in text
        assert "TABLE OF AUTHORITIES" in text
        assert "Word Count: 10" in text

    def test_format_irac_text(self):
        issue = LegalIssue(
            issue="Duty of care",
            rule="A duty exists when...",
            analysis="Applying to facts...",
            conclusion="Duty exists.",
        )
        text = format_irac_text(issue)
        assert "IRAC ANALYSIS" in text
        assert "ISSUE:" in text
        assert "RULE:" in text
        assert "APPLICATION:" in text
        assert "CONCLUSION:" in text
        assert "Duty of care" in text

    def test_display_brief_types(self):
        text = display_brief_types()
        assert "Available Brief Types" in text
        for bt in BriefType:
            assert bt.value in text


# ---------------------------------------------------------------------------
# Test Constants
# ---------------------------------------------------------------------------

class TestConstants:
    def test_legal_disclaimer_exists(self):
        assert len(LEGAL_DISCLAIMER) > 100
        assert "DISCLAIMER" in LEGAL_DISCLAIMER
        assert "attorney" in LEGAL_DISCLAIMER.lower()

    def test_system_prompt_exists(self):
        assert len(SYSTEM_PROMPT) > 100
        assert "legal" in SYSTEM_PROMPT.lower()
        assert "IRAC" in SYSTEM_PROMPT
