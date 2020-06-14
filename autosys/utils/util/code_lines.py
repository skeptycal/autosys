#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" py_code.py - print the number of lines
        of python code in a directory. """
# 'Standard Library'
import sys

from pathlib import Path

# 'package imports'
import autosys.as_ansi as ansi

from typing import Dict, List

ce = ansi.color_encode
cp = ansi.color_print

FG = ansi.FG_DICT


ATTN = FG["ATTN"]
RESET = FG["RESET"]
FORMAT_STR: str = f"Lines of code matching glob pattern '{ATTN}{{:<6}}{RESET}':{ATTN}{{:>10}}{RESET}"


# def c_print(c: str, args):
#     try:
#         print(FG[c], args, FG["RESET"])
#     except:
#         print(args)
#         print(FG["RESET"])


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
    print(FORMAT_STR.format(pattern, code_lines(pattern)))


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
    cp("MAIN", "-~*#^#*~-" * 8)
    cp("MAIN", "Current Path: {}".format(p))
    cp("MAIN", "-~*#^#*~-" * 8)
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
