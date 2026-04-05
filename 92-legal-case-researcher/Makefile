.PHONY: install test lint run-cli run-web run-api clean help

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

test: ## Run tests
	python -m pytest tests/ -v --tb=short

lint: ## Run linting
	python -m py_compile src/case_researcher/core.py
	python -m py_compile src/case_researcher/cli.py
	python -m py_compile src/case_researcher/web_ui.py
	python -m py_compile src/case_researcher/api.py
	python -m py_compile src/case_researcher/config.py
	@echo "All files compile successfully"

run-cli: ## Run CLI (usage: make run-cli ARGS="research 'your query'")
	python -m src.case_researcher.cli $(ARGS)

run-web: ## Run Streamlit web UI
	streamlit run src/case_researcher/web_ui.py --server.port 8501

run-api: ## Run FastAPI server
	uvicorn src.case_researcher.api:app --host 0.0.0.0 --port 8000 --reload

clean: ## Clean up generated files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned up"
