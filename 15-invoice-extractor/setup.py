"""Setup script for Invoice Extractor."""

from setuptools import setup, find_packages

setup(
    name="invoice-extractor",
    version="1.0.0",
    description="Production-grade invoice data extractor using local LLM",
    python_requires=">=3.11",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests", "rich", "click", "pyyaml", "streamlit", "python-dotenv",
    ],
    extras_require={"dev": ["pytest", "pytest-cov"]},
    entry_points={"console_scripts": ["invoice-extractor=invoice_extractor.cli:main"]},
)
