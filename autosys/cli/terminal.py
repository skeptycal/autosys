#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Terminal
    ---
    terminal - Utilities for macOS terminal io.

    AutoSys
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# from dataclasses import Field, dataclass, field
# from io import TextIOWrapper
# 'package imports'
# from os import environ as ENV, linesep as NL
# from platform import platform
from autosys.cli import *
from platform import platform

__all__ = [
    "BasicColors",
    "br",
    "CR",
    "DEFAULT_COLOR",
    "hr",
    "NL",
    "PLATFORM",
    "rprint",
    "s80",
    "SUPPORTS_COLOR",
    "Terminal",
    "vprint",
]

PLATFORM = platform()
DEFAULT_COLOR = "MAIN"
CR: str = "\r"

if True:  # !------------------------ CLI display utilities

    def hr(s: str = "-", width: int = 50, print_it: bool = True):
        """ yes, a dashed line inspired by `<HR />`
            ---
            s - character to use for line

            width - duh ... the width
            """
        if not print_it:
            return s * width
        else:
            print(f"{s}" * width)

    def br(n: int = 1):
        """ yes, a newline inspired by `<BR />`
            ---
            n - number of line breaks
            """
        print(NL * n, end='')

    def s80(s: str = "=", n: int = 1):
        """ string80
            ---
            print a 79 character repeating string

            n - number of times to print it
            """
        for _ in range(n):
            print(s * 79)

    def vprint(var_name: str, print_it: bool = True):
        fmt = f"{var_name}"
        if print_it:
            print(fmt)
        else:
            return fmt

    def rprint(*args, **kwargs):
        """ Carriage return without a newline.
            ---
            Moves back to the start of the line.

            Cool for progress bars and counters ...
            """
        try:
            kwargs['end'] = ''
            kwargs['sep'] = ''
        except:
            pass
        print(CR, *args, **kwargs)


@dataclass
class Terminal:  # !------------------------ Terminal Class
    _SUPPORTS_COLOR: bool = False
    _SIZE: Tuple[int, int] = None
    _stream: TextIOWrapper = stdout
    DEFAULT_TERMINAL_SIZE: NamedTuple = (80, 24)

    # !------------------------------ properties

    @property
    def SUPPORTS_COLOR(self) -> (bool):
        if not self._SUPPORTS_COLOR:
            self._SUPPORTS_COLOR = self._get_supports_color()
        return self._SUPPORTS_COLOR

    @property
    def SIZE(self) -> (Tuple[int, int]):
        if not self._SIZE:
            self._SIZE = self._get_terminal_size()
        return self._SIZE

    @property
    def cols(self) -> (int):
        return self.SIZE[0]

    @property
    def rows(self) -> (int):
        return self.SIZE[1]

    # !------------------------------ methods

    def __str__(self) -> (str):
        return f"Terminal object (Supports color? {self.SUPPORTS_COLOR})"

    def __repr__(self) -> (str):
        _repr_list = [self.__str__()]
        # ? s += f'Terminal properties:{NL}'
        for p in sorted(dir()):
            if not p.startswith("_"):
                f = f"{p}"
                _repr_list.append(f"  {p}: {eval(f)}")
        return NL.join(_repr_list)

    def _ioctl_get_win_size(self, fd: int) -> (Tuple[int, int], Exception):
        """ Return Tuple 'cr' - columns, rows of tty """
        try:
            from fcntl import ioctl
            from struct import unpack
            from termios import TIOCGWINSZ

            retval = unpack("hh", ioctl(fd, TIOCGWINSZ, "1234"))
            log.info(f"_ioctl_get_win_size returns: {retval=}")
            return int(retval[1]), int(retval[0])
        except Exception as e:
            return e

    def _get_terminal_size(self) -> (Tuple[int, int]):
        """ Return terminal SIZE as a tuple(COLS, ROWS).

                Attempts to locate a valid terminal SIZE using various fallback methods.

                Default is 80 columns x 24 rows.

                Reference: https://stackoverflow.com/questions/566746/how-to-get-linux-console-window-width-in-python
                """
        # import os
        import sys

        cr: Tuple[int, int] = None

        try:
            print(1 / 0)
            cr = (self._ioctl_get_win_size(0) or self._ioctl_get_win_size(1)
                  or self._ioctl_get_win_size(2))
            if cr:
                log.info(f"cr from 'or' ioctl's: {cr}")
                return cr
        except Exception as e:
            log.error(e)
        log.info(f"no cr from 'or' ioctl's")

        try:
            from os import close as _close, open as _open, ctermid, O_RDONLY

            fd = _open(ctermid(), O_RDONLY)
            cr = self._ioctl_get_win_size(fd)
            _close(fd)
            with _open(ctermid(), O_RDONLY) as fd:
                cr = self._ioctl_get_win_size(fd)
                log.info(f"cr from cterm(): {cr}")
            if cr:
                log.info(f"cr from cterm(): {cr}")
                return cr
        except Exception as e:
            log.error(e)
        log.info(f"no cr from cterm()")

        try:
            if ENV.get("LINES") and ENV.get("COLUMNS"):
                cr = (ENV.get("LINES"), ENV.get("COLUMNS"))
            if cr:
                log.info(f"env.get returns {cr}")
                return cr
        except Exception as e:
            log.error(e)
        log.info(f"no return from env.get")

        try:
            # 'fallback' also sets default if nothing else has worked
            from shutil import get_terminal_size as _SH_SIZE

            cr = _SH_SIZE(fallback=Terminal.DEFAULT_TERMINAL_SIZE)
            if cr:
                log.info(
                    f"shutil.get_terminal_size returns ({cr.columns},{cr.lines})"
                )
                return (cr.columns, cr.lines)
        except Exception as e:
            log.error(e)
        log.info("no return from shutil.get_terminal_size")
        log.info(f"using {Terminal.DEFAULT_TERMINAL_SIZE} for cr")

        return (
            Terminal.DEFAULT_TERMINAL_SIZE[0],
            Terminal.DEFAULT_TERMINAL_SIZE[1],
        )

    def _get_supports_color(self) -> (bool):
        """ generic script level stderr output characteristics """
        self._IS_A_TTY: bool = self._stream.isatty() and hasattr(
            self._stream, "isatty")
        # if self._IS_A_TTY:
        #     return True
        self._IS_PPC: bool = PLATFORM == "Pocket PC"
        self._IS_WIN32: bool = PLATFORM == "win32"
        self._IS_ANSICON: bool = "ANSICON" in ENV
        self._IS_WIN_COLOR: bool = self._IS_WIN32 and self._IS_ANSICON
        self._IS_EDGE_CASE: bool = self._IS_WIN_COLOR or self._IS_PPC
        return self._IS_A_TTY or self._IS_EDGE_CASE

    def _show_debug_info(self) -> (None):
        hr(s="=")
        print("Terminal Properties:")
        hr()
        constants = {k: eval(f"term.{k}") for k in dir(term) if k.isupper()}
        for k, v in constants.items():
            print(k, v)
        print("---------------------------------------")

    def out(self, *args, sep=" ", end=NL, flush=False) -> (bool, Exception):
        """ send output to the stream. catch and return errors. """
        try:
            print(*args, sep=sep, end=end, flush=flush, file=self._stream)
            return False
        except Exception as e:
            return e


term = Terminal()

SUPPORTS_COLOR: bool = term.SUPPORTS_COLOR


# some basic colors ..
class BasicColors:
    MAIN: str = "\x1B[38;5;229m" * SUPPORTS_COLOR
    WARN: str = "\x1B[38;5;203m" * SUPPORTS_COLOR
    BLUE: str = "\x1B[38;5;38m" * SUPPORTS_COLOR
    GO: str = "\x1B[38;5;28m" * SUPPORTS_COLOR
    CHERRY: str = "\x1B[38;5;124m" * SUPPORTS_COLOR
    CANARY: str = "\x1B[38;5;226m" * SUPPORTS_COLOR
    ATTN: str = "\x1B[38;5;178m" * SUPPORTS_COLOR
    RAIN: str = "\x1B[38;5;93m" * SUPPORTS_COLOR
    WHITE: str = "\x1B[37m" * SUPPORTS_COLOR
    RESET: str = "\x1B[0m" * SUPPORTS_COLOR


if True:

    def _test_terminal_():
        from pprint import pprint
        hr()
        log.var("PLATFORM")
        log.var("term")
        log.var("term.SUPPORTS_COLOR")
        log.var("SUPPORTS_COLOR")
        log.var("term._stream")
        log.var("term._SIZE")
        log.var("term.SIZE")
        log.info(f"Terminal SIZE is set to ({term.cols}, {term.rows})")
        hr()
        print(str(lc))
        print(lc.str())
        print(dir(lc))

    # _test_terminal_()

    # term._show_debug_info()

    def _slow_progress_example():
        from time import sleep

        hr()
        br()
        hr()
        s80('*')
        hr()
        for i in range(50):
            rprint('=' * i, '>', ' ' * (80 - i))
            sleep(0.02)
        for i in range(50, 0, -1):
            rprint('=' * i, '>', ' ' * (80 - i))
            sleep(0.02)

    # _slow_progress_example()
