from setuptools import setup, find_packages

setup(
    name="contract-clause-analyzer",
    version="1.0.0",
    description="AI-powered contract clause analysis with complete privacy using local LLMs",
    author="Nrk Raju Guthikonda",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "rich>=13.0.0",
        "click>=8.1.0",
        "pyyaml>=6.0",
        "streamlit>=1.30.0",
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "pydantic>=2.5.0",
    ],
    extras_require={"dev": ["pytest>=7.4.0", "pytest-cov>=4.1.0"]},
    entry_points={"console_scripts": ["contract-analyzer=contract_analyzer.cli:main"]},
    python_requires=">=3.10",
)
