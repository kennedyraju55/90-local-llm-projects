"""Click CLI interface for Deposition Summarizer."""

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
    LEGAL_DISCLAIMER,
    SAMPLE_TRANSCRIPT,
    summarize_deposition,
    find_admissions,
    find_contradictions,
    extract_testimony,
    generate_follow_up_questions,
    build_timeline,
    get_significance_color,
    get_significance_emoji,
)

logger = logging.getLogger(__name__)
console = Console()


def setup_logging(verbose: bool) -> None:
    """Configure logging level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def _read_transcript(file: str) -> str:
    """Read transcript from file path."""
    if not os.path.exists(file):
        console.print(f"[bold red]Error:[/bold red] File not found: {file}")
        sys.exit(1)
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        console.print("[bold red]Error:[/bold red] File is empty.")
        sys.exit(1)
    return text


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.option("--config", "config_path", type=click.Path(), default=None, help="Path to config.yaml.")
@click.pass_context
def cli(ctx, verbose: bool, config_path: str | None):
    """⚖️ Deposition Summarizer — AI-Powered Deposition Analysis

    Analyze deposition transcripts to extract key admissions, contradictions,
    important testimony, and more. 100% local processing via Ollama.
    """
    setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config_path)


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to deposition transcript file.")
@click.option("--model", "-m", default=None, help="LLM model to use (default: from config).")
@click.pass_context
def summarize(ctx, file: str, model: str | None):
    """Generate a comprehensive deposition summary."""
    config = ctx.obj["config"]
    model = model or config["llm"]["model"]

    transcript = _read_transcript(file)
    console.print(f"\n[dim]Analyzing transcript:[/dim] {file} ({len(transcript)} chars)")

    with console.status("[bold cyan]Analyzing deposition with LLM...[/bold cyan]", spinner="dots"):
        summary = summarize_deposition(transcript, model)

    # Display header
    header = Text()
    header.append("⚖️ Deposition Summary\n", style="bold cyan")
    header.append("Witness: ", style="dim")
    header.append(summary.witness or "Unknown", style="bold white")
    if summary.date:
        header.append(f"\nDate: ", style="dim")
        header.append(summary.date, style="white")
    console.print(Panel(header, border_style="cyan", padding=(1, 2)))

    # Overall summary
    if summary.overall_summary:
        console.print(Panel(
            Markdown(summary.overall_summary),
            title="[bold green]Overall Summary[/bold green]",
            border_style="green",
            padding=(1, 2),
        ))

    # Key admissions table
    if summary.key_admissions:
        table = Table(title="🎯 Key Admissions", border_style="yellow")
        table.add_column("Speaker", style="cyan", width=15)
        table.add_column("Statement", style="white")
        table.add_column("Ref", style="dim", width=12)
        table.add_column("Significance", width=12)
        for adm in summary.key_admissions:
            sig_color = get_significance_color(adm.significance)
            table.add_row(adm.speaker, adm.statement, adm.page_line,
                          f"[{sig_color}]{get_significance_emoji(adm.significance)} {adm.significance}[/{sig_color}]")
        console.print(table)

    # Contradictions
    if summary.contradictions:
        table = Table(title="⚡ Contradictions", border_style="red")
        table.add_column("Statement A", style="white")
        table.add_column("Statement B", style="white")
        table.add_column("Explanation", style="yellow")
        for con in summary.contradictions:
            table.add_row(con.statement_a, con.statement_b, con.explanation)
        console.print(table)

    # Topics covered
    if summary.topics_covered:
        topics = ", ".join(summary.topics_covered)
        console.print(Panel(topics, title="📋 Topics Covered", border_style="blue"))

    # Follow-up questions
    if summary.follow_up_questions:
        questions = "\n".join(f"  {i}. {q}" for i, q in enumerate(summary.follow_up_questions, 1))
        console.print(Panel(questions, title="❓ Follow-up Questions", border_style="magenta"))

    console.print()


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to deposition transcript file.")
@click.option("--model", "-m", default=None, help="LLM model to use.")
@click.pass_context
def admissions(ctx, file: str, model: str | None):
    """Find key admissions in a deposition transcript."""
    config = ctx.obj["config"]
    model = model or config["llm"]["model"]
    transcript = _read_transcript(file)

    with console.status("[bold cyan]Extracting key admissions...[/bold cyan]", spinner="dots"):
        results = find_admissions(transcript, model)

    if not results:
        console.print("[yellow]No key admissions found.[/yellow]")
        return

    table = Table(title="🎯 Key Admissions Found", border_style="yellow")
    table.add_column("#", style="dim", width=4)
    table.add_column("Speaker", style="cyan", width=15)
    table.add_column("Statement", style="white")
    table.add_column("Ref", style="dim", width=12)
    table.add_column("Significance", width=12)

    for i, adm in enumerate(results, 1):
        sig_color = get_significance_color(adm.significance)
        table.add_row(
            str(i), adm.speaker, adm.statement, adm.page_line,
            f"[{sig_color}]{get_significance_emoji(adm.significance)} {adm.significance}[/{sig_color}]",
        )

    console.print(table)
    console.print(f"\n[dim]Total admissions found: {len(results)}[/dim]")


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to deposition transcript file.")
@click.option("--model", "-m", default=None, help="LLM model to use.")
@click.pass_context
def contradictions(ctx, file: str, model: str | None):
    """Find contradictions in a deposition transcript."""
    config = ctx.obj["config"]
    model = model or config["llm"]["model"]
    transcript = _read_transcript(file)

    with console.status("[bold cyan]Detecting contradictions...[/bold cyan]", spinner="dots"):
        results = find_contradictions(transcript, model)

    if not results:
        console.print("[yellow]No contradictions found.[/yellow]")
        return

    for i, con in enumerate(results, 1):
        panel_content = Text()
        panel_content.append("Statement A: ", style="bold")
        panel_content.append(f"{con.statement_a}\n", style="white")
        if con.page_line_a:
            panel_content.append(f"  [{con.page_line_a}]\n", style="dim")
        panel_content.append("\nStatement B: ", style="bold")
        panel_content.append(f"{con.statement_b}\n", style="white")
        if con.page_line_b:
            panel_content.append(f"  [{con.page_line_b}]\n", style="dim")
        if con.explanation:
            panel_content.append(f"\nExplanation: ", style="bold yellow")
            panel_content.append(con.explanation, style="yellow")

        console.print(Panel(
            panel_content,
            title=f"[bold red]⚡ Contradiction #{i}[/bold red]",
            border_style="red",
            padding=(1, 2),
        ))

    console.print(f"\n[dim]Total contradictions found: {len(results)}[/dim]")


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to deposition transcript file.")
@click.option("--topic", "-t", required=True, help="Topic to search for in testimony.")
@click.option("--model", "-m", default=None, help="LLM model to use.")
@click.pass_context
def testimony(ctx, file: str, topic: str, model: str | None):
    """Extract testimony on a specific topic."""
    config = ctx.obj["config"]
    model = model or config["llm"]["model"]
    transcript = _read_transcript(file)

    with console.status(f"[bold cyan]Extracting testimony on '{topic}'...[/bold cyan]", spinner="dots"):
        results = extract_testimony(transcript, topic, model)

    if not results:
        console.print(f"[yellow]No testimony found on topic: {topic}[/yellow]")
        return

    table = Table(title=f"📄 Testimony on: {topic}", border_style="blue")
    table.add_column("Speaker", style="cyan", width=15)
    table.add_column("Summary", style="white")
    table.add_column("Ref", style="dim", width=12)
    table.add_column("Relevance", width=12)

    for t in results:
        rel_color = get_significance_color(t.relevance)
        table.add_row(
            t.speaker, t.summary, t.page_line,
            f"[{rel_color}]{get_significance_emoji(t.relevance)} {t.relevance}[/{rel_color}]",
        )

    console.print(table)


@cli.command(name="follow-up")
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to deposition transcript file.")
@click.option("--model", "-m", default=None, help="LLM model to use.")
@click.pass_context
def follow_up(ctx, file: str, model: str | None):
    """Generate follow-up questions for a deposition."""
    config = ctx.obj["config"]
    model = model or config["llm"]["model"]
    transcript = _read_transcript(file)

    with console.status("[bold cyan]Generating follow-up questions...[/bold cyan]", spinner="dots"):
        questions = generate_follow_up_questions(transcript, model)

    if not questions:
        console.print("[yellow]No follow-up questions generated.[/yellow]")
        return

    content = "\n".join(f"  {i}. {q}" for i, q in enumerate(questions, 1))
    console.print(Panel(
        content,
        title="[bold magenta]❓ Suggested Follow-up Questions[/bold magenta]",
        border_style="magenta",
        padding=(1, 2),
    ))


@cli.command()
@click.option("--file", "-f", required=True, type=click.Path(), help="Path to deposition transcript file.")
@click.option("--model", "-m", default=None, help="LLM model to use.")
@click.pass_context
def timeline(ctx, file: str, model: str | None):
    """Build a chronological timeline from a deposition."""
    config = ctx.obj["config"]
    model = model or config["llm"]["model"]
    transcript = _read_transcript(file)

    with console.status("[bold cyan]Building timeline...[/bold cyan]", spinner="dots"):
        events = build_timeline(transcript, model)

    if not events:
        console.print("[yellow]No timeline events extracted.[/yellow]")
        return

    table = Table(title="📅 Deposition Timeline", border_style="green")
    table.add_column("Date/Time", style="cyan", width=25)
    table.add_column("Event", style="white")

    for event in events:
        table.add_row(event.get("date", ""), event.get("event", ""))

    console.print(table)


@cli.command()
def disclaimer():
    """Display the legal disclaimer."""
    console.print(Panel(
        LEGAL_DISCLAIMER,
        title="[bold red]⚖️ Legal Disclaimer[/bold red]",
        border_style="red",
        padding=(0, 2),
    ))


@cli.command()
def sample():
    """Display the built-in sample deposition transcript."""
    console.print(Panel(
        SAMPLE_TRANSCRIPT,
        title="[bold cyan]📋 Sample Deposition Transcript[/bold cyan]",
        border_style="cyan",
        padding=(1, 2),
    ))
    console.print("[dim]Use this sample to test the summarizer.[/dim]")


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
