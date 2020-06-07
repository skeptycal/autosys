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
    from dataclasses import dataclass, Field, field
    from os import linesep as NL
    from sys import argv as _argv
    from setuptools import setup, find_packages
    from typing import Dict, Final, List, Optional, Tuple
    from shutil import rmtree as _rmtree

    from autosys.utils.readme import readme

if True:  # ? #################################### packaging utilities.

    DEFAULT_RE_FLAGS: Final[int] = re.MULTILINE | re.IGNORECASE
    print(DEFAULT_RE_FLAGS)

    RE_VERSION: re.Pattern = re.compile(
        pattern=r'^__version__\s?=\s?[\'"]([^\'"]*)[\'"]',
        flags=re.MULTILINE | re.IGNORECASE,
    )
    RE_PYPI_REPLACE: re.Pattern = re.compile(
        pattern=r"\s-", flags=re.MULTILINE | re.IGNORECASE
    )

    class SetupError(ValueError):
        "The parameters necessary to complete the setup process were not available."

    def pip_safe_name(s: str):
        """ Return a name that is converted to pypi safe format. """
        return s.lower().replace("-", "_").replace(" ", "_")

    def split_it(s: str, delimiter: str = "\s"):
        return re.split(pattern=s, string=delimiter)

    def table_dict(_vars: Dict, width=60, divider=": ", indent=2, key_size=15):
        print("-" * width)
        key_size = (key_size := width // 4) < min_width or True
        print(key_size)
        value_size = width - key_size - indent - len(divider) - 1
        for k, v in _vars.items():
            val = str(v)[:value_size]
            print(f"{indent*' '}{k:<{key_size}.{key_size}}{divider}{val}")

    # TODO - split off this class to a module ---------------------------------->>

    class Re_File_Error(ValueError):
        "There was a file error while attempting to match the pattern."

    class Re_Value_Error(ValueError):
        "There was a matching error while attempting to match the pattern."

    @dataclass
    class ReGetFileField:
        """ Return a string that matches `pattern` from `file_name`.

            file_name: str - a text file containing the `pattern`
            pattern: re.Pattern - a precompiled regex `pattern`
            default: str - a default value used if `pattern` is not found


            __version__ = 'version_string'


            - if there is a file error, Re_File_Error is raised
            - if there is a matching error, the `default` is returned
            - if there is a matching error and no default is provided,
                a Re_Value_Error is raised
            """

        file_name: str
        pattern: re.Pattern
        default: str
        _result: str = ""

        def __post_init__(self):
            self._result: str = ""

        @property
        def get_file_contents(self) -> (str, Exception):
            """ Wrapper for logging and error handling of file opening. """
            try:
                with open(self.file_name, "r") as fh:
                    return fh.read()
            except Exception as e:
                msg = f"File error while opening file '{file_name}'{NL}{e.args}"
                log.error(msg, e)
                raise Re_File_Error(msg, e)

        @property
        def get_data(self) -> (str, Exception):
            data = self.get_file_contents
            try:
                self._result = self.pattern.search(data).groups()[0] or self.default
                return self._result
            except (ValueError, KeyError, AttributeError, TypeError) as e:
                if self.default:
                    self._result = self.default
                    return self._result
                raise Re_Value_Error(
                    f"Pattern '{pattern}' not found in file '{file_name}'", e
                )
            except Exception as e:
                log(e)
                raise Re_Value_Error(
                    f"Error occurred while searching for pattern '{pattern}' in file '{file_name}'",
                    e,
                )
            return self._result

        def __str__(self):
            if not self._result:
                self._result = self.get_data
            return self._result

    # TODO - split off this class to a module <<--------------------------------
    @dataclass
    class GetVersion(ReGetFileField):
        """ Return a version number from a file.

            A line in the text file must match this pattern:

            __version__ = 'version_string'

            - version_string can be any valid text
            - the entire search string must start at the start of a line
            - the format of the 'version_string' part is *not* checked
            - the __version__ part shall have underscores
            - the `=` may use optional spaces
            - version_string shall use either single or double quotes
            - if there is a file error, the 'default' value is used
            """

        file_name = "VERSION.txt"
        pattern = RE_VERSION
        default = "0.0.1"
        _result = ""

    getversion = GetVersion("VERSION.txt", RE_VERSION, "0.0.1")


if True:  # ? #################################### package meta-data.
    # VERSION_INFO = VERSION.split(".")
    NAME: str = pip_safe_name("AutoSys")

    VERSION: str = getversion
    DESCRIPTION: str = "System utilities for Python on macOS."
    EMAIL: str = "skeptycal@gmail.com"
    AUTHOR: str = "Michael Treanor"
    LICENSE: str = "MIT"
    REQUIRES_PYTHON: str = ">=3.8.0"
    MAINTAINER: str = ""
    MAINTAINER_EMAIL: str = ""
    LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"
    # long_description_content_type="text/x-rst",
    URL = f"https://skeptycal.github.io/{NAME}/"
    DOWNLOAD_URL = f"https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz"

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
        "Website": f"https://skeptycal.github.io/{NAME}/",
        "Documentation": f"https://skeptycal.github.io/{NAME}/docs",
        "Source Code": f"https://www.github.com/skeptycal/{NAME}/",
        "Changelog": f"https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md",
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
    CLASSIFIERS = (
        [
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


def main(args=_argv[1:],):  # ? #################################### package Setup!
    if _debug_:
        _vars
        print(f"{NAME=}")
        print(f"{version()=}")
        print(f"{VERSION=}")
        # print(table_dict(k))

    else:
        setup(
            name=NAME,
            version=VERSION,
            description=DESCRIPTION,
            python_requires=REQUIRES_PYTHON,
            packages=find_packages(),
            py_modules=[f"{NAME}"],
            license=LICENSE,
            long_description=readme(),
            long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
            author=AUTHOR,
            author_email=EMAIL,
            maintainer=MAINTAINER or AUTHOR,
            maintainer_email=MAINTAINER_EMAIL or EMAIL,
            keywords=KEYWORDS,
            url=URL,
            download_url=DOWNLOAD_URL,
            zip_safe=False,
            include_package_data=True,
            package_data=PACKAGE_DATA,
            project_urls=PROJECT_URLS,
            install_requires=REQUIRED,
            extras_require=EXTRAS,
            classifiers=CLASSIFIERS,
        )


_vars = vars()
_vars = locals()
if __name__ == "__main__":
    _debug_: bool = True
    main()
