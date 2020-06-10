#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

import re
from locale import getpreferredencoding
from dataclasses import dataclass
from typing import Dict, Final, List, Tuple
import logging
from autosys.cli.terminal import SUPPORTS_COLOR, BasicColors

DEFAULT_ENCODING: str = getpreferredencoding(True)
DEFAULT_LOG_FORMAT = "%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s"
DEFAULT_LOG_DATE_FORMAT = "%H:%M:%S"
_ANSI_ESCAPE_SEQ = re.compile(r"\x1b\[[\d;]+m")


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

    CRITICAL: str = color.WARN
    ERROR: str = color.ATTN
    WARNING: str = color.CANARY
    INFO: str = color.BLUE
    DEBUG: str = color.GO


log_colors = LogColors()

# from pytest.logging.py
class ColoredLevelFormatter(logging.Formatter):
    """
    Colorize the %(levelname)..s part of the log format passed to __init__.
    """

    LOGLEVEL_COLOROPTS: Mapping[int, AbstractSet[str]] = {
        logging.CRITICAL: {"red"},
        logging.ERROR: {"red", "bold"},
        logging.WARNING: {"yellow"},
        logging.WARN: {"yellow"},
        logging.INFO: {"green"},
        logging.DEBUG: {"purple"},
        logging.NOTSET: set(),
    }  # type: Mapping[int, AbstractSet[str]]
    LEVELNAME_FMT_REGEX: re.Pattern = re.compile(r"%\(levelname\)([+-.]?\d*s)")

    def __init__(self, terminalwriter, *args, **kwargs) -> (None):
        super().__init__(*args, **kwargs)
        self._original_fmt: str = self._style._fmt
        self._level_to_fmt_mapping: Dict[int, str] = {}  # type: Dict[int, str]

        assert self._fmt is not None
        levelname_fmt_match = self.LEVELNAME_FMT_REGEX.search(self._fmt)
        if not levelname_fmt_match:
            return
        levelname_fmt = levelname_fmt_match.group()

        for level, color_opts in self.LOGLEVEL_COLOROPTS.items():
            formatted_levelname = levelname_fmt % {
                "levelname": logging.getLevelName(level)
            }

            # add ANSI escape sequences around the formatted levelname
            color_kwargs: Dict = {name: True for name in color_opts}
            colorized_formatted_levelname = terminalwriter.markup(
                formatted_levelname, **color_kwargs
            )
            self._level_to_fmt_mapping[level] = self.LEVELNAME_FMT_REGEX.sub(
                colorized_formatted_levelname, self._fmt
            )

    def format(self, record):
        fmt = self._level_to_fmt_mapping.get(record.levelno, self._original_fmt)
        self._style._fmt = fmt
        return super().format(record)


@dataclass
class Log:
    logger: logging.Logger = logging.getLogger(__name__)
    level: int = logging.DEBUG
    handler: logging.Handler = logging.StreamHandler()
    formatter: logging.Formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    def __post_init__(self):
        self.logger.setLevel(self.level)
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    # def __getattribute__(self, name):
    #     return self.logger.__getattribute__(name)


logger = Log()
# logger = logging.getLogger(__name__)


# create logger
# logger = logging.getLogger("simple_example")
# logger.setLevel(logging.DEBUG)

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
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")

logger.debug(DEFAULT_ENCODING)
# show_vars(logger)


def show_vars(obj):
    dict_blacklist = (
        []
    )  # ["__doc__", "__module__", "__init__", "__repr__", "__reduce__"]
    for k, v in vars(obj).items():
        if k not in dict_blacklist:
            print(f"  {k:<15.15}: {v}")
            logging.info(f"  {k:<15.15}: {v}")


""" dir(log) =

'addFilter'
'addHandler'
'callHandlers'
'critical'
'debug'
'error'
'exception'
'fatal'
'filter'
'findCaller'
'getChild'
'getEffectiveLevel'
'handle'
'hasHandlers'
'info'
'isEnabledFor'
'log'
'makeRecord'
'manager'
'removeFilter'
'removeHandler'
'root'
'setLevel'
'warn'
'warning'

"""
