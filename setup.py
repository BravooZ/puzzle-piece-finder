#!/usr/bin/env python3
"""
Setup script for Puzzle Piece Finder.

This allows installation of the package using:
pip install -e .
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="puzzle-piece-finder",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Computer vision system for solving jigsaw puzzles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/puzzle-piece-finder",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=3.0.0",
            "black>=21.0.0",
            "flake8>=4.0.0",
            "mypy>=0.910",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
        "analysis": [
            "jupyter>=1.0.0",
            "matplotlib>=3.5.0",
            "seaborn>=0.11.0",
            "scikit-image>=0.18.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "puzzle-solver=src.main:main",
            "puzzle-gui=src.gui:main",
        ],
    },
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    include_package_data=True,
    keywords="puzzle, jigsaw, computer-vision, opencv, image-processing, template-matching",
    project_urls={
        "Bug Reports": "https://github.com/your-username/puzzle-piece-finder/issues",
        "Source": "https://github.com/your-username/puzzle-piece-finder",
        "Documentation": "https://your-username.github.io/puzzle-piece-finder/",
        "Changelog": "https://github.com/your-username/puzzle-piece-finder/blob/main/CHANGELOG.md",
    },
)
