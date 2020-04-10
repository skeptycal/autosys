#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Initial Basic Tests for Autosys package.
For more information: https://docs.python-guide.org/writing/tests/
"""

import autosys
from autosys import *


def test_version_number():
    assert isinstance(autosys.__version__, str)


def test_CONSTANTS():
    assert autosys.__author__ == "Michael Treanor"
    assert autosys.__author_email__ == "skeptycal@gmail.com"
    assert autosys.__copyright__ == "Copyright (c) 2019 Michael Treanor"
    assert autosys.__license__ == "MIT"
    assert autosys.__name__ == "autosys"
    assert autosys.__python_requires__ == ">=3.8"
    assert autosys.__title__ == "autosys"


def test_docopt_import_status():
    try:
        import docopt

        assert autosys.DOCOPT_FLAG == True
    except:
        assert autosys.DOCOPT_FLAG == False


def test_ENV_import():
    tmp = "SHELL" in autosys.ENV
    assert tmp == True
    tmp = "zabiwickerwillowsky" not in autosys.ENV
    assert tmp == True


def test_NL_constant():
    assert ord(autosys.NL) == 10


def print_autosys_dir():
    DEFAULT_PRINT_WIDTH = 40
    for i, x in enumerate(dir(autosys)):
        if i > 30:
            fmt = f"autosys.{x}"
            f = str(eval(fmt))
            if len(f) > DEFAULT_PRINT_WIDTH:
                f = f[0 : DEFAULT_PRINT_WIDTH - 1]
            print(f"assert autosys.{x} == '{f}'")
            print()


test_version_number()


if __name__ == "__main__":
    print_autosys_dir()
