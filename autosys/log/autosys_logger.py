#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package - utilities for macOS apps
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

from locale import getpreferredencoding
from dataclasses import dataclass
from typing import Dict, Final, List, Tuple
import logging
from autosys.cli.terminal import SUPPORTS_COLOR, BasicColors

DEFAULT_ENCODING: str = getpreferredencoding(True)


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

    def str(self):
        print(self.LC_50, f"{self.LC_50}color")


log_colors = LogColors()


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
