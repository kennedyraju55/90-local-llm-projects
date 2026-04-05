"""
Clinical Note Generator - CLI Module

Command-line interface powered by Click and Rich.
"""

import sys
import os
import logging

_common_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.insert(0, os.path.abspath(_common_path))

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

from clinical_note_generator.core import (
    DISCLAIMER,
    NOTE_TEMPLATES,
    SPECIALTY_PROMPTS,
    display_disclaimer,
    generate_soap_note,
    generate_note_section,
    refine_note,
    NoteSession,
)
from common.llm_client import check_ollama_running

logger = logging.getLogger("clinical_note_generator.cli")
console = Console()
_session = NoteSession()


@click.group()
def cli():
    """🏥 Clinical Note Generator - AI-powered SOAP note generation (HIPAA-Friendly)."""
    pass


@cli.command()
@click.option("--encounter", "-e", required=True, help="Patient encounter description")
@click.option("--type", "-t", "note_type", default="general", type=click.Choice(list(NOTE_TEMPLATES.keys())), help="Note type")
@click.option("--specialty", "-s", default="internal_medicine", type=click.Choice(list(SPECIALTY_PROMPTS.keys())), help="Medical specialty")
@click.option("--age", default=None, help="Patient age")
@click.option("--sex", default=None, help="Patient sex")
def generate(encounter: str, note_type: str, specialty: str, age: str, sex: str):
    """Generate a SOAP note from an encounter description."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running. Start with: ollama serve")
        raise SystemExit(1)

    demographics = {}
    if age:
        demographics["age"] = age
    if sex:
        demographics["sex"] = sex

    console.print(f"\n[bold]Note Type:[/bold] {NOTE_TEMPLATES[note_type]}")
    console.print(f"[bold]Specialty:[/bold] {specialty}\n")
    console.print("[bold]Generating SOAP note...[/bold]\n")

    try:
        note = generate_soap_note(
            encounter_description=encounter,
            patient_demographics=demographics or None,
            note_type=note_type,
            specialty=specialty,
        )
        console.print(Panel(Markdown(note), title="📋 SOAP Note", border_style="blue"))
        _session.add_note(encounter, note, note_type, specialty)
    except Exception as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        raise SystemExit(1)

    console.print(Panel(
        "[bold red]⚠️ IMPORTANT:[/bold red] This AI-generated note must be reviewed and approved "
        "by the treating physician before use in clinical documentation.",
        border_style="red",
    ))


@cli.command()
@click.option("--encounter", "-e", required=True, help="Encounter description")
@click.option("--section", "-s", required=True, type=click.Choice(["S", "O", "A", "P"]), help="SOAP section")
def section(encounter: str, section: str):
    """Generate a specific SOAP section."""
    display_disclaimer()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        raise SystemExit(1)

    section_names = {"S": "Subjective", "O": "Objective", "A": "Assessment", "P": "Plan"}
    console.print(f"\n[bold]Generating {section_names[section]} section...[/bold]\n")

    try:
        result = generate_note_section(encounter, section)
        console.print(Panel(Markdown(result), title=f"📋 {section_names[section]}", border_style="cyan"))
    except Exception as exc:
        console.print(f"[bold red]Error:[/bold red] {exc}")
        raise SystemExit(1)


@cli.command()
def templates():
    """List available note templates."""
    table = Table(title="📋 Note Templates")
    table.add_column("Type", style="cyan")
    table.add_column("Description", style="white")
    for key, desc in NOTE_TEMPLATES.items():
        table.add_row(key, desc)
    console.print(table)


@cli.command()
def specialties():
    """List available medical specialties."""
    table = Table(title="🏥 Medical Specialties")
    table.add_column("Specialty", style="cyan")
    table.add_column("Focus", style="white")
    for key, desc in SPECIALTY_PROMPTS.items():
        table.add_row(key, desc[:80])
    console.print(table)


if __name__ == "__main__":
    cli()
