#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Logger
    ---
    logger - A wrapper class to setup common logging functions.

    AutoSys
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# from typing import NamedTuple, Sequence, Tuple
# from sys import stdout
# from os import linesep as NL, environ as ENV
# from platform import platform
# from io import TextIOWrapper
from dataclasses import dataclass
from os import linesep as NL

from autosys.cli.supports_color import *
# PLATFORM = platform()


@dataclass
class FakeLog:
    def _fakelog(self, *args, line_color: str = "MAIN"):
        args = arg_str(*args)
        fmt = eval(f"color.{line_color}")
        print(f"{fmt}{args}{color.RESET}")

    def info(self, *args):
        """ placeholder for logging function... """
        self._fakelog(*args, line_color="BLUE")

    def error(self, *args):
        """ placeholder for logging function ... """
        self._fakelog(*args, line_color="WARN")

    def var(self, my_var: str = ""):
        """ log value of a variable.

            my_var is translated to a safe version before processing."""
        try:
            my_var = str(my_var)
            evl: Sequence = replace_all(":=/!#;\\", my_var, "_")
            # evl: Sequence = make_safe_id(my_var)
            fmt: str = f"{my_var} | {eval(evl)}"
            self._fakelog(fmt, line_color="RAIN")
        except Exception as e:
            self.error(f"ERROR: {my_var=} | {type(my_var)=} |  {e.args[0]}")


log = FakeLog()


# some basic colors ..
class BasicColors:
    MAIN: str = "\x1B[38;5;229m" * SUPPORTS_COLOR
    WARN: str = "\x1B[38;5;203m" * SUPPORTS_COLOR
    BLUE: str = "\x1B[38;5;38m" * SUPPORTS_COLOR
    GO: str = "\x1B[38;5;28m" * SUPPORTS_COLOR
    CHERRY: str = "\x1B[38;5;124m" * SUPPORTS_COLOR
    CANARY: str = "\x1B[38;5;226m" * SUPPORTS_COLOR
    ATTN: str = "\x1B[38;5;178m" * SUPPORTS_COLOR
    RAIN: str = "\x1B[38;5;93m" * SUPPORTS_COLOR
    WHITE: str = "\x1B[37m" * SUPPORTS_COLOR
    RESET: str = "\x1B[0m" * SUPPORTS_COLOR


DEFAULT_COLOR = BasicColors.MAIN


class Color:
    name: str
    level: int
    color: str


@dataclass
class LogColors:
    CRITICAL: Color = ('Critical', 50, BasicColors.WARN)
    FATAL: Color = ('Fatal', 50, BasicColors.WARN)
    ERROR: Color = ('Error', 40, BasicColors.ATTN)
    WARNING: Color = ('Warning', 30, BasicColors.CANARY)
    INFO: Color = ('Info', 20, BasicColors.GO)
    DEBUG: Color = ('Debug', 10, BasicColors.RAIN)
    NOTSET: Color = ('NotSet', 0, BasicColors.RESET)

    FATAL: str = CRITICAL
    WARN: str = WARNING

    def __str__(self):
        print(self.__dict__)
        for c in self.__dict__:
            print(c)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww

        return ''

        # return NL.join([
        #     f"logger color {c.color}{c.name}{self.NOTSET}{c.level}"
        #     for c in self.__dict__ if not isinstance(c, Color)
        # ])


print(LogColors())
