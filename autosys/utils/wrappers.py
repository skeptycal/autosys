#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

import sys
import functools
import inspect
import io
import os
from typing import List

# from functools import lru_cache, wraps
# from inspect import Parameter, signature
# from io import StringIO
# from os import fsync, path
from dataclasses import dataclass
import file_ops
import cli
from cli.terminal import hr

# from file_ops import *
# from file_ops.pytemp_dirs import *

_debug_: bool = True  # Turn on extra debug info display

_NAME: str = os.path.basename(__file__)
_HERE: str = os.path.dirname(__file__)


# !---------------------------------------------- Dynamic Class
# ref: https://stackoverflow.com/a/6581949/9878098


def choose_dyn_class(name):
    print(name)
    if name == "foo":

        class Foo(object):
            pass

        return Foo  # return the class, not an instance
    else:

        class Bar(object):
            pass

        return Bar


class Capturing(io.StringIO):
    """
        ### Creates a context manager to capture `stdout` text lines from code block.

        Returns:
            List[str] -- list containing text lines

        (This class only writes to disk file on exit. It is intended for use in short blocks of code as a temporary context manager. Long term usage increases the risk of data loss and will act as a memory leak.)

        ### Usage:

        ```
        with Capturing() as output:
            do_something(my_object)
        ```
        output is now a list containing the lines printed by the function call.

        ### Advanced usage:

        This can be done more than once and the results concatenated:

        ```
        with Capturing() as output:
            print('hello world')

        print('displays on screen')

        with Capturing(output) as output:  # note the constructor argument
            print('hello world2')

        print('done')
        print('output:', output)
        ```

        Output:

        ```
        displays on screen
        done
        output: ['hello world', 'hello world2']
        ```

        (Ref: https://stackoverflow.com/a/16571630)
        """

    def __init__(self):
        self._stdout = sys.stdout
        super().__init__()

    def __enter__(self):
        sys.stdout = self
        return super().__enter__()

    def __exit__(self, *args):
        """
            This function only writes to disk file on exit. It is intended for use in short blocks of code as a temporary context manager. Long term usage increases the risk of data loss and will act as a memory leak.
            """
        # self.extend(self._stringio.getvalue().splitlines())
        print(self.get_data(), file=sys.stderr)

        self.truncate(0)
        sys.stdout = self._stdout
        del self  # free up some memory

    def get_data(self, keepends: bool = False) -> List:
        return self.getvalue().splitlines(keepends=keepends)

    def write_to_disk(self):
        with TMP_HERE(prefix=_NAME) as f:
            f.writelines([_ for _ in self.get_data()])
            f.flush()
        os.fsync()  # commit disk writes


# wrapper to auto assign variables in __init__ method
# e.g.
# class Foo(object):

#     @auto_assign
#     def __init__(self, a, b, c=None, d=None, e=3):
#         pass


def auto_assign(func):
    # Signature:
    sig = signature(func)
    for name, param in sig.parameters.items():
        if param.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD):
            raise RuntimeError(
                "Unable to auto assign if *args or **kwargs in signature."
            )
    # Wrapper:

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        for i, (name, param) in enumerate(sig.parameters.items()):
            # Skip 'self' param:
            if i == 0:
                continue
            # Search value in args, kwargs or defaults:
            if i - 1 < len(args):
                val = args[i - 1]
            elif name in kwargs:
                val = kwargs[name]
            else:
                val = param.default
            setattr(self, name, val)
        func(self, *args, **kwargs)

    return wrapper


def capture(capture_text):
    with Capturing() as output:
        if isinstance(capture_text, str):
            print(capture_text)
            return 0
        try:  # if iterable
            print(os.linesep.join([s for s in capture_text]))
            return 0
        except:
            pass
        try:
            print(str(capture_text))
            return 0
        except:
            return 1


def _test_():
    """
    #### Perform tests to produce additional debug info.

    (runs if _debug_ = True)
    """
    hr()
    print(f"{_NAME} is in DEBUG MODE.")

    print(choose_dyn_class)
    print(choose_dyn_class(auto_assign))
    hr()

    capture("capturing test - this should be captured to 'output'")
    # with Capturing() as output:
    #     print('capturing test - this should be captured to "output"')

    hr()
    print('capturing test - this should print to "stdout"')
    hr()
    print("\n --------------- done ...")


def _main_():
    """
    CLI script main entry point.
    """

    if _debug_:
        _test_()


if __name__ == "__main__":  # if script is loaded directly from CLI
    _main_()
