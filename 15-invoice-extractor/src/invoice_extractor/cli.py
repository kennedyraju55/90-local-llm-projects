"""Click CLI interface for Invoice Extractor."""

import json
import sys
import logging

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.json import JSON as RichJSON

from .config import load_config
from .core import (
    extract_invoice_data,
    batch_extract,
    detect_duplicates,
    categorize_items,
    export_to_csv,
)
from .utils import setup_logging, read_invoice_file, get_llm_client

logger = logging.getLogger(__name__)
console = Console()


def format_json(data: dict) -> None:
    """Display invoice data as a pretty-printed JSON panel."""
    json_str = json.dumps(data, indent=2)
    console.print(Panel(RichJSON(json_str), title="📄 Invoice Data", border_style="green"))


def format_table(data: dict) -> None:
    """Display invoice data as Rich tables."""
    meta_table = Table(title="🧾 Invoice Details", show_header=False, border_style="cyan")
    meta_table.add_column("Field", style="bold")
    meta_table.add_column("Value")

    vendor = data.get("vendor", {})
    meta_table.add_row("Vendor", vendor.get("name", "N/A"))
    meta_table.add_row("Address", vendor.get("address") or "N/A")
    meta_table.add_row("Phone", vendor.get("phone") or "N/A")
    meta_table.add_row("Email", vendor.get("email") or "N/A")
    meta_table.add_row("Invoice #", data.get("invoice_number") or "N/A")
    meta_table.add_row("Date", data.get("date") or "N/A")
    meta_table.add_row("Due Date", data.get("due_date") or "N/A")
    meta_table.add_row("Payment Terms", data.get("payment_terms") or "N/A")
    console.print(meta_table)
    console.print()

    items_table = Table(title="📦 Line Items", border_style="blue")
    items_table.add_column("#", justify="right", style="dim")
    items_table.add_column("Description")
    items_table.add_column("Qty", justify="right")
    items_table.add_column("Unit Price", justify="right")
    items_table.add_column("Total", justify="right", style="green")

    for idx, item in enumerate(data.get("line_items", []), start=1):
        items_table.add_row(
            str(idx), item.get("description", ""),
            str(item.get("quantity", "")),
            f"{item.get('unit_price', 0):.2f}",
            f"{item.get('total', 0):.2f}",
        )
    console.print(items_table)
    console.print()

    currency = data.get("currency", "USD")
    totals_table = Table(title="💰 Totals", show_header=False, border_style="yellow")
    totals_table.add_column("Label", style="bold")
    totals_table.add_column("Amount", justify="right", style="green")
    totals_table.add_row("Subtotal", f"{data.get('subtotal', 0):.2f} {currency}")
    totals_table.add_row("Tax", f"{data.get('tax', 0):.2f} {currency}")
    totals_table.add_row("Grand Total", f"[bold]{data.get('grand_total', 0):.2f} {currency}[/bold]")
    console.print(totals_table)


def format_csv(data: dict) -> None:
    """Display invoice line items as CSV to stdout."""
    print("description,quantity,unit_price,total")
    for item in data.get("line_items", []):
        desc = item.get("description", "").replace(",", ";")
        print(f"{desc},{item.get('quantity', '')},{item.get('unit_price', '')},{item.get('total', '')}")


OUTPUT_FORMATTERS = {"json": format_json, "table": format_table, "csv": format_csv}


@click.group()
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@click.option("--config", "config_path", type=click.Path(), default=None, help="Path to config.yaml.")
@click.pass_context
def cli(ctx, verbose: bool, config_path: str | None):
    """🧾 Invoice Extractor - Extract structured data from invoices."""
    setup_logging(verbose)
    ctx.ensure_object(dict)
    ctx.obj["config"] = load_config(config_path)


@cli.command()
@click.option("--file", "-f", "filepath", required=True, type=click.Path(exists=True), help="Invoice file.")
@click.option("--output", "-o", "output_format", type=click.Choice(["json", "table", "csv"]),
              default="json", show_default=True)
@click.pass_context
def extract(ctx, filepath: str, output_format: str):
    """Extract data from a single invoice."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[red bold]Error:[/] Ollama is not running.")
        sys.exit(1)

    console.print(f"[cyan]Reading invoice:[/] {filepath}")
    text = read_invoice_file(filepath)

    if not text.strip():
        raise click.ClickException("Invoice file is empty.")

    console.print("[cyan]Extracting data with LLM…[/]")
    data = extract_invoice_data(text, config)

    console.print()
    OUTPUT_FORMATTERS[output_format](data)


@cli.command()
@click.option("--files", "-f", required=True, multiple=True, type=click.Path(exists=True),
              help="Invoice files to process.")
@click.option("--export", "-e", type=click.Path(), default=None, help="Export CSV to file.")
@click.pass_context
def batch(ctx, files: tuple[str], export: str | None):
    """Process multiple invoices in batch."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[red bold]Error:[/] Ollama is not running.")
        sys.exit(1)

    console.print(f"[cyan]Processing {len(files)} invoices...[/]")
    results = batch_extract(list(files), config)

    # Display results
    for result in results:
        if "error" in result:
            console.print(f"[red]✗ {result['file']}: {result['error']}[/red]")
        else:
            console.print(f"[green]✓ {result['file']}[/green]")
            format_table(result["data"])

    # Check duplicates
    duplicates = detect_duplicates(results)
    if duplicates:
        console.print(Panel(
            "\n".join(f"⚠️ Files {results[i]['file']} and {results[j]['file']}: {reason}"
                      for i, j, reason in duplicates),
            title="🔍 Potential Duplicates", border_style="yellow",
        ))

    # Export CSV
    if export:
        csv_data = export_to_csv(results)
        with open(export, "w", encoding="utf-8") as f:
            f.write(csv_data)
        console.print(f"[green]✓ Exported to {export}[/green]")


@cli.command()
@click.option("--file", "-f", "filepath", required=True, type=click.Path(exists=True), help="Invoice file.")
@click.pass_context
def categorize(ctx, filepath: str):
    """Categorize invoice line items."""
    config = ctx.obj["config"]
    _, _, check_ollama_running = get_llm_client()

    if not check_ollama_running():
        console.print("[red bold]Error:[/] Ollama is not running.")
        sys.exit(1)

    text = read_invoice_file(filepath)
    data = extract_invoice_data(text, config)

    with console.status("[bold cyan]Categorizing items...[/bold cyan]"):
        result = categorize_items(data, config)

    items = result.get("categorized_items", [])
    if items:
        table = Table(title="📊 Categorized Items", border_style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Category", style="cyan")
        for item in items:
            table.add_row(item.get("description", ""), item.get("category", ""))
        console.print(table)


def main():
    cli()


if __name__ == "__main__":
    main()
