"""Click CLI interface for Regex Gen."""

import sys
import os
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import check_ollama_running

from .config import load_config, setup_logging, REGEX_FLAVORS
from .core import generate_regex, explain_regex, get_pattern_from_library, list_library_patterns
from .utils import run_regex_test, validate_regex

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.option("--config", "config_path", default=None, help="Path to config.yaml.")
@click.option("--verbose", "-v", is_flag=True, help="Verbose logging.")
@click.pass_context
def cli(ctx, config_path, verbose):
    """🔤 Regex Generator — Generate, explain, and test regular expressions with AI."""
    ctx.ensure_object(dict)
    config = load_config(config_path)
    if verbose:
        config.log_level = "DEBUG"
    setup_logging(config)
    ctx.obj["config"] = config


@cli.command()
@click.argument("description")
@click.option("--flavor", "-f", type=click.Choice(REGEX_FLAVORS), default="python", help="Regex flavor.")
@click.option("--test", "-t", multiple=True, help="Test strings to validate.")
@click.pass_context
def generate(ctx, description, flavor, test):
    """Generate a regex from a natural language description."""
    config = ctx.obj["config"]
    console.print(Panel(
        "[bold cyan]🔤 Regex Generator[/bold cyan]\nGenerate regex from natural language",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running.")
        sys.exit(1)

    console.print(f'[dim]Description:[/dim] "{description}"')
    console.print(f"[dim]Flavor:[/dim] {flavor}\n")

    with console.status("[bold cyan]Generating regex...[/bold cyan]", spinner="dots"):
        result = generate_regex(description, flavor, config)

    console.print(Panel(Markdown(result["explanation"]), title="🎯 Generated Regex", border_style="green"))

    if test and result.get("primary_pattern"):
        _show_test_results(result["primary_pattern"], list(test))


@cli.command()
@click.argument("pattern")
@click.pass_context
def explain(ctx, pattern):
    """Explain an existing regex pattern in plain English."""
    config = ctx.obj["config"]
    console.print(Panel(
        "[bold cyan]🔤 Regex Explainer[/bold cyan]",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running.")
        sys.exit(1)

    console.print(f"[dim]Pattern:[/dim] {pattern}\n")

    with console.status("[bold cyan]Analyzing regex...[/bold cyan]", spinner="dots"):
        result = explain_regex(pattern, config)

    console.print(Panel(Markdown(result["explanation"]), title="📖 Regex Explanation", border_style="green"))


@cli.command()
@click.argument("pattern")
@click.argument("strings", nargs=-1, required=True)
def test(pattern, strings):
    """Test a regex pattern against strings."""
    console.print(Panel("[bold cyan]🧪 Regex Tester[/bold cyan]", border_style="cyan"))
    _show_test_results(pattern, list(strings))


@cli.command()
@click.argument("name", required=False)
def library(name):
    """Browse the built-in pattern library."""
    if name:
        pattern = get_pattern_from_library(name)
        if pattern:
            console.print(f"[bold]{name}:[/bold] [cyan]{pattern}[/cyan]")
            val = validate_regex(pattern)
            console.print(f"[dim]Valid: {val['valid']} | Groups: {val.get('groups', 0)}[/dim]")
        else:
            console.print(f"[yellow]Pattern '{name}' not found in library.[/yellow]")
            console.print(f"[dim]Available: {', '.join(list_library_patterns().keys())}[/dim]")
    else:
        table = Table(title="📚 Pattern Library", border_style="cyan")
        table.add_column("Name", style="bold")
        table.add_column("Pattern", style="cyan")
        for n, p in list_library_patterns().items():
            table.add_row(n, p)
        console.print(table)


def _show_test_results(pattern: str, strings: list[str]):
    """Display test results in a table."""
    results = run_regex_test(pattern, strings)
    if results:
        table = Table(title=f"Pattern: {pattern}", border_style="cyan")
        table.add_column("String", style="white")
        table.add_column("Matches", style="green")
        table.add_column("Match Text", style="yellow")
        table.add_column("Position", style="dim")
        for r in results:
            table.add_row(
                r["string"],
                "✅" if r.get("matches") else "❌",
                r.get("match_text") or "-",
                str(r.get("span")) if r.get("span") else "-",
            )
        console.print(table)


def main():
    """Entry point."""
    cli(obj={})


if __name__ == "__main__":
    main()
