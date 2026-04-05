"""CLI interface for Legal Case Researcher.

Provides a rich command-line experience for legal research tasks.
"""

import os
import sys
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text
from rich import box

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from common.llm_client import check_ollama_running
from src.case_researcher.core import (
    research_case_law,
    find_precedents,
    analyze_legal_argument,
    extract_citations,
    summarize_case,
    LEGAL_DISCLAIMER,
    SAMPLE_SCENARIOS,
    get_strength_color,
    get_strength_emoji,
)

console = Console()

BANNER = r"""
  ⚖️  Legal Case Researcher
  ─────────────────────────────
  AI-Powered • 100% Local • Private
"""


def _check_ollama() -> None:
    """Verify Ollama is running, exit if not."""
    if not check_ollama_running():
        console.print("[bold red]Error:[/] Ollama is not running. Start it with: ollama serve")
        raise SystemExit(1)


@click.group()
@click.version_option(version="1.0.0", prog_name="Legal Case Researcher")
def cli():
    """⚖️  Legal Case Researcher — AI-powered case law research with complete privacy.

    All processing happens locally using Gemma 4 via Ollama.
    No data ever leaves your machine. Attorney-client privilege protected.
    """
    pass


@cli.command()
@click.argument("query")
@click.option("--jurisdiction", "-j", default="federal", help="Jurisdiction filter (federal, state, etc.)")
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def research(query: str, jurisdiction: str, model: str):
    """Research case law for a given legal question."""
    _check_ollama()
    console.print(Panel(BANNER, style="bold gold1"))
    console.print(f"\n🔍 Researching: [bold]{query}[/bold]")
    console.print(f"📍 Jurisdiction: [cyan]{jurisdiction}[/cyan]\n")

    with console.status("[bold green]Researching case law..."):
        result = research_case_law(query, jurisdiction=jurisdiction, model=model)

    # Summary
    console.print(Panel(result.summary, title="📋 Research Summary", border_style="blue"))

    # Cases table
    if result.relevant_cases:
        table = Table(title="📚 Relevant Cases", box=box.ROUNDED, show_lines=True)
        table.add_column("Case", style="bold", max_width=30)
        table.add_column("Citation", style="cyan")
        table.add_column("Year", style="green", justify="center")
        table.add_column("Court", style="yellow")
        table.add_column("Key Holding", max_width=40)

        for case in result.relevant_cases:
            table.add_row(
                case.case_name,
                case.citation,
                case.year,
                case.court,
                case.key_holding,
            )
        console.print(table)

    # Principles
    if result.key_legal_principles:
        console.print("\n[bold]⚖️  Key Legal Principles:[/bold]")
        for i, principle in enumerate(result.key_legal_principles, 1):
            console.print(f"  {i}. {principle}")

    # Analysis
    if result.analysis:
        console.print(Panel(result.analysis, title="📝 Analysis", border_style="green"))

    # Search terms
    if result.suggested_search_terms:
        terms = ", ".join(result.suggested_search_terms)
        console.print(f"\n🔎 Suggested search terms: [dim]{terms}[/dim]")

    console.print(f"\n[dim]{LEGAL_DISCLAIMER}[/dim]")


@cli.command()
@click.option("--facts", "-f", required=True, help="Description of case facts")
@click.option("--issue", "-i", required=True, help="The legal issue to research")
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def precedents(facts: str, issue: str, model: str):
    """Find relevant legal precedents for given case facts."""
    _check_ollama()
    console.print(Panel(BANNER, style="bold gold1"))
    console.print(f"\n📚 Finding precedents for: [bold]{issue}[/bold]\n")

    with console.status("[bold green]Searching for precedents..."):
        results = find_precedents(facts, issue, model=model)

    if not results:
        console.print("[yellow]No precedents found. Try rephrasing your query.[/yellow]")
        return

    for i, p in enumerate(results, 1):
        score_color = "green" if p.relevance_score >= 0.7 else "yellow" if p.relevance_score >= 0.4 else "red"
        panel_content = (
            f"[bold]Citation:[/bold] {p.citation}\n"
            f"[bold]Relevance:[/bold] [{score_color}]{p.relevance_score:.0%}[/{score_color}]\n\n"
            f"[bold]Factual Similarity:[/bold]\n{p.factual_similarity}\n\n"
            f"[bold]Legal Similarity:[/bold]\n{p.legal_similarity}\n\n"
            f"[bold]Recommendation:[/bold]\n{p.recommendation}"
        )
        console.print(Panel(
            panel_content,
            title=f"#{i} — {p.case_name}",
            border_style=score_color,
        ))

        if p.distinguishing_factors:
            console.print("  [bold]Distinguishing Factors:[/bold]")
            for f_item in p.distinguishing_factors:
                console.print(f"    • {f_item}")

        if p.applicable_holdings:
            console.print("  [bold]Applicable Holdings:[/bold]")
            for h in p.applicable_holdings:
                console.print(f"    • {h}")
        console.print()

    console.print(f"\n[dim]{LEGAL_DISCLAIMER}[/dim]")


@cli.command()
@click.argument("argument")
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def analyze(argument: str, model: str):
    """Analyze the strength of a legal argument."""
    _check_ollama()
    console.print(Panel(BANNER, style="bold gold1"))
    console.print(f"\n📋 Analyzing argument...\n")

    with console.status("[bold green]Analyzing legal argument..."):
        result = analyze_legal_argument(argument, model=model)

    color = get_strength_color(result.strength)
    emoji = get_strength_emoji(result.strength)

    console.print(Panel(
        f"[bold]Strength:[/bold] [{color}]{emoji} {result.strength.upper()}[/{color}]\n"
        f"[bold]Confidence:[/bold] {result.confidence_score:.0%}\n\n"
        f"[bold]Summary:[/bold]\n{result.argument_summary}",
        title="⚖️  Argument Analysis",
        border_style=color,
    ))

    if result.supporting_points:
        console.print("\n[bold green]✅ Supporting Points:[/bold green]")
        for p in result.supporting_points:
            console.print(f"  • {p}")

    if result.weaknesses:
        console.print("\n[bold red]❌ Weaknesses:[/bold red]")
        for w in result.weaknesses:
            console.print(f"  • {w}")

    if result.counter_arguments:
        console.print("\n[bold yellow]⚔️  Counter Arguments:[/bold yellow]")
        for c in result.counter_arguments:
            console.print(f"  • {c}")

    if result.suggested_improvements:
        console.print("\n[bold blue]💡 Suggested Improvements:[/bold blue]")
        for s in result.suggested_improvements:
            console.print(f"  • {s}")

    if result.relevant_doctrines:
        console.print("\n[bold magenta]📖 Relevant Doctrines:[/bold magenta]")
        for d in result.relevant_doctrines:
            console.print(f"  • {d}")

    console.print(f"\n[dim]{LEGAL_DISCLAIMER}[/dim]")


@cli.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def citations(filepath: str, model: str):
    """Extract legal citations from a file."""
    _check_ollama()
    console.print(Panel(BANNER, style="bold gold1"))

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    console.print(f"\n📄 Extracting citations from: [bold]{filepath}[/bold]\n")

    with console.status("[bold green]Extracting citations..."):
        results = extract_citations(text, model=model)

    if not results:
        console.print("[yellow]No citations found in the document.[/yellow]")
        return

    table = Table(title="📎 Extracted Citations", box=box.ROUNDED, show_lines=True)
    table.add_column("#", style="dim", justify="right")
    table.add_column("Case Name", style="bold", max_width=30)
    table.add_column("Citation", style="cyan")
    table.add_column("Year", style="green", justify="center")
    table.add_column("Court", style="yellow")
    table.add_column("Key Holding", max_width=35)

    for i, c in enumerate(results, 1):
        table.add_row(str(i), c.case_name, c.citation, c.year, c.court, c.key_holding)

    console.print(table)
    console.print(f"\n  Found [bold]{len(results)}[/bold] citation(s).")
    console.print(f"\n[dim]{LEGAL_DISCLAIMER}[/dim]")


@cli.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def summarize(filepath: str, model: str):
    """Summarize a legal case document."""
    _check_ollama()
    console.print(Panel(BANNER, style="bold gold1"))

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    console.print(f"\n📄 Summarizing: [bold]{filepath}[/bold]\n")

    with console.status("[bold green]Summarizing case document..."):
        result = summarize_case(text, model=model)

    if result.get("parse_error"):
        console.print(Panel(result.get("summary", ""), title="Case Summary"))
        return

    console.print(Panel(
        f"[bold]Case:[/bold] {result.get('case_name', 'N/A')}\n"
        f"[bold]Citation:[/bold] {result.get('citation', 'N/A')}\n"
        f"[bold]Court:[/bold] {result.get('court', 'N/A')}\n"
        f"[bold]Date:[/bold] {result.get('date_decided', 'N/A')}\n"
        f"[bold]Judge:[/bold] {result.get('judge', 'N/A')}",
        title="📋 Case Information",
        border_style="blue",
    ))

    parties = result.get("parties", {})
    if parties:
        console.print(f"\n  [bold]Plaintiff:[/bold] {parties.get('plaintiff', 'N/A')}")
        console.print(f"  [bold]Defendant:[/bold] {parties.get('defendant', 'N/A')}")

    if result.get("facts"):
        console.print(Panel(result["facts"], title="📝 Facts", border_style="cyan"))

    if result.get("issues"):
        console.print("\n[bold]⚖️  Legal Issues:[/bold]")
        for issue in result["issues"]:
            console.print(f"  • {issue}")

    if result.get("holding"):
        console.print(Panel(result["holding"], title="🔨 Holding", border_style="green"))

    if result.get("reasoning"):
        console.print(Panel(result["reasoning"], title="💭 Reasoning", border_style="yellow"))

    if result.get("rule_of_law"):
        console.print(Panel(result["rule_of_law"], title="📖 Rule of Law", border_style="magenta"))

    if result.get("significance"):
        console.print(Panel(result["significance"], title="⭐ Significance", border_style="gold1"))

    if result.get("key_quotes"):
        console.print("\n[bold]💬 Key Quotes:[/bold]")
        for q in result["key_quotes"]:
            console.print(f'  "{q}"')

    if result.get("dissent_summary"):
        console.print(Panel(result["dissent_summary"], title="👎 Dissenting Opinion", border_style="red"))

    console.print(f"\n[dim]{LEGAL_DISCLAIMER}[/dim]")


@cli.command()
def disclaimer():
    """Display the legal disclaimer."""
    console.print(Panel(
        LEGAL_DISCLAIMER,
        title="⚠️  Legal Disclaimer",
        border_style="red",
        padding=(1, 2),
    ))
    console.print(
        "\n[bold]This tool is designed to assist legal professionals with research.[/bold]\n"
        "It is not a substitute for professional legal judgment.\n\n"
        "🔒 [green]All processing happens locally on your machine.[/green]\n"
        "🔒 [green]No data is sent to any external server.[/green]\n"
        "🔒 [green]Attorney-client privilege is fully protected.[/green]\n"
    )


@cli.command()
def samples():
    """Show sample legal research scenarios."""
    console.print(Panel(BANNER, style="bold gold1"))
    console.print("\n[bold]📚 Sample Legal Research Scenarios[/bold]\n")

    table = Table(box=box.ROUNDED, show_lines=True)
    table.add_column("ID", style="dim")
    table.add_column("Title", style="bold")
    table.add_column("Jurisdiction", style="cyan", justify="center")
    table.add_column("Query", max_width=50)

    for key, scenario in SAMPLE_SCENARIOS.items():
        table.add_row(
            key,
            scenario["title"],
            scenario["jurisdiction"],
            scenario["query"],
        )

    console.print(table)
    console.print(
        "\n[dim]Use these scenarios with the research or precedents commands.[/dim]\n"
        "Example: [bold]case-researcher research \"What constitutes material breach of contract?\"[/bold]\n"
    )


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
