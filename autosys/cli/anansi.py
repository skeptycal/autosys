#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" anansi.py - Tricky and fun ansi text utilities for python programs.
        import anansi or use with the following CLI syntax:

    Usage:
        - anansi TEXT [-z]
        - anansi FILE(s) [-Rz] [-q | -v ] [--pattern PATTERN]
        - anansi TEMPLATE [-Rz] [-q | -v] [--pattern PATTERN]
        - anansi [--help | --version]

    Options:
        FILE(s)                 Search pattern to match
        -q, --quiet             Suppress most error messages  [default: True]
        -r, --recursive         Perform search recursively    [default: False]
        -v, --verbose           Display detailed progress     [default: False]
        -z, --zero              End each output line with NUL [default: False]

        -P PATTERN --pattern PATTERN    Pattern to highlight  [default: None]

        --version               Show version.
        --debug                 Show debug info and test results.
        -h, --help              Show this screen.

    Exit status:

        0 if all file names were printed without issue.
        1 otherwise.

    Based on ANSI standard ECMA-48:
    http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf
    """
"""               Anansi, A Bit of Lore

    # - named after Anansi, the trickster, of West African and Caribbean
    #   folklore. Before Anansi, there were no stories in the world. What
    #   a terrible and ignorant place that must have been!

    # It was Anansi who convinced Nyame, The Sky-God, to share his stories
    #   with the world, but only after capturing the Python, the Hornets,
    #   the Leopard, and the Fairy.
    """

if True:  # !------------------------ imports
    import re
    import sys
    from sys import argv
    from platform import platform
    from time import sleep
    from autosys import _version as VERSION
    from autosys.debug import dbprint, db_column_ruler
    from autosys.cli.terminal import *

    class Ansi(str):

        # !------------------------ ANSI formatting constants
        # - ANSI ECMA-48 Control Sequence Introducer
        CSI: str = f"{ESC}["
        ANSI_SEP: str = ";"  # - ANSI ECMA-48 default separator

        # - {n} - format string for basic 7 bit ansi escape codes
        FMT_CSI: str = f"{CSI}{{}}m"
        # format for 7 bit foreground (0-7)
        FMT_7BIT_FG: str = f"{CSI}3{{}}m"
        # format for 7 bit background (0-7)
        FMT_7BIT_BG: str = f"{CSI}4{{}}m"
        # format for 7 bit bright foreground (0-7)
        FMT_7BIT_FG_BRIGHT: str = f"{CSI}9{{}}m"
        # format for 7 bit bright foreground (0-7)
        FMT_7BIT_BG_BRIGHT: str = f"{CSI}10{{}}m"

        # - {3,4}{0-255} - format string for 256 color codes
        # - 3 is foreground; 4 is background
        #
        # ESC[38; 5; ⟨n⟩ m Select foreground color
        # ESC[48; 5; ⟨n⟩ m Select background color
        # - format string for 256 color codes
        FMT_CSI_8BIT: str = f"{CSI}{{}}8;5;{{}}m"
        # - format string for 8 bit foreground
        FMT_8BIT_FG: str = f"{CSI}38;5;{{}}m"
        # - format string for 8 bit background
        FMT_8BIT_BG: str = f"{CSI}48;5;{{}}m"

        # ESC[ 38;2;⟨r⟩;⟨g⟩;⟨b⟩ m Select RGB foreground color
        # ESC[ 48;2;⟨r⟩;⟨g⟩;⟨b⟩ m Select RGB background color
        # - use R;G;B to select foreground colors
        CSI_24BITFG: str = f"{CSI}[38;2;{{}};{{}};{{}}m"
        # - use R;G;B to select background colors
        CSI_24BITBG: str = f"{CSI}[48;2;{{}};{{}};{{}}m"
        SUFFIX: str = "m"  # - suffix for ansi codes
        # !------------------------ ANSI regex constants
        RE_CSI = r"\x1B\["  # - regex string for CSI

        # 7 bit C1 ANSI sequences
        ANSI_ESCAPE_7BIT = re.compile(
            r"""
            \x1B  # ESC
            (?:   # 7 bit C1 Fe (except CSI)
                [@-Z\\-_]
            |     # or [ for CSI, followed by a control sequence
                \[
                [0-?]*  # Parameter bytes
                [ -/]*  # Intermediate bytes
                [@-~]   # Final byte
            )
        """,
            re.VERBOSE,
        )  # ??? untested [1]

        def _un_ansi(self, n: str) -> str:
            """ Return string with 7 bit ANSI escape sequences removed. """
            return ANSI_ESCAPE_7BIT.sub("", n)

        ANSI_ESCAPE_8BIT = re.compile(
            r"""(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]"""
        )  # ??? untested [2]

        ANSI_ESCAPE = re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]")

        def remove_needle():
            pass

        def escape_ansi(self, needle: str):
            return self.ANSI_ESCAPE.sub("", needle)

        # !------------------------ ANSI default constants

        DEFAULT_FG_CODE: str = "229"
        DEFAULT_BG_CODE: str = "0"
        DEFAULT_EFFECT_CODE: str = "0"
        DEFAULT_FG: str = FMT_8BIT_FG.format(DEFAULT_FG_CODE)
        DEFAULT_BG: str = FMT_8BIT_BG.format(DEFAULT_BG_CODE)
        DEFAULT_ANSI_TEXT: str = f"{DEFAULT_EFFECT_CODE}{DEFAULT_FG}{DEFAULT_BG}"
        FG_DEFAULT: str = f"{DEFAULT_EFFECT_CODE}{DEFAULT_BG}{{}}"

        # !------------------------ ANSI class setup

        def __init__(self):
            super().__init__()
            self._add_8bit()

        def _add_dynamic_method(self, name, value):
            """ Add dynamic method to class. """

            def key_method(self, value=value):
                """ Dynamic method that returns <value>. """
                return value

            try:
                setattr(self.__class__, name, value)
            except Exception:
                pass

        def __getattribute__(self, name):
            # if SUPPORTS_COLOR:
            #     return ''
            return super().__getattribute__(name)
            # self.__getattribute__()

        # @lru_cache
        def _add_8bit(self):
            """ Create dynamic color methods for each ANSI 256 color codes, both foreground and background. """
            s: str = "COLOR"
            for i in range(255):
                if i == 232:
                    s = "GREY"
                self._add_dynamic_method(f"{s}{i}", self.FMT_8BIT_FG.format(i))
                self._add_dynamic_method(f"BG_{s}{i}", self.FMT_8BIT_BG.format(i))

        # def __iter__(self):
        #     yield from dataclasses.astuple(self)

        def __add__(self, value) -> str:
            try:
                return value + self
            except:
                return self

        def __mul__(self, value: int) -> str:
            try:
                return self * value
            except:
                return self

        def __contains__(self, key):
            return super().__contains__(key)

        def BOLD(self) -> str:
            try:
                self = self.B + self
            except Exception as e:
                dbprint(e)
            return self

        # !------------------------ encode ANSI color codes

        @lru_cache()
        def encode_color_str(
            self, fg=DEFAULT_FG_CODE, bg=DEFAULT_BG_CODE, ef=DEFAULT_EFFECT_CODE
        ) -> str:
            if SUPPORTS_COLOR:
                return f"{self.ef(ef)}{self.bg(bg)}{self.fg(fg)}"
            else:
                return ""

        @lru_cache()
        def encode_color_tuple(
            self, fg=DEFAULT_FG_CODE, bg=DEFAULT_BG_CODE, ef=DEFAULT_EFFECT_CODE
        ) -> Tuple[
            str,
        ]:
            return tuple(self.effect(ef), self.bg(bg), self.fg(fg))

        @lru_cache()
        def fg_default(self, c: str) -> str:
            """ Return string with default effect, default background, and
                forground color string <c> encoded.

                c: str - add any foreground string
                DEFAULT_EFFECT_CODE, DEFAULT_BG - added by default
                """
            if SUPPORTS_COLOR:
                return self.encode_color_str(self.fg(c))
            else:
                return ""

        @lru_cache()
        def effect(self, ef: int = 0) -> str:
            """ #### Encode ANSI effect code (default: 0)
                - NONE :            0
                - BOLD :            1
                - FAINT :           2
                - ITALIC :          3
                - UNDERLINE :       4
                - BLINK :           5
                - REVERSE :         7
                - CONCEAL :         8
                - STRIKE :          9
                - FRAME :           51
                - CIRCLE :          52
                - OVERLINE :        53
                """
            if SUPPORTS_COLOR:
                return self.FMT_CSI.format(ef)
            else:
                return ""

        @lru_cache()
        def fg(self, color: int = 15) -> str:
            """ Encode ANSI 8 bit foreground color (default: 15)

                    foreground encoding - `ESC[38;5;3{color}m`

                color -
                - 0-7:     standard colors(e.g. 7-bit ESC[30–37 m)
                - 8-15:    high intensity colors(e.g. 7-bit ESC[90–97 m)
                - 16-231:  6×6×6 cube(216 colors) 16 + 36×r + 6×g + b(0 ≤ r, g, b ≤ 5)
                - 232-255: grayscale from black to white in 24 steps
                """
            if SUPPORTS_COLOR:
                return self.FMT_8BIT_FG.format(color)
            else:
                return ""

        @lru_cache()
        def bg(self, color: int = 0) -> str:
            """ Encode ANSI 8 bit background color (default: 0)

                    background encoding - `ESC[48;5;4{color}m`

                color -
                - 0-7:     standard colors(e.g. 7-bit ESC(40–47 m)
                - 8-15:    high intensity colors(e.g. 7-bit ESC[90–97 m)
                - 16-231:  6×6×6 cube(216 colors) 16 + 36×r + 6×g + b(0 ≤ r, g, b ≤ 5)
                - 232-255: grayscale from black to white in 24 steps
                """
            if SUPPORTS_COLOR:
                return self.FMT_8BIT_BG.format(color)
            else:
                return ""

        @lru_cache()
        def _show_colors(self) -> int:
            if not SUPPORTS_COLOR:
                return -1
            else:
                c: str = "COLOR"
                for i in range(255):
                    if i == 233:
                        c = "GREY"
                    s = f"{c}{i}"
                    s = f"MAIN"
                    s = f"Ansi.{s}"
                    s = s + f"{c}.{s}"
                    print(f"{s:8} ", end="")
                    if i % 8 == 0:
                        print()
                return 0

        # @staticmethod
        # def set_code(self, s: str, file=stdout):
        #     print(s, file=file)

        # !------------------------ ANSI cursor controls

        def move_to(self, L: int, C: int):
            """ Position the Cursor:

                    <ESC>[<L>;<C>H
                        Or
                    <ESC>[<L>;<C>f

                puts the cursor at line L and column C.
                """
            if SUPPORTS_COLOR:
                print(f"\x1B[{L};{C}H")

        def up(self, n: int = 1):
            """ Move the cursor up N lines:

                    <ESC>033[<N>A
                """
            if SUPPORTS_COLOR:
                print(f"\x1B[{n}A")

        def down(self, n: int = 1):
            """ Move the cursor down N lines:

                    <ESC>033[<N>B
                """
            if SUPPORTS_COLOR:
                print(f"\x1B[{n}B")

        def left(self, n: int = 1):
            """ Move the cursor forward N columns:

                    <ESC>033[<N>C
                """
            if SUPPORTS_COLOR:
                print(f"\x1B[{n}C")

        def right(self, n: int = 1):
            """ Move the cursor backward N columns:

                    <ESC>033[<N>D
                """
            if SUPPORTS_COLOR:
                print(f"\x1B[{n}D")

        def clear(self):
            """ Clear the screen, move to (0,0):

                    <ESC>033[2J
                """
            if SUPPORTS_COLOR:
                print(f"\x1B[2J")

        def eol(self):
            """ Erase to end of line:

                    <ESC>033[K
                """
            if SUPPORTS_COLOR:
                print(f"\x1BK")

        def save_cursor(self):
            """ Save cursor position:

                    <ESC>033[s
                """
            if SUPPORTS_COLOR:
                print(f"\x1Bs")

        def restore_cursor(self):
            """ Restore cursor position:

                    <ESC>033[u
                """
            if SUPPORTS_COLOR:
                print(f"\x1Bu")

        def loading(
            self, delay: float = 0.1, message: str = "Loading ...", percent: bool = True
        ):
            """ ### Terminal progress Indicator

                # Usage:

                    loading(delay: float = 0.1, message: str = 'Loading ...', percent: bool = True )


                    delay - delay between ticks
                    message - feedback shown during countdown (default: 'Loading...')
                    percent - display the '%' symbol

                """
            sp: str = "%"
            if not percent:
                sp = ""
            print(message)
            for i in range(0, 100):
                sleep(delay)
                stdout.write("\x1B[1000D" + str(i + 1) + sp)
                stdout.flush()
            print()

    a = Ansi()


def _main_(args=argv[1:]):
    pass


if __name__ == "__main__":
    _debug_: bool = True
    _main_()
""" # !------------------------  TODO: Ideas and additions:

    1. integrate into <str> class so it works well with others ...
        e.g. output = some_string.capitaize.BLUE.strip

    2. Random changing letter colors in words
        (iterate over letters, interleve random formatting)

    3. Patterned changing letter colors in words
        (zip formatting with letters, join)

    4. Slice formatting options for sentences similar to sometext.format(x, y)
        e.g. some_string.format("1:3, 3, 4:6, 6:", [BLUE, RED, Color248,
        YELLOW]) (break string into slices, prepend formatting, join)

    5. Add common color formats and interfaces (1)
        css parsing, js library, 16bit color, 32bit color, etc.

    6. Add VSCssssssssssssssssssssode integration
    """
""" # !------------------------  References:

    General:

    - Wikipedia - ANSI escape codes - https://en.wikipedia.org/wiki/ANSI_escape_code

        >In 2016, Microsoft released the Windows 10 Version 1511 update which unexpectedly implemented support for ANSI escape sequences.[12] The change was designed to complement the Windows Subsystem for Linux, adding to the Windows Console Host used by Command Prompt support for character escape codes used by terminal-based software for Unix-like systems. This is not the default behavior and must be enabled programmatically with the Win32 API via SetConsoleMode(handle, ENABLE_VIRTUAL_TERMINAL_PROCESSING).[13] This was enabled by CMD.EXE but not initially by PowerShell;[14] however, Windows PowerShell 5.1 now enables this by default. The ability to make a string constant containing ESC was added in PowerShell 6 with (for example) "`e[32m";[15] for PowerShell 5 you had to use [char]0x1B+"[32m".



    - ECMA - http://www.ecma-international.org/publications/standards/Ecma-048.htm

    1. 7 bit CSI regex and great explanation of ANSI codes - https://stackoverflow.com/a/14693789/9878098

    2. 8 bit CSI regex - https://stackoverflow.com/a/33925425


    # Issue with Windows registry setting:
    #   https://stackoverflow.com/a/57154895
    #   File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/enum.py", line 221, in __new__

    """
""" # !------------------------  Color formatting
    # p1 {background-color: #ff0000;}                /* red in HEX format */
    # p2 {background-color: hsl(120, 100%, 50%);}    /* green in HSL format */
    # p3 {background-color: rgba(0, 4, 255, 0.733);} /* blue with alpha channel in RGBA format */
    """
