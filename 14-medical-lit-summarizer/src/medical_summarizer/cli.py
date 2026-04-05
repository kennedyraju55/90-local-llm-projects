"""Click CLI interface for Medical Literature Summarizer."""

import sys
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from .config import load_config
from .core import (
    SECTIONS,
    summarize_paper,
    extract_pico,
    rate_evidence_quality,
    format_citation,
)
from .utils import setup_logging, read_paper, get_llm_client

logger = logging.getLogger(__name__)
console = Console()

SECTION_STYLES = {
    "title_authors": "bold white", "abstract_summary": "green",
    "methodology": "yellow", "key_findings": "bright_cyan",
    "statistical_results": "magenta", "conclusions": "bright_green",
    "limitations": "red", "future_work": "blue",
}

SECTION_EMOJIS = {
    "title_authors": "📄", "abstract_summary": "📋",
    "methodology": "🔬", "key_findings": "🔑",
    "statistical_results": "📊", "conclusions": "✅",
    "limitations": "⚠️", "future_work": "🔮",
}


def format_output(results: dict) -> None:
    """Display the summarized paper results using Rich formatting."""
    console.print()
    console.print(Panel("[bold cyan]Medical Literature Summary[/bold cyan]",
                        border_style="bright_blue", expand=False))
    console.print()

    for section_key, section_title, _ in SECTIONS:
        content = results.get(section_key, "No content extracted.")
        style = SECTION_STYLES.get(section_key, "white")
        emoji = SECTION_EMOJIS.get(section_key, "📌")
        console.print(Panel(Markdown(content), title=f"{emoji} {section_title}",
                            border_style=style, padding=(1, 2)))
        console.print()


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.option("--config", "config_path", type=click.Path(), default=None, help="Path to config.yaml.")
@click.pass_context
def cli(ctx, verbose: bool, config_path: str | None):
    """🔬 Medical Literature Summarizer

    Summarizes medical and scientific papers by extracting key sections
    including methodology, findings, conclusions, and more.
    """
    setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config_path)


@cli.command()
@click.option("--paper", required=True, type=click.Path(), help="Path to the paper text file.")
@click.option("--detail", type=click.Choice(["brief", "standard", "comprehensive"]),
              default="standard", show_default=True)
@click.pass_context
def summarize(ctx, paper: str, detail: str):
    """Summarize a medical/scientific paper."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        paper_text = read_paper(paper)
        console.print(f"[green]✓[/green] Loaded paper ({len(paper_text):,} characters)")
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    console.print(f"[dim]Detail level:[/dim] [bold]{detail}[/bold]\n")
    console.print("[bold]Analyzing paper...[/bold]")
    results = summarize_paper(paper_text, detail, config)
    format_output(results)
    console.print("[bold green]Summary complete.[/bold green]\n")


@cli.command()
@click.option("--paper", required=True, type=click.Path(), help="Path to the paper text file.")
@click.pass_context
def pico(ctx, paper: str):
    """Extract PICO framework elements from a paper."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        paper_text = read_paper(paper)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold cyan]Extracting PICO elements...[/bold cyan]"):
        result = extract_pico(paper_text, config)

    console.print(Panel(Markdown(result), title="🔬 PICO Framework", border_style="cyan", padding=(1, 2)))


@cli.command()
@click.option("--paper", required=True, type=click.Path(), help="Path to the paper text file.")
@click.pass_context
def evidence(ctx, paper: str):
    """Rate the quality of evidence in a paper."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        paper_text = read_paper(paper)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status("[bold yellow]Rating evidence quality...[/bold yellow]"):
        result = rate_evidence_quality(paper_text, config)

    console.print(Panel(Markdown(result), title="📊 Evidence Quality", border_style="yellow", padding=(1, 2)))


@cli.command()
@click.option("--paper", required=True, type=click.Path(), help="Path to the paper text file.")
@click.option("--style", type=click.Choice(["APA", "MLA", "Chicago", "Vancouver"]),
              default="APA", show_default=True)
@click.pass_context
def cite(ctx, paper: str, style: str):
    """Format a citation for the paper."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]Error:[/bold red] Ollama is not running.")
        sys.exit(1)

    try:
        paper_text = read_paper(paper)
    except (FileNotFoundError, ValueError) as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    with console.status(f"[bold cyan]Formatting {style} citation...[/bold cyan]"):
        result = format_citation(paper_text, style, config)

    console.print(Panel(result, title=f"📚 {style} Citation", border_style="green", padding=(1, 2)))


def main():
    cli()


if __name__ == "__main__":
    main()
