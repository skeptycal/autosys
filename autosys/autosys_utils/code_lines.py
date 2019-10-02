#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" py_code.py - print the number of lines
        of python code in a directory. """
import sys
from pathlib import Path
from typing import Dict, List

import text_colors

FG_DICT: Dict[str, str] = {
    "MAIN": "\u001b[38;5;229m",
    "COOL": "\u001b[38;5;38m",
    "GO": "\u001b[38;5;28m",
    "WARN": "\u001b[38;5;203m",
    "CHERRY": "\u001b[38;5;124m",
    "CANARY": "\u001b[38;5;226m",
    "ATTN": "\u001b[38;5;178m",
    "PURPLE": "\u001b[38;5;93m",
    "RESET": "\u001b[0m",
}
ATTN = FG_DICT["ATTN"]
RESET = FG_DICT["RESET"]
FORMAT_STR: str = "Lines of code matching glob pattern '{}{:<6}{}':{}{:>10}{}"


def c_print(c: str, args):
    try:
        print(FG_DICT[c], args, FG_DICT["RESET"])
    except:
        print(args)
        print(FG_DICT["RESET"])


def get_suffix_list():
    pass


def file_len(file_name: str, encoding: str = "utf8") -> int:
    i: int = -1
    try:
        with open(file_name, encoding=encoding) as f:
            i = -1
            for i, line in enumerate(f):
                pass
    except (UnicodeDecodeError, FileNotFoundError):
        pass
    return i + 1


def code_lines(pattern: str, recursive: bool = True) -> int:
    if not recursive:
        return sum(file_len(f) for f in p.glob(pattern) if not f.is_dir())
    else:
        return sum(file_len(f) for f in p.rglob(pattern) if not f.is_dir())


def print_code(pattern: str):
    print(FORMAT_STR.format(ATTN, pattern, RESET, ATTN, code_lines(pattern), RESET))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
    else:
        pattern_list = [
            "py",
            "c",
            "sh",
            "js",
            "bas",
            "pas",
            "php",
            "css",
            "html",
            "cpp",
            "h",
            "md",
            "rst",
        ]
    p = Path().cwd()
    p = p.resolve()  # similar to os.path.abspath()
    c_print("MAIN", "-~*#^#*~-" * 8)
    c_print("MAIN", "Current Path: {}".format(p))
    c_print("MAIN", "-~*#^#*~-" * 8)
    pattern_list = [
        "py",
        "c",
        "sh",
        "js",
        "bas",
        "pas",
        "php",
        "css",
        "html",
        "cpp",
        "h",
        "md",
        "rst",
    ]
    for pattern in pattern_list:
        print_code("*." + pattern)


"""
References:

original: https://towardsdatascience.com/bite-sized-python-recipes-52cde45f1489

"""
