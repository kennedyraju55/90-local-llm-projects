"""
Patient Intake Summarizer - CLI Module

Command-line interface for intake form summarization powered by Click and Rich.
"""

import sys
import os
import logging

# Path setup for common module
_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

from patient_intake_summarizer.core import (
    DISCLAIMER,
    INTAKE_CATEGORIES,
    summarize_intake,
    extract_medical_history,
    generate_pre_visit_summary,
    identify_risk_factors,
    flag_missing_info,
    display_disclaimer,
    IntakeSession,
    check_ollama_running,
)

logger = logging.getLogger("patient_intake_summarizer.cli")
console = Console()

# Session-level tracker
_session = IntakeSession()


@click.group()
def cli():
    """🏥 Patient Intake Summarizer - AI-powered intake form summarization (HIPAA-friendly)."""
    pass


@cli.command()
@click.option("--text", "-t", required=True, help="Patient intake form text")
@click.option(
    "--format", "-f", "summary_format",
    type=click.Choice(["brief", "detailed", "structured"]),
    default="structured",
    help="Summary format",
)
@click.option("--focus", "-F", multiple=True, help="Focus areas (repeat for multiple)")
def summarize(text: str, summary_format: str, focus: tuple[str, ...]):
    """Summarize patient intake form text into a clinical summary."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    focus_areas = list(focus) if focus else None

    console.print(f"\n[bold]Summarizing intake form ({summary_format} format)...[/bold]\n")
    try:
        result = summarize_intake(text, summary_format, focus_areas)
        console.print(Panel(Markdown(result), title="📋 Intake Summary", border_style="blue"))
        _session.add_summary(text, result, summary_format, focus_areas)
    except Exception as exc:
        console.print(f"[bold red]Error during summarization:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This is an AI-generated summary. "
        "It MUST be reviewed by a licensed physician before use in patient care.",
        border_style="red",
    ))


@cli.command()
@click.option("--text", "-t", required=True, help="Patient intake form text")
def extract(text: str):
    """Extract and categorize medical history from intake text."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print("\n[bold]Extracting medical history categories...[/bold]\n")
    try:
        result = extract_medical_history(text)

        table = Table(title="📊 Extracted Medical History")
        table.add_column("Category", style="cyan", width=20)
        table.add_column("Content", style="white")

        for category, content in result.items():
            display_content = str(content)
            if len(display_content) > 100:
                display_content = display_content[:100] + "..."
            table.add_row(category, display_content)

        console.print(table)
    except Exception as exc:
        console.print(f"[bold red]Error during extraction:[/bold red] {exc}")
        raise SystemExit(1)


@cli.command("pre-visit")
@click.option("--text", "-t", required=True, help="Patient intake form text")
@click.option(
    "--type", "-T", "appointment_type",
    type=click.Choice(["general", "follow-up", "specialist", "annual_physical", "urgent"]),
    default="general",
    help="Appointment type",
)
def pre_visit(text: str, appointment_type: str):
    """Generate a pre-visit summary for the physician."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print(f"\n[bold]Generating pre-visit summary ({appointment_type})...[/bold]\n")
    try:
        intake_data = extract_medical_history(text)
        result = generate_pre_visit_summary(intake_data, appointment_type)
        console.print(Panel(Markdown(result), title="🩺 Pre-Visit Summary", border_style="green"))
    except Exception as exc:
        console.print(f"[bold red]Error during generation:[/bold red] {exc}")
        raise SystemExit(1)


@cli.command()
@click.option("--text", "-t", required=True, help="Patient intake form text")
def risks(text: str):
    """Identify clinical risk factors from intake text."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print("\n[bold]Identifying risk factors...[/bold]\n")
    try:
        result = identify_risk_factors(text)
        console.print(Panel(
            "\n".join(f"⚠️  {r}" for r in result) if result else "No significant risk factors identified.",
            title="🔍 Risk Factors",
            border_style="yellow",
        ))
    except Exception as exc:
        console.print(f"[bold red]Error during risk analysis:[/bold red] {exc}")
        raise SystemExit(1)


@cli.command()
@click.option("--text", "-t", required=True, help="Patient intake form text")
def missing(text: str):
    """Flag missing or incomplete information in the intake form."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print("\n[bold]Checking for missing information...[/bold]\n")
    try:
        result = flag_missing_info(text)
        console.print(Panel(
            "\n".join(f"❓ {item}" for item in result) if result else "✅ All standard categories appear complete.",
            title="📝 Missing Information",
            border_style="orange1",
        ))
    except Exception as exc:
        console.print(f"[bold red]Error during analysis:[/bold red] {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    cli()
