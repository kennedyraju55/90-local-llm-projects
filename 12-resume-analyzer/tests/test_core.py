"""Tests for Resume Analyzer core logic."""

import sys
import os
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock
from click import ClickException

from src.resume_analyzer.core import analyze_resume, score_against_jd, simulate_ats_score
from src.resume_analyzer.utils import read_file, parse_json_response
from src.resume_analyzer.config import load_config

SAMPLE_RESUME = """\
John Doe
Software Engineer
Email: john@example.com

EXPERIENCE
Senior Software Engineer — Acme Corp (2020–Present)
- Led a team of 5 engineers building microservices with Python and Go
- Reduced API latency by 40%

SKILLS
Python, Go, JavaScript, SQL, Docker, Kubernetes, AWS

EDUCATION
B.S. Computer Science — State University (2017)
"""

SAMPLE_JD = """\
Senior Backend Engineer
Requirements:
- 5+ years of experience with Python
- Experience with Kubernetes and Docker
- Experience with PostgreSQL and Redis
"""

MOCK_ANALYSIS = json.dumps({
    "skills": ["Python", "Go", "JavaScript"],
    "experience_summary": "6+ years experience",
    "education": ["B.S. Computer Science"],
    "achievements": ["Led team of 5", "Reduced latency 40%"],
    "strengths": ["Strong skills", "Leadership"],
    "weaknesses": ["No summary section"],
    "formatting_suggestions": ["Add summary"],
    "content_suggestions": ["Add metrics"],
    "overall_score": 72,
})

MOCK_JD_SCORE = json.dumps({
    "match_percentage": 78,
    "matching_skills": ["Python", "Docker", "Kubernetes"],
    "missing_skills": ["Redis", "PostgreSQL"],
    "experience_alignment": "Strong alignment",
    "suggestions": ["Add Redis experience"],
    "keyword_gaps": ["Redis"],
    "overall_assessment": "Good match.",
    "priority_improvements": ["Add Redis", "Add PostgreSQL", "Certifications"],
})


class TestReadFile:
    def test_read_valid_file(self, tmp_path):
        f = tmp_path / "resume.txt"
        f.write_text(SAMPLE_RESUME, encoding="utf-8")
        assert "John Doe" in read_file(str(f))

    def test_read_missing_file(self):
        with pytest.raises(ClickException, match="File not found"):
            read_file("nonexistent.txt")


class TestParseJsonResponse:
    def test_parse_clean_json(self):
        assert parse_json_response('{"score": 85}')["score"] == 85

    def test_parse_json_with_fences(self):
        assert parse_json_response('```json\n{"score": 90}\n```')["score"] == 90

    def test_parse_invalid_json(self):
        with pytest.raises(ClickException, match="Failed to parse"):
            parse_json_response("not json")


class TestAnalyzeResume:
    @patch("src.resume_analyzer.core.get_llm_client")
    def test_analyze_returns_expected_keys(self, mock_get):
        mock_gen = MagicMock(return_value=MOCK_ANALYSIS)
        mock_get.return_value = (MagicMock(), mock_gen, MagicMock())

        result = analyze_resume(SAMPLE_RESUME)
        assert result["overall_score"] == 72
        assert "Python" in result["skills"]


class TestScoreAgainstJD:
    @patch("src.resume_analyzer.core.get_llm_client")
    def test_score_returns_expected_keys(self, mock_get):
        mock_gen = MagicMock(return_value=MOCK_JD_SCORE)
        mock_get.return_value = (MagicMock(), mock_gen, MagicMock())

        result = score_against_jd(SAMPLE_RESUME, SAMPLE_JD)
        assert result["match_percentage"] == 78
        assert "Python" in result["matching_skills"]


class TestConfig:
    def test_default_config(self):
        config = load_config()
        assert config["llm"]["model"] == "gemma4"

    @patch.dict(os.environ, {"RESUME_ANALYZER_MODEL": "llama3"})
    def test_env_override(self):
        config = load_config()
        assert config["llm"]["model"] == "llama3"
