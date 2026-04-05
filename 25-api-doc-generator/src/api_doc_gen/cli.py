"""Click CLI interface for API Doc Gen."""

import sys
import os
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import check_ollama_running

from .config import load_config, setup_logging
from .core import generate_docs, generate_openapi, export_docs
from .utils import find_python_files

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.option("--config", "config_path", default=None, help="Path to config.yaml.")
@click.option("--verbose", "-v", is_flag=True, help="Verbose logging.")
@click.pass_context
def cli(ctx, config_path, verbose):
    """📚 API Doc Generator — Generate API docs from Python source code."""
    ctx.ensure_object(dict)
    config = load_config(config_path)
    if verbose:
        config.log_level = "DEBUG"
    setup_logging(config)
    ctx.obj["config"] = config


@cli.command()
@click.option("--source", "-s", required=True, help="Path to source file or directory.")
@click.option("--output", "-o", default="", help="Output file path (e.g., docs.md).")
@click.pass_context
def generate(ctx, source, output):
    """Generate Markdown API documentation."""
    config = ctx.obj["config"]
    console.print(Panel(
        "[bold cyan]📚 API Doc Generator[/bold cyan]\n"
        "Generate API documentation from Python source code",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running.")
        sys.exit(1)

    console.print(f"[dim]Source:[/dim] {source}")
    files = find_python_files(source)
    if not files:
        console.print(f"[yellow]No Python files found at {source}[/yellow]")
        sys.exit(1)
    console.print(f"[dim]Found {len(files)} Python file(s)[/dim]\n")

    with console.status("[bold cyan]Generating documentation...[/bold cyan]", spinner="dots"):
        result = generate_docs(source, config)

    if output:
        export_docs(result["docs"], output)
        console.print(f"[green]✅ Documentation written to:[/green] {output}")
    else:
        console.print(Panel(Markdown(result["docs"]), title="📚 API Documentation", border_style="green"))

    console.print(f"\n[dim]Files processed: {len(result['files'])} | Items documented: {result['items_count']}[/dim]")


@cli.command()
@click.option("--source", "-s", required=True, help="Path to source file or directory.")
@click.option("--output", "-o", default="", help="Output file path (e.g., openapi.yaml).")
@click.pass_context
def openapi(ctx, source, output):
    """Generate OpenAPI/Swagger specification."""
    config = ctx.obj["config"]
    console.print(Panel(
        "[bold cyan]📚 OpenAPI Generator[/bold cyan]",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running.")
        sys.exit(1)

    with console.status("[bold cyan]Generating OpenAPI spec...[/bold cyan]", spinner="dots"):
        result = generate_openapi(source, config)

    if output:
        export_docs(result["openapi_yaml"], output)
        console.print(f"[green]✅ OpenAPI spec written to:[/green] {output}")
    else:
        console.print(Panel(result["openapi_yaml"], title="📄 OpenAPI Specification", border_style="green"))


@cli.command()
@click.option("--source", "-s", required=True, help="Path to source file or directory.")
def inspect(source):
    """Inspect source code structure without generating docs."""
    files = find_python_files(source)
    if not files:
        console.print(f"[yellow]No Python files found at {source}[/yellow]")
        return

    from .utils import extract_functions
    from rich.table import Table

    for f in files:
        items = extract_functions(f)
        if items:
            table = Table(title=f"📄 {os.path.basename(f)}", border_style="cyan")
            table.add_column("Type", style="bold")
            table.add_column("Name", style="cyan")
            table.add_column("Args / Methods")
            table.add_column("Line", style="dim")
            for item in items:
                if item["type"] == "function":
                    args = ", ".join(a["name"] for a in item["args"])
                    table.add_row("fn", item["name"], args, str(item["lineno"]))
                elif item["type"] == "class":
                    methods = ", ".join(m["name"] for m in item["methods"])
                    table.add_row("class", item["name"], methods, str(item["lineno"]))
            console.print(table)


def main():
    """Entry point."""
    cli(obj={})


if __name__ == "__main__":
    main()
