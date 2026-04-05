.PHONY: help install test lint run-cli run-web clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt
	pip install -e .

test: ## Run tests
	pytest tests/ -v --tb=short

lint: ## Run linting
	python -m py_compile src/patient_intake_summarizer/core.py
	python -m py_compile src/patient_intake_summarizer/cli.py
	python -m py_compile src/patient_intake_summarizer/api.py

run-cli: ## Run CLI tool
	python -m patient_intake_summarizer.cli summarize --text "Patient: Jane Doe, 52F, back pain"

run-web: ## Launch Streamlit web UI
	streamlit run src/patient_intake_summarizer/web_ui.py

clean: ## Clean build artifacts
	rm -rf __pycache__ .pytest_cache build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
