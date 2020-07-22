#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" link manager - maintain symlinks between home and backup (~/.dotfiles)

    ---
    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """


import re
import os
import sys

from dataclasses import Field, dataclass, field
from enum import Enum, IntEnum
from functools import lru_cache
from locale import getpreferredencoding
from pathlib import Path
import platform
from io import TextIOWrapper

from autosys.text_utils.datetime import datetime as dt

from typing import Dict, List, Tuple

try:
    import ujson as to_json
except ImportError:
    import json

try:
    import lxml
    DEFAULT_PARSER = lxml
    XML_PARSER = lxml
except ImportError:
    XML_PARSER = False
    try:
        import html5lib
        DEFAULT_PARSER = html5lib
    except ImportError:
        import html
        DEFAULT_PARSER = html

try:
    import numpy as np
except ImportError:
    np = False


try:
    from autosys import logging
    log = logging.getLogger(__file__)
    USE_DEFAULT_LOGGER: bool = False  # if logging is not available
except:
    USE_DEFAULT_LOGGER: bool = True  # if logging is not available

obj = object()
Nul: str = chr(0)


# ? ========================= Base Class


@dataclass
class _GenericDataClass:

    ''' Base Class for most of *my* dataclass objects. Allows custom
        reporting, logging, etc to be designed once and to therefore offer
        consistent methods and interfaces.
        '''

    def default_logger(self, msg):
        ''' A generic stderr logger for use when logging fails. '''
        print(f" <default_logger> {msg}", file=sys.stderr)

    def info(self, msg):
        try:
            logging.info(msg=msg)
        except:
            if USE_DEFAULT_LOGGER:
                self.default_logger(msg=msg)

    def breakpointhook(self):
        sys.breakpointhook()

    def refcount(self, obj):
        return sys.getrefcount(obj)

    @property
    def myclass(self):
        return str(self.__class__).split('.')[1][:-2]

    def pulse(self, obj):
        ''' log a snapshot of the object's state. '''
        return f"class: {obj.myclass} - mem: {obj.__sizeof__()}"

    def size(self, obj):
        sys.getsizeof(obj)

    def log_pulse(self, obj):
        info(pulse(obj=obj))

    def pprint(self):
        self.pulse(self)
        print('='*50)
        print(f"{self.pulse(self)}")
        for k, v in self.__dict__.items():
            print(f"  {k:<20.20} : {repr(v):<50.30}")
        print('-'*50)

# ? ========================= Defaults


@dataclass
class _FileSystemDefaults(_GenericDataClass):
    ''' Generic Defaults for any system. Not intended to be used directly, but
    rather to create a specific defaults sub-class, like 'macOS' or 'Win32'
    '''
    BYTEORDER: str = sys.byteorder
    CPU_COUNT: int = os.cpu_count()
    NL: str = os.linesep
    PLAT: str = platform.platform()
    STDERR: TextIOWrapper = sys.stderr
    STDIN: TextIOWrapper = sys.stdin
    STDOUT: TextIOWrapper = sys.stdout

    ARGV: List = field(init=False)
    PY3: bool = field(init=False)
    PYTHONPATH: List = field(init=False)
    PYVER: Tuple = field(init=False)

    try:
        DEFAULT_ENCODING: str = getpreferredencoding(
            do_setlocale=True)
    except:
        DEFAULT_ENCODING: str = "utf-8"

    def __post_init__(self):
        self.ARGV = sys.argv
        self.PYTHONPATH = sys.path
        self.PYVER: Tuple = sys.version_info
        self.PY3: bool = self.PYVER[0] > 2


@dataclass
class PosixDefaults(_FileSystemDefaults):
    DEFAULT_FILE_PERMISSIONS: int = 664
    DEFAULT_DIRECTORY_PERMISSIONS: int = 775


@dataclass
class LinuxDefaults(PosixDefaults):
    ADD_ON_INSTALLER: str = 'apt-get'


@dataclass
class macOSDefaults(PosixDefaults):
    ADD_ON_INSTALLER: str = 'brew'


@dataclass
class WinDefaults(_FileSystemDefaults):
    ''' Includes windows specific defaults.

        Examples:
        - file separator character
        - newline character
        '''


MACHINE: str = platform.platform().lower()

try:
    assert (WIN32 := 'win' in MACHINE)
    import ntsecuritycon
    import win32security
    defaults = WinDefaults()
except AssertionError:
    try:
        assert (MACOS := 'macos' in MACHINE)
        defaults = macOSDefaults()
    except AssertionError:
        defaults = LinuxDefaults()


# ? ========================= Types and Tags


class WordLink:
    ''' a connection in a graph '''
    linkid: int
    date_added: dt
    date_updated: dt
    file_set: str  # a set of connected words


class Graph:
    graphid: int


class Word:
    word_id: int
    date_added: dt
    date_updated: dt
    name: str
    linkset: Graph  # a set of connections to other words


class FileTag:
    ''' a topic tag that is attached to items where it is related.

        a 'weighting' or 'percentage' of 'something(??)' should be included
        with the link to document the actual connection and keep the two
        items' properties separate
        '''
    name: str
    description: str
    link: str  # Wikipedia, etc.
    graphnodes: Graph  # a set of connections to other FileTags
    keywords: WordLink  # a set of relationships to words


class ItemTypes(IntEnum):
    file: int = 1
    link: int = 2
    directory: int = 3
    volume: int = 4
    url: int = 5
    stream: int = 6

# ? ========================= Containers


@dataclass
class _GenericContainerItem(_GenericDataClass):
    ''' A basic "file system object" that includes anything that can be
        accessed from a file system request, stream, socket, etc.
        '''
    file_name: str      # name of resource
    url: str = ''       # location of resource
    kind: ItemTypes = ItemTypes.file  # type of resource
    protected: bool = True
    encrypted: bool = False
    encryption_algoritm: Field = field(init=False)


@dataclass
class _StorageItem(_GenericContainerItem):
    ''' A generic storage item ... meaning an item that is stored on a disk
        and can be accessed with the pathlib library. Most 'file' commands
        work on these items. e.g. stat, open, ls

        It could be a 'model' of a container that is used as an interface to
        another device. e.g. an adapter to access a database with file
        commands ...
        '''
    _stat: Field = field(init=False)  # file system stats (on demand)

    def __post_init__(self):
        self.file_name = self.me.resolve()

    @ property
    def me(self):
        return Path(self.file_name)

    def chmod(self, mode: int = 664):
        self.me.chmod(mode=mode)

    def stat(self):
        self._stat = self.me.stat()
        return self._stat

    def isfile(self) -> (bool):
        return self.me.is_file()

    def isdir(self) -> (bool):
        return self.me.is_dir()

    def islink(self) -> (bool):
        return self.me.is_symlink()

    @ property
    def realpath(self):
        return self.me.resolve()

    @ property
    def parent(self):
        return self.me.parent()

    @ property
    def parents(self):
        return self.me.parents()


class Directory(_GenericContainerItem):
    ''' A directory on a file system ... or equivalent.

        Mainly used as a container for files and links ... '''
    kind: ItemTypes = ItemTypes.file  # type of resource

    def chmod(self, mode: int = 775):
        self.me.chmod(mode=mode)


class SymLink(_StorageItem):
    ''' A symlink to a file on the file system. '''

    def stat(self):
        self._stat = self.me.stat()
        return self._stat

    def chmod(self, mode: int = 664):
        self.me.lchmod(mode=mode)


@dataclass
class DataFile(_StorageItem):
    ''' A generic data file. This can be any file that is 'readable' in some
        standard way. This is a file that can be access with the os.stat or
        equivalent command.

        Could be text or bytes ... basically, not a compiled executable.

        The stat and tags are generated on demand or when triggered.
        '''
    _tags: Field = field(init=False)  # a list of related keywords


@dataclass
class TextFile(DataFile):
    data: str = field(init=False)  # loaded as needed
    # a record of the main source
    main_source: str = field(init=False)
    # derived from the text or topic/type
    main_topic: str = field(init=False)
    # a measure of social media pressense ???
    presence: int = field(init=False)
    # a list of related sources
    sources: Field = field(init=False)

    def to_json(self):
        pass

    def to_markdown(self):
        pass

    def to_csv(self):
        pass

    def to_html(self):
        pass

    def to_man(self):
        pass

    def to_doc(self):
        pass


@dataclass
class Folder(_StorageItem):
    _storage: Field = field(init=False)
    _index: Field = field(init=False)

    def __post_init(self):
        self.parse()

    def parse(self):
        ''' Parse the directory tree and collect data.

            This MUST be done when a new directory is indexed.

            After that, individual files requested can be read as needed.

            This may also be done periodically to keep information fresh. The
            frequency depends on whether other programs access the directory
            and how often changes are made.
            '''
        pass

    def _add(self, file_name):
        ''' Add a file to this folder. '''
        pass

    def _del(self, file_name):
        ''' Delete a file from this Folder. '''
        pass

    def _stat(self, file_name):
        ''' Get file information. '''
        pass

    def _copy(self, from_file, to_file):
        ''' Copy a file to another Folder. '''
        pass

    def _move(self, from_spot, to_spot):
        ''' Move a file to another Folder. '''
        pass


home_list: List = []
dotfiles_list: List = []

defaults.pprint()

tmp = _GenericContainerItem('testfile')

tmp.pprint()
