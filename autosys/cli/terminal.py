from typing import NamedTuple, Sequence, Tuple
from sys import stdout
from os import linesep as NL, environ as ENV
from platform import platform
from io import TextIOWrapper
from dataclasses import dataclass

PLATFORM = platform()
DEFAULT_COLOR = "MAIN"


def replace_all(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> Sequence:
    """ return a sequence with all `needles` in `haystack` replaced with `volunteers` """
    return "".join(volunteer if c in needle else c for c in haystack)


def rep_whitelist(
    needle: Sequence, haystack: Sequence, volunteer: Sequence = ""
) -> Sequence:
    """ return a sequence with all `needles` in `haystack` saved and all other characters replaced with `volunteers` """
    return "".join(volunteer if c not in needle else c for c in haystack)


def make_safe_id(haystack: Sequence, volunteer: Sequence = "_") -> Sequence:
    """ return a string that has only alphanumeric and _ characters.

        others are replaced with `volunteer` (default `_`) """
    return "".join(volunteer if not c.isidentifier() else c for c in haystack)


if True:  # !------------------------ CLI display utilities

    def hr(s: str = "-", n: int = 50, print_it: bool = True):
        """ 'hard return' (yes, a dashed line) """
        if not print_it:
            return s * n
        else:
            print(s * n)

    def s80(s: str = "=", n: int = 79, print_it: bool = True):
        """ string80 - a 79 character repeating string """
        return hr(s=s, n=n, print_it=print_it)

    def br(n: int = 1, print_it: bool = True):
        """ yes, a newline inspired by <BR />

            n: int = number of blank lines

            set retval=True to return instead of print."""
        return hr(s=" ", n=n, print_it=print_it)

    def vprint(var_name: str, print_it: bool = True):
        fmt = f"{var_name}"
        if print_it:
            print(fmt)
        else:
            return fmt


@dataclass
class Terminal:  # !------------------------ Terminal Class
    _SUPPORTS_COLOR: bool = False
    _SIZE: Tuple[int, int] = None
    _stream: TextIOWrapper = stdout
    DEFAULT_TERMINAL_SIZE: NamedTuple = (80, 24)

    # !------------------------------ properties

    @property
    def SUPPORTS_COLOR(self) -> bool:
        if not self._SUPPORTS_COLOR:
            self._SUPPORTS_COLOR = self._get_supports_color()
        return self._SUPPORTS_COLOR

    @property
    def SIZE(self) -> Tuple[int, int]:
        if not self._SIZE:
            self._SIZE = self._get_terminal_size()
        return self._SIZE

    @property
    def cols(self) -> int:
        return self.SIZE[0]

    @property
    def rows(self) -> int:
        return self.SIZE[1]

    # !------------------------------ methods

    def __str__(self) -> str:
        return f"Terminal object (Supports color? {self.SUPPORTS_COLOR})"

    def __repr__(self):
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

    def _get_terminal_size(self) -> Tuple[int, int]:
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
            cr = (
                self._ioctl_get_win_size(0)
                or self._ioctl_get_win_size(1)
                or self._ioctl_get_win_size(2)
            )
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
                log.info(f"shutil.get_terminal_size returns ({cr.columns},{cr.lines})")
                return (cr.columns, cr.lines)
        except Exception as e:
            log.error(e)
        log.info("no return from shutil.get_terminal_size")
        log.info(f"using {Terminal.DEFAULT_TERMINAL_SIZE} for cr")

        return Terminal.DEFAULT_TERMINAL_SIZE[0], Terminal.DEFAULT_TERMINAL_SIZE[1]

    def _get_supports_color(self) -> bool:
        # generic script level stderr output characteristics
        self._STREAM_ISATTY = self._stream.isatty()
        self._HASATTR_ISATTY = hasattr(self._stream, "isatty")
        self._IS_A_TTY: bool = self._STREAM_ISATTY and self._HASATTR_ISATTY
        self._IS_PPC: bool = PLATFORM == "Pocket PC"
        self._IS_WIN32: bool = PLATFORM == "win32"
        self._IS_ANSICON: bool = "ANSICON" in ENV
        self._IS_WIN_COLOR: bool = self._IS_WIN32 and self._IS_ANSICON
        self._IS_EDGE_CASE: bool = self._IS_WIN_COLOR or self._IS_PPC
        self._IS_EDGE_TTY: bool = self._IS_EDGE_CASE and self._IS_A_TTY
        return self._IS_A_TTY or self._IS_EDGE_TTY

    def _show_debug_info(self):
        hr(s="=")
        print("Terminal Properties:")
        hr()
        constants = {k: eval(f"term.{k}") for k in dir(term) if k.isupper()}
        for k, v in constants.items():
            print(k, v)
        print("---------------------------------------")

    def out(self, *args, sep=" ", end=NL, flush=False):
        print(*args, sep=sep, end=end, flush=flush, file=self._stream)


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


color = BasicColors()


@dataclass
class LogColors:
    LC_50: str = color.WARN
    LC_40: str = color.ATTN
    LC_30: str = color.CANARY
    LC_20: str = color.BLUE
    LC_10: str = color.GO

    def str(self):
        print(self.LC_50, f"{self.LC_50}color")


lc = LogColors()

if __name__ == "__main__":
    from pprint import pprint

    def _test_terminal_():

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

        # term._show_debug_info()

    _test_terminal_()
