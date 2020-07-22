#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """

# example json logger
# https://www.datadoghq.com/blog/python-logging-best-practices/

from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
