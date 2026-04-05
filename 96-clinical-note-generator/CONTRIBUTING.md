# Contributing

Thank you for your interest in contributing! 🎉

## How to Contribute

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/clinical-note-generator.git`
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

pip install -e .
pip install pytest pytest-cov

pytest tests/ -v --cov=src/
```

## Code Style

- Follow PEP 8
- Add type hints to function signatures
- Write docstrings for public functions
- Keep functions focused and small

## Reporting Issues

- Use GitHub Issues
- Include steps to reproduce
- Include expected vs actual behavior
- Include Python version and OS

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
