# -*- coding: utf-8 -*-

import os
import sys
import locale
from typing import List, Dict, Any

DEFAULT_ENCODING: str = sys.getfilesystemencoding()
DEFAULT_LOCALE: str = locale.getlocale()

PLATFORM: str = {
    "linux": "Linux",
    "win32": "Windows",
    "cygwi": "Windows/Cygwin",
    "darwi": "macOS"
}.get(sys.platform.lower()[0:5])


def basename(s: str) -> str:
    """
    get only basename from full path
    # TODO translate to pathlib
    """
    return os.path.basename(s)


borders = {
    "176": "░",
    "177": "▒",
    "178": "▓",
    "185": "╣",
    "186": "║",
    "187": "╗",
    "188": "╝",
    "201": "╔",
    "200": "╚",
    "202": "╩",
    "203": "╦",
    "204": "╠",
    "205": "═",
    "206": "╬",
    "219": "█",
    "220": "▄",
    "223": "▀",
    "240": "≡",
    "254": "■",
}


def pprint_dict(width: int, data: dict, sep: str = ',', align: str = 'left'):
    key_width = max(len(x) for x in data.keys()) + 1
    values_width = width - key_width - 3  # 3 for main borders, value borders extra
    print()
    print(key_width)
    values: List[str] = list(data.values())
    print(values)


def pprint_globals():
    print()
    print("Globals: ")
    print("*"*40)
    for s in globals():
        print("{:<15.15} : {:<64.64}".format(s, str(globals().get(s))))


if __name__ == "__main__":
    # pprint_globals()
    print()
    print()
    print("basename: ", basename(__file__))
    print("platform: ", PLATFORM)
    print("encoding: ", DEFAULT_ENCODING)
    print()
    print(type(globals()))

    # pprint_dict(60, globals())
    print(globals().__str__())
    # print(globals())
