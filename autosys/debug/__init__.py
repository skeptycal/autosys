#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
""" GOALS:
    By creating this app, I wanted to answer these questions:

    - What are the internet activities that I use or want most often?
    - What are the things that are feasible, but that I cannot easily do?

    Here is a list of items I came up with. I have solved them to some degree, but any advice or suggestions is welcome. See Contributors document for information.

    1. "Give me the information I want or need to do a better job."
    2. "Store data for later use ... I haven't thought of the question yet."
    3. "Encrypt and Secure data."

    - Create a map of variables, functions, and errors
    - Include links to manual descriptions
    - Convert to a 3d object
    - Create a "developer log" with timestamps in a database
        - Interact with underlying database
        - Used to generate timelines of error tracing
        - "The detective novels of coding."
    - Disable certain features on the fly (decorator?)
    - Disable or interact with certain trackers / loggers
    - Track file io and database io
    - Use this data to "auto-Mock" a database of test features
    - Search for English (or language) words and separate them from tags
    - Test for API functionality
    - Create "auto-API"
    """
if True:  # !------------------------ config
    import logging
    from pathlib import Path
    # from autosys.util import
    from typing import List

    _debug_: bool = True  # True => use Debug features
    _verbose_: int = 0  # Verbosity level => 0 - 4
    _log_flag_: bool = _debug_ and True  # True => log to file

    _DEBUG_COLOR: str = "\x1B[38;5;178m"  # private ansi CLI color code
    _RESET: str = "\x1B[0m"  # private ansi CLI reset code

# if True:  # !------------------------ Debug Utilities

#     def v_name(**var):
#         """ #### Return the name of a keyword variable as a string.

#             Example:
#             ```
#                 the_value = 'some_value'
#                 print(v_name(the_value=the_value))
#             ```

#             This method is 2x faster than f_name (n = 10000)
#             - 'profile_v_name'  4.98 ms
#             - 'profile_f_name'  10.97 ms

#             >(deprecated: f_name()  :  Return the name of a keyword variable as a string. An alternative to using a list comprehension with function <v_name> that manipulates f-strings directly.)
#             """
#         return [_ for _ in var][0]

#     def tryit(func):
#         """ Decorator to wrap function in a try/except block.

#             Will only catch the first error ... best used for short, quick functions...

#             """
#         def tried(*args, **kwargs):
#             try:
#                 result = func(*args, **kwargs)
#             except Exception as e:
#                 log_it(e)
#                 result = "failed..."
#             else:
#                 # print(args)  # TODO <-- your code here
#                 result = "tried..."
#             finally:
#                 dbprint(result)
#             return result

#         return tried

#     def get_class_name(obj, verbose=True):
#         _cls_name: str = obj.__class__.__name__
#         if not verbose:
#             return _cls_name
#         return f"{_cls_name=}"

# if True:  # !------------------------ Logging Utilities

#     def info(*args):
#         logging.info(*args)

#     def log_error(*args):
#         """ Error reporting in debug mode.

#             current (temporary) behavior: print error messages to <stderr> using dbprint. (if _debug_ flag is True)
#             """
#         # TODO - fix temporary functionality
#         if _log_flag_:
#             logging.info(*args)
#             dbprint(*args)  # ! temp

#     def logex(func):
#         """ Decorator to catch and log errors. """
#         if _log_flag_:
#             try:
#                 result = func()
#             except IOError as e:
#                 log_error(
#                     f"logex caused an error while reporting <{func}>: {e}.")
#             else:
#                 if isinstance(result, Exception):
#                     log_error(f"Function <{func}> caught an error: {e}.")
#             finally:
#                 del e

#     def verbose(v: int, *args, **kwargs):
#         """ Print based on '_verbose_' allowed verbosity level.

#             v: int - requested verbosity level
#             """
#         try:  # if _verbose_ constant does not exist, skip this function
#             _verbose_ == 0
#         except NameError:
#             return -1
#         if _verbose_ >= v:
#             if v < 2:
#                 kwargs["file"] = "sys.stdout"
#                 print(*args, **kwargs)
#             elif v == 2:
#                 kwargs["file"] = "sys.stderr"
#                 print(*args, **kwargs)

if True:  # !------------------------ String Utilities

    def isutf8(f):
        # TODO - create a function version of `isutf8 -li *`
        pass

    def read(filename: str, ignore_errors: bool = not _debug_):
        """ Returns the text of `filename`.

            filename: str       - name of file to read and return
            ignore_errors: bool - ignore all errors and return None instead
            """
        dbprint(f"function `read` with args {filename=} and {ignore_errors=}.")
        try:
            file_path = Path(__file__).resolve().parents[0] / filename
            dbprint(f"read from: {file_path}")  # debug
            with open(file_path, encoding=DEFAULT_ENCODING) as f:
                return f.read()
        except (OSError, NameError, TypeError) as e:
            if not ignore_errors:
                return e
        return None


if True:  # !------------------------ CLI display utilities

    def hr(s: str = "-", n: int = 50, print_it: bool = False):
        """ 'hard return' (yes, a dashed line) """
        if not print_it:
            return s * n
        else:
            print(s * n)

    def s80(s: str = "=", n: int = 79, print_it: bool = False):
        return hr(s=s, n=n, print_it=print_it)

    def br(n: int = 1, print_it: bool = False):
        """ yes, a newline inspired by <BR /> 

            n: int = number of blank lines

            set retval=True to return instead of print."""
        return hr(s=' ', n=n, print_it=print_it)

    def db_column_ruler(n: int = 5, cols: int = 79):
        """ Print a column ruler of width 'col'. """
        # dbprint('column ruler col: ', col)
        col = cols // n
        dbprint(f'__width:{col:>d}{s80("_", (col - 1) * 10 - 1)}', sep="")
        dbprint("".join([f"         {i}" for i in range(1, col)]))
        dbprint("")
        dbprint(f"1234567890" * (col))
        dbprint(s80("=", col * 10))

    # def vprint(*args, **kwargs):
    #     for arg in args:
    #         fmt = f"{arg} = {eval(arg)}"  # TODO use ast ...
    #         print(fmt, **kwargs)

    # def show_version():
    #     hr()
    #     print(f"  {__title__} {Path(__file__).name} version {__version__}")
    #     print(f"  {__copyright__}")
    #     print(f"  License: {__license__} --- {__author_email__}")
    #     hr()

    # def _dos(*args: List[str]) -> (str, Exception):
    #     """ Display, log, and return output from a system command. """

    #     # from subprocess import check_output
    #     from tempfile import NamedTemporaryFile
    #     from os.path import curdir

    #     # from os import linesep as NL

    #     if len(args) < 1 or not isinstance(args, List):  # If bad args
    #         e = Exception(
    #             f"Incorrect arguments given: {args}{NL} Use {sys.argv[0]}--help for options."
    #         )
    #         raise e
    #         return e
    #     else:
    #         # !-------------------- good args, try system call
    #         try:
    #             # get system response
    #             result = check_output(args).decode()
    #         except Exception as e:  # bad response
    #             if _verbose_:
    #                 # print, not log, error
    #                 print(e, file=stderr)
    #             raise e  # raise AND return
    #             return e  # in case of 'try'
if True:  # !------------------------ Script Tests

    def _test_err(i):
        hr()
        dbprint(f"{err(2)=}")
        x = ErrC(i)  # once initialized, cannot be changed
        dbprint(f"{x.EX_OK=}")
        dbprint(f"{x.EX_OSERR=}")
        dbprint(f"{x.EX_NOTFOUND=}")
        dbprint("")
        dbprint(f"{err(78)=}")  # to change value, create a new ErrC instance
        dbprint(f"{err(78)=}")
        dbprint(f"{err(69)=}")

        dbprint(f"{x.name} :  {x.value}")
        dbprint("")

    def _test_errc_():
        x = ErrC.EX_CTRL_C
        _test_err(x)
        _test_err(66)
        _test_err(72)
        _test_err(err.EX_NOHOST)

        for errno in ErrC:
            print(f"  {errno.name:15} = {errno.value}")

    def _test_log_():
        logging.basicConfig(filename="example.log", level=logging.DEBUG)
        logging.debug("This message should go to the log file")
        logging.info("So should this")
        logging.warning("And this, too")

    def _tests_():
        """ Debug Tests for script. """
        # COLS, ROWS = _term.
        # db_column_ruler(12, COLS)

        # _test_errc_()
        # show_dis(br)
        br()


def _main_():  # !------------------------ Script Main
    """
    CLI script main entry point.
    """
    if _debug_:
        _tests_()


if __name__ == "__main__":
    # argv.append('version')  # ! test
    # argv.append('help')  # ! test
    term = Terminal()
    print(f"term: {term}")
    print(f"ARGS: {ARGS}")
    if "version" in ARGS:
        show_version()
    else:
        if "help" in ARGS or "debug" in ARGS:
            _debug_ = True
        _main_()
""" Error alternates:

    class _Enum_ish(tuple):
        # alternate Enum:
        # ref: https://stackoverflow.com/a/9201329
        __getattr__ = tuple.index
        __setattr__ = None
        __del__ = None


    class _Enum_like(object):
        # alternate Enum
        # ref: https://stackoverflow.com/a/4092436
        values = []

        class __metaclass__(type):
            def __getattr__(self, name):
                return self.values.index(name)

            def name_of(self, i):
                # There's another handy advantage: really fast reverse lookups:
                return self.values[i]

    """
