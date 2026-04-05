"""Click CLI interface for Resume Analyzer."""

import sys
import logging

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn

from .config import load_config
from .core import (
    analyze_resume,
    score_against_jd,
    simulate_ats_score,
    generate_improvement_suggestions,
)
from .utils import setup_logging, read_file, get_llm_client

logger = logging.getLogger(__name__)
console = Console()


def display_analysis(analysis: dict) -> None:
    """Display general resume analysis results with rich formatting."""
    score = analysis.get("overall_score", 0)
    console.print()

    score_color = "green" if score >= 75 else "yellow" if score >= 50 else "red"
    console.print(Panel(
        f"[bold {score_color}]{score}/100[/]",
        title="📊 Overall Resume Score", border_style=score_color, expand=False,
    ))

    with Progress(
        TextColumn("[bold blue]Score"),
        BarColumn(bar_width=50, complete_style=score_color),
        TextColumn(f"{score}%"),
        console=console, transient=True,
    ) as progress:
        progress.add_task("Score", total=100, completed=score)

    skills = analysis.get("skills", [])
    if skills:
        table = Table(title="🛠️  Extracted Skills", show_lines=True)
        table.add_column("#", style="dim", width=4)
        table.add_column("Skill", style="cyan")
        for i, skill in enumerate(skills, 1):
            table.add_row(str(i), skill)
        console.print(table)

    exp = analysis.get("experience_summary", "")
    if exp:
        console.print(Panel(exp, title="💼 Experience Summary", border_style="blue"))

    education = analysis.get("education", [])
    if education:
        console.print(Panel("\n".join(f"• {e}" for e in education), title="🎓 Education", border_style="blue"))

    achievements = analysis.get("achievements", [])
    if achievements:
        console.print(Panel("\n".join(f"⭐ {a}" for a in achievements), title="🏆 Achievements", border_style="green"))

    strengths = analysis.get("strengths", [])
    weaknesses = analysis.get("weaknesses", [])
    if strengths or weaknesses:
        sw_table = Table(title="💪 Strengths & Weaknesses", show_lines=True)
        sw_table.add_column("Strengths ✅", style="green")
        sw_table.add_column("Weaknesses ⚠️", style="red")
        for i in range(max(len(strengths), len(weaknesses))):
            s = strengths[i] if i < len(strengths) else ""
            w = weaknesses[i] if i < len(weaknesses) else ""
            sw_table.add_row(s, w)
        console.print(sw_table)

    for label, key, emoji in [
        ("Formatting Suggestions", "formatting_suggestions", "📐"),
        ("Content Suggestions", "content_suggestions", "📋"),
    ]:
        items = analysis.get(key, [])
        if items:
            console.print(Panel("\n".join(f"💡 {s}" for s in items), title=f"{emoji} {label}", border_style="yellow"))


def display_jd_score(result: dict) -> None:
    """Display JD scoring results with rich formatting."""
    match_pct = result.get("match_percentage", 0)
    console.print()

    match_color = "green" if match_pct >= 75 else "yellow" if match_pct >= 50 else "red"
    console.print(Panel(
        f"[bold {match_color}]{match_pct}%[/]",
        title="🎯 Resume-JD Match Score", border_style=match_color, expand=False,
    ))

    with Progress(
        TextColumn("[bold blue]Match"),
        BarColumn(bar_width=50, complete_style=match_color),
        TextColumn(f"{match_pct}%"),
        console=console, transient=True,
    ) as progress:
        progress.add_task("Match", total=100, completed=match_pct)

    matching = result.get("matching_skills", [])
    missing = result.get("missing_skills", [])
    if matching or missing:
        skills_table = Table(title="🛠️  Skills Comparison", show_lines=True)
        skills_table.add_column("Matching ✅", style="green")
        skills_table.add_column("Missing ❌", style="red")
        for i in range(max(len(matching), len(missing))):
            m = matching[i] if i < len(matching) else ""
            mi = missing[i] if i < len(missing) else ""
            skills_table.add_row(m, mi)
        console.print(skills_table)

    for key, title, style in [
        ("experience_alignment", "💼 Experience Alignment", "blue"),
        ("overall_assessment", "📝 Overall Assessment", "blue"),
    ]:
        text = result.get(key, "")
        if text:
            console.print(Panel(text, title=title, border_style=style))

    gaps = result.get("keyword_gaps", [])
    if gaps:
        console.print(Panel("\n".join(f"🔑 {k}" for k in gaps), title="🔍 Keyword Gaps", border_style="red"))

    priorities = result.get("priority_improvements", [])
    if priorities:
        pri_table = Table(title="🚀 Priority Improvements", show_lines=True)
        pri_table.add_column("Priority", style="bold", width=4)
        pri_table.add_column("Improvement", style="cyan")
        for i, p in enumerate(priorities, 1):
            pri_table.add_row(str(i), p)
        console.print(pri_table)


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.option("--config", "config_path", type=click.Path(), default=None, help="Path to config.yaml.")
@click.pass_context
def cli(ctx, verbose: bool, config_path: str | None):
    """📄 Resume Analyzer — Analyze resumes and score them against job descriptions."""
    setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config_path)


@cli.command()
@click.option("--resume", required=True, type=click.Path(), help="Path to the resume text file.")
@click.pass_context
def analyze(ctx, resume: str):
    """Perform general resume analysis."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]❌ Ollama is not running![/]")
        sys.exit(1)

    resume_text = read_file(resume)
    if not resume_text:
        raise click.ClickException("Resume file is empty.")

    console.print(f"[green]✓[/] Loaded resume: [cyan]{resume}[/]")
    with console.status("[bold cyan]Analyzing with LLM...", spinner="dots"):
        analysis = analyze_resume(resume_text, config)

    display_analysis(analysis)


@cli.command()
@click.option("--resume", required=True, type=click.Path(), help="Path to the resume text file.")
@click.option("--jd", required=True, type=click.Path(), help="Path to the job description file.")
@click.pass_context
def score(ctx, resume: str, jd: str):
    """Score resume against a job description."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]❌ Ollama is not running![/]")
        sys.exit(1)

    resume_text = read_file(resume)
    jd_text = read_file(jd)

    with console.status("[bold cyan]Scoring against job description...", spinner="dots"):
        result = score_against_jd(resume_text, jd_text, config)

    display_jd_score(result)


@cli.command()
@click.option("--resume", required=True, type=click.Path(), help="Path to the resume text file.")
@click.option("--jd", required=True, type=click.Path(), help="Path to the job description file.")
@click.pass_context
def ats(ctx, resume: str, jd: str):
    """Simulate ATS (Applicant Tracking System) score."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]❌ Ollama is not running![/]")
        sys.exit(1)

    resume_text = read_file(resume)
    jd_text = read_file(jd)

    with console.status("[bold cyan]Simulating ATS evaluation...", spinner="dots"):
        result = simulate_ats_score(resume_text, jd_text, config)

    ats_score = result.get("ats_score", 0)
    color = "green" if ats_score >= 75 else "yellow" if ats_score >= 50 else "red"
    console.print(Panel(f"[bold {color}]{ats_score}/100[/]", title="🤖 ATS Score", border_style=color, expand=False))

    for key, title in [
        ("keyword_match_score", "Keyword Match"),
        ("experience_match_score", "Experience Match"),
        ("education_match_score", "Education Match"),
        ("formatting_score", "Formatting"),
    ]:
        val = result.get(key, 0)
        c = "green" if val >= 75 else "yellow" if val >= 50 else "red"
        console.print(f"  [{c}]{title}: {val}/100[/{c}]")

    issues = result.get("formatting_issues", [])
    if issues:
        console.print(Panel("\n".join(f"⚠️ {i}" for i in issues), title="Formatting Issues", border_style="yellow"))

    recs = result.get("recommendations", [])
    if recs:
        console.print(Panel("\n".join(f"💡 {r}" for r in recs), title="Recommendations", border_style="cyan"))


@cli.command()
@click.option("--resume", required=True, type=click.Path(), help="Path to the resume text file.")
@click.pass_context
def improve(ctx, resume: str):
    """Get detailed improvement suggestions."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[bold red]❌ Ollama is not running![/]")
        sys.exit(1)

    resume_text = read_file(resume)
    with console.status("[bold cyan]Generating suggestions...", spinner="dots"):
        result = generate_improvement_suggestions(resume_text, config)

    for section in ["summary_section", "experience_section", "skills_section", "education_section"]:
        data = result.get(section, {})
        if data:
            title = section.replace("_", " ").title()
            console.print(Panel(
                f"**Assessment:** {data.get('current_assessment', 'N/A')}\n\n" +
                "\n".join(f"• {s}" for s in data.get("suggestions", [])),
                title=f"📝 {title}", border_style="cyan",
            ))

    power_words = result.get("power_words_to_add", [])
    if power_words:
        console.print(Panel(", ".join(power_words), title="💪 Power Words to Add", border_style="green"))


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
