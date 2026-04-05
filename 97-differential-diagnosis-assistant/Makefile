.PHONY: help install test lint run-cli run-web clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt
	pip install -e .

test: ## Run tests
	pytest tests/ -v --tb=short

lint: ## Run linting
	python -m py_compile src/differential_diagnosis/core.py
	python -m py_compile src/differential_diagnosis/cli.py

run-cli: ## Run CLI tool
	python -m differential_diagnosis.cli diagnose --symptoms "chest pain, shortness of breath"

run-web: ## Launch Streamlit web UI
	streamlit run src/differential_diagnosis/web_ui.py

clean: ## Clean build artifacts
	rm -rf __pycache__ .pytest_cache build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
