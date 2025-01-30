import os
from setuptools import setup, find_packages
from datetime import datetime

# Get the current UTC timestamp
BUILD_TIMESTAMP = "2025-01-29 16:10:53"
AUTHOR = "AmarnathaGowda"

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    required = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#") and not line.startswith("git+")
    ]

setup(
    name="movieloop_plugin",
    version="1.0.0",
    author=AUTHOR,
    author_email="amarnatha.gowda@example.com",  # Replace with your email
    description="A DaVinci Resolve plugin for AI-powered color grading using OpenAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmarnathaGowda/movieloop_plugin",
    project_urls={
        "Bug Tracker": "https://github.com/AmarnathaGowda/movieloop_plugin/issues",
        "Documentation": "https://github.com/AmarnathaGowda/movieloop_plugin/docs",
        "Source Code": "https://github.com/AmarnathaGowda/movieloop_plugin",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Video :: Non-Linear Editor",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Plugins",
        "Framework :: DaVinci Resolve",
    ],
    python_requires=">=3.8",
    install_requires=required,
    extras_require={
        'dev': [
            'pytest>=7.4.4',
            'pytest-qt>=4.2.0',
            'pytest-cov>=4.1.0',
            'black>=23.12.1',
            'flake8>=7.0.0',
            'isort>=5.13.2',
            'mypy>=1.8.0',
            'pre-commit>=3.6.0',
        ],
        'docs': [
            'Sphinx>=7.2.6',
            'sphinx-rtd-theme>=2.0.0',
            'autodoc>=0.5.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'movieloop=movieloop_plugin.main:main',
        ],
    },
    package_data={
        'movieloop_plugin': [
            'resources/styles/*.qss',
            'resources/icons/*.png',
            'resources/templates/*.json',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
    keywords=[
        'davinci resolve',
        'color grading',
        'video editing',
        'openai',
        'lut generation',
        'movie look',
        'color correction',
    ],
    license="MIT",
    data_files=[
        ('', ['LICENSE', 'README.md']),
    ],
    # Add build metadata
    options={
        'build': {
            'build_base': 'build',
        },
    },
    # Custom metadata for the project
    metadata={
        'build_timestamp': BUILD_TIMESTAMP,
        'author_username': AUTHOR,
    }
)

# Post-setup configuration
if __name__ == "__main__":
    # Create necessary directories if they don't exist
    directories = [
        "logs",
        "temp",
        "cache",
    ]
    
    for directory in directories:
        os.makedirs(os.path.join("src", "movieloop_plugin", directory), exist_ok=True)

    # Print setup completion message
    print(f"""
MovieLook Plugin Setup Complete
-----------------------------
Author: {AUTHOR}
Build Time: {BUILD_TIMESTAMP}
Python Package: movieloop_plugin

Installation successful! You can now use the plugin by running:
    movieloop

For development:
    pip install -e .[dev]

For documentation:
    pip install -e .[docs]
    """)