# -*- coding: utf-8 -*-
# Python program to print
# colored text and background
# https://www.geeksforgeeks.org/print-colors-python-terminal/

from typing import Dict, List

MAIN = "\u001b[38; 5; 229m"
RESET = "\u001b[0m"

ATTR: Dict[str, str] = {
    "0": "\u001b[0m",
    "Reset": "\u001b[0m",
    "1": "\u001b[1m",
    "Bold": "\u001b[1m",
    "2": "\u001b[2m",
    "Dim": "\u001b[2m",
    "3": "\u001b[3m",
    "Italic": "\u001b[3m",
    "4": "\u001b[4m",
    "Underline": "\u001b[4m",
    "7": "\u001b[7m",
    "Reverse": "\u001b[7m",
    "8": "\u001b[8m",
    "Conceal": "\u001b[8m",
}
# Generator resources:
# ATTRIBUTE_CODES: List[int] = [0, 1, 2, 3, 4, 7, 8]
# ATTR: Dict[int, str] = {k: '\u001b['+str(k)+'m' for k in [0, 1, 2, 3, 4, 7, 8]}


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 37):
            s1 = ""
            for bg in range(40, 47):
                format = ";".join([str(style), str(fg), str(bg)])
                s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
            print(s1)
        print("\n")


def print_attributes_table():
    """
    prints table of formatted text attribute options
    """
    for style in [0, 1, 2, 3, 4, 7, 8]:
        print(MAIN, style, " : ", RESET, end="")
        for fg in range(30, 37):
            s1 = ""
            # for bg in range(40, 47):
            format = ";".join([str(style), str(fg), str(40)])
            s1 += "\x1b[%sm %s \x1b[\t" % (format, format)
            print(s1, end="")
        print("\n")


print_format_table()
# print_attributes_table()
print(RESET, MAIN, ATTR)
