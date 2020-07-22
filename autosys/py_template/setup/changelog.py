#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" autosys package """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal/autosys
# https://www.twitter.com/skeptycal

# `AutoSys` is licensed under the `MIT <https://opensource.org/licenses/MIT>`.

# 'Standard Library'
import sys

# _SET_DEBUG: bool = True
# NL: str = "\n"


def br(n: int = 1, file=sys.stdout) -> int:
    NL_print = (
        ""
        if not _SET_DEBUG
        else (" --> (DEBUG: <br> function - blank line ...)")
    )
    try:
        int(n)
        if n > 20:
            n = n % 20
        print(f"n = {n}")
        print(NL * n, sep="", end=NL_print)
        return 0
    except TypeError as e:
        if _SET_DEBUG:
            print(f"Error: n must be an integer ...")
            print(f"{e}")
        return 1
    return -1


def main():
    """
    CLI script main entry point.
    """
    print(
        "The <br> function is a ridiculous python CLI mirror of the HTML <br /> tag."
    )
    result = br(3)
    print("There should be 3 blank lines above this text...")
    print(f"The return value for br was {result}.")


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
