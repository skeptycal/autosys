#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" <<< This is a *fork* of the Python 3.8.3 logging built-in handlers.py >>>
    ##########################################################################
        *** see log/__init__.py for details ***
    ##########################################################################
    #######  Original File Begins Below:
    ##########################################################################
    Copyright 2001-2017 by Vinay Sajip. All Rights Reserved.

    Permission to use, copy, modify, and distribute this software and its
    documentation for any purpose and without fee is hereby granted,
    provided that the above copyright notice appears in all copies and that
    both that copyright notice and this permission notice appear in
    supporting documentation, and that the name of Vinay Sajip
    not be used in advertising or publicity pertaining to distribution
    of the software without specific, written prior permission.

    VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
    INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
    EVENT SHALL VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR
    CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
    USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
    OTHER TORTIOUS ACTION, ARISING OUTOF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
    """
""" Additional handlers for the logging package for Python. The core package is
    based on PEP 282 and comments thereto in comp.lang.python.

    Copyright (C) 2001-2016 Vinay Sajip. All Rights Reserved.

    To use, simply 'import logging.handlers' and log away!
    """

import copy, logging, os, pickle, queue, re, socket, struct, threading, time
from stat import (ST_DEV, ST_INO, ST_MTIME)

#
# Some constants...
#

DEFAULT_TCP_LOGGING_PORT    = 9020
DEFAULT_UDP_LOGGING_PORT    = 9021
DEFAULT_HTTP_LOGGING_PORT   = 9022
DEFAULT_SOAP_LOGGING_PORT   = 9023
SYSLOG_UDP_PORT             = 514
SYSLOG_TCP_PORT             = 514

_MIDNIGHT = 24 * 60 * 60  # number of seconds in a day

class BaseRotatingHandler(logging.FileHandler):
    """
    Base class for handlers that rotate log files at a certain point.
    Not meant to be instantiated directly.  Instead, use RotatingFileHandler
    or TimedRotatingFileHandler.
    """
    def __init__(self, filename, mode, encoding=None, delay=False):
        """
        Use the specified filename for streamed logging
        """
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)
        self.mode = mode
        self.encoding = encoding
        self.namer = None
        self.rotator = None

    def emit(self, record):
        """
        Emit a record.

        Output the record to the file, catering for rollover as described
        in doRollover().
        """
        try:
            if self.shouldRollover(record):
