"""Click CLI interface for Code Reviewer."""

import sys
import os
import logging
import glob as glob_module

import click
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.markdown import Markdown
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import check_ollama_running

from .config import load_config, setup_logging
from .core import review_single_file, review_multiple_files, generate_autofix, export_report
from .utils import detect_language, SEVERITY_COLORS, CATEGORY_ICONS

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.option("--config", "config_path", default=None, help="Path to config.yaml file.")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.pass_context
def cli(ctx, config_path, verbose):
    """🔍 Code Review Bot — AI-powered code review with severity scoring."""
    ctx.ensure_object(dict)
    config = load_config(config_path)
    if verbose:
        config.log_level = "DEBUG"
    setup_logging(config)
    ctx.obj["config"] = config


@cli.command()
@click.option("--file", "-f", "filepath", required=True, help="Path to code file to review.")
@click.option("--focus", "-F", default="", help="Comma-separated focus areas (e.g., 'security,performance').")
@click.option("--show-code", is_flag=True, help="Display source code before review.")
@click.option("--autofix", is_flag=True, help="Generate auto-fix suggestions.")
@click.option("--output", "-o", default="", help="Export report to file (supports .md, .json).")
@click.pass_context
def review(ctx, filepath, focus, show_code, autofix, output):
    """Review a single code file."""
    config = ctx.obj["config"]
    console.print(Panel(
        "[bold cyan]🔍 Code Review Bot[/bold cyan]\n"
        "AI-powered code review with severity scoring & auto-fix",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running. Start it with: ollama serve")
        sys.exit(1)

    focus_areas = [f.strip() for f in focus.split(",") if f.strip()] if focus else []
    if focus_areas:
        console.print(f"[dim]Focus areas:[/dim] {', '.join(focus_areas)}")
    console.print(f"[dim]Reviewing:[/dim] {filepath}\n")

    if show_code:
        from .utils import read_file_safe
        code = read_file_safe(filepath)
        if code:
            lang = detect_language(filepath)
            syntax = Syntax(code, lang, line_numbers=True, theme="monokai")
            console.print(Panel(syntax, title=f"📄 {os.path.basename(filepath)}", border_style="dim"))
            console.print()

    with console.status("[bold cyan]Analyzing code...[/bold cyan]", spinner="dots"):
        result = review_single_file(filepath, focus_areas, config)

    if result.get("error"):
        console.print(f"[red]Error:[/red] {result['error']}")
        sys.exit(1)

    console.print(Panel(Markdown(result["review"]), title="📋 Code Review Results", border_style="green"))

    if autofix:
        console.print()
        with console.status("[bold cyan]Generating auto-fix...[/bold cyan]", spinner="dots"):
            fix = generate_autofix(filepath, result["review"], config)
        console.print(Panel(Markdown(fix), title="🔧 Auto-Fix Suggestions", border_style="yellow"))

    if output:
        fmt = "json" if output.endswith(".json") else "markdown"
        export_report([result], output, fmt)
        console.print(f"\n[green]✅ Report exported to:[/green] {output}")

    # Summary table
    table = Table(title="Review Summary", border_style="cyan")
    table.add_column("File", style="white")
    table.add_column("Language", style="cyan")
    table.add_column("Lines", style="dim")
    table.add_column("Focus", style="yellow")
    table.add_column("Status", style="green")
    table.add_row(
        result.get("filename", ""),
        result.get("language", ""),
        str(result.get("lines", 0)),
        ", ".join(focus_areas) if focus_areas else "All",
        "✅ Complete",
    )
    console.print(table)


@cli.command(name="review-dir")
@click.option("--dir", "-d", "directory", required=True, help="Directory to review.")
@click.option("--pattern", "-p", default="*.py", help="File glob pattern (default: *.py).")
@click.option("--focus", "-F", default="", help="Comma-separated focus areas.")
@click.option("--output", "-o", default="", help="Export report to file.")
@click.pass_context
def review_dir(ctx, directory, pattern, focus, output):
    """Review all matching files in a directory."""
    config = ctx.obj["config"]
    console.print(Panel(
        "[bold cyan]🔍 Multi-File Code Review[/bold cyan]",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running.")
        sys.exit(1)

    files = sorted(glob_module.glob(os.path.join(directory, "**", pattern), recursive=True))
    if not files:
        console.print(f"[yellow]No files matching '{pattern}' found in {directory}[/yellow]")
        sys.exit(0)

    console.print(f"[dim]Found {len(files)} file(s) to review[/dim]\n")
    focus_areas = [f.strip() for f in focus.split(",") if f.strip()] if focus else []

    results = []
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        task = progress.add_task("Reviewing files...", total=len(files))
        for fp in files:
            result = review_single_file(fp, focus_areas, config)
            results.append(result)
            progress.advance(task)

    for r in results:
        if not r.get("error"):
            console.print(Panel(
                Markdown(r["review"]),
                title=f"📋 {r.get('filename', '')}",
                border_style="green",
            ))

    if output:
        fmt = "json" if output.endswith(".json") else "markdown"
        export_report(results, output, fmt)
        console.print(f"\n[green]✅ Report exported to:[/green] {output}")


def main():
    """Entry point for the CLI."""
    cli(obj={})


if __name__ == "__main__":
    main()
