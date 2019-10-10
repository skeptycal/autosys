#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" as_80col.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal


import fileinput
import sys
import pathlib
import textwrap
import locale
from typing import List
from autosys.as_constants import DEFAULT


def create_test_file(filename: str = "testfile.txt", encoding: str = as_constants.DEFAULT_ENCODING) -> str:
    """ Create test file and return resolved Purepath """
    p = pathlib.Path(filename)
    p = p.resolve()
    with open(p, mode="w", encoding=encoding, errors="ignore") as f:
        for n in range(20):
            line_str = "X" * (n + 70) + "\n"
            # print(line_str)
            f.write(line_str)
    return p


def trunc_string_width(s: str) -> str:
    return s


if __name__ == "__main__":

    test_value = """This function wraps the input paragraph such that each line
    in the paragraph is at most width characters long. The wrap method
    returns a list of output lines. The returned list
    is empty if the wrapped
    output has no content."""

    set_width = DEFAULT_CLI_WIDTH
    print("Default Language: ", DEFAULT_LANG)
    print("Default Encoding: ", DEFAULT_ENCODING)
    exit

    if len(sys.argv) < 2:
        print("No arguments given. Creating testfile.txt.")
        file_list.append(create_test_file("testfile.txt"))
        show_test = 1
    else:
        try:
            arg_int = int(sys.argv[1])
        except (IndexError, ValueError):
            # print("Unable to parse code as an integer")
            file_list = sys.argv[1:]
        else:
            # print("first argument is int")
            set_width = arg_int
            file_list = sys.argv[2:]

    with fileinput.input(file_list, inplace=True) as f:
        for line in f:
            # process(line)

            value: str = line.strip()
            # Wrap this text.
            wrapper = textwrap.TextWrapper(width=79)
            word_list = "\n".join(wrapper.wrap(value))

            # Process the line here
            print(word_list)
