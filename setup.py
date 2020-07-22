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


if True:  # ? ################### imports and utilities
    # import os
    # import sys

    # from dataclasses import Field, dataclass, field
    from os import linesep as NL
    from pathlib import Path
    from sys import argv as _argv, path as PYTHONPATH, stderr, stdout

    from docopt import docopt
    from loguru import logger  # NOQA
    from setuptools import find_namespace_packages, setup

    from typing import Dict, Final, List, Optional, Sequence, Tuple

    from package_metadata import *

    DOC: docopt = docopt(__doc__, version=f"{NAME} version {VERSION}")

    _debug_: bool = True

    HERE = Path(__file__).resolve().parent.as_posix()

    # ... because this stuff never seems to work right ...
    if PY_INTERPRETER_PATH not in PYTHONPATH:
        PYTHONPATH.insert(0, PY_INTERPRETER_PATH)
    if HERE not in PYTHONPATH:
        PYTHONPATH.insert(0, HERE)

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


class SetupConfigError(Exception):
    """ An error occurred in SetupConfig. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.exception()


class SetupConfig:
    def __init__(
        self,
        name: str = NAME,
        version: str = __version__,
        debug: bool = _debug_,
        verbose: bool = False,
        logging: bool = True,
        encoding: str = DEFAULT_ENCODING,
        doc: docopt = DOC,
    ):

        self._opt_: docopt = doc
        self._debug_: bool = debug
        self._verbose_: bool = verbose
        self._logging_: bool = logging
        logger.info(f"Debug value is set to '{self.debug}'")
        logger.info(f"Verbose value is set to '{self.verbose}'")

        self._name_: str = name
        logger.info(f"Package name: {self.name}")
        self._version_: str = version
        logger.info(f"Package version: '{self.version}'")
        self._here_: str = ""
        logger.info(f"Script path: {self.here}")

        self._setup_args_: str = ""
        self._encoding_: str = encoding
        logger.info(f"Setup Arguments set to '{self.setup_args}'")
        logger.info(f"Encoding set to '{self.encoding}'")

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
    def here(self) -> str:
        if not self._here_:
            self._here_ = Path(__file__).resolve().parent.as_posix()
        return self._here_

    @property
    def debug(self) -> bool:
        """ Return debug flag. """
        if self.arg("--debug"):
            self._debug_ = bool(self.arg("--debug"))
        elif not self._debug_:
            self._debug_ = _debug_
        return self._debug_

    @property
    def name(self) -> str:
        if self.arg("--setname"):
            self._name_ = self.arg("--setname")
        elif not self._name_:
            self._name_ = self.here.name
        return self._name_

    @property
    def verbose(self) -> bool:
        """ Return verbose flag. """
        if self.arg("--verbose"):
            self._debug_ = self.arg("--verbose")
        elif not self._verbose_:
            self._verbose_ = True
        return self._verbose_

    @property
    def setup_args(self) -> str:
        """ Return verbose flag. """
        if self.arg("<setup_args>"):
            self._setup_args_ = self.arg("<setup_args>")
        elif not self._setup_args_:
            self._setup_args_ = "--help"
        return self._setup_args_

    def err(self, e):
        """ Log last exception. """
        logger.exception(e)

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
            self.err(e)
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
    sc = SetupConfig()
    sc.info(f"SetupConfig for {sc.name} version {sc.version}.")

    if sc.debug:  # do some live tests if setup process has changed ...
        sc.info(f"sc.debug mode set to {sc.debug}.")
        print(f"setup {sc.setup_args}")
        # else:  # run setup ...
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
