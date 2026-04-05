"""Tests for Medical Literature Summarizer CLI."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from click.testing import CliRunner

from src.medical_summarizer.cli import cli


class TestCLI:
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Medical Literature" in result.output

    def test_summarize_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize", "--help"])
        assert result.exit_code == 0

    def test_pico_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["pico", "--help"])
        assert result.exit_code == 0

    def test_evidence_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["evidence", "--help"])
        assert result.exit_code == 0

    def test_cite_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["cite", "--help"])
        assert result.exit_code == 0

    def test_summarize_missing_paper(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["summarize"])
        assert result.exit_code != 0
