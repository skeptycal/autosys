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

    * Use single quotes around setup_args that contain dashes in order to
    pass them through to the Python Setup utility.

    ```
    e.g. Use these:
    ```
    python3 -m setup build '-vn'
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


# import logging
import os
import sys

# from dataclasses import Field, dataclass, field
from os import linesep as NL
from pathlib import Path
from sys import argv as _argv, path as PYTHONPATH, stderr, stdout

from docopt import docopt
from loguru import logger  # NOQA
from setuptools import find_namespace_packages, setup

from typing import Dict, Final, List, Optional, Sequence, Tuple

if True:
    try:
        from locale import getpreferredencoding

        DEFAULT_ENCODING = getpreferredencoding(do_setlocale=True)
        del getpreferredencoding
    except ImportError:
        DEFAULT_ENCODING = "utf-8"
    except:
        DEFAULT_ENCODING = "utf-8"
        del getpreferredencoding

    from package_metadata import *

    __version__: str = "0.4.4"
    _debug_: bool = True

    PY3 = sys.version_info.major > 2

    PY_INTERPRETER_PATH = os.path.abspath(sys.executable)
    # FYI, when in a Jupyter notebook, this gives the path to the kernel launcher script.
    PY_INTERPRETER_PATH_ALT = os.environ["_"]
    # if not run from virtual environment, this will be wrong...
    try:
        PY_VENV_PATH = os.environ["VIRTUAL_ENV"]
    except KeyError:
        PY_VENV_PATH = None
    # stream = os.popen("pip show pip")
    # PY_PACKAGES_LOCATION = stream.read()
    # stream.close()
    # print(PY3)
    # print(PY_INTERPRETER_PATH)
    # print(PY_PACKAGES_LOCATION)
    # print(PY_VENV_PATH)

    sys.path.insert(0, os.path.abspath("."))
    sys.path.insert(0, os.path.abspath(PY_INTERPRETER_PATH))
    if PY3:
        pass


def readme(
    file_name: str = "readme.md",
    search_list: List[str] = ["readme.md", "readme.rst", "readme", "readme.txt"],
):
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
            with open(find_path, mode="r", encoding=SetupConfig().encoding) as f:
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
        tmp.extend([f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()])
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


class SetupConfigError(Exception):
    """ An error occurred in SetupConfig. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.exception()


class SetupConfig:
    # _file_: str = __file__

    # _logger_: Field = None
    # _opt_: Field = None
    # setup_args: str = ""

    def __init__(
        self,
        name: str = "",
        version: str = __version__,
        debug: bool = _debug_,
        verbose: bool = False,
        logging: bool = True,
        encoding: str = DEFAULT_ENCODING,
        usage: docopt = doc,
    ):

        self._here_: Path = None
        self._doc_: docopt = doc
        self._opt_: docopt = None
        # make sure script path is in Python's path
        if self.here.as_posix() not in PYTHONPATH:
            PYTHONPATH.insert(0, self.here.as_posix())

        self._version_: str = version
        self._debug_: bool = debug
        self._verbose_: bool = verbose
        self._logging_: bool = logging
        self._encoding_: str = encoding

        logger.info(f"Begin logging: SetupConfig for package: {self.name}")
        logger.info(f"Setup Path (here): {self.here}")
        logger.info(f"Package version is set to '{self.version}'")
        logger.info(f"Debug value is set to '{self.debug}'")
        logger.info(f"Verbose value is set to '{self.verbose}'")
        logger.info(f"Setup Arguments set to '{self.setup_args}'")

    @property
    def encoding(self):
        """ Return file encoding (or lazy load default) """
        if not self._encoding_:
            self._encoding_ = DEFAULT_ENCODING
        return self._encoding_

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

    @property
    def here(self):
        if not self._here_:
            self._here_ = Path(__file__).resolve().parents[0]
        return self._here_

    @property
    def debug(self):
        """ Return debug flag. """
        if self.arg("--debug"):
            self._debug_ = self.arg("--debug")
        elif not self._debug_:
            self._debug_ = _debug_
        return self._debug_

    @property
    def name(self):
        if self.arg("--setname"):
            self._name_ = self.arg("--setname")
        elif not self._name_:
            self._name_ = self.here.name
        return self._name_

    @property
    def verbose(self):
        """ Return verbose flag. """
        if self.arg("--verbose"):
            self._debug_ = self.arg("--verbose")
        elif not self._verbose_:
            self._verbose_ = True
        return self._verbose_

    @property
    def setup_args(self):
        """ Return verbose flag. """
        if self.arg("<setup_args>"):
            self.setup_args = self.arg("<setup_args>")
        elif not self.setup_args:
            self.setup_args = "--help"
        return self.setup_args

    @property
    def err(self):
        """ Log last exception. """
        logger.error("Exception occurred", exc_info=True)

    @property
    def opt(self):
        """ Return CLI arguments from 'docopt' package (or lazy load) """
        if not self._opt_:
            self._opt_ = doc
        return self._opt_

    def arg(self, name: str = "") -> (str, None):
        """ Return a specific CLI argument from 'docopt' package (or None). """
        try:
            return self.opt[name]
        except KeyError as e:
            logger.exception(e)
            self.err
            return None

    @property
    def logger(self):
        # omg logging is a pain ... I'm using the 'loguru' package for now
        # I do eventually want to make my own, for learning purposes,
        #   but for now, I just want to use some logging ...
        if not self._logger_:
            self._logger_ = logger  # TODO - replacement for my work in progress

            # # lazy load a custom logger
            # datefmt = "%a, %d %b %Y %H:%M:%S"

            # # add stderr output if 'verbose' is set
            # if self.verbose:
            #     stream_format = logging.Formatter(
            #         "%(name)s - %(levelname)s - %(message)s"
            #     )
            #     self._logger_.addHandler(
            #         self._set_log_handler(stream_format, logging.StreamHandler(),)
            #     )

            # # add log file output if 'logging' is set
            # if self.logging:
            #     log_file_name: str = f"Logs/{self.name}.log"
            #     print(log_file_name)
            #     file_format = logging.Formatter(
            #         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            #     )
            #     print(file_format)

            #     self._logger_.addHandler(
            #         self._set_log_handler(
            #             file_format, logging.FileHandler(log_file_name),
            #         )
            #     )
            #     print(self._logger_)
        return self._logger_

    @property
    def logging(self):
        """ Return logging flag. """
        return self._logging_

    @property
    def version(self):
        """ Return verbose flag. """
        if not self._version_:
            if self.arg("--setver"):
                self._version_ = self.arg("--setver")
            elif __version__:
                self._version_ = __version__
            else:
                self._version_ = "0.0.1"
        return self._version_


# ? ############################## Setup!


if __name__ == "__main__":
    doc: docopt = docopt(__doc__, version=f"{__name__} version {__version__}")
    sc = SetupConfig()
    print(f"Setup for {sc.name} version {sc.version}.")
    if sc.debug:  # do some live tests if setup process has changed ...
        print(f"debug mode set to {sc.debug}")
    else:  # run setup ...
        setup(
            name=NAME,
            version=VERSION,
            description=DESCRIPTION,
            python_requires=REQUIRES_PYTHON,
            package_dir=PACKAGE_DIR,
            packages=find_namespace_packages(f"{NAME}", exclude=PACKAGE_EXCLUDE),
            # py_modules=[f"{NAME}"],
            license=LICENSE,
            long_description=LONG_DESCRIPTION,
            long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            maintainer=MAINTAINER or AUTHOR,
            maintainer_email=MAINTAINER_EMAIL or AUTHOR_EMAIL,
            url=URL,
            download_url=DOWNLOAD_URL,
            zip_safe=ZIP_SAFE,
            include_package_data=INCLUDE_PACKAGE_DATA,
            # setup_requires=["isort"],
            install_requires=REQUIRED,
            extras_require=EXTRAS,
            package_data=PACKAGE_DATA,
            project_urls=PROJECT_URLS,
            keywords=KEYWORDS,
            classifiers=CLASSIFIERS,
        )

    """
    # references ...
    colorama_Fore: Dict[str, str] = {
        'BLACK': '\x1b[30m',
        'BLUE': '\x1b[34m',
        'CYAN': '\x1b[36m',
        'GREEN': '\x1b[32m',
        'LIGHTBLACK_EX': '\x1b[90m',
        'LIGHTBLUE_EX': '\x1b[94m',
        'LIGHTCYAN_EX': '\x1b[96m',
        'LIGHTGREEN_EX': '\x1b[92m',
        'LIGHTMAGENTA_EX': '\x1b[95m',
        'LIGHTRED_EX': '\x1b[91m',
        'LIGHTWHITE_EX': '\x1b[97m',
        'LIGHTYELLOW_EX': '\x1b[93m',
        'MAGENTA': '\x1b[35m',
        'RED': '\x1b[31m',
        'RESET': '\x1b[39m',
        'WHITE': '\x1b[37m',
        'YELLOW': '\x1b[33m',
    }
    colorama_Back: Dict[str, str] = {
        'BLACK': '\x1b[40m',
        'BLUE': '\x1b[44m',
        'CYAN': '\x1b[46m',
        'GREEN': '\x1b[42m',
        'LIGHTBLACK_EX': '\x1b[100m',
        'LIGHTBLUE_EX': '\x1b[104m',
        'LIGHTCYAN_EX': '\x1b[106m',
        'LIGHTGREEN_EX': '\x1b[102m',
        'LIGHTMAGENTA_EX': '\x1b[105m',
        'LIGHTRED_EX': '\x1b[101m',
        'LIGHTWHITE_EX': '\x1b[107m',
        'LIGHTYELLOW_EX': '\x1b[103m',
        'MAGENTA': '\x1b[45m',
        'RED': '\x1b[41m',
        'RESET': '\x1b[49m',
        'WHITE': '\x1b[47m',
        'YELLOW': '\x1b[43m'
    }
    colorama_Style: Dict[str, str] = {
        'BRIGHT': '\x1b[1m',
        'DIM': '\x1b[2m',
        'NORMAL': '\x1b[22m',
        'RESET_ALL': '\x1b[0m'
    }
    """

    # def _set_log_handler(
    #     self,
    #     formatter_: logging.Formatter,
    #     handler_: logging.Handler,
    #     level_: int = logging.DEBUG,
    # ) -> logging.Handler:
    # _h: logging.Handler = handler_
    # _h.setLevel(level_)
    # _h.setFormatter(formatter_)
    # return _h
    # self._logger_.addHandler(handler_)
