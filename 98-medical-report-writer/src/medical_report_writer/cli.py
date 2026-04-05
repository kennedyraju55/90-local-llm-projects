"""
Medical Report Writer - CLI Module

Command-line interface for clinical report generation powered by Click and Rich.
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

from medical_report_writer.core import (
    DISCLAIMER,
    REPORT_TYPES,
    generate_report,
    generate_discharge_summary,
    generate_referral_letter,
    display_disclaimer,
    ReportSession,
    check_ollama_running,
)

logger = logging.getLogger("medical_report_writer.cli")
console = Console()

# Session-level report tracker
_session = ReportSession()


@click.group()
def cli():
    """🏥 Medical Report Writer - AI-powered clinical report generation."""
    pass


@cli.command()
@click.option("--type", "-t", "report_type", required=True,
              type=click.Choice(list(REPORT_TYPES.keys())),
              help="Type of medical report to generate")
@click.option("--data", "-d", required=True, help="Clinical data for the report")
@click.option("--demographics", "-p", default=None, help="Patient demographics")
def generate(report_type: str, data: str, demographics: str):
    """Generate a medical report from clinical data."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    report_info = REPORT_TYPES[report_type]
    console.print(f"\n[bold]Generating {report_info['name']}...[/bold]\n")

    try:
        report = generate_report(data, report_type, demographics)
        console.print(Panel(
            Markdown(report),
            title=f"📄 {report_info['name']}",
            border_style="blue",
        ))

        _session.add_report(report_type, data, report)
    except Exception as exc:
        console.print(f"[bold red]Error during generation:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This report is AI-drafted and MUST be "
        "reviewed and approved by a licensed physician before clinical use.",
        border_style="red",
    ))


@cli.command()
@click.option("--admission", "-a", required=True, help="Admission data")
@click.option("--course", "-c", required=True, help="Hospital course description")
@click.option("--discharge-info", "-d", required=True, help="Discharge information")
def discharge(admission: str, course: str, discharge_info: str):
    """Generate a discharge summary."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print("\n[bold]Generating Discharge Summary...[/bold]\n")

    try:
        report = generate_discharge_summary(admission, course, discharge_info)
        console.print(Panel(
            Markdown(report),
            title="📄 Discharge Summary",
            border_style="blue",
        ))

        _session.add_report("discharge_summary", admission, report)
    except Exception as exc:
        console.print(f"[bold red]Error during generation:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This report requires physician review and signature.",
        border_style="red",
    ))


@cli.command()
@click.option("--patient", "-p", required=True, help="Patient information")
@click.option("--reason", "-r", required=True, help="Reason for referral")
@click.option("--findings", "-f", required=True, help="Clinical findings")
@click.option("--physician", default=None, help="Requesting physician name")
def referral(patient: str, reason: str, findings: str, physician: str):
    """Generate a referral letter."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print("\n[bold]Generating Referral Letter...[/bold]\n")

    try:
        report = generate_referral_letter(patient, reason, findings, physician)
        console.print(Panel(
            Markdown(report),
            title="📄 Referral Letter",
            border_style="blue",
        ))

        _session.add_report("referral_letter", patient, report)
    except Exception as exc:
        console.print(f"[bold red]Error during generation:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This letter requires physician review and signature.",
        border_style="red",
    ))


@cli.command()
def templates():
    """List all available report types."""
    console.print()
    table = Table(title="📋 Available Report Types")
    table.add_column("Type Key", style="cyan")
    table.add_column("Name", style="white")
    table.add_column("Description", style="green")
    table.add_column("Sections", style="yellow")

    for key, info in REPORT_TYPES.items():
        table.add_row(
            key,
            info["name"],
            info["description"],
            info["sections"][:80] + "..." if len(info["sections"]) > 80 else info["sections"],
        )

    console.print(table)
    console.print()


if __name__ == "__main__":
    cli()
