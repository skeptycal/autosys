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

import re
import logging
from locale import getpreferredencoding
from dataclasses import dataclass
from typing import AbstractSet, Dict, Final, List, Mapping, Tuple
from autosys.cli.terminal import SUPPORTS_COLOR, BasicColors

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

DEFAULT_ENCODING: str = getpreferredencoding(True)

DEFAULT_LOG_FORMAT = "%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s"
DEFAULT_LOG_DATE_FORMAT = "%H:%M:%S"

RE_ANSI_ESCAPE_SEQ = re.compile(r"\x1b\[[\d;]+m",flags=re.IGNORECASE|re.DOTALL|re.MULTILINE,)



def _remove_ansi_escape_sequences(text):
    return _ANSI_ESCAPE_SEQ.sub("", text)


@dataclass
class LogColors:
    """ Level       Numeric value
        -------------------------
        CRITICAL        50
        ERROR           40
        WARNING         30
        INFO            20
        DEBUG           10
        NOTSET           0
        """

    CRITICAL: str = BasicColors.WARN
    ERROR: str = BasicColors.ATTN
    WARNING: str = BasicColors.CANARY
    INFO: str = BasicColors.GO
    DEBUG: str = BasicColors.RAIN
    NOTSET: str = BasicColors.RESET

class VarTester:
    indent: int = 2
    indent_char: str = ' '

def log_var(obj_name: str = '__name__', indent: int = 2):
    """ Log Variable
        ---
        *** variable name must be a string in quotes!! ***

        Quick logging tool to log:

        - variable name
        - variable type
        - variable contents
        """
    obj: object = f"{obj_name}"
    ind: str = ' '*indent
    if hasattr(obj_name, 'iter'):
        print('iter')
    try:
        logger.info(f"{ind}Variable - {obj_name}({obj_name.__class__}): {eval(obj_name)}")
    except:
        pass
    try:
        print(f"{ind}Variable - {obj_name}({obj_name.__class__}): {eval(obj_name)}")
    except:
        pass

def _test_log_var(*args):
    print('='*50)
    print('log_var testing')
    print('-'*50)
    log_var('DEFAULT_ENCODING')

    log_var()
    ind: int = 0
    for arg in args:
        ind += 2
        try:
            for sub in arg:
                ind += 2
                log_var(f"'{sub}'", indent=ind)
            ind -= 2
        except:
            log_var(f"'{arg}'")
        ind -= 2
    print('-'*50)


def _test_logger(debug:bool = False):
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")

    logger.debug(f"default encoding: {DEFAULT_ENCODING}")
    logger.warning(DEFAULT_ENCODING)
    _test_log_var()


_test_logger(True)




# # from pytest.logging.py
# class ColoredLevelFormatter(logging.Formatter):
#     """
#     Colorize the %(levelname)..s part of the log format passed to __init__.
#     """

#     LOGLEVEL_COLOROPTS: Mapping[int, AbstractSet[str]] = {
#         logging.CRITICAL: {"red"},
#         logging.ERROR: {"red", "bold"},
#         logging.WARNING: {"yellow"},
#         logging.WARN: {"yellow"},
#         logging.INFO: {"green"},
#         logging.DEBUG: {"purple"},
#         logging.NOTSET: set(),
#     }  # type: Mapping[int, AbstractSet[str]]
#     LEVELNAME_FMT_REGEX: re.Pattern = re.compile(r"%\(levelname\)([+-.]?\d*s)")

#     def __init__(self, terminalwriter, *args, **kwargs) -> (None):
#         super().__init__(*args, **kwargs)
#         self._original_fmt: str = self._style._fmt
#         self._level_to_fmt_mapping: Dict[int, str] = {}  # type: Dict[int, str]

#         assert self._fmt is not None
#         levelname_fmt_match = self.LEVELNAME_FMT_REGEX.search(self._fmt)
#         if not levelname_fmt_match:
#             return
#         levelname_fmt = levelname_fmt_match.group()

#         for level, color_opts in self.LOGLEVEL_COLOROPTS.items():
#             formatted_levelname = levelname_fmt % {
#                 "levelname": logging.getLevelName(level)
#             }

#             # add ANSI escape sequences around the formatted levelname
#             color_kwargs: Dict = {name: True for name in color_opts}
#             colorized_formatted_levelname = terminalwriter.markup(
#                 formatted_levelname, **color_kwargs
#             )
#             self._level_to_fmt_mapping[level] = self.LEVELNAME_FMT_REGEX.sub(
#                 colorized_formatted_levelname, self._fmt
#             )

#     def format(self, record):
#         fmt = self._level_to_fmt_mapping.get(record.levelno, self._original_fmt)
#         self._style._fmt = fmt
#         return super().format(record)


# @dataclass
# class Log():
#     logger: object
#     level: int = logging.DEBUG
#     handler: logging.Handler = logging.StreamHandler()
#     formatter: logging.Formatter = ColoredLevelFormatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#     )

#     def __post_init__(self):
#         self.logger.setLevel(self.level)
#         self.handler.setFormatter(self.formatter)
#         self.logger.addHandler(self.handler)

#     def __repr__(self):
#         return self.logger
#     # def __getattribute__(self, name):
#     #     return self.logger.__getattribute__(name)




# create console handler and set level to debug
# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)

# create formatter
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
# handler.setFormatter(formatter)

# add ch to logger
# logger.addHandler(handler)

# 'application' code
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warn message")
# logger.error("error message")
# logger.critical("critical message")

# logger.debug(DEFAULT_ENCODING)
# show_vars(logger)
