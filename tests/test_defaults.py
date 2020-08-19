#!/usr/bin/env python3
""" Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# based on the pathlib2 testing setup:
# Reference: https://github.com/mcmtroffaes/pathlib2
# Copyright (c) 2014-2017 Matthias C. M. Troffaes
# Copyright (c) 2012-2014 Antoine Pitrou and contributors
# Distributed under the terms of the MIT License.
import errno
import io
import os
import pickle
import platform
import socket
import stat
import sys
import tempfile
import unittest

from os import PathLike, linesep as NL
from sys import version_info

from loguru import logger

from typing import (
    Any, Callable, Dict, List, MutableMapping,
    MutableSequence, NoReturn, Optional, Sequence,
    TextIO, Tuple, Type, TypeVar, Union, overload)

try:
    import pathlib2 as pathlib
    from pathlib2 import Path
    PATHLIB_LIBRARY: str = 'pathlib2'
except:
    import pathlib
    from pathlib import Path
    PATHLIB_LIBRARY: str = 'pathlib'


# *####################################### Version checking for imports
if sys.version_info >= (3, 3):
    import collections.abc as collections_abc
else:
    import collections as collections_abc

if sys.version_info < (2, 7):
    try:
        import unittest2 as unittest
    except ImportError:
        raise ImportError("unittest2 is required for tests on pre-2.7")
else:
    import unittest

if sys.version_info < (3, 3):
    try:
        from unittest import mock
    except ImportError:
        raise ImportError("mock is required for tests on pre-3.3")
else:
    from unittest import mock

# assertRaisesRegex is missing prior to Python 3.2
if sys.version_info < (3, 2):
    unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegexp

if sys.version_info >= (3, 7):
    pass

try:
    from test import support
except ImportError:
    from test import test_support as support

android_not_root = getattr(support, "android_not_root", False)


TESTFN = support.TESTFN


class SystemProperties:

    def __init__(self) -> None:
        self._platform: str = platform.platform().lower()
        self.is_64bits: bool = sys.maxsize > 2**32

    @property
    def platform(self):
        if not self._platform:
            self._platform = platform.platform().lower()
        return self._platform

    @property
    def is_win(self) -> bool:
        return 'win' in self._platform

    @property
    def is_mac(self) -> bool:
        return 'macos' in self._platform

    @property
    def platform(self) -> str:
        if self.is_mac:
            return 'macOS'
        return 'Windows' if self.is_win else 'Linux'

    @property
    def py_version(self) -> sys.version_info:
        return sys.version_info

    def py_major(self) -> int:
        return self.py_version.major

    def py_minor(self) -> int:
        return self.py_version.minor

    def py_micro(self) -> int:
        return self.py_version.micro


sp = SystemProperties()

PLATFORM = sp.platform
IS_WIN = sp.is_win
IS_MAC = sp.is_mac


only_pathlib2 = unittest.skipIf(
    PATHLIB_LIBRARY != 'pathlib2',
    'test requires the pathlib2 library',
)

# work around broken support.rmtree on Python 3.3 on Windows
if (
    os.name == 'nt'
    and sys.version_info >= (3, 0) and sys.version_info < (3, 4)
):
    import shutil
    support.rmtree = shutil.rmtree

try:
    import grp
    import pwd
except ImportError:
    grp = pwd = None

# support.can_symlink is missing prior to Python 3
support_can_symlink = support.can_symlink
support_skip_unless_symlink = support.skip_unless_symlink

# Backported from 3.4


def fs_is_case_insensitive(directory):
    """Detects if the file system for the specified directory is
    case-insensitive.
    """
    base_fp, base_path = tempfile.mkstemp(dir=directory)
    case_path = base_path.upper()
    if case_path == base_path:
        case_path = base_path.lower()
    try:
        return os.path.samefile(base_path, case_path)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise
        return False
    finally:
        os.unlink(base_path)


support.fs_is_case_insensitive = fs_is_case_insensitive
