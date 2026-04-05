"""Click CLI interface for Legal Document Summarizer."""

import sys
import os
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text

from .config import load_config
from .core import (
    summarize_document,
    extract_clauses,
    score_risks,
    compare_documents,
    generate_export_markdown,
)
from .utils import setup_logging, read_document, get_llm_client

logger = logging.getLogger(__name__)
console = Console()


def display_summary(summary: str, filepath: str, output_format: str) -> None:
    """Display the summary using Rich formatting."""
    filename = os.path.basename(filepath)

    header = Text()
    header.append("📜 Legal Document Summary\n", style="bold cyan")
    header.append("File: ", style="dim")
    header.append(filename, style="bold white")
    header.append("\nFormat: ", style="dim")
    header.append(output_format.capitalize(), style="bold yellow")

    console.print()
    console.print(Panel(header, border_style="cyan", padding=(1, 2)))
    console.print()
    console.print(Panel(
        Markdown(summary),
        title="[bold green]Analysis Results[/bold green]",
        border_style="green",
        padding=(1, 2),
    ))

    info_table = Table(show_header=False, box=None, padding=(0, 2))
    info_table.add_column("Key", style="dim")
    info_table.add_column("Value", style="white")
    info_table.add_row("Model", "gemma4 (local via Ollama)")
    info_table.add_row("Temperature", "0.3")

    console.print()
    console.print(Panel(info_table, title="[dim]Generation Info[/dim]", border_style="dim"))
    console.print()


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.option("--config", "config_path", type=click.Path(), default=None, help="Path to config.yaml.")
@click.pass_context
def cli(ctx, verbose: bool, config_path: str | None):
    """📜 Legal Document Summarizer - Production CLI

    Analyze legal documents, contracts, and agreements.
    Extracts key clauses, obligations, dates, parties, and more.
    """
    setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config_path)


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to the legal document.")
@click.option(
    "--format", "-fmt", "output_format",
    type=click.Choice(["bullet", "narrative", "detailed"], case_sensitive=False),
    default="bullet", show_default=True,
    help="Output format for the summary.",
)
@click.option("--export", "-e", type=click.Path(), default=None, help="Export results to markdown file.")
@click.pass_context
def summarize(ctx, file: str, output_format: str, export: str | None):
    """Summarize a legal document."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print(Panel("[bold red]Error:[/bold red] Ollama is not running.\n"
                            "Please start Ollama first: [cyan]ollama serve[/cyan]", border_style="red"))
        sys.exit(1)

    try:
        console.print(f"\n[dim]Reading document:[/dim] {file}")
        text = read_document(file)
        console.print(f"[dim]Extracted [bold]{len(text)}[/bold] characters of text.[/dim]")
    except (FileNotFoundError, ValueError, ImportError) as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold cyan]Analyzing document with LLM...[/bold cyan]", spinner="dots"):
        summary = summarize_document(text, output_format, config)

    display_summary(summary, file, output_format)

    if export:
        md = generate_export_markdown(summary, filepath=file)
        with open(export, "w", encoding="utf-8") as f:
            f.write(md)
        console.print(f"[green]✓ Exported to {export}[/green]")


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to the legal document.")
@click.pass_context
def clauses(ctx, file: str):
    """Extract and categorize clauses from a document."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        text = read_document(file)
    except (FileNotFoundError, ValueError, ImportError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold cyan]Extracting clauses...[/bold cyan]", spinner="dots"):
        result = extract_clauses(text, config)

    console.print(Panel(Markdown(result), title="📋 Clause Extraction", border_style="cyan", padding=(1, 2)))


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to the legal document.")
@click.pass_context
def risks(ctx, file: str):
    """Score risk factors in a legal document."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        text = read_document(file)
    except (FileNotFoundError, ValueError, ImportError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold cyan]Analyzing risks...[/bold cyan]", spinner="dots"):
        result = score_risks(text, config)

    console.print(Panel(Markdown(result), title="⚠️ Risk Analysis", border_style="yellow", padding=(1, 2)))


@cli.command()
@click.option("--files", "-f", required=True, multiple=True, type=click.Path(), help="Documents to compare.")
@click.pass_context
def compare(ctx, files: tuple[str]):
    """Compare multiple legal documents."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    if len(files) < 2:
        console.print("[bold red]Error:[/bold red] Provide at least 2 files to compare.")
        sys.exit(1)

    with console.status("[bold cyan]Comparing documents...[/bold cyan]", spinner="dots"):
        result = compare_documents(list(files), config)

    console.print(Panel(Markdown(result), title="📊 Document Comparison", border_style="blue", padding=(1, 2)))


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to the legal document.")
@click.option("--output", "-o", required=True, type=click.Path(), help="Output markdown file path.")
@click.option("--format", "-fmt", "output_format",
              type=click.Choice(["bullet", "narrative", "detailed"]), default="detailed")
@click.pass_context
def export(ctx, file: str, output: str, output_format: str):
    """Generate a comprehensive PDF-ready markdown report."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        text = read_document(file)
    except (FileNotFoundError, ValueError, ImportError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold cyan]Generating comprehensive report...[/bold cyan]", spinner="dots"):
        summary = summarize_document(text, output_format, config)
        clause_text = extract_clauses(text, config)
        risk_text = score_risks(text, config)

    md = generate_export_markdown(summary, clause_text, risk_text, file)
    with open(output, "w", encoding="utf-8") as f:
        f.write(md)

    console.print(f"[bold green]✓ Report exported to {output}[/bold green]")


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
