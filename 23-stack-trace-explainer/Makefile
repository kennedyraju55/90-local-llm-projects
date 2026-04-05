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
	python -m pytest tests/ -v --cov=src/stack_explainer --cov-report=term-missing

lint: ## Run linting
	python -m py_compile src/stack_explainer/core.py
	python -m py_compile src/stack_explainer/cli.py
	python -m py_compile src/stack_explainer/web_ui.py

run: ## Explain a stack trace (usage: make run TRACE=error.txt)
	python -m stack_explainer.cli explain --trace $(TRACE)

web: ## Launch Streamlit web UI
	streamlit run src/stack_explainer/web_ui.py

clean: ## Clean up cache and temp files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	rm -rf *.egg-info/ dist/ build/
