"""Tests for Invoice Extractor CLI."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from click.testing import CliRunner

from src.invoice_extractor.cli import cli


class TestCLI:
    def test_cli_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Invoice Extractor" in result.output

    def test_extract_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["extract", "--help"])
        assert result.exit_code == 0

    def test_batch_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["batch", "--help"])
        assert result.exit_code == 0

    def test_categorize_help(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["categorize", "--help"])
        assert result.exit_code == 0

    def test_extract_missing_file(self):
        runner = CliRunner()
        result = runner.invoke(cli, ["extract"])
        assert result.exit_code != 0
