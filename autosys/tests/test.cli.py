#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Initial Basic Tests for Autosys package.
For more information: https://docs.python-guide.org/writing/tests/
"""
from autosys.cli import *


def test_stdout():
    assert stdout.hasattr(tty)


if __name__ == "__main__":
    pass
    # print_autosys_dir(globals())
