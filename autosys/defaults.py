#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Defaults (defaults.py) - common resources for all `autosys` modules

    Common imports, CONSTANTS, and utilities for the `AutoSys` package. These are resources that are used by many modules, classes, and functions. They are available in all `AutoSys` modules.

    ---------------------------------------------------------------------------
    *Goals for dependency imports:

        1. Only import what is needed
            - avoid importing everything all the time
            - use what is needed for the code
            
        2. Clearly show dependencies at the top of the module
            - standard library imports can be centralized in __init__.py
            
        3. Defer import until later (specific cases)
            - this should be avoided since it hides `import` statements all
                over the code base
            - make a comment in the `imports` section to clarify 
            
        4. Use absolute imports 
            - they can become very long 
            - code folding in VSCode with 'if True:' blocks is my hacky fix

    *Reference: imports - best practices    
        - https://stackoverflow.com/a/37126790
        "1. Errors importing modules with circular imports"

        ```
        import package.a           # (1) Absolute import
        import package.a as a_mod  # (2) Absolute import bound to different name
        from package import a      # (3) Alternate absolute import
        import a                   # (4) Implicit relative import (deprecated, python 2 only)
        from . import a            # (5) Explicit relative import
        ```
        
        Unfortunately, only the 1st and 4th options actually work when you have circular dependencies (the rest all raise ImportError or AttributeError). In general, you shouldn't be using the 4th syntax, since it only works in python2 and runs the risk of clashing with other 3rd party modules. 
        
        *So really, only the first syntax is guaranteed to work.*
        
        The ImportError and AttributeError issues only occur in python 2. In python 3 the import machinery has been rewritten and all of these import statements (with the exception of 4) will work, even with circular dependencies. While the solutions in this section may help refactoring python 3 code, they are mainly intended for people using python 2.

    ---------------------------------------------------------------------------
    Part of the `AutoSys` package - utilities for macOS apps
    copyright (c) 2019 Michael Treanor
    https://www.github.com/skeptycal/autosys
    https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

if True:  # !------------------------ Package Imports
    if True:  # !------------------------ System Imports
        import asyncio
        import contextvars
        import importlib
        import inspect
        import platform
        import sys
        import logging

        try:
            import ujson as json  # use faster version if available
        except ImportError:
            import json  # type: ignore

    if True:  # !------------------------ Specific Imports
        from dataclasses import dataclass, field, is_dataclass, asdict, make_dataclass
        from os import environ as ENV, linesep as NL
        from pathlib import Path
        from pprint import pprint, pformat
        from sys import stdout, stderr, argv, path as PYTHON_PATH
        from functools import wraps  # This convenience func preserves name and docstring
        from locale import getpreferredencoding
        from sys import stdout, stderr, argv

        # from time import sleep
        from enum import unique, IntEnum, Enum
        from typing import Any, Dict, Iterable, List, NamedTuple, Sequence, Tuple

        # package and version data
        from autosys._version import *

        # basic cli colors
        from autosys.data.colors import BASE_COLORS

if True:  # !------------------------ Module CONSTANTS
    _debug_: bool = True  # True => use Debug features
    _verbose_: int = 0  # Verbosity level => 0 - 4
    _log_flag_: bool = _debug_ and True  # True => log to file if _debug_

if True:  # !------------------------ Common CONSTANTSs
    try:
        DEFAULT_ENCODING = getpreferredencoding(do_setlocale=True) or "utf-8"
    except:
        DEFAULT_ENCODING: str = "utf-8"
    DEFAULT_LOG_FILE_NAME: str = "log_autosys_private.log"

    # sys.maxsize is more reliable than platform
    # Ref: https://docs.python.org/3.9/library/platform.html
    IS_64BITS: bool = sys.maxsize > 2 ** 32

    # is python 3 or above
    PY3 = sys.version_info.major >= 3
    PLATFORM: str = platform.platform()
    WHICH_PY: str = platform.python_implementation()
    WHICH_OS: str = platform.system()

if True:  # !------------------------ General Utilities
    _EXPORT_BLACKLIST: str = ["arepl_store", "howdoi", "help"]
    _EXPORT_WHITELIST: str = ["_debug_", "_log_flag_", "_verbose_"]

    def LOG_PATH(f=DEFAULT_LOG_FILE_NAME) -> Path:
        return Path().cwd().resolve() / f

    SCRIPT_PATH: str = argv[0]  # path to this script
    ARGS: List[str] = argv[1:]  # CLI arguments

    def export(fn):
        """ Decorator to export functions and classes. """
        mod = sys.modules[fn.__module__]
        if hasattr(mod, "__all__"):
            mod.__all__.append(fn.__name__)
        else:
            mod.__all__ = [fn.__name__]
        return fn

    def filter_list(d=dir(), prefix="_", whitelist=[], blacklist=[]) -> List:
        """ Filter a list with prefix to exclude, whitelist, and blacklist. """
        return [
            x
            for x in sorted(d)
            if x in whitelist or (not x.startswith(prefix) and x not in blacklist)
        ]

    def all_export(
        d=dir(), prefix="_", whitelist=_EXPORT_WHITELIST, blacklist=_EXPORT_BLACKLIST
    ) -> List:
        """ Return a list of all exports not starting with `_` """
        return filter_list(d=d, prefix=prefix, whitelist=whitelist, blacklist=blacklist)


if True:  # !------------------------ Class and Method Utilities

    def __getattr__(name):
        if name in __all__:
            return importlib.import_module("." + name, __name__)
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    # generic test class for `add_method`
    A = type("A", (object,), dict(a=1))

    def add_method(cls):
        """ Decorator to add method to class 'cls' """

        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                return func(*args, **kwargs)

            setattr(cls, func.__name__, wrapper)
            # Note we are not binding func, but wrapper which accepts self but does exactly the same as func
            return func  # returning func means func can still be used normally

        return decorator

    # Samples

    # Decorator can be written to take normal functions and make them methods. These functions still act as normal if passed a standard variable. If they are passed a method parameter, they are run as class methods with 'self' injected in as needed
    @add_method(A)
    def foo():
        print("hello world!")

    @add_method(A)
    def bar(s):
        print(f"Message: {s}")

    def get_class_name(_name, verbose=True):
        """ Alternate class name function with optional formatting """
        _cls_name = eval(f"{_name}.__class__.__name__")
        if not verbose:
            return _cls_name
        return f"{_name} - <class '{_cls_name}'>"

    def get_methods(mod_list):
        """ return filter methods list - `filter_list` works better. """
        a = []
        for arg in mod_list:
            if arg.startswith("__"):
                continue
            if arg.startswith("arepl"):
                continue
            a.append(f"{arg}")
        return a


if True:  # !------------------------ Dataclass Utilities

    def get_argv():
        try:
            return sys.argv[1] or ""
        except:
            return "Nan"

    # _plat_dict = {
    #     k: v
    #     for k, v in platform.__dict__.items()
    #     if not k.startswith("_") and not str(type(v)).startswith("<class 'mod")
    # }

    # Plat = make_dataclass('Plat', _plat_dict)
    # plat = Plat()

    # @dataclass(init=True, order=True, unsafe_hash=True)
    # class PLAT:
    #     """ Dynamically add methods to dataclasses.

    #         Honestly, this was just a chance to work through all
    #         of the features of dataclases after 3.7 went live.

    #         I'm not sure how useful this would be as a replacement
    #         for a basic module import:

    #         ```
    #         import platform as PLAT

    #         print(PLAT.python_implementation())
    #         ```
    #         """

    #     field_a: str = field(default="field `a`")
    #     field_b: str = field(default_factory=platform.machine)
    #     field_c: str = field(default_factory=get_argv)
    #     libc_ver: Any = field(default_factory=platform.libc_ver)

    #     _plat_dict = {
    #         k: v
    #         for k, v in platform.__dict__.items()
    #         if not k.startswith("_") and not str(type(v)).startswith("<class 'mod")
    #     }

    #     print(_plat_dict)
    #     for _k, _v in _plat_dict.items():
    #         eval_string = f"{_k}: Any = field(default_factory=platform.{_k})"
    #         eval(eval_string)

    #     # https://medium.com/@mgarod/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6

    #     def __post_init__(self):
    #         self.field_b = self.field_b.upper()
    #         self._width: int = 20
    #         self._space: int = 20
    #         self._alt: bool = True
    #         self._supports_color: bool = False
    #         self._default_color: str = "\x1B[38;5;124m\x1B[48;5;215m\x1B[1m" * \
    #             self._supports_color
    #         self._alt_color: str = "\x1B[38;5;174m\x1B[48;5;231m" * \
    #             self._supports_color
    #         self._reg_color: str = "\x1B[38;5;11m\x1B[48;5;246m" * \
    #             self._supports_color
    #         self._reset: str = "\x1B[0m" * self._supports_color
    #         self._default_divider: str = "="
    #         self._alt_divider: str = " "

    #     def __str__(self) -> str:
    #         return pformat(self.__dict__, indent=4)

    #     @property
    #     def toggle(self):
    #         self._alt = not self._alt

    #     @property
    #     def FMT_SIZE(self):
    #         return f"{self._width}.{self._space}"

    #     def v(self, v, justify="<", is_repr=False):
    #         if is_repr:
    #             return f"{v!r:{justify}{self.FMT_SIZE}}"
    #         return f"{v!s:{justify}{self.FMT_SIZE}}"

    #     @property
    #     def color(self) -> str:
    #         return f"{self._alt_color*self._alt}{self._reg_color*(not self._alt)}"

    #     @property
    #     def divider(self) -> str:
    #         return (
    #             f"{self._default_divider*self._alt}{self._alt_divider*(not self._alt)}"
    #         )

    #     @property
    #     def alt(self) -> str:
    #         return f" {self.divider}{self._default_divider}{self.divider} "

    #     def print_fields(self):
    #         for k, v in self.__dataclass_fields__.items():
    #             print(f"{self._default_color}{v.name}{self._reset}")
    #             for p in filter_list(dir(v)):
    #                 ep = eval(f"v.{p}")
    #                 print(
    #                     f"{self.color}{self.v(p,justify='>')}{self.alt}{self.v(ep)}{self._reset}"
    #                 )
    #                 self.toggle


if True:  # !------------------------ Script Tests
    def _tests_(args):
        """
        Run Debug Tests for script if _debug_ = True.
        """
        print("=================================================================")
        # plat2 = Plat()
        # print(plat2)

        # plat2.print_fields()
        return 0

    def _main_(args=ARGS):
        """ CLI script main entry point. """

        #! script testing
        if _debug_:
            # print('exports (__all__):')
            print(__all__)
            # inject `args` here ...
            # args.append('--version')
            # args.append('--verbose')
            return _tests_(args)
        return 0

    __all__ = all_export(whitelist=['_debug_', '_verbose_', '_log_flag_'])

if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()


# class PythonConfig:
#     """
#         debug: bool     - if True, output debug info to stream (default stderr)
#         verbosity: int  - output verbosity (0 - 5)
#         logging: bool   - if True, use file logging
#         tempfile: bool  - if True, use random temp file (default False*)

#         * if not using tempfile, default is current directory and append
#     """

#     def __init__(self, debug=_debug_, verbosity=_verbose_, logging=_log_flag_, use_tempfile=True):
#         self.debug = debug
#         self.verbosity = verbosity
#         self.logging = logging
#         self.use_tempfile = use_tempfile
#         if self.logging:
#             self._setup_log()

#     def _setup_log(self, append=True, delete_log=False):
#         if self.logging:
#             file_mode = 'a+b' if append else 'w+b'
#             if self.use_tempfile:
#                 self.log_path: TextIOWrapper = \
#                     tempfile.NamedTemporaryFile(
#                         # mode=f'{file_mode}+b',
#                         delete=delete_log,
#                         # dir=self._get_cwd(),
#                         suffix='log',
#                         prefix='autosys'
#                     )
#             else:
#                 self.log_path = self._get_cwd() / DEFAULT_LOG_FILE_NAME
#             logging.basicConfig(
#                 filename=_LOG_PATH.as_posix(),
#                 filemode=file_mode,
#                 level=logging.DEBUG)
#             logging.info(
#                 f'Logging is on for {__title__} version {__version__}')
#             logging.info(f'  {__copyright__}  -  License: {__license__}')

#     def _get_cwd(self) -> Path:
#         return Path(__title__).cwd().resolve()

#     @property
#     def log_path(self) -> Path:
#         return self.log_path

#     @property
#     def log_file(self) -> str:
#         return self.log_path.as_posix()

# config = PythonConfig(debug=True, verbosity=3, logging=True)

LORE_NEWLINE_ASIDE: str = """ <aside>            NewLine, A Bit of Lore

    Newline is a control character or sequence of control characters in a
    character encoding specification (e.g. ASCII or EBCDIC) that is used to
    signify the end of a line of text and the start of a new one.

    In the mid-1800s, long before the advent of teletype machines, Morse code
    operators invented and used Morse code prosigns to encode white space
    text formatting in formal written text messages. Two 'A' characters sent
    without the normal spacing is used to indicate a new line of text.

    --------------------------------------------------------------------------

    - In computing and telecommunication, a control character or non-printing
        character (NPC) is a code point (a number) in a character set, that
        does not represent a written symbol.

    - During the 1960s, ISO and ASA (who later became ANSI), simultaneously
        developed ASCII for modern teleprinters. The sequence they agreed on
        for newline was CR+LF. This sequence carried forward to the first
        computers that had to share printers with other older devices.

    - The separation of newline into two functions concealed the fact that the
        print head could not return from the far right to the beginning of the
        next line in time to print the next character. Any character printed
        after a CR would often print as a smudge in the middle of the page
        while the print head was still moving the carriage back to the first
        position.

    - Many early video displays also required multiple character times to scroll
        the display. MS-DOS adopted CP/M's CR+LF standard to be compatible. When
        the widespread adoption of the personal computer, the tradition became
        imprinted in newer versions of DOS and Windows.

    - During the same period, Multics (1964) used only the LF character because
        CR was useful for bold and strikethrough effects. This convention was
        adopted by ISO in 1967 and later by UNIX. All UNIX based operating
        systems carried the LF flag forward, with one exception being Apple.

    - The Apple II computer, as well as Commodore, TRS-80, classic Mac OS used CR
        alone. This led to even greater confusion as files encoded on Unix, Apple,
        and Dos based operating systems were all using ASCII encoding and yet were
        frustratingly mutually incompatible.

    - Apple has since joined the Multics crowd and ends lines with LF (0A) instead
        of the old CR (0D). Microsoft has continued to use the 2 character set for
        encoding line endings, but software drivers have eliminated most of the
        prior confusion.

    </aside>
    """
