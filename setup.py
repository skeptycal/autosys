#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Setup

    Usage:  Setup [-dv] [--setname=<name>] [--setver=<version>] <setup_args>
            Setup [-h | --help] [--version]

    Arguments:
        setup_args              Python Setup Commands

    Options:
        --setname=<name>        Set Package Name
        --setver=<version>      Set Version Name
        -d --debug              Set Debug Mode [default=True]
        -v --verbose            Set Verbose Mode [default=True]
        -h --help               Show this screen.
        --version               Show version.
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

import logging
import os
from dataclasses import Field, dataclass, field
from locale import getpreferredencoding
from os import linesep as NL
from pathlib import Path
from sys import argv as _argv, path as PYTHONPATH, stderr, stdout
from docopt import docopt
from setuptools import find_namespace_packages, setup
from typing import Dict, Final, List, Optional, Sequence, Tuple
if True:
    from package_metadata import *
    __version__: str = '0.4.4'
    _debug_: bool = True


@dataclass
class SetupConfig:
    _file_: str = __file__
    _version_: str = __version__
    _debug_: bool = _debug_
    _verbose_: bool = False
    encoding: str = getpreferredencoding(do_setlocale=True) or "utf-8"
    _parents_: List = field(init=False)
    here: Path = field(init=False)
    _logging_: bool = True
    _logger_: Field = None
    _opt_: Field = None
    name: str = ''
    setup_args: str = ''

    def __post_init__(self):
        self._parents_: List = Path(self._file_).resolve().parents
        self.here = self._parents_[0]

        # 'name' must be set before the 'logger' is initialized
        # CLI argument overides hard coded or default value
        if self.arg('--setname'):
            self.name = self.arg('--setname')
        # if no arg and no hard coded value, use default (parent folder)
        elif not self.name:
            self.name = self.here.name

        # initialize logger by logging package name
        self.info(f'Begin logging: SetupConfig for package: {self.name}')
        self.info(f"Setup Path (here): {self.here}")

        if self.arg('--setver'):
            self._version_ = self.arg('--setver')
        if not self._version_:
            self._version_ = '0.0.1'
        self.info(f"Package version is set to '{self._version_}'")

        if self.arg('--debug'):
            self._debug_ = self.arg('--debug')
        self.info(f"Debug value is set to '{self._debug_}'")

        if self.arg('--verbose'):
            self._verbose_ = self.arg('--verbose')
        self.info(f"Verbose value is set to '{self._verbose_}'")

        if self.arg('<setup_args>'):
            self.setup_args = self.arg('<setup_args>')
        self.info(f"Setup Arguments set to '{self.setup_args}'")

        # make sure script path is in Python's path
        if self.here.as_posix() not in PYTHONPATH:
            PYTHONPATH.insert(0, self.here.as_posix())

    def dbprint(self, *args, **kwargs):
        ''' Print Debug Output '''
        if self.debug:
            print(*args, file=stderr, **kwargs)

    def info(self, *args):
        msg: str = ''
        for arg in args:
            # msg += str(arg)
            msg = f"{msg}{str(arg)} "
        self.logger.info(msg.rstrip())

    @property
    def debug(self):
        return self._debug_

    @property
    def opt(self):
        if not self._opt_:
            self._opt_ = docopt(
                __doc__, version=f'{self.name} version {self._version_}')
        return self._opt_

    def arg(self, name: str = ''):
        try:
            return self.opt[name]
        except KeyError:
            return None

    @property
    def logger(self):
        if not self._logger_:
            if not self._logging_:
                self._logger_ = self.dbprint
            else:
                self._logger_ = logging.getLogger(self.name)
                logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                                    datefmt='%a, %d %b %Y %H:%M:%S', filename=f'Logs/{self.name}.log', filemode='w')
        return self._logger_

    def load_fake_args(self, tmp: List = _argv[1:]):
        tmp.extend(['--debug', '--setname=stuff'])
        return tmp

    @staticmethod
    def table_print(data: (Dict, Sequence), **kwargs):
        ''' Pretty Print sequences or dictionaries.
        '''
        tmp: List = []
        if isinstance(data, (str, bytes)):
            raise TypeError(
                'Strings and bytes cannot be used for "table_print". Try another form of iterable')

        elif isinstance(data, dict):
            key_width = len(max(data.keys()))
            print(f'key_width = {key_width}.')
            tmp.extend(
                [f"{str(k):<15.15} :  {repr(v):<45.45}" for k, v in data.items()])
        elif isinstance(data, (list, tuple, set)):
            for x in data:
                try:
                    tmp.append(f"{str(x):<15.15} :  {repr(f'{x}'):<45.45}")
                except:
                    tmp.append(f"{str(x)}")
        else:
            raise TypeError(
                'Parameter must be an iterable Mapping or Sequence (Strings are excluded).')
        print(NL.join(tmp), **kwargs)

    @staticmethod
    def pip_safe_name(s: str):
        """ Return a name that is converted to pypi safe format.
            ####
            (Returns a lowercase string has no spaces or dashes)
            """
        return s.lower().replace("-", "_").replace(" ", "_")

    @staticmethod
    def readme(file_name: str = "readme.md", search_list: List[str] = ["readme.md", "readme.rst", "readme", "readme.txt"]):
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
                with open(find_path, mode="r", encoding=SetupConfig.encoding) as f:
                    return f.read()
            except IOError as e:
                raise IOError(
                    f"Cannot read from the 'readme' file '{find_path}'")
        else:
            raise FileNotFoundError(
                f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
            )


# ? ############################## Setup!


if __name__ == "__main__":
    s = SetupConfig()
    print(s.opt)
    if s.debug:  # do some live tests if setup process has changed ...
        print('debug mode ...')
        s.info('This debug message is used in place of the actual "setup" program.')
    # else:  # run setup ...
        # setup(**meta_data)
        setup(name=NAME,
              version=VERSION,
              description=DESCRIPTION,
              python_requires=REQUIRES_PYTHON,
              package_dir=PACKAGE_DIR,
              packages=find_namespace_packages(
                  f'{NAME}', exclude=PACKAGE_EXCLUDE),
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

    '''
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
    '''
