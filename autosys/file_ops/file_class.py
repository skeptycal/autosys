#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" file_class.py - A python representation of a file from the file system.

    Utilities for ease of use and clarity.
    # *-------------------------------------

    Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """


""" ---> from macOS <file> program:

    Usage: file [OPTION...] [FILE...]
    Determine type of FILEs.

        --help                 display this help and exit
    -v, --version              output version information and exit
    -m, --magic-file LIST      use LIST as a colon-separated list of magic
                                number files
    LIST                    use LIST as a colon-separated list of magic
                                number files in place of default
    -z, --uncompress           try to look inside compressed files
    -Z, --uncompress-noreport  only print the contents of compressed files
    -b, --brief                do not prepend filenames to output lines
    -c, --checking-printout    print the parsed form of the magic file, use in
                                conjunction with -m to debug a new magic file
                                before installing it
                            use default magic file
    -e, --exclude TEST         exclude TEST from the list of test to be
                                performed for file. Valid tests are:
                                apptype, ascii, cdf, compress, elf, encoding,
                                soft, tar, json, text, tokens
    -f, --files-from FILE      read the filenames to be examined from FILE
    -F, --separator STRING     use string as separator instead of `:'
                            do not further classify regular files
    -I, --mime                 output MIME type strings (--mime-type and
                                --mime-encoding)
        --apple                output the Apple CREATOR/TYPE
        --extension            output a slash-separated list of extensions
        --mime-type            output the MIME type
        --mime-encoding        output the MIME encoding
    -k, --keep-going           don't stop at the first match
    -l, --list                 list magic strength
    -L, --dereference          follow symlinks
    -h, --no-dereference       don't follow symlinks (default)
    -n, --no-buffer            do not buffer output
    -N, --no-pad               do not pad output
    -0, --print0               terminate filenames with ASCII NUL
    -p, --preserve-date        preserve access times on files
    -P, --parameter            set file engine parameter limits
                                indir        15 recursion limit for indirection
                                name         30 use limit for name/use magic
                                elf_notes   256 max ELF notes processed
                                elf_phnum   128 max ELF prog sections processed
                                elf_shnum 32768 max ELF sections processed
    -r, --raw                  don't translate unprintable chars to \ooo
    -s, --special-files        treat special (block/char devices) files as
                                ordinary ones
    -C, --compile              compile file specified by -m
    -D, --debug                print debugging messages

    Report bugs to https://bugs.astron.com/

    """

# !------------------------------------- Imports
if True:  # pathlib.py "basic imports"
    import datetime
    # import fnmatch
    # import functools
    # import io
    # import ntpath
    # import os
    # import posixpath
    # import re
    # import sys
    # from _collections_abc import Sequence
    # from errno import EINVAL, ENOENT, ENOTDIR, EBADF, ELOOP
    # from operator import attrgetter
    # from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO
    # from urllib.parse import quote_from_bytes as urlquote_from_bytes


if True:  # pathlib.py "Internals" - private api
    # it is NOT recommended that these be directly manipulated
    import file_ops.pathlib as pl
    Path = pl.Path
    IS_WIN = pl.IS_WIN
    # supports_symlinks = True
    # if os.name == 'nt':
    #     import nt
    #     if sys.getwindowsversion()[:2] >= (6, 0):
    #         from nt import _getfinalpathname
    #     else:
    #         supports_symlinks = False
    #         _getfinalpathname = None
    # else:
    #     nt = None

    # from pathlib import _IGNORED_ERROS, _IGNORED_WINERRORS
    # from pathlib import _ignore_error, _is_wildcard_pattern
    # from pathlib import _Flavour
    # from pathlib import _WindowsFlavour, _PosixFlavour
    # Reference for Windows paths can be found at
    # http://msdn.microsoft.com/en-us/library/aa365247%28v=vs.85%29.aspx
    # from pathlib import _windows_flavour, _posix_flavour, _normal_accessor

    # from file_ops.pathlib import _PathParents
    # from file_ops.pathlib import PurePath, Path
    # from file_ops.pathlib import *  # ! hmmm

if True:  # basic imports
    from datetime import date
    from functools import lru_cache
    from io import TextIOWrapper
    from sys import argv
    from typing import Any, Generator, List, Sequence
    # from typing import *

if True:  # other modules from autosys.py
    import cli
    import parsing
    import dev
    from cli.terminal import COLS, ROWS
    # from dev.debug import dbprint
    from parsing.string_utils import br

# TODO - time module: https://realpython.com/python-time-module/


__all__ = [
    "File",
]

# IS_WIN = os.name == 'nt'

# re.findall(r'[^A-Za-z0-9_\-\\]', userpath)


def get_file_contents(path, recursive=False, test=False):
    """ Return a List containing the contents of files listed in path. Wildcards are allowed.

    <recursive> chooses directory recursion (default = False)

    <test> triggers function tests. (default = False)
    """
    p = Path(path)

    def _test_():
        if _debug_:
            pass
        pass

    def _return_():
        if not p.exists():
            return None
        elif recursive:
            return [_.read_text() for _ in p.rglob(path) if Path(_).is_file()]
        else:
            return [_.read_text() for _ in p.glob(path) if Path(_).is_file()]

    return _return_


# !------------------------------------- class File


@lru_cache  # use cache as needed
class File(Path):
    """ A python representation of a file from the file system.

        Utilities for ease of use and clarity.
        """
# !----------------------------- class setup
    _flavour = _windows_flavour if IS_WIN else _posix_flavour
    _path: Path = None
    _folder: str = ''
    _filename: str = ''
    _basename: str = ''
    _parents: _PathParents = []
    _size: int = 0
    _atime: date = None

    _RE_PATTERN_PATH_VALID: str = r'[^A-Za-z0-9_\-\\]'
    _RE_PATH_VALID: re.Pattern = \
        re.compile(_RE_PATTERN_PATH_VALID)

    def __init__(self, filename):
        self._flavour = _windows_flavour if IS_WIN else _posix_flavour
        self._filename = filename
        self._path = self.resolve()

    def _file_validator(self, needle: str):
        needle = needle.strip().lower()
        return re.match(self._RE_PATH_VALID, needle)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def __str__(self):
        return self.basename

    def __gt__(self, other):
        return sort(set(self.name, other.name))[1] is self.name

    def __lt__(self, other):
        return sort(set(self.name, other.name))[0] is self.name

    def __eq__(self, other):
        return (self.size == other.size) and (self.stat())
        # return super().__eq__(other)

    def get_file_contents(self, path: str = '*', recursive=False, test=False):
        """ Return a List containing the contents of files listed in
            path. Wildcards are allowed.

            <recursive> chooses directory recursion (default = False)

            <test> triggers function tests. (default = False)
            """
        try:
            p = Path(path)
        except:
            p = self

        def _test_():
            if _debug_:
                pass
            pass

        def _return_():
            if not p.exists():
                return None
            elif recursive:
                return [_.read_text() for _ in p.rglob(path) if Path(_).is_file()]
            else:
                return [_.read_text() for _ in p.glob(path) if Path(_).is_file()]

        if test and _debug_:
            _test_()
        return _return_

# !----------------------------- properties
    # properties are generated on demand in these methods instead of
    # in <self.__init__>. This reduces cumbersome processing and
    # memory usage for items that are rarely used.

    # In addition, it greatly speeds up the generation of lists and
    # trees since only the names and links are stored.

    @property
    def filename(self) -> str:
        if not self._filename:
            self._filename = self.as_posix()
        return self._filename

    @filename.setter
    def filename(self, name: str):
        if not self._filename:
            self._filename = self.as_posix()
        try:
            self = self.rename(name)
            self._filename = str(name)
        except IOError as e:
            raise IOError(f"Cannot rename {self.name} to {name}.")

    @property
    def basename(self) -> str:
        if not self._basename:
            self._basename = self.name
        return self._basename

    @basename.setter
    def basename(self, name: str):
        self._basename = str(name)

    @property
    def folder(self) -> str:
        if not self._folder:
            self._folder = self.parents[0].as_posix()
        return self._folder

    @property
    def drive(self):
        return self.drive

    @property
    def is_file(self):
        return self.is_file()

    @property
    def size(self) -> int:
        if not self._size:
            try:
                self._size = self.stat().st_size
                return self._size
            except:
                return 0

    @property
    def atime(self) -> float:
        if not self._atime:
            try:
                self._atime = self.stat().st_atime
                return self._atime
            except:
                return None

    @property
    def methods(self):
        """ List methods of the <file> class. """
        for prop in self.__dir__():
            if prop[0] != '_':
                yield prop


class DirTree():

    def __init__(self):
        first = File(Path.cwd)
        super().__init__()


class DisplayablePath(object):
    DISPLAY_FILENAME_PREFIX_MIDDLE = '├──'
    DISPLAY_FILENAME_PREFIX_LAST = '└──'
    DISPLAY_PARENT_PREFIX_MIDDLE = '    '
    DISPLAY_PARENT_PREFIX_LAST = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        children = sorted(list(path
                               for path in root.iterdir()
                               if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.DISPLAY_FILENAME_PREFIX_LAST
                            if self.is_last
                            else self.DISPLAY_FILENAME_PREFIX_MIDDLE)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.DISPLAY_PARENT_PREFIX_MIDDLE
                         if parent.is_last
                         else self.DISPLAY_PARENT_PREFIX_LAST)
            parent = parent.parent

        return ''.join(reversed(parts))


def _test_():
    f = File('test')
    print(f"{f=}")
    print(f"{f.__class__=}")
    br()
    print(f"{f.__annotations__=}")
    br()
    # print(f.as_posix())
    br()

    print(f"{f.filename=}")

    print(f"{f.__str__()=}")
    print(f"{f.basename=}")
    print(f"{f.folder=}")
    print(f"{f.size=}")
    print(f"{f.atime=}")

    print(f"{f.parent=}")
    print(f"{f.parents=}")
    # print(f"{f.drive=}")
    print(str(f.atime))
    print(f"{f._file_validator('')=}")
    br()
    print("methods in <File>")
    for s in f.__dir__():
        print('  ', s)
    br()
    # for s in f.get_lines():
    #     print(s, end="")


def _main_():
    '''
    CLI script main entry point.
    '''
    _debug_ = True
    if len(argv) > 1:
        filenames = argv[1:]
    else:
        filenames = ['testfile.txt']

    for filename in filenames:
        f = File(filename)
        if _debug_:
            _test_()


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()


# # !----------------------------- file info

#     def get_size(self):
#         return f"{self._path.stat().st_size} bytes"

#     def get_atime(self):
#         return date.fromtimestamp(self._path.stat().st_atime)

#     # @logit
#     def set_in_sys_path(self):
#         """ Insert parent folder of <File> in the system python path if it is not.
#         """
#         if self._file not in path:
#             path.insert(0, self._file)

#     def print_file_info(self):
#         """ #### Print temp file debug information.

#             Return a File object from <f> or <Exception>.

#             (all display errors are ignored)
#             """
#         try:
#             if f:
#                 f = File().file(f)
#             else:
#                 f = self.file(f)
#             _desc = self.basename(f)
#         except IOError as e:
#             return e
#         print(f"\n --------------- with {_desc} ...")
#         with open(file=f, mode='r') as fd:
#             try:
#                 print(f)
#             except:
#                 pass
#             try:
#                 print(f'object:        {str(fd):<50.50}')
#             except:
#                 pass
#             try:
#                 print(f'file handle:   {str(fd.file):<50.50}')
#             except:
#                 pass
#             try:
#                 print(f'file name:     {str(fd.name):<50.50}')
#             except:
#                 pass
#             try:
#                 print(f'exists:        {str(os.path.exists(fd.name)):<50.50}')
#             except:
#                 pass
#             try:
#                 print(f'type:          {str(type(fd))}')
#             except:
#                 pass
#             try:
#                 print(f'file mode:     {str(fd.mode):<50.50}')
#             except:
#                 pass
#             try:
#                 print(f'file size:     {str(fd.__sizeof__()):<50.50}')
#             except:
#                 pass

#     # @logit
#     def print_file_lines(self, n: int = 0,
#                          tail: bool = False,
#                          linenumbers=False,
#                          header=True,
#                          stat=True):
#         """ #### Print the lines in a text file.

#             - n           -- number of lines (default 0 = all)
#             - tail        -- print the lines backwards (default = False)
#             - linenumbers -- include line numbers (default = False)
#             - header      -- print a file header (default = True)
#             - stat        -- print file info (default = True)
#             """
#         if stat:
#             print(f"{self.basename}  {self.size:>14.14}  {self.atime} ")
#         if header:
#             print(f"{self._path.stat()}")
#             print('-'*COLS)
#             print(f"\n Contents of {basename(_path)}...")
#         lines = self.get_lines(n=n, tail=tail)
#         i: int = 0
#         for line in lines:
#             i += 1
#             print(linenumbers * f"{str(i):>4.4} " + line)
#             if i == n:
#                 break
# !----------------------------- file activity

    # @logit
    # def get_lines(self, n: int = 0,
    #               tail: bool = False) -> Generator[str, None, None]:
    #     """ Yield the lines in a text file.

    #         n           -- number of lines (default 0 = all)
    #         tail        -- return the lines backwards (default = False)
    #         """
    #     if self.isfile:
    #         with open(self._file) as f:
    #             lines = reversed(f.readlines()) if tail else f.readlines()
    #             for line in lines:
    #                 yield line

    # def as_text(self) -> str:
    #     with open(self._file, mode='r') as f:
    #         return f.read()

    # def as_bytes(self) -> bytes:
    #     with open(self._file, mode='rb') as f:
    #         return f.read()


###########################################################

    # @classmethod
    # def __new__(cls, *args):
    #     """Construct a PurePath from one or several strings and or existing
    #     PurePath objects.  The strings and path objects are combined so as
    #     to yield a canonicalized path, which is incorporated into the
    #     new PurePath object.
    #     """
    #     if cls is Path:
    #         if IS_WIN:
    #             cls = WindowsPath
    #             cls._flavour = _WindowsFlavour
    #         else:
    #             cls = PosixPath
    #             cls._flavour = _PosixFlavour
    #     return cls.__class__
