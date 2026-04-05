"""Tests for Resume Analyzer CLI."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.resume_analyzer.cli import cli


class TestCLI:
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Resume Analyzer" in result.output

    def test_analyze_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["analyze", "--help"])
        assert result.exit_code == 0
        assert "--resume" in result.output

    def test_score_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["score", "--help"])
        assert result.exit_code == 0

    def test_ats_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["ats", "--help"])
        assert result.exit_code == 0

    def test_analyze_missing_resume(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["analyze"])
        assert result.exit_code != 0
