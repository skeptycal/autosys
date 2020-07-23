#!/usr/bin/env false python3
# -*- coding: utf-8 -*-
""" AutoSys Package Metadata
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# import sys
# import os

# from pathlib import Path
# from typing import Dict, List, Tuple

# # ? ################################### Default Metadata
# NAME: str = "AutoSys"
# VERSION: str = "0.5.0"
# DESCRIPTION: str = "System utilities for Python on macOS."
# REQUIRES_PYTHON: str = ">=3.8.0"
# # ? ####################################################

# try:
#     from locale import getpreferredencoding

#     DEFAULT_ENCODING = getpreferredencoding(do_setlocale=True)
#     del getpreferredencoding
# except ImportError:
#     DEFAULT_ENCODING = "utf-8"
# except:
#     DEFAULT_ENCODING = "utf-8"
#     del getpreferredencoding

# PY3 = sys.version_info.major > 2

# PY_INTERPRETER_PATH = os.path.abspath(sys.executable)
# # FYI, when in a Jupyter notebook, this gives the path to the kernel launcher script.
# PY_INTERPRETER_PATH_ALT = os.environ["_"]
# # if not run from virtual environment, this will be wrong...
# try:
#     PY_VENV_PATH = os.environ["VIRTUAL_ENV"]
# except KeyError:
#     PY_VENV_PATH = None


# def readme(file_name: str = "readme.md", search_list: List[str] = []):
#     """ Returns the text of the file (defaults to README files)

#         The default file is `README.md` and is *NOT* case sensitive. (e.g. `README` is the same as `readme`)
#         Can load *any* text file, but the default search path is setup for readme files

#         ```
#         Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
#         ```

#         Example:

#         ```
#         long_description=readme()
#         ```
#         """

#     # add default search list for README files
#     if not search_list:
#         search_list = ["readme.md", "readme.rst", "readme", "readme.txt"]
#     # make sure 'file_name' is in 'search_list' at index 0
#     if file_name not in search_list:
#         search_list.insert(0, file_name)
#     found: bool = False
#     # traverse up through directory tree searching for each file in 'search_list'
#     for searchfile in search_list:
#         # search in this script's path and above
#         for parent in Path(file_name).resolve().parents:
#             find_path = Path(parent / searchfile)
#             if find_path.exists():
#                 found = True
#                 break
#         if found:
#             break
#     if found:
#         try:
#             with open(find_path, mode="r", encoding=DEFAULT_ENCODING) as f:
#                 return f.read()
#         except IOError as e:
#             raise IOError(f"Cannot read from the 'readme' file '{find_path}'")
#     else:
#         raise FileNotFoundError(
#             f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
#         )


# def pip_safe_name(s: str):
#     """ Return a name that is converted to pypi safe format.
#         ####
#         (Returns a lowercase string has no spaces or dashes)
#         """
#     return s.lower().replace("-", "_").replace(" ", "_")

NAME = pip_safe_name(NAME)

# use alternate for RST
# LONG_DESCRIPTION_CONTENT_TYPE="text/x-rst",,

# meta_data = {
#     "__version__": VERSION.split("."),
#     "PACKAGE_DIR": {"": f"{NAME}"},
#     "PACKAGE_EXCLUDE": ["*test*", "*bak*"],
#     "LICENSE": "MIT",
#     "LONG_DESCRIPTION": readme(),
#     "LONG_DESCRIPTION_CONTENT_TYPE": "text/markdown",
#     "AUTHOR": "Michael Treanor",
#     "AUTHOR_EMAIL": "skeptycal@gmail.com",
#     "MAINTAINER": AUTHOR,
#     "MAINTAINER_EMAIL": AUTHOR_EMAIL,
#     "URL": f"https://skeptycal.github.io/{NAME}/",
#     "DOWNLOAD_URL": f"https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz",
#     "ZIP_SAFE": False,
#     "INCLUDE_PACKAGE_DATA": True,
#     # What packages are required for this module to be "e""xecuted"?,
#     "REQUIRED": [
#         "colorama>=0.3.4 ; sys_platform=='win32'",
#         "win32-setctime>=1.0.0 ; sys_platform=='win32'",
#         "APScheduler>=3.6.3",
#         "bs4>=0.0.1",
#         "click-spinner>=0.1.10",
#         "Cython>=0.29.19",
#         "docopt>=0.6.2",
#         "Flask>=1.1.2",
#         "pathlib2>=2.3.5",
#         "pathspec>=0.8.0",
#         "pydash>=4.8.0",
#         "regex>=2020.6.8",
#         "shellingham>=1.3.2",
#         "streamlit>=0.61.0",
#         "tabulate>=0.8.7",
#         "trafaret>=2.0.2",
#         "twine>=3.1.1",
#         "typed-ast>=1.4.1",
#         "typer>=0.2.1",
#         "ujson>=3.0.0",
#         "yfinance>=0.1.54",
#     ],
#     # What packages are optional?
#     "EXTRAS": {
#         "dev": [
#             "APScheduler>=3.6.3",
#             "autopep8>=1.5.3",
#             "bs4>=0.0.1",
#             "click-spinner>=0.1.10",
#             "codecov>=2.1.4",
#             "Cython>=0.29.19",
#             "docopt>=0.6.2",
#             "flake8>=3.8.3",
#             "Flask>=1.1.2",
#             "isort>=4.3.20",
#             "pathlib2>=2.3.5",
#             "pathspec>=0.8.0",
#             "pydash>=4.8.0",
#             "pygments-pytest>=2.0.0",
#             "pylint>=2.5.3",
#             "pytest-bench>=0.3.0",
#             "pytest-cov>=2.10.0",
#             "pytest-pydocstyle>=2.1.3",
#             "pytest-race>=0.1.1",
#             "pytest-sugar>=0.9.3",
#             "pytest>=4.6.2",
#             "regex>=2020.6.8",
#             "shellingham>=1.3.2",
#             "sphinx-autobuild>=0.7.1",
#             "sphinx-rtd-theme>=0.4.3",
#             "sphinxcontrib-napoleon>=0.7",
#             "streamlit>=0.61.0",
#             "tabulate>=0.8.7",
#             "tox-travis>=0.12",
#             "tox>=3.9.0",
#             "trafaret>=2.0.2",
#             "twine>=3.1.1",
#             "typed-ast>=1.4.1",
#             "typer>=0.2.1",
#             "ujson>=3.0.0",
#             "yfinance>=0.1.54",
#         ],
#     },
#     "PACKAGE_DATA": {
#         # If any package contains these files, include them:
#         "": [
#             "*.txt",
#             "*.rst",
#             "*.md",
#             "*.ini",
#             "*.png",
#             "*.jpg",
#             "*.py",
#             "__init__.pyi",
#             "py.typed",
#         ]
#     },
#     "PROJECT_URLS": {
#         "Website": f"https://skeptycal.github.io/{NAME}/",
#         "Documentation": f"https://skeptycal.github.io/{NAME}/docs",
#         "Source Code": f"https://www.github.com/skeptycal/{NAME}/",
#         "Changelog": f"https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md",
#     },
#     "KEYWORDS": [
#         "application",
#         "macOS",
#         "dev",
#         "devops",
#         "cache",
#         "utilities",
#         "cli",
#         "python",
#         "cython",
#         "text",
#         "console",
#         "log",
#         "debug",
#         "test",
#         "testing",
#         "logging",
#         "logger",
#     ],
#     "CLASSIFIERS": [
#         "Development Status :: 4 - Beta",
#         "License :: OSI Approved :: MIT License",
#         "Environment :: Console",
#         "Environment :: MacOS X",
#         "Intended Audience :: Developers",
#         "Natural Language :: English",
#         "Operating System :: MacOS",
#         "Operating System :: OS Independent",
#         "Programming Language :: Cython",
#         "Programming Language :: Python",
#         "Programming Language :: Python :: 3 :: Only",
#         "Programming Language :: Python :: 3",
#         # These are the Python versions tested; it may work on others
#         "Programming Language :: Python :: 3.8",
#         "Programming Language :: Python :: 3.9",
#         "Programming Language :: Python :: Implementation :: CPython",
#         "Programming Language :: Python :: Implementation :: PyPy",
#         "Topic :: Software Development :: Libraries :: Python Modules",
#         "Topic :: Software Development :: Testing",
#         "Topic :: Utilities",
#     ],
# }

# meta_data: Dict = {}
#     meta_exclude: List = [
#         "__name__",
#         "__doc__",
#         "__package__",
#         "__loader__",
#         "__spec__",
#         "__file__",
#         "__cached__",
#         "__builtins__",
#         "__annotations__",
#         "Dict",
#         "List",
#         "Tuple",
#         "meta_exclude",
#     ]

# meta_data = {k: v for k, v in locals().items() if k not in meta_exclude}
# __all__ = [k for k in meta_data.keys()]
