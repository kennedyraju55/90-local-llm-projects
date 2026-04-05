# Contributing to Contract Clause Analyzer

Thank you for your interest in contributing! ⚖️

## How to Contribute

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/contract-clause-analyzer.git`
3. **Create a branch**: `git checkout -b feature/your-feature`
4. **Make changes** and add tests
5. **Run tests**: `pytest tests/ -v`
6. **Commit**: `git commit -m "feat: your feature description"`
7. **Push**: `git push origin feature/your-feature`
8. **Open a Pull Request**

## Development Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -e ".[dev]"
pytest tests/ -v --cov=src/
```

## Code Style

- Follow PEP 8
- Add type hints to function signatures
- Write docstrings for public functions
- Keep functions focused and small

## Privacy Commitment

All contributions must maintain our privacy-first approach:
- No external API calls (only local Ollama)
- No data collection or telemetry
- No logging of user contract content

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
