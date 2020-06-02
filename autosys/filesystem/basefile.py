#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" basefile.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal

from dataclasses import dataclass, field
from pathlib import Path
import os
import shutil


@dataclass
class BaseFile:
    file_name: str
    _path: Path = None

    def __post_init__(self):
        try:
            self._path = Path(self.file_name).resolve()
        except:
            raise BaseFileError(f"Unable to initialize file '{self.file_name}' ...")

    @property
    def basename(self) -> str:
        """ Return only the basename of the file. """
        try:
            return self.file_name.split(".")[0].split("/")[-1]
        except:
            raise BaseFileError(f"Unable to return basename of file.")

    @property
    def extension(self) -> str:
        """ Return only the extension of the file. """
        try:
            return self.file_name.split(".")[-1]
        except:
            raise BaseFileError(f"Unable to return extension of file.")

    @property
    def path(self) -> Path:
        if not self._path:
            self._path = Path(self.file_name).resolve()
        return self._path

    @property
    def as_posix(self):
        return self._path.as_posix()

    @property
    def stat(self):
        """ Return os.stat type information.

            e.g.
            os.stat_result(
                st_mode     =33188,
                st_ino      =60176618,
                st_dev      =16777224,
                st_nlink    =1,
                st_uid      =501,
                st_gid      =20,
                st_size     =71,
                st_atime    =1591045258,
                st_mtime    =1591044549,
                st_ctime    =1591044549
                )
            """
        return self.path.stat()


class TextFile(BaseFile):
    def get_line_count(filename) -> int:
        with open(filename) as f:
            return sum(True for line in f)


class BaseFileError(IOError):
    """ There was a problem initializing the file object. """

    pass


if False:
    _test_file = "/Users/skeptycal/Documents/coding/python/autosys/autosys/tests/test_basefile.txt"
    test_file = BaseFile(_test_file)
    print(test_file.stat)
    print(os.stat(test_file.path))
    print(test_file.stat == os.stat(test_file.path))
