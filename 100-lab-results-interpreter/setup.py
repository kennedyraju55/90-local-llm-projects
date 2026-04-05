from setuptools import setup, find_packages

setup(
    name="lab-results-interpreter",
    version="1.0.0",
    description="AI-powered laboratory result analysis using local LLMs",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "requests",
        "rich",
        "click",
        "pyyaml",
        "streamlit",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
    },
    entry_points={
        "console_scripts": [
            "lab-interpreter=lab_results_interpreter.cli:cli",
        ],
    },
)
