"""
Contract Clause Analyzer - Command-line interface.

⚖️ LEGAL DISCLAIMER: This tool provides AI-assisted contract analysis for
informational purposes only. It is NOT legal advice.

🔒 PRIVACY: All processing happens locally. No data ever leaves your machine.
"""

import sys
import click
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from contract_analyzer.core import (
    LEGAL_DISCLAIMER,
    SAMPLE_CLAUSES,
    analyze_clause,
    analyze_contract,
    compare_clauses,
    get_risk_color,
    get_risk_emoji,
    check_ollama_running,
)

console = Console()


@click.group()
def cli():
    """⚖️ Contract Clause Analyzer - AI-powered contract analysis with complete privacy."""
    pass


@cli.command()
def disclaimer():
    """Show legal disclaimer."""
    console.print(Panel(LEGAL_DISCLAIMER, title="⚖️ Legal Disclaimer", border_style="yellow"))


@cli.command()
@click.option("--text", "-t", help="Contract clause text to analyze")
@click.option("--file", "-f", "file_path", type=click.Path(exists=True), help="File containing clause text")
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def analyze(text: str, file_path: str, model: str):
    """Analyze a contract clause for risks and obligations."""
    if not check_ollama_running():
        console.print("[red]Error: Ollama is not running. Start it with: ollama serve[/red]")
        sys.exit(1)

    if file_path:
        with open(file_path, 'r') as f:
            text = f.read()
    elif not text:
        text = Prompt.ask("[cyan]Paste the contract clause to analyze[/cyan]")

    if not text.strip():
        console.print("[red]No text provided.[/red]")
        return

    console.print("\n[yellow]⏳ Analyzing clause...[/yellow]\n")
    result = analyze_clause(text, model=model)

    # Display results
    risk_emoji = get_risk_emoji(result.risk_level)
    risk_color = get_risk_color(result.risk_level)

    console.print(Panel(
        f"[bold]Type:[/bold] {result.clause_type.replace('_', ' ').title()}\n"
        f"[bold]Risk:[/bold] [{risk_color}]{risk_emoji} {result.risk_level.upper()}[/{risk_color}]\n"
        f"[bold]Summary:[/bold] {result.summary}",
        title="📋 Clause Analysis",
        border_style="blue"
    ))

    if result.obligations:
        table = Table(title="📌 Obligations", show_header=True, header_style="bold cyan")
        table.add_column("#", style="dim", width=4)
        table.add_column("Obligation", style="white")
        for i, ob in enumerate(result.obligations, 1):
            table.add_row(str(i), ob)
        console.print(table)

    if result.deadlines:
        table = Table(title="⏰ Deadlines", show_header=True, header_style="bold yellow")
        table.add_column("#", style="dim", width=4)
        table.add_column("Deadline", style="white")
        for i, dl in enumerate(result.deadlines, 1):
            table.add_row(str(i), dl)
        console.print(table)

    if result.red_flags:
        table = Table(title="🚩 Red Flags", show_header=True, header_style="bold red")
        table.add_column("#", style="dim", width=4)
        table.add_column("Red Flag", style="red")
        for i, rf in enumerate(result.red_flags, 1):
            table.add_row(str(i), rf)
        console.print(table)

    if result.recommendations:
        table = Table(title="💡 Recommendations", show_header=True, header_style="bold green")
        table.add_column("#", style="dim", width=4)
        table.add_column("Recommendation", style="green")
        for i, rec in enumerate(result.recommendations, 1):
            table.add_row(str(i), rec)
        console.print(table)

    console.print(f"\n[dim]⚖️ This is not legal advice. Consult a qualified attorney.[/dim]")


@cli.command()
@click.option("--file", "-f", "file_path", type=click.Path(exists=True), required=True, help="Contract file to analyze")
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def full_analysis(file_path: str, model: str):
    """Analyze a complete contract document."""
    if not check_ollama_running():
        console.print("[red]Error: Ollama is not running. Start it with: ollama serve[/red]")
        sys.exit(1)

    with open(file_path, 'r') as f:
        contract_text = f.read()

    console.print("\n[yellow]⏳ Analyzing full contract...[/yellow]\n")
    result = analyze_contract(contract_text, model=model)

    risk_emoji = get_risk_emoji(result.overall_risk)
    risk_color = get_risk_color(result.overall_risk)

    console.print(Panel(
        f"[bold]Title:[/bold] {result.title}\n"
        f"[bold]Overall Risk:[/bold] [{risk_color}]{risk_emoji} {result.overall_risk.upper()}[/{risk_color}]\n"
        f"[bold]Total Clauses:[/bold] {result.total_clauses}\n"
        f"[bold]High Risk Clauses:[/bold] {result.high_risk_count}\n"
        f"[bold]Total Obligations:[/bold] {result.obligations_count}\n"
        f"[bold]Total Deadlines:[/bold] {result.deadlines_count}\n"
        f"[bold]Red Flags:[/bold] {result.red_flags_count}\n\n"
        f"[bold]Summary:[/bold] {result.summary}",
        title="📄 Full Contract Analysis",
        border_style="blue"
    ))

    for i, clause in enumerate(result.clause_analyses, 1):
        c_emoji = get_risk_emoji(clause.risk_level)
        c_color = get_risk_color(clause.risk_level)
        console.print(f"\n[bold]Clause {i}: {clause.clause_type.replace('_', ' ').title()}[/bold]")
        console.print(f"  Risk: [{c_color}]{c_emoji} {clause.risk_level.upper()}[/{c_color}]")
        console.print(f"  {clause.summary}")
        if clause.red_flags:
            for rf in clause.red_flags:
                console.print(f"  [red]🚩 {rf}[/red]")

    console.print(f"\n[dim]⚖️ This is not legal advice. Consult a qualified attorney.[/dim]")


@cli.command()
@click.option("--model", "-m", default="gemma4:latest", help="Ollama model to use")
def compare(model: str):
    """Compare two contract clauses."""
    if not check_ollama_running():
        console.print("[red]Error: Ollama is not running. Start it with: ollama serve[/red]")
        sys.exit(1)

    console.print("[cyan]Paste the first clause:[/cyan]")
    clause_a = Prompt.ask("Clause A")
    console.print("[cyan]Paste the second clause:[/cyan]")
    clause_b = Prompt.ask("Clause B")

    console.print("\n[yellow]⏳ Comparing clauses...[/yellow]\n")
    result = compare_clauses(clause_a, clause_b, model=model)

    if "differences" in result:
        table = Table(title="🔍 Key Differences", show_header=True, header_style="bold cyan")
        table.add_column("#", style="dim", width=4)
        table.add_column("Difference", style="white")
        for i, diff in enumerate(result.get("differences", []), 1):
            table.add_row(str(i), diff)
        console.print(table)

    if result.get("recommendation"):
        console.print(Panel(result["recommendation"], title="💡 Recommendation", border_style="green"))

    console.print(f"\n[dim]⚖️ This is not legal advice. Consult a qualified attorney.[/dim]")


@cli.command()
def samples():
    """Show sample contract clauses for testing."""
    for name, text in SAMPLE_CLAUSES.items():
        console.print(Panel(text, title=f"📋 {name.replace('_', ' ').title()}", border_style="blue"))


def main():
    """Entry point."""
    console.print(Panel(
        "[bold]⚖️ Contract Clause Analyzer[/bold]\n"
        "[dim]AI-powered contract analysis with complete privacy[/dim]\n"
        "[dim]🔒 100% Local • Zero Data Leakage • Attorney-Client Privilege Protected[/dim]",
        border_style="blue"
    ))
    cli()


if __name__ == "__main__":
    main()
