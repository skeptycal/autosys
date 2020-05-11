#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Initial Basic Tests for Autosys package.
For more information: https://docs.python-guide.org/writing/tests/
"""
import sys
sfrom autosys import *


def test_stdout():
    assert stdout.hasattr(tty)


def test_version_number():
    assert isinstance(autosys.__version__, str)


def test_constants():
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


def test_env_import():
    tmp = "SHELL" in autosys.ENV
    assert tmp == True
    # some random, absolutely made up name ....
    tmp = "zabiwickerwillowsky" not in autosys.ENV
    assert tmp == True


def test_nl_constant():
    if PLATFORM().startswith('win'):

        #  linux, macOS:
        assert ord(autosys.NL) == 10


if __name__ == "__main__":
    print_autosys_dir(globals())
