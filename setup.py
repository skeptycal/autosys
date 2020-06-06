#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

if True:  # ? #################################### package imports.

    # Note: To use the 'upload' functionality of this file, you must:
    #   $ pip install twine

    import os
    import re
    from sys import argv as _argv
    from setuptools import setup, find_packages
    from typing import Dict, List, Optional, Tuple
    from shutil import rmtree as _rmtree

    from autosys.utils.readme import readme

if True:  # ? #################################### packaging utilities.

    def pip_safe_name(s: str):
        """ Return a name that is converted to pypi safe format. """
        return s.lower().replace("-", "_").replace(" ", "_")

    name = pip_safe_name

    def version(
        file_name: str = "VERSION.txt", default: str = "0.0.1"
    ) -> (str):
        """ Return a version number from a file.

            A line in the text file must match this pattern:

            __version__ = 'version_string'

            - version_string can be any valid text
            - the format of the 'version_string' part is *not* checked
            - the __version__ part shall have underscores
            - the `=` may use optional spaces
            - version_string shall use either single or double quotes
            - if there is a file error, the 'default' value is used
            """
        try:
            with open(file_name, "r") as fh:
                # match a string like this:  __version__ = 'x.x.x'
                RE_VERSION = r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]'
                return (
                    re.search(
                        RE_VERSION, fh.read(), re.MULTILINE | re.IGNORECASE
                    )[0].split("'")[1]
                    or default
                )
        except OSError:
            return default

    """
        def readme(file_name: str = "README.md") -> str:
            with open(file_name, "rb") as file:
                return file.read().decode("utf-8")
        """

if True:  # ? #################################### package meta-data.
    NAME: str = "AutoSys"
    VERSION: str = version()
    VERSION_INFO: Tuple[int] = VERSION.split(".")
    DESCRIPTION: str = "System utilities for Python on macOS."
    EMAIL: str = "skeptycal@gmail.com"
    AUTHOR: str = "Michael Treanor"
    LICENSE: str = "MIT"
    REQUIRES_PYTHON: str = ">=3.8.0"
    MAINTAINER: str = ""
    MAINTAINER_EMAIL: str = ""

    name: str = pip_safe_name(NAME)

    # What packages are required for this module to be executed?
    REQUIRED = [
        "colorama>=0.3.4 ; sys_platform=='win32'",
        "aiocontextvars>=0.2.0 ; python_version<'3.7'",
        "win32-setctime>=1.0.0 ; sys_platform=='win32'",
    ]

    # What packages are optional?
    EXTRAS = {
        "dev": [
            "black>=19.3b0 ; python_version>='3.8'",
            "codecov>=2.0.15",
            "colorama>=0.3.4",
            "flake8>=3.7.7",
            "isort>=4.3.20",
            "tox>=3.9.0",
            "tox-travis>=0.12",
            "pytest>=4.6.2",
            "pytest-cov>=2.7.1",
            "Sphinx>=2.2.1",
            "sphinx-autobuild>=0.7.1",
            "sphinx-rtd-theme>=0.4.3",
        ]
    }

    PACKAGE_DATA = {
        # If any package contains these files, include them:
        "": [
            "*.txt",
            "*.rst",
            "*.md",
            "*.ini",
            "*.png",
            "*.jpg",
            "__init__.pyi",
            "py.typed",
        ]
    }

    PROJECT_URLS = {
        "Website": f"https://skeptycal.github.io/{name}/",
        "Documentation": f"https://skeptycal.github.io/{name}/docs",
        "Source Code": f"https://www.github.com/skeptycal/{name}/",
        "Changelog": f"https://github.com/skeptycal/{name}/blob/master/CHANGELOG.md",
    }

    KEYWORDS = [
        "application",
        "macOS",
        "dev",
        "devops",
        "cache",
        "utilities",
        "cli",
        "python",
        "cython",
        "text",
        "console",
        "log",
        "debug",
        "test",
        "testing",
        "logging",
        "logger",
    ]


def main(
    args=_argv[1:],
):  # ? #################################### package Setup!
    if _debug_:
        _vars
        print(f"{name=}")
        print(f"{version()=}")
        print("-" * 50)
        for k, v in _vars.items():
            val = str(v)[:40]
            print(f"{k:<15.15}: {val}")
    else:
        setup(
            name=name,
            version=VERSION,
            description=DESCRIPTION,
            python_requires=REQUIRES_PYTHON,
            packages=find_packages(),
            py_modules=[f"{name}"],
            license=LICENSE,
            long_description=readme(),
            long_description_content_type="text/markdown",
            # long_description_content_type="text/x-rst",
            author=AUTHOR,
            author_email=EMAIL,
            maintainer=MAINTAINER or AUTHOR,
            maintainer_email=MAINTAINER_EMAIL or EMAIL,
            keywords=KEYWORDS,
            url=f"https://skeptycal.github.io/{name}/",
            download_url=f"https://github.com/skeptycal/{name}/archive/{version}.tar.gz",
            zip_safe=False,
            include_package_data=True,
            package_data=PACKAGE_DATA,
            project_urls=PROJECT_URLS,
            install_requires=REQUIRED,
            extras_require=EXTRAS,
            classifiers=[
                "Development Status :: 4 - Beta",
                "License :: OSI Approved :: MIT License",
                "Environment :: Console",
                "Environment :: MacOS X",
                "Intended Audience :: Developers",
                "Natural Language :: English",
                "Operating System :: MacOS",
                "Operating System :: OS Independent",
                "Programming Language :: Cython",
                "Programming Language :: Python",
                "Programming Language :: Python :: 3 :: Only",
                "Programming Language :: Python :: 3",
                # These are the Python versions tested; it may work on others
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: Implementation :: CPython",
                "Programming Language :: Python :: Implementation :: PyPy",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "Topic :: Software Development :: Testing",
                "Topic :: Utilities",
            ],
        )


_vars = vars()
_vars = locals()
if __name__ == "__main__":
    _debug_: bool = True
    main()
