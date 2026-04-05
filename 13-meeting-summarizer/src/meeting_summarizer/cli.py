"""Click CLI interface for Meeting Summarizer."""

import sys
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

from .config import load_config
from .core import (
    summarize_meeting,
    identify_speakers,
    extract_decision_log,
    generate_followup_reminders,
    save_summary,
)
from .utils import setup_logging, read_transcript, parse_action_items, extract_section, get_llm_client

logger = logging.getLogger(__name__)
console = Console()


def display_summary(summary: str) -> None:
    """Display the meeting summary with Rich formatting."""
    console.print()

    overall = extract_section(summary, "SUMMARY")
    console.print(Panel(overall, title="📋 Meeting Summary", border_style="bright_blue", padding=(1, 2)))

    attendees = extract_section(summary, "ATTENDEES")
    console.print(Panel(attendees, title="👥 Attendees", border_style="cyan", padding=(1, 2)))

    agenda = extract_section(summary, "AGENDA TOPICS")
    console.print(Panel(agenda, title="📌 Agenda Topics", border_style="green", padding=(1, 2)))

    decisions = extract_section(summary, "KEY DECISIONS")
    console.print(Panel(decisions, title="✅ Key Decisions", border_style="yellow", padding=(1, 2)))

    action_items = parse_action_items(summary)
    if action_items:
        table = Table(title="📝 Action Items", show_header=True, header_style="bold magenta", border_style="magenta")
        table.add_column("Who", style="bold cyan", min_width=15)
        table.add_column("What", style="white", min_width=30)
        table.add_column("When", style="yellow", min_width=12)
        for item in action_items:
            table.add_row(item["who"], item["what"], item["when"])
        console.print(table)
    else:
        console.print(Panel("No action items identified.", title="📝 Action Items", border_style="magenta"))

    followups = extract_section(summary, "FOLLOW-UPS")
    console.print(Panel(followups, title="🔄 Follow-ups", border_style="bright_red", padding=(1, 2)))
    console.print()


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.option("--config", "config_path", type=click.Path(), default=None, help="Path to config.yaml.")
@click.pass_context
def cli(ctx, verbose: bool, config_path: str | None):
    """📋 Meeting Summarizer - Extract insights from meeting transcripts."""
    setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config_path)


@cli.command()
@click.option("--transcript", required=True, type=click.Path(), help="Path to transcript file.")
@click.option("--output", default=None, type=click.Path(), help="Save summary to file.")
@click.pass_context
def summarize(ctx, transcript: str, output: str | None):
    """Summarize a meeting transcript."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        transcript_text = read_transcript(transcript)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    console.print(f"[dim]Loaded transcript: {transcript} ({len(transcript_text)} chars)[/dim]")

    with console.status("[bold green]Analyzing meeting transcript...[/bold green]"):
        summary = summarize_meeting(transcript_text, config)

    display_summary(summary)

    if output:
        save_summary(summary, output)
        console.print(f"[green]✅ Summary saved to: {output}[/green]")


@cli.command()
@click.option("--transcript", required=True, type=click.Path(), help="Path to transcript file.")
@click.pass_context
def speakers(ctx, transcript: str):
    """Identify and profile speakers from a transcript."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        transcript_text = read_transcript(transcript)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold cyan]Identifying speakers...[/bold cyan]"):
        result = identify_speakers(transcript_text, config)

    console.print(Panel(Markdown(result), title="👥 Speaker Identification", border_style="cyan", padding=(1, 2)))


@cli.command()
@click.option("--transcript", required=True, type=click.Path(), help="Path to transcript file.")
@click.pass_context
def decisions(ctx, transcript: str):
    """Extract decision log from a transcript."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        transcript_text = read_transcript(transcript)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold yellow]Extracting decisions...[/bold yellow]"):
        result = extract_decision_log(transcript_text, config)

    console.print(Panel(Markdown(result), title="✅ Decision Log", border_style="yellow", padding=(1, 2)))


@cli.command()
@click.option("--transcript", required=True, type=click.Path(), help="Path to transcript file.")
@click.pass_context
def followups(ctx, transcript: str):
    """Generate follow-up reminders from a transcript."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        transcript_text = read_transcript(transcript)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold red]Generating follow-up reminders...[/bold red]"):
        result = generate_followup_reminders(transcript_text, config)

    console.print(Panel(Markdown(result), title="🔄 Follow-up Reminders", border_style="red", padding=(1, 2)))


def main():
    cli()


if __name__ == "__main__":
    main()
