"""CLI interface for Court Filing Generator.

Provides command-line access to all filing generation features
with Rich-formatted output and privacy-first messaging.
"""

import json
import sys
import os
from pathlib import Path

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.filing_generator.core import (
    LEGAL_DISCLAIMER,
    CaseInfo,
    FilingType,
    FILING_TEMPLATES,
    generate_filing,
    generate_motion,
    generate_discovery_request,
    validate_filing,
    format_filing_header,
)
from src.filing_generator.config import load_config
from common.llm_client import check_ollama_running

console = Console()


def _check_ollama() -> None:
    """Check Ollama is running and exit gracefully if not."""
    if not check_ollama_running():
        console.print(
            Panel(
                "[red]Ollama is not running![/red]\n\n"
                "Start it with: [bold]ollama serve[/bold]\n"
                "Then pull the model: [bold]ollama pull gemma4[/bold]",
                title="⚠️ Connection Error",
                border_style="red",
            )
        )
        raise SystemExit(1)


def _build_case_info(
    case_number: str, court: str, plaintiff: str, defendant: str,
    judge: str, jurisdiction: str,
) -> CaseInfo:
    """Build a CaseInfo from CLI options."""
    return CaseInfo(
        case_number=case_number,
        court=court,
        parties={"plaintiff": plaintiff, "defendant": defendant},
        judge=judge,
        jurisdiction=jurisdiction,
    )


@click.group()
@click.version_option(version="1.0.0", prog_name="Court Filing Generator")
def cli() -> None:
    """⚖️ Court Filing Generator - AI-powered legal document drafting.

    100% local processing with Gemma 4 via Ollama.
    No data ever leaves your machine. Attorney-client privilege preserved.
    """
    pass


@cli.command()
@click.option("--type", "filing_type", required=True, type=click.Choice([ft.value for ft in FilingType]), help="Type of filing to generate.")
@click.option("--case-number", required=True, help="Case number.")
@click.option("--court", default="United States District Court", help="Court name.")
@click.option("--plaintiff", required=True, help="Plaintiff name.")
@click.option("--defendant", required=True, help="Defendant name.")
@click.option("--judge", default="", help="Judge name.")
@click.option("--jurisdiction", default="federal", help="Jurisdiction (federal/state).")
@click.option("--facts", default="", help="Statement of facts (or path to .txt file).")
@click.option("--arguments", default="", help="Legal arguments (or path to .txt file).")
@click.option("--model", default="gemma4:latest", help="LLM model to use.")
@click.option("--output", "-o", default=None, help="Output file path.")
def generate(
    filing_type: str, case_number: str, court: str, plaintiff: str,
    defendant: str, judge: str, jurisdiction: str, facts: str,
    arguments: str, model: str, output: str,
) -> None:
    """📄 Generate a court filing document."""
    _check_ollama()

    # Load facts/arguments from file if path given
    if facts and Path(facts).is_file():
        facts = Path(facts).read_text(encoding="utf-8")
    if arguments and Path(arguments).is_file():
        arguments = Path(arguments).read_text(encoding="utf-8")

    case_info = _build_case_info(case_number, court, plaintiff, defendant, judge, jurisdiction)

    console.print(Panel(
        f"[bold]Generating:[/bold] {filing_type.replace('_', ' ').title()}\n"
        f"[bold]Case:[/bold] {case_number}\n"
        f"[bold]Model:[/bold] {model}\n"
        f"[dim]🔒 100% Local Processing - No data leaves your machine[/dim]",
        title="⚖️ Court Filing Generator",
        border_style="gold1",
    ))

    with console.status("[bold green]Generating filing...[/bold green]"):
        result = generate_filing(filing_type, case_info, facts, arguments, model)

    # Display result
    console.print(Panel(result.content, title=f"📄 {result.title}", border_style="blue"))

    if result.warnings:
        for warning in result.warnings:
            console.print(f"  [yellow]⚠️ {warning}[/yellow]")

    if output:
        Path(output).write_text(result.content, encoding="utf-8")
        console.print(f"\n[green]✅ Saved to {output}[/green]")


@cli.command()
@click.option("--type", "motion_type", required=True, help="Type of motion.")
@click.option("--case-number", required=True, help="Case number.")
@click.option("--court", default="United States District Court", help="Court name.")
@click.option("--plaintiff", required=True, help="Plaintiff name.")
@click.option("--defendant", required=True, help="Defendant name.")
@click.option("--judge", default="", help="Judge name.")
@click.option("--jurisdiction", default="federal", help="Jurisdiction.")
@click.option("--grounds", required=True, help="Grounds for the motion (or path to .txt file).")
@click.option("--model", default="gemma4:latest", help="LLM model to use.")
@click.option("--output", "-o", default=None, help="Output file path.")
def motion(
    motion_type: str, case_number: str, court: str, plaintiff: str,
    defendant: str, judge: str, jurisdiction: str, grounds: str,
    model: str, output: str,
) -> None:
    """⚖️ Generate a legal motion."""
    _check_ollama()

    if grounds and Path(grounds).is_file():
        grounds = Path(grounds).read_text(encoding="utf-8")

    case_info = _build_case_info(case_number, court, plaintiff, defendant, judge, jurisdiction)

    console.print(Panel(
        f"[bold]Motion Type:[/bold] {motion_type.replace('_', ' ').title()}\n"
        f"[bold]Case:[/bold] {case_number}\n"
        f"[dim]🔒 100% Local Processing[/dim]",
        title="⚖️ Motion Generator",
        border_style="gold1",
    ))

    with console.status("[bold green]Generating motion...[/bold green]"):
        result = generate_motion(motion_type, case_info, grounds, model)

    console.print(Panel(result.content, title=f"⚖️ {result.title}", border_style="blue"))

    if result.warnings:
        for warning in result.warnings:
            console.print(f"  [yellow]⚠️ {warning}[/yellow]")

    if output:
        Path(output).write_text(result.content, encoding="utf-8")
        console.print(f"\n[green]✅ Saved to {output}[/green]")


@cli.command()
@click.option("--case-number", required=True, help="Case number.")
@click.option("--court", default="United States District Court", help="Court name.")
@click.option("--plaintiff", required=True, help="Plaintiff name.")
@click.option("--defendant", required=True, help="Defendant name.")
@click.option("--judge", default="", help="Judge name.")
@click.option("--jurisdiction", default="federal", help="Jurisdiction.")
@click.option("--discovery-type", required=True, type=click.Choice(["interrogatories", "rfp", "rfa"]), help="Type of discovery.")
@click.option("--items", required=True, multiple=True, help="Discovery topics/items (can specify multiple).")
@click.option("--model", default="gemma4:latest", help="LLM model to use.")
@click.option("--output", "-o", default=None, help="Output file path.")
def discovery(
    case_number: str, court: str, plaintiff: str, defendant: str,
    judge: str, jurisdiction: str, discovery_type: str, items: tuple,
    model: str, output: str,
) -> None:
    """🔍 Generate discovery requests."""
    _check_ollama()

    case_info = _build_case_info(case_number, court, plaintiff, defendant, judge, jurisdiction)

    console.print(Panel(
        f"[bold]Discovery Type:[/bold] {discovery_type.upper()}\n"
        f"[bold]Items:[/bold] {len(items)} topics\n"
        f"[bold]Case:[/bold] {case_number}\n"
        f"[dim]🔒 100% Local Processing[/dim]",
        title="🔍 Discovery Generator",
        border_style="gold1",
    ))

    with console.status("[bold green]Generating discovery requests...[/bold green]"):
        result = generate_discovery_request(case_info, discovery_type, list(items), model)

    console.print(Panel(result.content, title=f"🔍 {result.title}", border_style="blue"))

    if result.warnings:
        for warning in result.warnings:
            console.print(f"  [yellow]⚠️ {warning}[/yellow]")

    if output:
        Path(output).write_text(result.content, encoding="utf-8")
        console.print(f"\n[green]✅ Saved to {output}[/green]")


@cli.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.option("--model", default="gemma4:latest", help="LLM model to use.")
def validate(filepath: str, model: str) -> None:
    """✅ Validate a court filing document."""
    _check_ollama()

    filing_text = Path(filepath).read_text(encoding="utf-8")

    console.print(Panel(
        f"[bold]File:[/bold] {filepath}\n"
        f"[bold]Length:[/bold] {len(filing_text)} characters\n"
        f"[dim]🔒 100% Local Processing[/dim]",
        title="✅ Filing Validator",
        border_style="gold1",
    ))

    with console.status("[bold green]Validating filing...[/bold green]"):
        result = validate_filing(filing_text, model)

    # Build validation table
    table = Table(title="Validation Results", border_style="blue")
    table.add_column("Metric", style="bold")
    table.add_column("Value")

    table.add_row("Valid", "✅ Yes" if result.get("is_valid") else "❌ No")
    table.add_row("Score", f"{result.get('score', 0)}/100")
    table.add_row("Citations", str(result.get("citation_check", "N/A")))

    console.print(table)

    if result.get("issues"):
        console.print("\n[bold red]Issues Found:[/bold red]")
        for issue in result["issues"]:
            console.print(f"  [red]• {issue}[/red]")

    if result.get("missing_sections"):
        console.print("\n[bold yellow]Missing Sections:[/bold yellow]")
        for section in result["missing_sections"]:
            console.print(f"  [yellow]• {section}[/yellow]")

    if result.get("suggestions"):
        console.print("\n[bold green]Suggestions:[/bold green]")
        for suggestion in result["suggestions"]:
            console.print(f"  [green]• {suggestion}[/green]")


@cli.command()
def templates() -> None:
    """📋 List available filing templates."""
    table = Table(title="⚖️ Available Filing Templates", border_style="gold1")
    table.add_column("#", style="dim", width=4)
    table.add_column("Filing Type", style="bold cyan")
    table.add_column("Sections", style="green")
    table.add_column("Description", style="white", max_width=50)

    for idx, (ft, template) in enumerate(FILING_TEMPLATES.items(), 1):
        table.add_row(
            str(idx),
            template["title"],
            str(len(template["sections"])),
            template["description"][:50] + "..." if len(template["description"]) > 50 else template["description"],
        )

    console.print(table)
    console.print(f"\n[dim]Total templates: {len(FILING_TEMPLATES)}[/dim]")


@cli.command()
def disclaimer() -> None:
    """⚠️ Show legal disclaimer."""
    console.print(Panel(
        LEGAL_DISCLAIMER,
        title="⚠️ Legal Disclaimer",
        border_style="red",
    ))


def main() -> None:
    """Entry point for the CLI."""
    console.print(
        "[dim]🔒 Court Filing Generator - 100% Local AI Processing | No data leaves your machine[/dim]\n"
    )
    cli()


if __name__ == "__main__":
    main()
