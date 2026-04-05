"""Click CLI interface for Stack Explainer."""

import sys
import os
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import check_ollama_running

from .config import load_config, setup_logging, SUPPORTED_LANGUAGES
from .core import explain_trace, generate_fix_code, find_similar_errors
from .utils import read_trace_from_file

console = Console()
logger = logging.getLogger(__name__)


def _read_stdin() -> str:
    """Read from stdin if available."""
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


@click.group()
@click.option("--config", "config_path", default=None, help="Path to config.yaml.")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.pass_context
def cli(ctx, config_path, verbose):
    """🔥 Stack Trace Explainer — Understand errors in plain English."""
    ctx.ensure_object(dict)
    config = load_config(config_path)
    if verbose:
        config.log_level = "DEBUG"
    setup_logging(config)
    ctx.obj["config"] = config


@cli.command()
@click.option("--trace", "-t", type=click.Path(exists=True), help="File containing the stack trace.")
@click.option("--lang", "-l", default="", help="Language hint (python, javascript, java, etc.).")
@click.option("--text", help="Paste stack trace directly as text.")
@click.option("--fix", is_flag=True, help="Generate fix code suggestions.")
@click.option("--similar", is_flag=True, help="Find similar/related errors.")
@click.pass_context
def explain(ctx, trace, lang, text, fix, similar):
    """Explain a stack trace in plain English."""
    config = ctx.obj["config"]

    console.print(Panel(
        "[bold cyan]🔥 Stack Trace Explainer[/bold cyan]\n"
        "Understand stack traces and errors in plain English",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running. Start it with: ollama serve")
        sys.exit(1)

    # Get trace from various sources
    trace_text = ""
    if text:
        trace_text = text
        console.print("[dim]Reading trace from --text argument[/dim]")
    elif trace:
        trace_text = read_trace_from_file(trace)
        if trace_text is None:
            console.print(f"[red]Error:[/red] Could not read file: {trace}")
            sys.exit(1)
        console.print(f"[dim]Reading trace from:[/dim] {trace}")
    else:
        trace_text = _read_stdin()
        if trace_text:
            console.print("[dim]Reading trace from stdin[/dim]")

    if not trace_text.strip():
        console.print(
            "[yellow]No stack trace provided.[/yellow]\n"
            "Usage: python -m stack_explainer.cli explain --trace error.txt\n"
            "   or: python -m stack_explainer.cli explain --text \"Traceback ...\""
        )
        sys.exit(1)

    # Show the trace
    console.print(Panel(trace_text.strip()[:2000], title="📜 Stack Trace", border_style="red"))

    with console.status("[bold cyan]Analyzing stack trace...[/bold cyan]", spinner="dots"):
        result = explain_trace(trace_text, lang, config)

    if result.get("language") and result["language"] != "unknown":
        console.print(f"[dim]Detected language:[/dim] {result['language']}")
    if result.get("error_hint"):
        console.print(f"[dim]Quick hint:[/dim] {result['error_hint']}")

    console.print()
    console.print(Panel(Markdown(result["explanation"]), title="💡 Explanation & Fix", border_style="green"))

    if fix:
        with console.status("[bold cyan]Generating fix code...[/bold cyan]", spinner="dots"):
            fix_code = generate_fix_code(trace_text, result["explanation"], config)
        console.print(Panel(Markdown(fix_code), title="🔧 Fix Code", border_style="yellow"))

    if similar:
        with console.status("[bold cyan]Finding similar errors...[/bold cyan]", spinner="dots"):
            similar_text = find_similar_errors(trace_text, config)
        console.print(Panel(Markdown(similar_text), title="🔗 Related Errors", border_style="blue"))


def main():
    """Entry point for the CLI."""
    cli(obj={})


if __name__ == "__main__":
    main()
