.PHONY: install test lint run web clean help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt

install-dev: ## Install with dev dependencies
	pip install -r requirements.txt
	pip install pytest pytest-cov

test: ## Run tests
	python -m pytest tests/ -v --tb=short

test-cov: ## Run tests with coverage
	python -m pytest tests/ -v --cov=src/code_reviewer --cov-report=term-missing

lint: ## Run linting
	python -m py_compile src/code_reviewer/core.py
	python -m py_compile src/code_reviewer/cli.py
	python -m py_compile src/code_reviewer/web_ui.py

run: ## Run CLI review (usage: make run FILE=script.py)
	python -m code_reviewer.cli review --file $(FILE)

web: ## Launch Streamlit web UI
	streamlit run src/code_reviewer/web_ui.py

clean: ## Clean up cache and temp files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf .tmp/ *.egg-info/ dist/ build/
