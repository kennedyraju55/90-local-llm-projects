.PHONY: install test lint run-cli run-web clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

test: ## Run tests
	python -m pytest tests/ -v

test-cov: ## Run tests with coverage
	python -m pytest tests/ -v --cov=src/invoice_extractor --cov-report=term-missing

run-cli: ## Run CLI (use ARGS="extract --file invoice.txt")
	python -m src.invoice_extractor.cli $(ARGS)

run-web: ## Launch Streamlit web UI
	streamlit run src/invoice_extractor/web_ui.py

clean: ## Remove cache files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
