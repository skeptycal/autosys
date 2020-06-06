#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# !---------------------------------------------- Utilities
import re
import sys
from pprint import pprint
from typing import Dict, List

from autosys.defaults import _debug_
from autosys.cli.debug import *

# regex
RE_SAFE_WORD_Pattern: re.Pattern = r"\w"
RE_NOT_SAFE_WORD_Pattern: re.Pattern = r"\W"
RE_NOT_ALPHA_UNDER_Pattern: re.Pattern = r"[^\w_]"

RE_SAFE_WORD = re.compile(fr"{RE_SAFE_WORD_Pattern}")
RE_NOT_SAFE_WORD = re.compile(fr"{RE_NOT_SAFE_WORD_Pattern}")

RE_NOT_ALPHA_UNDER = re.compile(fr"{RE_NOT_ALPHA_UNDER_Pattern}")

# pre-made translation table
TRANSLATE_TABLE_SAFE_WORD = dict.fromkeys(map(ord, "!@#$"), None)

# in place translation table creation
unicode_line: str = ""
unicode_line = unicode_line.translate({ord(c): None for c in "!@#$"})


def translate(translation_table, string):
    return string.translate(translation_table)


def safe_word(s):
    return re.sub(RE_NOT_SAFE_WORD, "", s)


def safe_filename(s):
    """ Truncates text and returns only alphanumeric and underscore characters. """
    s = fr"{s}"
    return re.sub(RE_NOT_ALPHA_UNDER, "", s)


class ASCIIRecord(str):
    """
    {
        name: str,
        code: int,
        char: str,
        desc: str
    }
    """

    pass
    # def __init__(self, name, num, desc):
    #     self._name = name
    #     self._num = num
    #     self._char = chr(num)
    #     self._desc = desc

    # def __str__(self):
    #     return self.char

    # @property
    # def name(self):
    #     return self._name

    # @property
    # def ord(self):
    #     return self._num

    # @property
    # def char(self):
    #     return self._char

    # @property
    # def desc(self):
    #     return self._desc

    # @property
    # def _unsafe(self):
    #     return self._char

    # @property
    # def utf8(self):
    #     return self._char.encode('')

    # @property
    # def info(self):
    #     return f'ASCII {self.name}'

    # def filesafe(self):
    #     " Return text with only alphanumeric and underscore characters."
    #     return self._char if re.match(r'\w', self._char) else ''


class ASCII:
    """
        # 10#13 — Indicates a new line &crarr  
        # 7 — bell (computer beeps)  
        # 26 — Ctrl+Z →  
        # 8 — backspace  
        # 127 — delete  
        # 27 — escape  
        # 32 — space  
        # 9 — tab  
        # 160 — a  
        # 163 — c  
        # 65 — A  
        # 68 — C  
        # 42 — *  
        """

    CRLF: str = chr(10) + chr(13)
    BELL: str = chr(7)
    BKSP: str = chr(8)
    TAB: str = chr(9)
    LF: str = chr(10)
    CTL_Z: str = chr(26)
    DEL: str = chr(127)
    ESC: str = chr(27)
    SPACE: str = chr(32)
    ASTERISK: str = chr(42)
    UPPER_A: str = chr(65)
    LOWER_A: str = chr(97)
    UPPER_C: str = chr(67)
    LOWER_C: str = chr(99)
    ELLIPSIS: str = chr(133)

    """ ASCII Control Codes:
        NUL (null)
        SOH (start of heading)
        STX (start of text)
        ETX (end of text)
        EOT (end of transmission) - Not the same as ETB
        ENQ (enquiry)
        ACK (acknowledge)
        BEL (bell) - Caused teletype machines to ring a bell. Causes a beep in many common terminals and terminal emulation programs.
        BS (backspace) - Moves the cursor (or print head) move backwards (left) one space.
        TAB (horizontal tab) - Moves the cursor (or print head) right to the next tab stop. The spacing of tab stops is dependent on the output device, but is often either 8 or 10.
        LF (NL line feed, new line) - Moves the cursor (or print head) to a new line. On Unix systems, moves to a new line AND all the way to the left.
        VT (vertical tab)
        FF (form feed) - Advances paper to the top of the next page (if the output device is a printer).
        CR (carriage return) - Moves the cursor all the way to the left, but does not advance to the next line.
        SO (shift out) - Switches output device to alternate character set.
        SI (shift in) - Switches output device back to default character set.
        DLE (data link escape)
        DC1 (device control 1)
        DC2 (device control 2)
        DC3 (device control 3)
        DC4 (device control 4)
        NAK (negative acknowledge)
        SYN (synchronous idle)
        ETB (end of transmission block) - Not the same as EOT
        CAN (cancel)
        EM (end of medium)
        SUB (substitute)
        ESC (escape)
        FS (file separator)
        GS (group separator)
        RS (record separator)
        US (unit separator)
        """


class Default:  # CLI Defaults
    """ Defaults for CLI formats and settings """

    SHOW_UNDERS = True
    SHOW_DUNDERS = True
    USE_REPR = False

    INDENT: int = 4
    TABLE_CHAR: str = "-"
    TABLE_GRAPHICS_TOP: str = ""
    TABLE_GRAPHICS_MID: str = ""
    TABLE_GRAPHICS_BOTTOM: str = ""

    DICT_KEY_WIDTH: int = 20
    DICT_VALUE_WIDTH: int = 35
    STR_WIDTH: int = 20
    LIST_ITEM_WIDTH: int = 35
    INT_WIDTH: float = 3.2

    FMT_DICT_KEY: str = f":>{DICT_KEY_WIDTH}"
    FMT_DICT_VALUE: str = f":>{DICT_VALUE_WIDTH}"
    FMT_LIST_ITEM_WIDTH: str = f":>{LIST_ITEM_WIDTH}"
    FMT_STR_WIDTH: str = f":>{STR_WIDTH}"
    FMT_INT_WIDTH: str = f":>{INT_WIDTH}"


class PrettyCLI:
    """ Provides a common cli interface. """

    def __init__(self, d: Dict):
        if not isinstance(d, dict):
            raise TypeError("Parameter should be of type `dict`")
        else:
            self._dict: Dict = d

    def print_dict(
        self,
        indent=Default.INDENT,
        group=10,
        blacklist=[],
        no_unders=True,
        no_dunders=True,
        value_repr=True,
        trim=True,
    ):
        c = Default.TABLE_CHAR
        kw = Default.DICT_KEY_WIDTH
        vw = Default.DICT_VALUE_WIDTH
        w = kw + vw + indent + 4
        TABLE_BREAK: str = c * w
        print(TABLE_BREAK)
        print(f"{'keys:':<{kw}s} -- {'values:':<{vw}}")
        for i, (k, v) in enumerate(self.items()):
            # k, v = x
            # kick out unwanted keys:
            if no_unders and k.startswith("_"):
                continue
            if no_dunders and k.startswith("__"):
                continue
            if k in blacklist:
                continue
            if int(i % group) == 0:
                print(TABLE_BREAK)

            if isinstance(v, dict):  # recursive if v is dict
                print_dict(v, indent=indent + Default.INDENT)
            else:
                v = f"{v!r}" if value_repr else f"{v!s}"
                v = str(v)
                if trim:
                    try:
                        v = v[: vw - 1] + ASCII.ELLIPSIS
                    except:
                        pass
                    try:
                        k = k[: kw - 1]
                    except:
                        pass
                    # v = f"{v:<{vw}}"
                print(f"{' '*indent}{k:<{kw}s} -- {v:<{vw}s}")
        print(TABLE_BREAK)
        return 0

    def print_list(
        self,
        indent=Default.INDENT,
        group=10,
        blacklist=[],
        no_unders=True,
        no_dunders=True,
        value_repr=True,
        trim=True,
    ):
        c = Default.TABLE_CHAR
        kw = Default.DICT_KEY_WIDTH
        vw = Default.DICT_VALUE_WIDTH
        w = kw + vw + indent + 4
        TABLE_BREAK: str = c * w
        print(TABLE_BREAK)
        print(f"{'keys:':<{kw}s} -- {'values:':<{vw}}")
        for i, (k, v) in enumerate(self.items()):
            # k, v = x
            # kick out unwanted keys:
            if no_unders and k.startswith("_"):
                continue
            if no_dunders and k.startswith("__"):
                continue
            if k in blacklist:
                continue
            if int(i % group) == 0:
                print(TABLE_BREAK)

            if isinstance(v, dict):  # recursive if v is dict
                print_dict(v, indent=indent + Default.INDENT)
            else:
                v = f"{v!r}" if value_repr else f"{v!s}"
                v = str(v)
                if trim:
                    try:
                        v = v[: vw - 1] + ASCII.ELLIPSIS
                    except:
                        pass
                    try:
                        k = k[: kw - 1]
                    except:
                        pass
                    # v = f"{v:<{vw}}"
                print(f"{' '*indent}{k:<{kw}s} -- {v:<{vw}s}")
        print(TABLE_BREAK)
        return 0


if True:  # !------------------------ Script Tests

    def _tests_(args):
        """
        Run Debug Tests for script if _debug_ = True.
        """
        print(f"{args=}")
        print()
        print(get_class_name("platform.uname()"))
        print(get_class_name("LOG_PATH"))
        print(get_class_name("SCRIPT_PATH()"))
        print(get_class_name("_debug_"))
        return 0

    def _main_(args):
        """ CLI script main entry point. """

        #! script testing
        if _debug_:
            # inject `args` here ...
            args.append("--version")
            args.append("--verbose")
            return _tests_(args)
        return 0


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_(ARGS())
test_str = r"f_fkj3*$//\\fadkjkk"
print(RE_NOT_ALPHA_UNDER)
print(safe_word(test_str))
print(safe_filename(test_str))
# pprint(dir(), indent=4, width=50, depth=3)
