from typing import NamedTuple, Tuple
from sys import stdout
from os import linesep as NL, environ as ENV
from platform import platform as PLATFORM
from io import TextIOWrapper


def info(*args):
    ''' placeholder for logging function... '''
    print(args)


class Terminal:  # !------------------------ Terminal Class
    DEFAULT_TERMINAL_SIZE: NamedTuple = (80, 24)

    # !------------------------------ initialize

    def __init__(self, stream: TextIOWrapper = stdout):
        super().__init__()
        self._stream: TextIOWrapper = stream
        self._SUPPORTS_COLOR = self._get_supports_color()
        self._size: Tuple[int, int] = self._get_terminal_size()

    # !------------------------------ properties
    @property
    def cols(self):
        return self._size[0]  # if self._IS_A_TTY else 0

    @property
    def rows(self):
        return self._size[1]  # if self._IS_A_TTY else 0

    @property
    def size(self):
        return self._size

    @property
    def SUPPORTS_COLOR(self):
        if not self._SUPPORTS_COLOR:
            self._SUPPORTS_COLOR = self._get_supports_color()
        return self._SUPPORTS_COLOR

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

    def _ioctl_get_win_size(self, fd: int) -> (Tuple[int, int]):
        """ Return Tuple 'cr' - columns, rows of tty """
        try:
            from fcntl import ioctl
            from struct import unpack
            from termios import TIOCGWINSZ

            retval = unpack("hh", ioctl(fd, TIOCGWINSZ, "1234"))
            info(f"_ioctl_get_win_size returns: {retval=}")
            return int(retval[1]), int(retval[0])
        except Exception as e:
            return e

    def _get_terminal_size(self) -> Tuple[int, int]:
        """ Return terminal size as a tuple(COLS, ROWS).

                Attempts to locate a valid terminal size using various fallback methods.

                Default is 80 columns x 24 lines (rows).

                (uses `dbprint()` for debug output)

                Reference: https://stackoverflow.com/questions/566746/how-to-get-linux-console-window-width-in-python
                """
        import os
        import sys
        from shutil import get_terminal_size as SH_SIZE

        cr: Tuple[int, int] = None

        try:
            cr = (self._ioctl_get_win_size(0) or self._ioctl_get_win_size(1)
                  or self._ioctl_get_win_size(2))
            if cr:
                info(f"cr from 'or' ioctl's: {cr}")
                return cr
        except:
            pass
        info(f"no cr from 'or' ioctl's")

        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = self._ioctl_get_win_size(fd)
            os.close(fd)
            if cr:
                info(f"cr from cterm(): {cr}")
                return cr
        except:
            pass
        info(f"no cr from cterm()")

        try:
            if ENV.get("LINES") and ENV.get("COLUMNS"):
                cr = (ENV.get("LINES"), ENV.get("COLUMNS"))
            if cr:
                info(f"env.get returns {cr}")
                return cr
        except:
            pass
        info(f"no return from env.get")

        try:
            # 'fallback' also sets default if nothing else has worked
            cr = SH_SIZE(fallback=Terminal.DEFAULT_TERMINAL_SIZE)
            if cr:
                info(
                    f"shutil.get_terminal_size returns ({cr.columns},{cr.lines})"
                )
                return cr.columns, cr.lines
        except:
            pass
        info("no return from shutil.get_terminal_size")
        info(f"using {Terminal.DEFAULT_TERMINAL_SIZE} for cr")

        return Terminal.DEFAULT_TERMINAL_SIZE[
            0], Terminal.DEFAULT_TERMINAL_SIZE[1]

    def _get_supports_color(self) -> bool:
        # generic script level stderr output characteristics
        self._IS_A_TTY: bool = self._stream.isatty() and hasattr(
            self._stream, "isatty")
        self._IS_PPC: bool = PLATFORM == "Pocket PC"
        self._IS_WIN32: bool = PLATFORM == "win32"
        self._IS_ANSICON: bool = "ANSICON" in ENV
        self._IS_WIN_COLOR: bool = self._IS_WIN32 and self._IS_ANSICON
        self._IS_EDGE_CASE: bool = self._IS_WIN_COLOR or self._IS_PPC
        self._IS_EDGE_TTY: bool = self._IS_EDGE_CASE and self._IS_A_TTY
        return self._IS_A_TTY or self._IS_EDGE_TTY

    def _show_debug_info(self):
        print("---------------------------------------")
        print("Terminal Properties:")
        print("---------------------------------------")
        print(f"  {self._IS_A_TTY=}")
        print(f"  {self._IS_PPC=}")
        print(f"  {self._IS_WIN32=}")
        print(f"  {self._IS_ANSICON=}")
        print(f"  {self._IS_WIN_COLOR=}")
        print(f"  {self._IS_EDGE_CASE=}")
        print(f"  {self._IS_EDGE_TTY=}")
        print(f"  {self._stream.isatty()=}")
        print(f"  {hasattr(self._stream, 'isatty')=}")
        print(f"  {self._stream.isatty()=}")
        print("---------------------------------------")

    def out(self, *args, sep=" ", end=NL, flush=False):
        print(*args, sep=sep, end=end, flush=False, file=self.stream)


if __name__ == "__main__":

    def _test_terminal_():
        term = Terminal()

        print(term._stream)
        print(term._size)
        print(term.size)
        # COLS, ROWS = term.size
        print(f"{PLATFORM=}")
        # print(f"Terminal size is set to ({term.cols}, {term.rows})")
        term._show_debug_info()

        print(term.SUPPORTS_COLOR)

        # print(f"{SUPPORTS_COLOR=}")

    _test_terminal_()
