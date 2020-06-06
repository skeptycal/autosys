#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" basefile.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

import os
from os import stat, stat_result
from pathlib import Path as _Path
from sys import path as python_path
from tempfile import NamedTemporaryFile

import pytest
from autosys.filesystem.basefile import *


def add_one(x):
    return x + 1


def test_add_one_answer():
    assert add_one(3) == 4


class TestBaseFileAttributes:
    def __init__(self):
        with NamedTemporaryFile(mode="x+t", delete=False) as self.tmp:
            self._test_file_name = Path(self.tmp.name).name
            self._test_file_suffix = Path(self.tmp.name).suffix
            self.test_BaseFile = BaseFile(self.tmp.name)

    def __del__(self):
        del self.tmp

    def test_return_basefile_basename(self):
        assert test_BaseFile.basename == _test_file_name

    def test_return_basefile_extension(self):
        assert test_BaseFile.extension == "txt"


"""


    def test_return_basefile_path(self):
        assert test_BaseFile.path == _Path(_test_file).resolve()


    def test_return_basefile_path_as_posix(self):
        assert test_BaseFile.as_posix == _Path(_test_file).resolve().as_posix()


    def test_return_basefile_os_stat():
        assert test_file.stat == os.stat(_test_file)
    """
