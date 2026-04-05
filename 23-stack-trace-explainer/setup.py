"""Setup script for Stack Explainer."""

from setuptools import setup, find_packages

setup(
    name="stack-explainer",
    version="1.0.0",
    description="AI-powered stack trace analysis and debugging assistant",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Local LLM Projects",
    python_requires=">=3.10",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests>=2.31.0",
        "rich>=13.0.0",
        "click>=8.1.0",
        "pyyaml>=6.0",
        "streamlit>=1.28.0",
    ],
    extras_require={
        "dev": ["pytest>=7.4.0", "pytest-cov>=4.0.0"],
    },
    entry_points={
        "console_scripts": [
            "stack-explainer=stack_explainer.cli:main",
        ],
    },
)
