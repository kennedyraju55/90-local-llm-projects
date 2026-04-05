"""
Lab Results Interpreter - CLI Interface
Click-based command line tool for lab result analysis.
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

from src.lab_results_interpreter.core import (
    interpret_results,
    identify_abnormalities,
    suggest_followup_tests,
    explain_lab_value,
    get_reference_range,
    display_disclaimer,
    REFERENCE_RANGES,
    LAB_PANELS,
    DISCLAIMER,
)

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """🏥 Lab Results Interpreter - AI-Powered Laboratory Analysis

    Interpret lab results, identify abnormalities, and get follow-up
    recommendations using Gemma 4 running locally via Ollama.

    100% HIPAA-friendly — no patient data leaves your machine.
    """
    pass


@cli.command()
@click.option("--results", "-r", required=True, help="Lab results text or file path")
@click.option("--panel", "-p", default="", help="Lab panel type (e.g., CBC, BMP)")
@click.option("--context", "-c", default="", help="Patient context (age, sex, medications)")
def interpret(results: str, panel: str, context: str):
    """Interpret laboratory results."""
    console.print(Panel(DISCLAIMER, title="⚠️  Disclaimer", border_style="yellow"))
    console.print()

    with console.status("[bold cyan]Analyzing lab results..."):
        response = interpret_results(
            lab_results_text=results,
            patient_context=context,
            panel_type=panel,
        )

    console.print(Panel(Markdown(response), title="🔬 Lab Results Interpretation", border_style="green"))


@cli.command()
@click.option("--results", "-r", required=True, help="Lab results text")
@click.option("--panel", "-p", default="", help="Lab panel type")
def abnormalities(results: str, panel: str):
    """Identify abnormal values in lab results."""
    console.print(Panel(DISCLAIMER, title="⚠️  Disclaimer", border_style="yellow"))
    console.print()

    with console.status("[bold cyan]Scanning for abnormalities..."):
        response = identify_abnormalities(
            lab_results_text=results,
            panel_type=panel,
        )

    console.print(Panel(Markdown(response), title="🚨 Abnormal Values", border_style="red"))


@cli.command()
@click.option("--results", "-r", required=True, help="Lab results text")
@click.option("--context", "-c", default="", help="Clinical context")
def followup(results: str, context: str):
    """Suggest follow-up tests based on results."""
    console.print(Panel(DISCLAIMER, title="⚠️  Disclaimer", border_style="yellow"))
    console.print()

    with console.status("[bold cyan]Generating follow-up recommendations..."):
        response = suggest_followup_tests(
            lab_results_text=results,
            clinical_context=context,
        )

    console.print(Panel(Markdown(response), title="📋 Follow-Up Recommendations", border_style="blue"))


@cli.command()
@click.option("--test", "-t", required=True, help="Test name (e.g., Hemoglobin)")
@click.option("--value", "-v", required=True, help="Test value")
@click.option("--unit", "-u", default="", help="Unit of measurement")
def explain(test: str, value: str, unit: str):
    """Explain a specific lab value in detail."""
    console.print(Panel(DISCLAIMER, title="⚠️  Disclaimer", border_style="yellow"))
    console.print()

    with console.status(f"[bold cyan]Explaining {test}..."):
        response = explain_lab_value(
            test_name=test,
            value=value,
            unit=unit,
        )

    console.print(Panel(Markdown(response), title=f"📖 {test} Explanation", border_style="cyan"))


@cli.command()
@click.option("--panel", "-p", required=True, help="Lab panel name (e.g., CBC, BMP)")
def reference(panel: str):
    """Show reference ranges for a lab panel."""
    if panel not in REFERENCE_RANGES:
        console.print(f"[red]Unknown panel: {panel}[/red]")
        console.print(f"Available panels: {', '.join(REFERENCE_RANGES.keys())}")
        return

    table = Table(title=f"📊 Reference Ranges — {panel}", show_lines=True)
    table.add_column("Test", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    table.add_column("Reference Range", style="green")
    table.add_column("Unit", style="yellow")

    for test_name, info in REFERENCE_RANGES[panel].items():
        table.add_row(
            test_name,
            info["description"],
            info["range"],
            info["unit"],
        )

    console.print(table)


@cli.command()
def panels():
    """List all available lab panels."""
    table = Table(title="🧪 Available Lab Panels", show_lines=True)
    table.add_column("#", style="dim", width=4)
    table.add_column("Panel Name", style="cyan")
    table.add_column("Reference Data", style="green")

    for i, panel_name in enumerate(LAB_PANELS, 1):
        has_ref = "✅ Available" if panel_name in REFERENCE_RANGES else "—"
        table.add_row(str(i), panel_name, has_ref)

    console.print(table)


if __name__ == "__main__":
    cli()
