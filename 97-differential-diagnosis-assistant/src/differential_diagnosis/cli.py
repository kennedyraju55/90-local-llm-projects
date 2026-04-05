"""
Differential Diagnosis Assistant - CLI Module

Command-line interface for diagnostic reasoning powered by Click and Rich.
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

from differential_diagnosis.core import (
    DISCLAIMER,
    SYSTEM_PROMPT,
    BODY_SYSTEMS,
    URGENCY_LABELS,
    assess_urgency,
    get_affected_systems,
    generate_differential,
    rank_diagnoses,
    get_workup_recommendations,
    compare_diagnoses,
    display_disclaimer,
    DiagnosisSession,
    check_ollama_running,
)

logger = logging.getLogger("differential_diagnosis.cli")
console = Console()

# Session-level tracker
_session = DiagnosisSession()


@click.group()
def cli():
    """🏥 Differential Diagnosis Assistant - AI-powered diagnostic reasoning (EDUCATIONAL ONLY)."""
    pass


@cli.command()
@click.option("--symptoms", "-s", required=True, help="Describe the presenting symptoms")
@click.option("--patient-info", "-p", default="", help="Patient demographics & history")
@click.option("--exam-findings", "-e", default="", help="Physical examination findings")
def diagnose(symptoms: str, patient_info: str, exam_findings: str):
    """Generate a ranked differential diagnosis from symptoms."""
    display_disclaimer()

    # Urgency assessment
    level, label, advice = assess_urgency(symptoms)
    systems = get_affected_systems(symptoms)

    console.print()
    console.print(Panel(
        f"[bold]Urgency Level:[/bold] {label}\n[bold]Advice:[/bold] {advice}",
        title="📊 Urgency Assessment",
        border_style="yellow" if level <= 2 else ("red" if level >= 4 else "orange1"),
    ))

    systems_text = ", ".join(f"[cyan]{s}[/cyan]" for s in systems)
    console.print(f"\n🗺️  [bold]Affected Body Systems:[/bold] {systems_text}\n")

    # LLM analysis
    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print("[bold]Generating differential diagnosis...[/bold]\n")
    try:
        response = generate_differential(symptoms, patient_info, exam_findings)
        console.print(Panel(Markdown(response), title="🔍 Differential Diagnosis", border_style="blue"))

        _session.add_entry(symptoms, patient_info, exam_findings, level, systems, response)
    except Exception as exc:
        console.print(f"[bold red]Error during analysis:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This is for educational purposes ONLY. "
        "Always consult a qualified healthcare professional for clinical decisions.",
        border_style="red",
    ))


@cli.command()
@click.option("--diagnosis", "-d", required=True, help="Diagnosis to get workup for")
def workup(diagnosis: str):
    """Get workup recommendations for a specific diagnosis."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print(f"[bold]Getting workup recommendations for:[/bold] {diagnosis}\n")
    try:
        response = get_workup_recommendations(diagnosis)
        console.print(Panel(Markdown(response), title="🧪 Workup Recommendations", border_style="green"))
    except Exception as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This is for educational purposes ONLY.",
        border_style="red",
    ))


@cli.command()
@click.option("--diagnosis1", "-a", required=True, help="First diagnosis")
@click.option("--diagnosis2", "-b", required=True, help="Second diagnosis")
@click.option("--clinical-data", "-c", default="", help="Clinical context")
def compare(diagnosis1: str, diagnosis2: str, clinical_data: str):
    """Compare two diagnoses side by side."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    console.print(f"[bold]Comparing:[/bold] {diagnosis1} vs {diagnosis2}\n")
    try:
        response = compare_diagnoses(diagnosis1, diagnosis2, clinical_data)
        console.print(Panel(Markdown(response), title="⚖️ Diagnosis Comparison", border_style="cyan"))
    except Exception as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]Remember:[/bold red] This is for educational purposes ONLY.",
        border_style="red",
    ))


@cli.command("chat")
def chat_mode():
    """Start an interactive diagnostic reasoning chat session."""
    display_disclaimer()
    console.print("\n[bold cyan]Interactive Diagnostic Reasoning Chat[/bold cyan]")
    console.print("Describe symptoms, patient history, or exam findings. "
                  "Type [bold]'quit'[/bold] or [bold]'exit'[/bold] to end.\n")

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. "
                      "Please start Ollama first (`ollama serve`).")
        raise SystemExit(1)

    conversation_history: list[dict] = []

    while True:
        try:
            user_input = console.input("[bold green]You:[/bold green] ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Session ended.[/yellow]")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            console.print("[yellow]Session ended. Stay healthy![/yellow]")
            break

        # Show urgency
        level, label, advice = assess_urgency(user_input)
        systems = get_affected_systems(user_input)

        if level >= 4:
            console.print(f"\n[bold red]{label}[/bold red]: {advice}\n")

        try:
            response = generate_differential(user_input, conversation_history=conversation_history)
            console.print(Panel(Markdown(response), title="🩺 Diagnostic Reasoning", border_style="blue"))

            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": response})

            _session.add_entry(user_input, "", "", level, systems, response)
        except Exception as exc:
            console.print(f"[bold red]Error:[/bold red] {exc}")

    # Show session summary
    summary = _session.get_summary()
    if summary["total_consultations"] > 0:
        console.print(Panel(
            f"Total consultations: {summary['total_consultations']}\n"
            f"Max urgency: {summary['max_urgency']}\n"
            f"Systems involved: {', '.join(summary['systems_involved'])}",
            title="📋 Session Summary",
            border_style="cyan",
        ))


if __name__ == "__main__":
    cli()
