.PHONY: help install test lint run-cli run-web run-api clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install -r requirements.txt
	pip install -e .

test: ## Run tests
	pytest tests/ -v --tb=short

lint: ## Run linting
	python -m py_compile src/lab_results_interpreter/core.py
	python -m py_compile src/lab_results_interpreter/cli.py
	python -m py_compile src/lab_results_interpreter/api.py

run-cli: ## Run CLI tool
	python -m lab_results_interpreter.cli interpret --results "WBC: 12.5, Hemoglobin: 11.0"

run-web: ## Launch Streamlit web UI
	streamlit run src/lab_results_interpreter/web_ui.py

run-api: ## Launch FastAPI server
	uvicorn src.lab_results_interpreter.api:app --host 0.0.0.0 --port 8000 --reload

clean: ## Clean build artifacts
	rm -rf __pycache__ .pytest_cache build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
