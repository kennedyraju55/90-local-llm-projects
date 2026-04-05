.PHONY: install test lint run-cli run-web run-api clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

install-dev: ## Install with dev dependencies
	pip install -r requirements.txt
	pip install pytest pytest-cov

test: ## Run tests
	python -m pytest tests/ -v

test-cov: ## Run tests with coverage
	python -m pytest tests/ -v --cov=src/deposition_summarizer --cov-report=term-missing

run-cli: ## Run CLI (use ARGS="summarize --file transcript.txt")
	python -m src.deposition_summarizer.cli $(ARGS)

run-web: ## Launch Streamlit web UI
	streamlit run src/deposition_summarizer/web_ui.py

run-api: ## Launch FastAPI server
	uvicorn src.deposition_summarizer.api:app --host 0.0.0.0 --port 8000 --reload

clean: ## Remove cache files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
