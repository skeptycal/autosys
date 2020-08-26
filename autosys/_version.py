#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" _version.py - version and demographic information

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
# 'Standard Library'
import json
# Standard Library
import sys

from dataclasses import Field, dataclass, field
from io import TextIOWrapper
from os import linesep as NL
from pathlib import Path
from tempfile import NamedTemporaryFile, mkstemp

# 'package imports'
from autosys.text_utils.nowandthen import now

from typing import Any, Dict, Final, List, Optional, Sequence, Set, Tuple

_debug_: Final[bool] = True
copyright_symbol: Final[str] = "©"  # could be (c)
temp_file: TextIOWrapper = NamedTemporaryFile(mode="x+t",
                                              encoding="utf-8",
                                              prefix="versionxxxxxx",
                                              suffix="bak")

VERSION_TAG: Final[str] = "# @version"


def my_class(func):
    return str(type(func)).split(".")[-1][:-2]


class MyVersionError(Exception):
    "An Error has occured during project version and metadata preparation."


@dataclass
class MyVersion(PrettyDict):
    name: str
    _start_year: int = now.year
    version: str = field(default="0.0.1")
    author: str = field(default="Michael Treanor")
    author_email: str = field(default="skeptycal@gmail.com")
    _license: str = field(default="MIT")
    python_requires: str = field(default=">=3.8")
    _copyright: str = ""

    def __post_init(self):
        if not self.name:
            raise ValueError("Project must have a name.")
        # * >>--------> add other necessary fields here
        for field in __dict__:
            # add property
            pass

    @property
    def version_info(self) -> (Tuple[int, int, int]):
        return self.version.split(".")

    @property
    def license(self) -> (str):
        return self._license.upper()

    @property
    def copyright(self) -> (str):
        if not self._copyright:
            self._copyright = self._get_copyright_date()
        return self._copyright

    def _get_copyright_date(self) -> (str):
        """ Return a correct formatted copyright string. """
        year = now.year
        tmp: str = ""
        try:
            self._start_year = int(self._start_year)
            # include start year if it is in [1900..now]?
            tmp = (f"{self._start_year}-"
                   if 1900 < self._start_year < year else "")
        except:
            self._start_year = year

        return f"Copyright {copyright_symbol} {tmp}{year} {self.author}"

    @property
    def _my_class(self):
        return my_class(self)

    def _export_all(self) -> (List[str]):
        """ Returns an '__all__' list.

            e.g.
                [
                    "__author__",
                    "__author_email__",
                    "__copyright__",
                    "__license__",
                    "__python_requires__",
                    "__title__",
                    "__version__",
                    "__version_info__",
                ] """

        return [dunder_it(x) for x in vars(self).keys()]

    def update_version_file(self,
                            files=List[TextIOWrapper]) -> Optional[Exception]:

        for original in files:
            with NamedTemporaryFile(
                    mode="wt",
                    encoding=self.DEFAULT_ENCODING,
                    prefix=__file__,
                    suffix="tmp",
            ) as temp_file:
                with open(file=original,
                          mode="rt",
                          encoding=self.DEFAULT_ENCODING) as fd:
                    data = fd.readlines()

                    # process lines
                try:
                    temp_file.writelines(data)
                except Exception as e:
                    raise MyVersionError(e)
                    return e
                response = Path(temp_file).replace(fd.name)

    def set_exports(self):
        """ Update script with project metadata. """
        tmp: List[str] = []
        with open(Path(__file__).resolve(), mode="+") as fp:
            lines = fp.readlines()
        with open(temp_file, mode="w") as temp_file:
            for line in lines:
                tmp.append(line)
            if line.startswith(VERSION_TAG):
                tmp.append(self.write_version)  # TODO make this
        temp_file.writelines(tmp)


""" def mkstemp(suffix: Optional[AnyStr]=...,
                prefix: Optional[AnyStr]=...,
                dir: Optional[_DirT[AnyStr]]=...,
                text: bool=...)

    User-callable function to create and return a unique temporary file. The return value is a pair (fd, name) where fd is the file descriptor returned by os.open, and name is the filename.

    If 'suffix' is not None, the file name will end with that suffix, otherwise there will be no suffix.

    If 'prefix' is not None, the file name will begin with that prefix, otherwise a default prefix is used.

    If 'dir' is not None, the file will be created in that directory, otherwise a default directory is used.

    If 'text' is specified and true, the file is opened in text mode. Else (the default) the file is opened in binary mode. On some operating systems, this makes no difference.

    If any of 'suffix', 'prefix' and 'dir' are not None, they must be the same type. If they are bytes, the returned name will be bytes; str otherwise.

    The file is readable and writable only by the creating user ID. If the operating system uses permission bits to indicate whether a file is executable, the file is executable by no one. The file descriptor is not inherited by children of this process.

    Caller is responsible for deleting the file when done with it.
    """

version = MyVersion(_start_year=2019, name="AutoSys", version="0.4.4")

# @version

if _debug_:
    import json

    _intro = f"{version.name} version {version.version} setup information"
    _hr = "=" * 60
    print(_intro)
    print(version.copyright)
    print()
    print(__file__)
    print()
    print(_hr)
    print("__all__ = ")
    print(version._export_all())
    print()
    # print(version.thats_all())
    print(_hr)
    print("dictionary created from 'version.to_dict()'")
    print(_hr)
    print(version.to_dict())
    print()
    # print(version.pretty_dict())
    print("to_json = ")
    print(version.to_json())
    print(_hr)
