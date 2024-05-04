"""Sphinx configuration."""

project = "Tdd"
author = "Mohamed YAHYA"
copyright = "2024, Mohamed YAHYA"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
