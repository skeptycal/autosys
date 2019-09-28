#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# ============================================================================
# utilities for Standard Script Modules (ssm.py)
#
# Copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# MIT License <https://opensource.org/licenses/MIT>
# Intended for Python 3.7+ , ymmv on 2.7
# ============================================================================

def py3up() -> bool:
    """ Return True if 'Python >= 3' else False

        If you want to detect pre-Python 3 and don't want to import anything...
        ... you can (ab)use list comprehension scoping changes
    """
    # https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script/35294211
    # https://stackoverflow.com/a/52825819/9878098
    return (lambda x: [x for x in [False]] and None or x)(True)

def py2() -> bool:
    """ Return True if 'Python < 3' else False

        If you want to detect pre-Python 3 and don't want to import anything...
        ... you can (ab)use list comprehension scoping changes
    """
    # https://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script/35294211
    # https://stackoverflow.com/a/52825819/9878098
    return (lambda x: [x for x in [True]] and None or x)(False)

def pyver() -> str:
    """ Returns string with python version number in major.minor.micro format.
            (e.g. 3.7.3  or  2.7.12)
    """
    return '.'.join(str(i) for i in __import__('sys').version_info[:3])

def py_shell() -> str:
    """ Returns string containing current python shell name. """
    import os
    shell: str = "cpython"
    PY_ENV = os.environ
    if "JPY_PARENT_PID" in PY_ENV:
        shell = "ipython notebook"
    elif "pypy" in PY_ENV:
        shell = "pypy"
    else:
        PY_BASE = os.path.basename(PY_ENV["_"])
        if "jupyter-notebook" in PY_BASE:
            shell = "jupyter notebook"
        elif "ipython" in PY_BASE:
            shell = "ipython"
        else:
            try:
                import platform
                shell = platform.python_implementation()
            except ImportError:
                pass
    # print("pyshell() output: ", shell.strip())
    return shell.strip()

def py2_3_checks():
    python2 = not py3up()

    if python2:  # pragma: nocover
        from itertools import izip_longest as zip_longest  # NOQA
    else:  # pragma: nocover
        from itertools import zip_longest  # NOQA

    if python2:  # pragma: nocover
        from backports import csv  # NOQA
        # monkey patch backports.csv until bug is fixed
        # https://github.com/ryanhiebert/backports.csv/issues/30
        from collections import OrderedDict
        csv.dict = OrderedDict
    else:  # pragma: nocover
        import csv  # NOQA

if __name__ == "__main__":
    py2_3_checks()
