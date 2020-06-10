#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Usage:
    err [OPTION]... N

Options:
    -n, --quiet, --silent     suppress most output
    -d, --debug               annotate program execution
    -o file, --output=file    send output to this file
    -l N, --line-length=N     specify the desired line-wrap length
    -z, --null-data           separate lines by NUL characters
    --help                    display this help and exit
    --version                 output version information and exit



err.py - Provides processing, formating, output, and logging for errors.
    Imported module provides the Err class that is used to catch and process errors in python programs.

The CLI version provides lookup information on errors and features for testing/development,
  but is not very functional as an ongoing solution.

AutoSys home page: <https://skeptycal.github.io/autosys/>.
General help using GNU software: <https://www.gnu.org/gethelp/>.
Bug reports and collaboration: <https://github.com/skeptycal/autosys>.

Usage: err [-dhtv] n


    DEFAULT_ARGS: Dict[str, List[Sequence[str]]] = {
        "debug": [
            'Provide debug feedback - not for production use.',
            ['debug', '-d', '--debug'],
        ],
        "help": [
            'Display command information.',
            ['help', '-h', '--help'],
        ],
        "test": [
            'Run test scripts.',
            ['test', '-t', '--test'],
        ],
        "version": [
            'Display version information.',
            ['version', '-v', '--version'],
        ],

"""

import enum
from enum import Enum, auto
from typing import Dict, List, Sequence, Tuple

import sentry_sdk

sentry_sdk.init("https://853c4343706c4a139a7f1c43b7eb2a51@sentry.io/1887434")
sentry_sdk.init(release="as-anansi@0.3.0")

# ! ############# Sentry Test - do not use
# ! division_by_zero = 1 / 0


class CLI:
    """ Command line interface with argument parsing, default values, and """

    from sys import argv
    from docopt import docopt

    # defaults setup from common CLI interfaces
    DEFAULT_ARGS: Dict[str, List[Sequence[str]]] = {
        "debug": [
            "Provide debug feedback - not for production use.",
            ["debug", "-d", "--debug"],
        ],
        "help": ["Display command information.", ["help", "-h", "--help"],],
        "test": ["Run test scripts.", ["test", "-t", "--test"],],
        "version": [
            "Display version information.",
            ["version", "-v", "--version"],
        ],
    }

    # FLAGS_ARGS are autofilled with keys from DEFAULT_ARGS
    FLAGS_ARGS = [f"FL_{k.upper()}" for k in DEFAULT_ARGS.keys()]

    def __init__(self, args):
        super().__init__()
        args = docopt(__doc__, version=f"AutoSys {__version__}")

        ARGS = self.DEFAULT_ARGS

    @classmethod
    def is_arg(cls, arg, test: str) -> bool:
        # if arg[0:1] == '--':
        #     arg = arg[2:]
        args = cls.DEFAULT_ARGS.get(test)
        s = f'Is "{arg}" in {args}? ... {arg in args}'  # type:ignore
        print(s)
        return arg in args  # type:ignore

    @classmethod
    def _add_defaults(cls, d):
        try:
            cls.DEFAULT_ARGS = cls.DEFAULT_ARGS.update(d)
        except:  # noqa
            pass

    @classmethod
    def _load_new_defaults(cls, d):
        try:
            cls.DEFAULT_ARGS = d
        except:  # noqa
            pass


class Err(Enum):
    """ C++ style error messages """

    # setup C++ style error messages
    # reference: Advanced Bash-Scripting Guide
    #   <http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF>

    # from /usr/include/sysexits.h
    # Copyright (c) 1987, 1993
    # The Regents of the University of California.  All rights reserved.
    ERR_OK_ = 0  # successful termination

    # - The Linux Documentation Project has a list of reserved codes that
    #   also offers advice on what code to use for specific scenarios. These
    #   are the standard error codes in Linux or UNIX.

    # some fake errors used for testing:
    TST_NEG_ERROR = -1
    TST_FLOAT_ERROR = 3.14159
    TST_STRING_NUMBER = "42"
    TST_SOME_ERROR = "SOME ERROR"

    ERR_ERROR_ = 1  # catchall for general errors
    ERR_SHELLERR_ = 2  # misuse of shell builtins (BASH)

    ERR__BASE_ = 64  # base value for error messages
    ERR_USAGE_ = 64  # command line usage error
    ERR_DATAERR_ = 65  # data format error
    ERR_NOINPUT_ = 66  # cannot open input
    ERR_NOUSER_ = 67  # addressee unknown
    ERR_NOHOST_ = 68  # host name unknown
    ERR_UNAVAILABL_ = 69  # service unavailable
    ERR_SOFTWARE_ = 70  # internal software error
    ERR_OSERR_ = 71  # system error (e.g., can't fork)
    ERR_OSFILE_ = 72  # critical OS file missing
    ERR_CANTCREAT_ = 73  # can't create (user) output file
    ERR_IOERR_ = 74  # input/output error
    ERR_TEMPFAIL_ = 75  # temp failure; user is invited to retry
    ERR_PROTOCOL_ = 76  # remote error in protocol
    ERR_NOPERM_ = 77  # permission denied
    ERR_CONFIG_ = 78  # configuration error
    ERR__MAX_ = 78  # maximum listed value

    # Linux / Unix codes
    ERR_CANTEXECUTE_ = 126  # command invoked cannot execute
    ERR_NOTFOUND_ = 127  # command not found; possible $PATH error or typo
    ERR_BADARG_ = 128  # invalid argument
    ERR_FATALARG_ = 129  # fatal error
    ERR_CTRL_C_ = 130  # script terminated by Control-C

    def __str__(self):
        a = self.value
        return str(f"Error: {self.name} (code: {self.value})")

    def err_msg(self):
        retval = f"Error "


def path_parts(p):
    return p.split("/")


def test_err():
    # some fake errors used for testing:
    # TST_NEG_ERROR = -1
    # TST_FLOAT_ERROR = 3.14159
    # TST_STRING_NUMBER = '42'
    # TST_SOME_ERROR = 'SOME ERROR'

    script_name = argv[0]
    name = path_parts(script_name)[-1]
    print(name)
    print(f"Testing {name} error codes ...\n\n")

    err_list = ["Err(72)", "Err."]
    errno = Err(72)

    print(errno)
    print(errno.ERR_IOERR_)

    for m in Enum.__dir__(errno):
        # print(m)
        detail = f"enum.Enum.{m}"
        s = f"{detail}"
        print(s)


def main():
    """
    CLI script main entry point.
    """
    print()
    print(FLAGS_ARGS)
    print()
    print(is_arg("--test", "test"))
    print()

    args = argv[1:]
    for arg in args:
        if is_arg(arg, "debug"):
            _DEBUG = True
            args.pop(arg)
        if is_arg(arg, "help"):
            _HELP = True
            args.pop(arg)
        if is_arg(arg, "test"):
            _RUN_TEST = True
            args.pop(arg)
        if is_arg(arg, "version"):
            _RUN_TEST = True
            args.pop(arg)
    if _RUN_TEST:
        test_err()
    else:
        for arg in args:
            s = f"Err({arg})"
            t = eval(s)
            u = f"{t:20}"
            print(s)
            print(u)
            return f"{s}"


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
