#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" #### AutoSys Setup

    ```
    Usage:  Setup [-dv] [--setname=<name>] [--setver=<version>] <setup_args>
            Setup [-h | --help] [--version]

    Arguments:
        setup_args              passed through to Python Setup (*)

    Options:
        --setname=<name>        Set Package Name
        --setver=<version>      Set Version Name
        -d --debug              Set Debug Mode [default=True]
        -v --verbose            Set Verbose Mode [default=True]
        -h --help               Show this screen.
        --version               Show version.

    * Use single quotes around 'setup_args' that contain dashes in order to
    pass them through to the Python Setup utility.

    ```
    e.g. Use these:
    ```
    python3 -m setup 'build -vn'
    python3 -m setup '--help-commands'
    ```
    instead of these:
    ```
    python3 -m setup build -vn
    python3 -m setup --help-commands
    ```
    """
""" Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

_debug_: bool = False


if True:  # ? ################### imports
    import os
    import sys

    from os import linesep as NL
    from os import sep as SEP
    from sys import argv as _argv, path as PYTHONPATH, stderr, stdout

    IS_WIN32 = sys.platform == "win32" or (getattr(os, "_name", False) == "nt")

    if sys.version_info[:2] >= (3, 6):
        from pathlib import Path, PurePath
    else:
        from pathlib2 import Path, PurePath

    try:
        from locale import getpreferredencoding

        DEFAULT_ENCODING = getpreferredencoding(do_setlocale=True)
        del getpreferredencoding
    except ImportError:
        DEFAULT_ENCODING = "utf-8"
    except:
        DEFAULT_ENCODING = "utf-8"
        del getpreferredencoding

    from loguru import logger  # NOQA
    from autosys._log import logger
    from setuptools import find_namespace_packages, setup
    from pep517.envbuild import build_wheel, build_sdist

    from typing import Dict, List, Optional, Sequence, Tuple

# ? ################################### Default Metadata
NAME: str = "AutoSys"
VERSION: str = "0.5.0"
DESCRIPTION: str = "System utilities for Python on macOS."
PYTHON_REQUIRES: str = ">=3.8.0"
KEYWORDS: List[str] = [
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
# ? ####################################################

if True:  # ? ################### imports
    PY3: bool = sys.version_info.major > 2

    HOME: str = Path().home().as_posix()
    HERE: str = Path(__file__).resolve().parent.as_posix()
    if not NAME:
        NAME = Path(HERE).name

    PY_INTERPRETER: Path = Path(sys.executable).resolve()
    PY_INTERPRETER_PATH: str = PY_INTERPRETER.parent.as_posix()

    try:
        PY_INT: Path = Path(PY_INTERPRETER).relative_to(HERE)
    except ValueError:
        PY_INT: Path = PY_INTERPRETER

    # FYI, when in a Jupyter notebook, this gives the path to the kernel launcher script.
    PY_INTERPRETER_NB: str = os.environ["_"]
    # if not run from virtual environment, this will be wrong...
    try:
        PY_VENV_PATH: str = Path(os.environ["VIRTUAL_ENV"]).resolve().as_posix()
    except KeyError:
        PY_VENV_PATH: str = None

    if PY_VENV_PATH:
        try:
            PY_VENV_PATH = Path(PY_VENV_PATH).relative_to(HERE)
        except ValueError:
            pass

    __version__: str = VERSION
    VERSION_INFO: Tuple[int] = VERSION.split(".")

    # from package_metadata import *

    # ... because this stuff never seems to work right ...
    if PY_VENV_PATH:
        for p in ["bin", f"lib/python@3.8/site-packages", "include"]:
            add_path = Path().joinpath(PY_VENV_PATH, p)
            if add_path.is_dir():
                add_path = Path(add_path).resolve().as_posix()
                logger.debug(f"adding path to PYTHON_PATH: {add_path}")
                if p not in PYTHONPATH:
                    PYTHONPATH.insert(0, p)
    if PY_INTERPRETER_PATH not in PYTHONPATH:
        logger.debug(f"adding path to PYTHON_PATH: {PY_INTERPRETER_PATH}")
        PYTHONPATH.insert(0, PY_INTERPRETER_PATH)
    if HERE not in PYTHONPATH:
        logger.debug(f"adding path to PYTHON_PATH: {HERE}")
        PYTHONPATH.insert(0, HERE)

    LOG_FORMAT: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    # choose a common location if you consolidate logs
    LOG_LOCATION: str = f"{HERE}/logs/"

    def readme(file_name: str = "readme.md", search_list: List[str] = []):
        """ Returns the text of the file (defaults to README files)

            The default file is `README.md` and is *NOT* case sensitive. (e.g. `README` is the same as `readme`)
            Can load *any* text file, but the default search path is setup for readme files

            ```
            Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
            ```

            Example:

            ```
            long_description=readme()
            ```
            """

        # add default search list for README files
        if not search_list:
            search_list = ["readme.md", "readme.rst", "readme", "readme.txt"]
        # make sure 'file_name' is in 'search_list' at index 0
        if file_name not in search_list:
            search_list.insert(0, file_name)
        found: bool = False
        # traverse up through directory tree searching for each file in 'search_list'
        for searchfile in search_list:
            # search in this script's path and above
            for parent in Path(file_name).resolve().parents:
                find_path = Path(parent / searchfile)
                if find_path.exists():
                    found = True
                    break
            if found:
                break
        if found:
            try:
                with open(find_path, mode="r", encoding=DEFAULT_ENCODING) as f:
                    return f.read()
            except IOError as e:
                raise IOError(f"Cannot read from the 'readme' file '{find_path}'")
        else:
            raise FileNotFoundError(
                f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
            )

    def pip_safe_name(s: str):
        """ Return a name that is converted to pypi safe format.
            ####
            (Returns a lowercase string has no spaces or dashes)
            """
        return s.lower().replace("-", "_").replace(" ", "_")

    def table_print(data: (Dict, Sequence), **kwargs):
        """ Pretty Print sequences or dictionaries.
        """
        tmp: List = []
        if isinstance(data, (str, bytes)):
            raise TypeError(
                'Strings and bytes cannot be used for "table_print". Try another form of iterable'
            )

        elif isinstance(data, dict):
            key_width = len(max(data.keys()))
            print(f"key_width = {key_width}.")
            tmp.extend(
                [f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()]
            )
        elif isinstance(data, (list, tuple, set)):
            for x in data:
                try:
                    tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
                except:
                    tmp.append(f"{str(x)}")
        else:
            raise TypeError(
                "Parameter must be an iterable Mapping or Sequence (Strings are excluded)."
            )
        print(NL.join(tmp), **kwargs)

    def get_version(file_name: str = f"{NAME}/__init__.py") -> str:
        try:
            NAME
        except ValueError:
            NAME = HERE.name
        with Path(file_name).open("r") as fp:
            regex_version = r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]'
            return re.search(regex_version, fp.read(), re.MULTILINE).group(1)


class LoggedException(Exception):
    def __init__(self, *args, **kwargs):
        logger.error(*args, **kwargs)
        super().__init__(*args, **kwargs)


@logger.catch
class SetupConfigError(LoggedException):
    """ An error occurred in SetupConfig. """


@logger.catch
class SetupConfig:
    def __init__(
        self,
        name: str = NAME,
        version: str = VERSION,
        description: str = DESCRIPTION,
        python_requires: str = PYTHON_REQUIRES,
        debug: bool = False,
        verbose: bool = False,
        logging: bool = True,
        encoding: str = DEFAULT_ENCODING,
    ):

        self._debug_: bool = debug
        self._verbose_: bool = verbose
        self._logging_: bool = logging
        if self.logging:  # TODO - check this stuff
            # standard log - kept for 3 days
            logger.add(f"{LOG_LOCATION}{NAME}.log", retention="3 days")
            # json log - kept for 10 days
            logger.add(
                f"{LOG_LOCATION}{NAME}_log.json", serialize=True, retention="10 days",
            )
        if self.debug:
            logger.configure()
            logger.level = "DEBUG"  # TODO - level setting is not working
        elif self.verbose:
            logger.level = "INFO"
        else:
            logger.level = "SUCCESS"
        logger.debug(f"Debug value is set to '{self.debug}'")
        logger.debug(f"Verbose value is set to '{self.verbose}'")

        self._name_: str = name
        logger.debug(f"Package name: {self.name}")
        self._version_: str = version
        logger.debug(f"Package version: '{self.version}'")
        self._here_: str = ""
        logger.debug(f"Script path: {self.here}")
        self._meta_data_: Dict = None
        self._description_: str = description
        self._python_requires_: str = python_requires
        self._encoding_: str = encoding

    def dbprint(self, *args, **kwargs):
        """ Print Debug Output to stderr. """
        if self.debug:
            print(*args, file=stderr, **kwargs)

    def info(self, *args):
        """ Join args into a single string 'info' message and log it. """
        msg: str = ""
        # TODO - ' '.join(args) had issues
        for arg in args:
            # msg += str(arg) # TODO - is this better than fstrings? ...
            msg = f"{msg}{str(arg)} "
        logger.info(msg.rstrip())

    def err(self, e):
        """ Log last exception. """
        logger.exception(e)

    @property
    def name(self) -> str:
        if not self._name_:
            if NAME:
                self._name_ = pip_safe_name(NAME)
            else:
                self._name_ = pip_safe_name(self.here.name)
        return self._name_

    @property
    def version(self):
        """ Return verbose flag. """
        if not self._version_:
            if VERSION:
                self._version_ = VERSION
            else:
                self._version_ = "0.0.1"
        return self._version_

    @property
    def python_requires(self):
        if not self._python_requires_:
            self._python_requires_ = PYTHON_REQUIRES
        return self._python_requires_

    @property
    def description(self):
        if not self._description_:
            self._description_ = DESCRIPTION
        return self._description_

    @property
    def meta_data(self):
        if not self._meta_data_:
            self._meta_data_ = {
                "name": self.name,
                "version": self.version,
                "description": self.description,
                "python_requires": self.python_requires,
                "package_dir": {"": f"{self.name}"},
                "packages": find_namespace_packages(
                    f"{self.name}", exclude=["*test*", "*bak*"]
                ),
                "py_modules": [f"{self.name}"],
                "license": "MIT",
                "long_description": readme(),
                "long_description_content_type": "text/markdown",
                "author": "Michael Treanor",
                "author_email": "skeptycal@gmail.com",
                "maintainer": "Michael Treanor",
                "maintainer_email": "skeptycal@gmail.com",
                "url": f"https://skeptycal.github.io/{self.name}/",
                "download_url": f"https://github.com/skeptycal/{self.name}/archive/{self.version}.tar.gz",
                "zip_safe": False,
                "include_package_data": True,
                # What packages are required for this module to be "e""xecuted"?,
                # "required": [
                #     "colorama>=0.3.4 ; sys_platform=='win32'",
                #     "win32-setctime>=1.0.0 ; sys_platform=='win32'",
                #     "APScheduler>=3.6.3",
                # ],
                # What packages are optional?
                # "extras": {
                #     "dev": [
                #         "pytest>=4.6.2",
                #     ],
                # },
                "package_data": {
                    # If any package contains these files, include them:
                    "": [
                        "*.txt",
                        "*.rst",
                        "*.md",
                        "*.ini",
                        "*.png",
                        "*.jpg",
                        "*.py",
                        "__init__.pyi",
                        "py.typed",
                    ]
                },
                "project_urls": {
                    "Website": f"https://skeptycal.github.io/{self.name}/",
                    "Documentation": f"https://skeptycal.github.io/{self.name}/docs",
                    "Source Code": f"https://www.github.com/skeptycal/{self.name}/",
                    "Changelog": f"https://github.com/skeptycal/{self.name}/blob/master/CHANGELOG.md",
                },
                "keywords": [
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
                ],
                "classifiers": [
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
                    "Programming Language :: Python :: Implementation :: CPython",
                    "Programming Language :: Python :: Implementation :: PyPy",
                    "Topic :: Software Development :: Libraries :: Python Modules",
                    "Topic :: Software Development :: Testing",
                    "Topic :: Utilities",
                ],
            }
        return self._meta_data_

    @property
    def here(self) -> str:
        if not self._here_:
            self._here_ = Path(__file__).resolve().parent.as_posix()
        return self._here_

    @property
    def debug(self) -> bool:
        """ Return debug flag. """
        if not self._debug_:
            self._debug_ = _debug_
        return self._debug_

    @property
    def logging(self) -> bool:
        """ Return debug flag. """
        if not self._logging_:
            self._logging_ = True
        return self._logging_

    @property
    def verbose(self) -> bool:
        """ Return verbose flag. """
        if not self._verbose_:
            self._verbose_ = True
        return self._verbose_

    @property
    def encoding(self):
        """ Return file encoding (or lazy load default) """
        if not self._encoding_:
            self._encoding_ = DEFAULT_ENCODING
        return self._encoding_

    def run(self):
        if self.debug:
            table_print(self.metadata)
        else:
            setup(**self.meta_data)


# ? ############################## Setup!
sc = SetupConfig(debug=_debug_)


@logger.catch
def main():
    sc.info(f"SetupConfig for {sc.name} version {sc.version}.")
    if sc.debug:  # do some live tests in debug mode ...
        sc.debug(f"sc.debug mode set to {sc.debug}.")
    else:  # run setup ...
        sc.run()


if __name__ == "__main__":
    main()


# setup(
#     name=self.name,
#     version=self.version,
#     description=self.metadata.description,
#     python_requires=REQUIRES_PYTHON,
#     package_dir=PACKAGE_DIR,
#     packages=find_namespace_packages(f"{NAME}", exclude=PACKAGE_EXCLUDE),
#     # py_modules=[f"{NAME}"],
#     license=LICENSE,
#     long_description=LONG_DESCRIPTION,
#     long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
#     author=AUTHOR,
#     author_email=AUTHOR_EMAIL,
#     maintainer=MAINTAINER or AUTHOR,
#     maintainer_email=MAINTAINER_EMAIL or AUTHOR_EMAIL,
#     url=URL,
#     download_url=DOWNLOAD_URL,
#     zip_safe=ZIP_SAFE,
#     include_package_data=INCLUDE_PACKAGE_DATA,
#     # setup_requires=["isort"],
#     install_requires=REQUIRED,
#     extras_require=EXTRAS,
#     package_data=PACKAGE_DATA,
#     project_urls=PROJECT_URLS,
#     keywords=KEYWORDS,
#     classifiers=CLASSIFIERS,
# )


# meta_data = {
#     "name": NAME,
#     "version": VERSION,
#     "description": DESCRIPTION,
#     "python_requires": REQUIRES_PYTHON,
#     "package_dir": {"": f"{NAME}"},
#     "packages": find_namespace_packages(f"{NAME}", exclude=["*test*", "*bak*"]),
#     "py_modules": [f"{NAME}"],
#     "license": "MIT",
#     "long_description": readme(),
#     "long_description_content_type": "text/markdown",
#     "author": "Michael Treanor",
#     "author_email": "skeptycal@gmail.com",
#     "maintainer": "Michael Treanor",
#     "maintainer_email": "skeptycal@gmail.com",
#     "url": f"https://skeptycal.github.io/{NAME}/",
#     "download_url": f"https://github.com/skeptycal/{NAME}/archive/{VERSION}.tar.gz",
#     "zip_safe": False,
#     "include_package_data": True,
#     # What packages are required for this module to be "e""xecuted"?,
#     # "required": [
#     #     "colorama>=0.3.4 ; sys_platform=='win32'",
#     #     "win32-setctime>=1.0.0 ; sys_platform=='win32'",
#     #     "APScheduler>=3.6.3",
#     #     "bs4>=0.0.1",
#     #     "click-spinner>=0.1.10",
#     #     "Cython>=0.29.19",
#     #     "docopt>=0.6.2",
#     #     "Flask>=1.1.2",
#     #     "pathlib2>=2.3.5",
#     #     "pathspec>=0.8.0",
#     #     "pydash>=4.8.0",
#     #     "regex>=2020.6.8",
#     #     "shellingham>=1.3.2",
#     #     "streamlit>=0.61.0",
#     #     "tabulate>=0.8.7",
#     #     "trafaret>=2.0.2",
#     #     "twine>=3.1.1",
#     #     "typed-ast>=1.4.1",
#     #     "typer>=0.2.1",
#     #     "ujson>=3.0.0",
#     #     "yfinance>=0.1.54",
#     # ],
#     # What packages are optional?
#     # "extras": {
#     #     "dev": [
#     #         "APScheduler>=3.6.3",
#     #         "autopep8>=1.5.3",
#     #         "bs4>=0.0.1",
#     #         "click-spinner>=0.1.10",
#     #         "codecov>=2.1.4",
#     #         "Cython>=0.29.19",
#     #         "docopt>=0.6.2",
#     #         "flake8>=3.8.3",
#     #         "Flask>=1.1.2",
#     #         "isort>=4.3.20",
#     #         "pathlib2>=2.3.5",
#     #         "pathspec>=0.8.0",
#     #         "pydash>=4.8.0",
#     #         "pygments-pytest>=2.0.0",
#     #         "pylint>=2.5.3",
#     #         "pytest-bench>=0.3.0",
#     #         "pytest-cov>=2.10.0",
#     #         "pytest-pydocstyle>=2.1.3",
#     #         "pytest-race>=0.1.1",
#     #         "pytest-sugar>=0.9.3",
#     #         "pytest>=4.6.2",
#     #         "regex>=2020.6.8",
#     #         "shellingham>=1.3.2",
#     #         "sphinx-autobuild>=0.7.1",
#     #         "sphinx-rtd-theme>=0.4.3",
#     #         "sphinxcontrib-napoleon>=0.7",
#     #         "streamlit>=0.61.0",
#     #         "tabulate>=0.8.7",
#     #         "tox-travis>=0.12",
#     #         "tox>=3.9.0",
#     #         "trafaret>=2.0.2",
#     #         "twine>=3.1.1",
#     #         "typed-ast>=1.4.1",
#     #         "typer>=0.2.1",
#     #         "ujson>=3.0.0",
#     #         "yfinance>=0.1.54",
#     #     ],
#     # },
#     "package_data": {
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
#     "project_urls": {
#         "Website": f"https://skeptycal.github.io/{NAME}/",
#         "Documentation": f"https://skeptycal.github.io/{NAME}/docs",
#         "Source Code": f"https://www.github.com/skeptycal/{NAME}/",
#         "Changelog": f"https://github.com/skeptycal/{NAME}/blob/master/CHANGELOG.md",
#     },
#     "keywords": [
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
#     "classifiers": [
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
