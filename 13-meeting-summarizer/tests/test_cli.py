"""Tests for Meeting Summarizer CLI."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

from src.meeting_summarizer.cli import cli


class TestCLI:
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Meeting Summarizer" in result.output

    def test_summarize_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize", "--help"])
        assert result.exit_code == 0

    def test_speakers_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["speakers", "--help"])
        assert result.exit_code == 0

    def test_decisions_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["decisions", "--help"])
        assert result.exit_code == 0

    def test_followups_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["followups", "--help"])
        assert result.exit_code == 0

    def test_summarize_missing_transcript(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize"])
        assert result.exit_code != 0
