"""CLI interface for Legal Brief Writer using Click and Rich."""

import os
import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich.prompt import Prompt

from .core import (
    BriefType,
    CaseDetails,
    BriefResult,
    LEGAL_DISCLAIMER,
    BRIEF_TEMPLATES,
    write_brief,
    write_memorandum,
    write_irac_analysis,
    improve_legal_writing,
    format_brief_text,
    format_irac_text,
    display_brief_types,
)
from .config import load_config

console = Console()


def _get_model() -> str:
    """Get the configured model name."""
    config = load_config()
    return os.environ.get("LLM_MODEL", config.llm.model)


def _read_file_or_text(value: str) -> str:
    """Read from file if path exists, otherwise return as text."""
    if os.path.isfile(value):
        with open(value, "r", encoding="utf-8") as f:
            return f.read()
    return value


@click.group()
@click.version_option(version="1.0.0", prog_name="Legal Brief Writer")
def cli():
    """⚖️ Legal Brief Writer - AI-powered legal document generation.

    All processing happens locally using Ollama. No data leaves your machine.
    Perfect for maintaining attorney-client privilege.
    """
    pass


@cli.command()
@click.option("--type", "-t", "brief_type", default="memorandum_of_law",
              help="Type of brief to write (use 'templates' command to see options)")
@click.option("--facts-file", "-f", required=True,
              help="File containing statement of facts, or inline text")
@click.option("--issues", "-i", required=True,
              help="Legal issues to address (file path or inline text)")
@click.option("--arguments", "-a", required=True,
              help="Key arguments (file path or inline text)")
@click.option("--case-name", "-n", default="Case", help="Case name")
@click.option("--case-number", "-c", default="", help="Case number")
@click.option("--court", default="", help="Court name")
@click.option("--jurisdiction", "-j", default="", help="Jurisdiction")
@click.option("--client-position", "-p", default="", help="Client position (Plaintiff/Defendant)")
@click.option("--opposing-party", "-o", default="", help="Opposing party name")
@click.option("--output", "output_file", default=None, help="Output file path")
@click.option("--model", "-m", default=None, help="LLM model to use")
def write(brief_type, facts_file, issues, arguments, case_name, case_number,
          court, jurisdiction, client_position, opposing_party, output_file, model):
    """Write a complete legal brief."""
    if model is None:
        model = _get_model()

    console.print(Panel("⚖️ Legal Brief Writer", style="bold gold1", expand=False))
    console.print(f"[dim]Generating {brief_type.replace('_', ' ').title()}...[/dim]\n")

    facts = _read_file_or_text(facts_file)
    issues_text = _read_file_or_text(issues)
    args_text = _read_file_or_text(arguments)

    case_details = CaseDetails(
        case_name=case_name,
        case_number=case_number,
        court=court,
        jurisdiction=jurisdiction,
        client_position=client_position,
        opposing_party=opposing_party,
    )

    with console.status("[bold green]Generating brief with local LLM...", spinner="dots"):
        result = write_brief(
            brief_type=brief_type,
            case_details=case_details,
            facts=facts,
            issues=issues_text,
            arguments=args_text,
            model=model,
        )

    output_text = format_brief_text(result)
    console.print(Panel(Markdown(output_text), title=result.title, border_style="gold1"))
    console.print(f"\n[green]✓ Word count: {result.word_count}[/green]")

    if result.warnings:
        console.print("\n[yellow]⚠ Warnings:[/yellow]")
        for w in result.warnings:
            console.print(f"  [yellow]• {w}[/yellow]")

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_text)
        console.print(f"\n[green]✓ Saved to {output_file}[/green]")


@cli.command()
@click.option("--question", "-q", required=True, help="Question presented")
@click.option("--facts", "-f", required=True, help="Statement of facts (file or text)")
@click.option("--case-name", "-n", default="Case", help="Case name")
@click.option("--case-number", "-c", default="", help="Case number")
@click.option("--court", default="", help="Court name")
@click.option("--output", "output_file", default=None, help="Output file path")
@click.option("--model", "-m", default=None, help="LLM model to use")
def memo(question, facts, case_name, case_number, court, output_file, model):
    """Write a legal memorandum."""
    if model is None:
        model = _get_model()

    console.print(Panel("📋 Legal Memorandum Writer", style="bold gold1", expand=False))

    facts_text = _read_file_or_text(facts)

    case_details = CaseDetails(
        case_name=case_name,
        case_number=case_number,
        court=court,
    )

    with console.status("[bold green]Generating memorandum with local LLM...", spinner="dots"):
        result = write_memorandum(
            case_details=case_details,
            question_presented=question,
            facts=facts_text,
            model=model,
        )

    output_text = format_brief_text(result)
    console.print(Panel(Markdown(output_text), title=result.title, border_style="gold1"))
    console.print(f"\n[green]✓ Word count: {result.word_count}[/green]")

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_text)
        console.print(f"\n[green]✓ Saved to {output_file}[/green]")


@cli.command()
@click.option("--issue", "-i", required=True, help="Legal issue to analyze")
@click.option("--facts", "-f", required=True, help="Relevant facts (file or text)")
@click.option("--output", "output_file", default=None, help="Output file path")
@click.option("--model", "-m", default=None, help="LLM model to use")
def irac(issue, facts, output_file, model):
    """Perform IRAC (Issue, Rule, Application, Conclusion) analysis."""
    if model is None:
        model = _get_model()

    console.print(Panel("🔍 IRAC Analysis", style="bold gold1", expand=False))

    facts_text = _read_file_or_text(facts)

    with console.status("[bold green]Performing IRAC analysis with local LLM...", spinner="dots"):
        result = write_irac_analysis(
            issue=issue,
            facts=facts_text,
            model=model,
        )

    output_text = format_irac_text(result)
    console.print(Panel(output_text, title="IRAC Analysis", border_style="gold1"))

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_text)
        console.print(f"\n[green]✓ Saved to {output_file}[/green]")


@cli.command()
@click.option("--text", "-t", required=True, help="Legal text to improve (file or inline)")
@click.option("--output", "output_file", default=None, help="Output file path")
@click.option("--model", "-m", default=None, help="LLM model to use")
def improve(text, output_file, model):
    """Improve and edit legal writing."""
    if model is None:
        model = _get_model()

    console.print(Panel("✍️ Legal Writing Improvement", style="bold gold1", expand=False))

    input_text = _read_file_or_text(text)

    with console.status("[bold green]Improving legal writing with local LLM...", spinner="dots"):
        result = improve_legal_writing(text=input_text, model=model)

    console.print(Panel(
        result["improved_text"],
        title="Improved Text",
        border_style="green",
    ))

    if result.get("changes"):
        console.print("\n[bold]Changes Made:[/bold]")
        for change in result["changes"]:
            console.print(f"  [cyan]• {change}[/cyan]")

    if result.get("suggestions"):
        console.print("\n[bold]Suggestions:[/bold]")
        for suggestion in result["suggestions"]:
            console.print(f"  [yellow]• {suggestion}[/yellow]")

    console.print(f"\n[dim]Readability: {result.get('readability_score', 'N/A')}[/dim]")

    if result.get("legal_accuracy_notes"):
        console.print(f"[dim]Legal Accuracy Notes: {result['legal_accuracy_notes']}[/dim]")

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["improved_text"])
        console.print(f"\n[green]✓ Saved to {output_file}[/green]")


@cli.command()
def templates():
    """List available brief types and templates."""
    console.print(Panel("📚 Available Brief Types", style="bold gold1", expand=False))

    table = Table(show_header=True, header_style="bold gold1")
    table.add_column("Type", style="cyan", width=30)
    table.add_column("Description", width=50)
    table.add_column("Sections", style="dim", width=30)

    for bt in BriefType:
        template = BRIEF_TEMPLATES.get(bt, {})
        desc = template.get("description", "N/A")
        sections = ", ".join(template.get("sections", [])[:3]) + "..."
        table.add_row(bt.value, desc, sections)

    console.print(table)


@cli.command()
def disclaimer():
    """Display the legal disclaimer."""
    console.print(Panel(
        LEGAL_DISCLAIMER,
        title="⚖️ Legal Disclaimer",
        border_style="red",
    ))


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
