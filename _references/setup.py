#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" setup.py """
# pylint: disable=missing-docstring
# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

# https://setuptools.readthedocs.io/en/latest/setuptools.html

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "text_colors"
DESCRIPTION = "The obligatory ANSI text colors implementation."
KEYWORDS_LIST = "ANSI color terminal iterm2 linux macos cli colorful rainbow"
URL = "https://github.com/skeptycal/text_colors"
EMAIL = "skeptycal@gmail.com"
AUTHOR = "Michael Treanor"
REQUIRES_PYTHON = ">=3.6.0"
README_FILENAME = "README.md"

SCRIPTS_LIST = [
    # ''
]

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

PACKAGE_DATA = {
    # If any package contains *.txt or *.rst files, include them:
    "": ["*.md", "*.txt", "*.rst", "*.yml", "*.yaml", "*.cfg"],
    # And include any *.msg files found in the 'hello' package, too:
    # 'hello': ['*.msg'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
#   Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, README_FILENAME), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(
            "{0} setup.py sdist bdist_wheel --universal".
            format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


# Where the magic happens:
setup(
    # * Demographic Information
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=KEYWORDS_LIST,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # * Package Contents
    scripts=SCRIPTS_LIST,
    include_package_data=True,
    package_data=PACKAGE_DATA,
    packages=find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['text_colors.py'],
    # * Options for packaging:
    # packages=find_packages('src'),  # include all packages under src
    # package_dir={'':'src'},   # tell distutils packages are under src
    # package_data={
    # If any package contains *.txt files, include them:
    # '': ['*.txt'],
    # And include any *.dat files found in the 'data' subdirectory
    # of the 'mypkg' package, also:
    # 'mypkg': ['data/*.dat'],
    # }
    # # ...but exclude README.txt from all packages
    # exclude_package_data={'': ['README.txt']},
    # * Build Options
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    # * License Information
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
