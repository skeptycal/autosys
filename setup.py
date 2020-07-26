#!/usr/bin/env python3
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
# flake8: noqa: E501

_debug_: bool = False

# ? ################################### Default Metadata
NAME: str = 'AutoSys'
USERNAME: str = 'skeptycal'
DESCRIPTION: str = 'System utilities for Python on macOS.'
PYTHON_REQUIRES: str = '>=3.6.0'
# ? ####################################################

if True:  # ? ################### imports
    import os
    import re
    import sys

    from io import TextIOWrapper
    from os import linesep as NL
    from sys import stderr, path as PYTHONPATH

    IS_WIN32 = sys.platform == 'win32' or (getattr(os, '_name', False) == 'nt')

    if sys.version_info[:2] >= (3, 6):
        from pathlib import Path, PurePath
    else:
        from pathlib2 import Path, PurePath

    try:
        from locale import getpreferredencoding

        DEFAULT_ENCODING = getpreferredencoding(do_setlocale=True)
        del getpreferredencoding
    except ImportError:
        DEFAULT_ENCODING = 'utf-8'
    except Exception:
        DEFAULT_ENCODING = 'utf-8'
        del getpreferredencoding

    # from loguru import logger
    from auto_loguru import logger
    from setuptools import find_namespace_packages, setup

    # from pep517.envbuild import build_wheel, build_sdist

    from typing import (
        Any,
        AnyStr,
        Dict,
        List,
        Match,
        Optional,
        Sequence,
        Set,
        Tuple,
        Union,
    )

    PathLike = Union[Path, str, None]


if True:  # ? ################### imports
    PY3: bool = sys.version_info.major > 2

    HOME: str = Path().home().as_posix()
    HERE: str = Path(__file__).resolve().parent.as_posix()

    if not NAME:
        NAME = Path(HERE).name

    LOG_FORMAT: str = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'
    # choose a common location if you consolidate logs
    LOG_LOCATION: str = f'{HERE}/logs/'

    def readme(file_name: str = 'readme.md', search_list: List[str] = []) -> str:
        """ Returns the text of the file (defaults to README files)

            The default file is `README.md` and is *NOT* case sensitive.
            (e.g. `README` is the same as `readme`)
            Can load *any* text file, but the default search path is setup
            for readme files

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
            search_list = ['readme.md', 'readme.rst', 'readme', 'readme.txt']
        # make sure 'file_name' is in 'search_list' at index 0
        if file_name not in search_list:
            search_list.insert(0, file_name)
        found: bool = False
        # traverse up through directory tree searching for each
        # file in 'search_list'
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
                with open(find_path, mode='r', encoding=DEFAULT_ENCODING) as f:
                    return f.read()
            except OSError:
                raise OSError(
                    f"Cannot read from the \
                    'readme' file '{find_path}'",
                )
        else:
            raise FileNotFoundError(
                f"Cannot find project 'readme' file in project \
                    tree. Search list = {search_list}",
            )

    def pip_safe_name(s: str) -> str:
        """ Return a name that is converted to pypi safe format.
            ####
            (Returns a lowercase string has no spaces or dashes)
            """
        return s.lower().replace('-', '_').replace(' ', '_')

    NAME = pip_safe_name(NAME)

    def get_version(file_name: str = f'{HERE}/pyproject.toml') -> str:
        logger.info(f'pyproject.toml file: {file_name}')
        with Path(file_name).open('r') as fp:
            regex_version: re.Pattern[Any] = re.compile(
                r'^version\s*=\s*[\'"]([^\'"]*)[\'"]', re.MULTILINE,
            )
            return re.search(regex_version, fp.read()).group(1)  # type: ignore

    VERSION: str = get_version()
    __version__: str = VERSION
    VERSION_INFO: Tuple[int, ...] = tuple(map(int, VERSION.split('.')))

    def table_print(data: (Dict, Sequence), **kwargs) -> None:  # type: ignore
        """ Pretty Print sequences or dictionaries.
        """
        tmp: List[str] = []
        if isinstance(data, AnyStr):
            raise TypeError(
                'Strings and bytes cannot be used for "table_print". \
                    Try another form of iterable',
            )

        elif isinstance(data, dict):
            key_width: int = len(max(data.keys()))
            print(f'key_width = {key_width}.')
            tmp.extend(
                [
                    f'{str(k):<15.15} :  \
                    {repr(v):<45.45}'
                    for k, v in data.items()
                ],
            )
        elif isinstance(data, (list, tuple, set)):
            for x in data:
                try:
                    tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
                except:
                    tmp.append(f'{str(x)}')
        else:
            raise TypeError(
                'Parameter must be an iterable Mapping or Sequence \
                    (Strings are excluded).',
            )
        print(NL.join(tmp), **kwargs)


class LoggedException(Exception):
    def __init__(self, *args: Any) -> None:
        logger.error(*args)
        super().__init__(*args)


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
            logger.add(f'{LOG_LOCATION}{NAME}.log', retention='3 days')
            # json log - kept for 10 days
            logger.add(
                f'{LOG_LOCATION}{NAME}_log.json', serialize=True, retention='10 days',
            )
        if self.debug:
            logger.configure()
            logger.level = 'DEBUG'  # TODO - level setting is not working
        elif self.verbose:
            logger.level = 'INFO'
        else:
            logger.level = 'SUCCESS'
        logger.debug(f"Debug value is set to '{self.debug}'")
        logger.debug(f"Verbose value is set to '{self.verbose}'")

        self._name_: str = name
        logger.debug(f'Package name: {self.name}')
        self._version_: str = version
        logger.debug(f"Package version: '{self.version}'")
        self._here_: str = ''
        logger.debug(f'Script path: {self.here}')
        self._meta_data_: Dict[str, Any] = {}
        self._description_: str = description
        self._python_requires_: str = python_requires
        self._encoding_: str = encoding

    def dbprint(self, *args, **kwargs) -> None:  # type: ignore
        """ Print Debug Output to stderr. """
        if self.debug:
            print(*args, file=stderr, **kwargs)  # type: ignore

    def info(self, *args: Sequence[str]) -> None:
        """ Join args into a single string 'info' message and log it. """
        msg: str = ''
        # TODO - ' '.join(args) had issues
        for arg in args:
            # msg += str(arg) # TODO - is this better than fstrings? ...
            msg = f'{msg}{str(arg)} '
        logger.info(msg.rstrip())

    def err(self, e: Exception) -> None:
        """ Log last exception. """
        logger.exception(e)

    @property
    def name(self) -> str:
        if not self._name_:
            if NAME:
                self._name_ = pip_safe_name(NAME)
            else:
                self._name_ = pip_safe_name(Path(self.here).name)
        return self._name_

    @property
    def version(self) -> str:
        """ Return verbose flag. """
        if not self._version_:
            if VERSION:
                self._version_ = VERSION
            else:
                self._version_ = '0.0.1'
        return self._version_

    @property
    def python_requires(self) -> str:
        if not self._python_requires_:
            self._python_requires_ = PYTHON_REQUIRES
        return self._python_requires_

    @property
    def description(self) -> str:
        if not self._description_:
            self._description_ = DESCRIPTION
        return self._description_

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
    def encoding(self) -> str:
        """ Return file encoding (or lazy load default) """
        if not self._encoding_:
            self._encoding_ = DEFAULT_ENCODING
        return self._encoding_

    def run(self) -> None:
        if self.debug:
            table_print(self.__dict__)
        else:
            setup(
                name=NAME,
                version=VERSION,
                long_description=readme(),
                package_dir={'': f'{self.name}'},
                packages=find_namespace_packages(
                    f'{self.name}', exclude=['*test*', '*bak*'],
                ),
                py_modules=[f'{self.name}'],
                url=f'https://{USERNAME}.github.io/{self.name}/',
                download_url=f'https://github.com/{USERNAME}/{self.name}/archive/{self.version}.tar.gz',
                project_urls={
                    'Website': f'https://{USERNAME}.github.io/{self.name}/',
                    'Documentation': f'https://{USERNAME}.github.io/{self.name}/docs',
                    'Source Code': f'https://www.github.com/{USERNAME}/{self.name}/',
                    'Changelog': f'https://github.com/{USERNAME}/{self.name}/blob/master/CHANGELOG.md',
                },
            )


# ? ############################## Setup!
sc = SetupConfig(debug=_debug_)


@logger.catch
def main() -> None:
    sc.info(f'SetupConfig for {sc.name} version {sc.version}.')
    if sc.debug:  # do some live tests in debug mode ...
        logger.debug(f'sc.debug mode set to {sc.debug}.')
    else:  # run setup ...
        sc.run()


if __name__ == '__main__':
    main()
