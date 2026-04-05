.PHONY: install test lint run-cli run-web run-api clean help

help: ## Show this help message
	@echo "Court Filing Generator - Available Commands:"
	@echo ""
	@echo "  make install    Install dependencies"
	@echo "  make test       Run tests"
	@echo "  make lint       Run linter"
	@echo "  make run-cli    Run CLI interface"
	@echo "  make run-web    Run Streamlit web UI"
	@echo "  make run-api    Run FastAPI server"
	@echo "  make clean      Clean build artifacts"
	@echo ""

install: ## Install dependencies
	pip install -r requirements.txt
	pip install -e .

test: ## Run tests with pytest
	python -m pytest tests/ -v --tb=short

lint: ## Run linter
	python -m ruff check src/filing_generator/ tests/
	python -m ruff format --check src/filing_generator/ tests/

run-cli: ## Run CLI interface
	python -m src.filing_generator.cli templates

run-web: ## Run Streamlit web UI
	streamlit run src/filing_generator/web_ui.py --server.port 8501

run-api: ## Run FastAPI server
	uvicorn src.filing_generator.api:app --host 0.0.0.0 --port 8000 --reload

clean: ## Clean build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf build/ dist/ *.egg-info .pytest_cache .ruff_cache
