# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# -- Project information -----------------------------------------------------

project = "AutoSys"
copyright = "2020, Michael Treanor"
author = "Michael Treanor"

# The full version, including alpha/beta/rc tags
release = "0.5.2"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx-autobuild",
    "sphinxcontrib-applehelp",
    "sphinxcontrib-devhelp",
    "sphinxcontrib-htmlhelp",
    "sphinxcontrib-jsmath",
    "sphinxcontrib-napoleon",
    "sphinxcontrib-qthelp",
    "sphinxcontrib-serializinghtml",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

rst_epilog = """
.. |psf| replace:: Python Software Foundation
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "**/*bak*",
    "**/*private*",
    "_build",
    "_dist",
    "**/Thumbs.db",
    "**/.DS_Store",
    ".git",
    ".tox",
    "bak_ideas",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
