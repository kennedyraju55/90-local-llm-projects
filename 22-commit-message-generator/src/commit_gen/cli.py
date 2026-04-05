"""Click CLI interface for Commit Gen."""

import sys
import os
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
from common.llm_client import check_ollama_running

from .config import load_config, setup_logging, COMMIT_TYPES
from .core import generate_commit_messages
from .utils import get_git_diff, get_git_stat, get_git_staged_files, get_git_branch, read_diff_from_stdin

console = Console()
logger = logging.getLogger(__name__)


@click.group()
@click.option("--config", "config_path", default=None, help="Path to config.yaml file.")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.pass_context
def cli(ctx, config_path, verbose):
    """📝 Commit Message Generator — AI-powered conventional commit messages."""
    ctx.ensure_object(dict)
    config = load_config(config_path)
    if verbose:
        config.log_level = "DEBUG"
    setup_logging(config)
    ctx.obj["config"] = config


@cli.command()
@click.option("--staged", is_flag=True, default=True, help="Use staged changes only (default).")
@click.option("--all", "all_changes", is_flag=True, help="Include unstaged changes too.")
@click.option("--type", "msg_type", type=click.Choice(COMMIT_TYPES, case_sensitive=False), help="Specify commit type.")
@click.option("--diff-file", type=click.Path(exists=True), help="Read diff from a file.")
@click.option("--no-emoji", is_flag=True, help="Disable emoji prefixes.")
@click.pass_context
def generate(ctx, staged, all_changes, msg_type, diff_file, no_emoji):
    """Generate commit messages from git diff."""
    config = ctx.obj["config"]
    if no_emoji:
        config.use_emoji = False

    console.print(Panel(
        "[bold cyan]📝 Commit Message Generator[/bold cyan]\n"
        "Generate conventional commit messages from git diffs",
        border_style="cyan",
    ))

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running. Start it with: ollama serve")
        sys.exit(1)

    # Get diff from various sources
    diff = ""
    if diff_file:
        with open(diff_file, "r", encoding="utf-8") as f:
            diff = f.read()
        console.print(f"[dim]Reading diff from:[/dim] {diff_file}")
    else:
        stdin_diff = read_diff_from_stdin()
        if stdin_diff:
            diff = stdin_diff
            console.print("[dim]Reading diff from stdin[/dim]")
        else:
            use_staged = not all_changes
            diff = get_git_diff(staged_only=use_staged)
            mode = "staged" if use_staged else "all"
            branch = get_git_branch()
            console.print(f"[dim]Branch:[/dim] {branch} | [dim]Mode:[/dim] {mode}")

    if not diff.strip():
        console.print("[yellow]No changes found.[/yellow] Stage some changes or provide a diff.")
        sys.exit(0)

    # Show diff stats
    stat = get_git_stat(staged_only=not all_changes)
    if stat:
        console.print(Panel(stat, title="📊 Changes Summary", border_style="dim"))

    # Show staged files
    files = get_git_staged_files()
    if files:
        console.print(f"[dim]Staged files:[/dim] {', '.join(files[:10])}")

    with console.status("[bold cyan]Generating commit messages...[/bold cyan]", spinner="dots"):
        result = generate_commit_messages(diff, msg_type or "", config)

    console.print()
    console.print(Panel(Markdown(result), title="💡 Suggested Commit Messages", border_style="green"))


@cli.command()
@click.argument("diff_text")
@click.option("--type", "msg_type", type=click.Choice(COMMIT_TYPES, case_sensitive=False), help="Commit type.")
@click.pass_context
def from_text(ctx, diff_text, msg_type):
    """Generate commit message from pasted diff text."""
    config = ctx.obj["config"]

    if not check_ollama_running():
        console.print("[red]Error:[/red] Ollama is not running.")
        sys.exit(1)

    with console.status("[bold cyan]Generating...[/bold cyan]", spinner="dots"):
        result = generate_commit_messages(diff_text, msg_type or "", config)

    console.print(Panel(Markdown(result), title="💡 Suggested Commit Messages", border_style="green"))


def main():
    """Entry point for the CLI."""
    cli(obj={})


if __name__ == "__main__":
    main()
