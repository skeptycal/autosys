#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_tempfile.py - temporary files and folders

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

import shutil
import sys
import tempfile
from dataclasses import Field, dataclass, field
from io import TextIOWrapper
from locale import getpreferredencoding
from os import linesep as NL
from pathlib import Path
from typing import Any, Deque, Dict, Final, List, Sequence, Set, Tuple

from autosys.text_utils.nowandthen import now

_debug_: Final[bool] = True
DEFAULT_ENCODING: Final[str] = getpreferredencoding(do_setlocale=True) or "utf-8"
copyright_symbol: Final[str] = "©"  # could be (c)

TMP_FD: TextIOWrapper = None



@dataclass
class TempFile:
    """ Temporary File Utility.
        Creates and manages temporary files, providing utilities for:

        - prefix
        - suffix
        - folder
        - delete when done?
        - named?
        - iterator?
        - generator?
        - log access?
        - cache access?
        -


        if name is provided, use name.
        if folder is provided, use folder.
        if delete?, use ...
        """

    fh: int = 0
    name: str = ""
    path: Path = field(default_factory=Path)
    log: bool = field(default=False)
    history: int = field(default=1000)

    def __post_init__(self):
        pass

    def __del__(self):
        pass
        # if not shutil.rm_tree():
        # del self

    def temp_it(self, func):
        def _temp_it_(self):
            with tempfile.NamedTemporaryFile as TMP_FD:
                result = func()
            return result

        return _temp_it_()

    def __enter__(self):
        return super().__enter__()

    def __exit__(self, *args):
        """
            This function only writes to disk file on exit. It is intended for use in short blocks of code as a temporary context manager. Long term usage increases the risk of data loss and will act as a memory leak.
            """
        # self.extend(self._stringio.getvalue().splitlines())
        # print(self.get_data(), file=sys.stderr)

        # self.truncate(0)
        # sys.stdout = self._stdout
        # del self  # free up some memory
        pass


tmp = TempFile()


@tmp.temp_it
def test_it():
    print(f"{temp_file=}")
    print(f"{TMP_FD}")


if __name__ == "__main__":

    # # fake 'with' block for directory
    # tmpdir = tempfile.mkdtemp()
    # print("temporary directory at " + tmpdir)
    # # do things with the tmpdir
    # shutil.rm_tree(tmpdir)

    print("testing decorated function ...")
    test_it()
