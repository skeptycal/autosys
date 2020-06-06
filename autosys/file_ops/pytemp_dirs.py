#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" ### Various temporary file implementations:

    - TMP: 'secure' temp file with no directory entry
    - TMP_NAMED: temp file with name that can be used in code
    - TMP_HERE: temp file with name; created in the current directory
    """

import enum
import os
import sys
import tempfile

# from io import StringIO
# from pathlib import Path

import autosys.parsing.file_ops.file_class


# !------------------------------------- Dev and Debugging
_debug_: bool = True  # Turn on extra debug info display

_NAME: str = os.path.basename(__file__)
_HERE: str = os.path.dirname(__file__)
_TMP_PREFIX: str = f"_{_NAME}_".replace(".", "_").strip().lower()
_TMP_SUFFIX: str = ".log"


class TempFile:
    TMP = tempfile.TemporaryFile()  # e.g. with TMP as f:
    TMP_NAMED = tempfile.NamedTemporaryFile()  # e.g. with TMP_NAMED as f:
    TMP_HERE = tempfile.NamedTemporaryFile(
        prefix=_TMP_PREFIX, suffix=_TMP_SUFFIX, dir=_HERE
    )
    TMP_SPOOL = tempfile.SpooledTemporaryFile(
        max_size=1024, prefix=_TMP_PREFIX, suffix=_TMP_SUFFIX, dir=_HERE
    )
    TMP_DIR = tempfile.TemporaryDirectory(
        prefix=_TMP_PREFIX, suffix=_TMP_SUFFIX
    )

    def __init__(self, temp_type: str = "TMP"):
        super().__init__()


def tmp_file(temp_type: str = "TMP"):
    try:
        return TempFile(f"{temp_type}")
    except Exception as e:
        return e


def temp_it(func):
    """ Wrapper for temp files. """
    pass


__all__ = ["TMP", "TMP_NAMED", "TMP_HERE"]

# !------------------------------------- Dev and Debugging


def _test_():
    """ #### Perform tests to produce additional debug info.

        (runs if _debug_ = True)
        """

    print(f"{_NAME=}")
    print(f"{_HERE=}")
    print(f"{_TMP_PREFIX=}")
    print(f"{_TMP_SUFFIX=}")
    print()

    script_name: str = os.path.basename(__file__)
    print(f"{script_name} is in DEBUG MODE.")
    print(TempFile.TMP)
    print(TempFile.TMP_HERE)
    print(TempFile.TMP_NAMED)
    print(TempFile.TMP_SPOOL)
    print(tmp_file())
    with TempFile.TMP as f:
        print_file_info(f)
    # print('exists after: ', os.path.exists(f.name))

    # with TMP_NAMED as f:
    #     print_file_info(f)
    # print('exists after: ', os.path.exists(f.name))

    # with TMP_HERE as f:
    #     print_file_info(f)
    # print('exists after: ', os.path.exists(f.name))

    print()

    print("\n --------------- done ...")


# !------------------------------------- main entry point


def _main_():
    """
    CLI script main entry point.
    """
    if _debug_:
        _test_()  # CLI testing - only runs if _DEBUG_ = True


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()  # CLI functionality
