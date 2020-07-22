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
    from os import linesep as NL
    from pathlib import Path
    from sys import argv as _argv, path as PYTHONPATH, stderr, stdout

    from loguru import logger  # NOQA
    from setuptools import find_namespace_packages, setup

    from typing import Dict, List, Optional, Sequence, Tuple

    from package_metadata import *

    _debug_: bool = False

    HERE = Path(__file__).resolve().parent.as_posix()

    # ... because this stuff never seems to work right ...
    if PY_INTERPRETER_PATH not in PYTHONPATH:
        PYTHONPATH.insert(0, PY_INTERPRETER_PATH)
    if HERE not in PYTHONPATH:
        PYTHONPATH.insert(0, HERE)

    LOG_FORMAT: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"

    logger.add(f"{HERE}/logs/{NAME}.log", retention="3 days")
    logger.add(
        f"{HERE}/logs/{NAME}_log.json", serialize=True, retention="10 days",
    )

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
        debug: bool = _debug_,
        verbose: bool = False,
        logging: bool = True,
        encoding: str = DEFAULT_ENCODING,
    ):

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

        self._encoding_: str = encoding
        logger.info(f"Encoding set to '{self.encoding}'")

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
    def here(self) -> str:
        if not self._here_:
            self._here_ = Path(__file__).resolve().parent.as_posix()
        return self._here_

    @property
    def debug(self) -> bool:
        """ Return debug flag. """
        # if self.arg("--debug"):
        #     self._debug_ = bool(self.arg("--debug"))
        if not self._debug_:
            self._debug_ = _debug_
        return self._debug_

    @property
    def encoding(self):
        """ Return file encoding (or lazy load default) """
        if not self._encoding_:
            self._encoding_ = DEFAULT_ENCODING
        return self._encoding_

    @property
    def name(self) -> str:
        if not self._name_:
            self._name_ = self.here.name
        return self._name_

    @property
    def verbose(self) -> bool:
        """ Return verbose flag. """
        if not self._verbose_:
            self._verbose_ = True
        return self._verbose_

    @property
    def version(self):
        """ Return verbose flag. """
        if not self._version_:
            if __version__:
                self._version_ = __version__
            else:
                self._version_ = "0.0.1"
        return self._version_


# ? ############################## Setup!


def main():
    sc = SetupConfig()
    sc.info(f"SetupConfig for {sc.name} version {sc.version}.")

    if sc.debug:  # do some live tests in debug mode ...
        sc.info(f"sc.debug mode set to {sc.debug}.")
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


if __name__ == "__main__":
    main()
