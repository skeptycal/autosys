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

    from autosys import *
    print(dir())
    _debug_: bool = True  # True => use Debug features
    _verbose_: int = 0  # Verbosity level => 0 - 4
    _log_flag_: bool = _debug_ and True  # True => log to file

    _DEBUG_COLOR: str = "\x1B[38;5;178m"  # private ansi CLI color code
    _RESET: str = "\x1B[0m"  # private ansi CLI reset code

    # generic script level stderr output characteristics
    _IS_A_TTY: bool = stderr.isatty() and hasattr(stderr, "isatty")
    _IS_PPC: bool = PLATFORM == "Pocket PC"
    _IS_WIN32: bool = PLATFORM == "win32"
    IS_WIN: bool = "win" in PLATFORM.lower()
    _IS_ANSICON: bool = "ANSICON" in ENV
    _IS_WIN_COLOR: bool = _IS_WIN32 and _IS_ANSICON
    _IS_EDGE_CASE: bool = _IS_WIN_COLOR and not _IS_PPC
    SUPPORTS_COLOR = _IS_A_TTY or _IS_EDGE_CASE

    _DB_PREFIX: str = _DEBUG_COLOR * SUPPORTS_COLOR
    _DB_SUFFIX: str = _RESET * SUPPORTS_COLOR
if True:  # !------------------------ Debug Utilities

    def all_export():
        """ Return a list of all globals not starting with '_' """
        yield [x for x in sorted(globals()) if not x.startswith("_")]

    def v_name(**var):
        """ #### Return the name of a keyword variable as a string.

            Example:
            ```
                the_value = 'some_value'
                print(v_name(the_value=the_value))
            ```

            This method is 2x faster than f_name (n = 10000)
            - 'profile_v_name'  4.98 ms
            - 'profile_f_name'  10.97 ms

            >(deprecated: f_name()  :  Return the name of a keyword variable as a string. An alternative to using a list comprehension with function <v_name> that manipulates f-strings directly.)
            """
        return [_ for _ in var][0]

    def tryit(func):
        """ Decorator to wrap function in a try/except block.

            Will only catch the first error ... best used for short, quick functions...

            """

        def tried(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                log_it(e)
                result = "failed..."
            else:
                # print(args)  # TODO <-- your code here
                result = "tried..."
            finally:
                dbprint(result)
            return result

        return tried

    def get_class_name(obj, verbose=True):
        _cls_name: str = obj.__class__.__name__
        if not verbose:
            return _cls_name
        return f"{_cls_name=}"


if True:  # !------------------------ Logging Utilities

    def info(*args):
        logging.info(*args)

    def log_error(*args):
        """ Error reporting in debug mode.

            current (temporary) behavior: print error messages to <stderr> using dbprint. (if _debug_ flag is True)
            """
        # TODO - fix temporary functionality
        if _log_flag_:
            logging.info(*args)
            dbprint(*args)  # ! temp

    def logex(func):
        """ Decorator to catch and log errors. """
        if _log_flag_:
            try:
                result = func()
            except IOError as e:
                log_error(
                    f"logex caused an error while reporting <{func}>: {e}.")
            else:
                if isinstance(result, Exception):
                    log_error(f"Function <{func}> caught an error: {e}.")
            finally:
                del e

    def verbose(v: int, *args, **kwargs):
        """ Print based on '_verbose_' allowed verbosity level.

            v: int - requested verbosity level
            """
        try:  # if _verbose_ constant does not exist, skip this function
            _verbose_ == 0
        except NameError:
            return -1
        if _verbose_ >= v:
            if v < 2:
                kwargs["file"] = "sys.stdout"
                print(*args, **kwargs)
            elif v == 2:
                kwargs["file"] = "sys.stderr"
                print(*args, **kwargs)


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

    def hr(s: str = "-", n: int = 50, retval=False, debug_val=_debug_):
        """ 'hard return' (yes, a dashed line) """
        if retval:
            return s * n
        else:
            if debug_val:
                dbprint(s * n)
            else:
                print(s * n)

    def s80(s: str = "=", col: int = 79, retval=True, debug_val=_debug_):
        return hr(s, col, retval=retval, debug_val=debug_val)

    def br(n: int = 1, retval=False, debug_val=_debug_):
        """ yes, a newline inspired by <BR /> 

            n: int = number of blank lines

            set retval=True to return instead of print."""
        if retval:
            return NL * n
        else:
            if debug_val:
                dbprint(NL * n, end="")
            else:
                print(NL * n, end="")

    def db_column_ruler(n: int = 5, cols: int = 79):
        """ Print a column ruler of width 'col'. """
        # dbprint('column ruler col: ', col)
        col = cols // n
        dbprint(f'__width:{col:>d}{s80("_", (col - 1) * 10 - 1)}', sep="")
        dbprint("".join([f"         {i}" for i in range(1, col)]))
        dbprint("")
        dbprint(f"1234567890" * (col))
        dbprint(s80("=", col * 10))

    def vprint(*args, **kwargs):
        for arg in args:
            fmt = f"{arg} = {eval(arg)}"  # TODO use ast ...
            print(fmt, **kwargs)

    def show_version():
        hr()
        print(f"  {__title__} {Path(__file__).name} version {__version__}")
        print(f"  {__copyright__}")
        print(f"  License: {__license__} --- {__author_email__}")
        hr()

    def _dos(*args: List[str]) -> (str, Exception):
        """ Display, log, and return output from a system command. """

        # from subprocess import check_output
        from tempfile import NamedTemporaryFile
        from os.path import curdir

        # from os import linesep as NL

        if len(args) < 1 or not isinstance(args, List):  # If bad args
            e = Exception(
                f"Incorrect arguments given: {args}{NL} Use {sys.argv[0]}--help for options."
            )
            raise e
            return e
        else:
            # !-------------------- good args, try system call
            try:
                # get system response
                result = check_output(args).decode()
            except Exception as e:  # bad response
                if _verbose_:
                    # print, not log, error
                    print(e, file=stderr)
                raise e  # raise AND return
                return e  # in case of 'try'


if True:  # !------------------------ Classes

    @unique
    class ErrC(IntEnum):  # !------------------------ ErrC Class
        """ #### C-style error messages. 
            Enum where members are also unique ints.

            - Reference: Advanced Bash-Scripting Guide
            <http://tldp.org/LDP/abs/html/exitcodes.html#EXITCODESREF>

            - `from /usr/include/sysexits.h`
            - Copyright (c) 1987, 1993
            - The Regents of the University of California.  All rights reserved.


            >The Linux Documentation Project has a list of reserved codes that also offers advice on what code to use for specific scenarios. These are the standard error codes in Linux or UNIX.

            GOALS:
            By creating this app, I wanted to answer these questions:

            - What are the historical roots of error codes in computing?
            - How can I use industry standard error codes in my programming?
            - How can I use an enum class in python in a useful way?
            """

        EX_OK = (0,)  # successful termination
        EX_ERROR = (1,)  # catchall for general errors
        EX_SHELLERR = (2,)  # misuse of shell builtins; missing keyword
        EX_USAGE = (64,)  # command line usage error
        EX_DATAERR = (65,)  # data format error
        EX_NOINPUT = (66,)  # cannot open input
        EX_NOUSER = (67,)  # addressee unknown
        EX_NOHOST = (68,)  # host name unknown
        EX_UNAVAILABL = (69,)  # service unavailable
        EX_SOFTWARE = (70,)  # internal software error
        EX_OSERR = (71,)  # system error (e.g., cant fork)
        EX_OSFILE = (72,)  # critical OS file missing
        EX_CANTCREAT = (73,)  # cant create (user) output file
        EX_IOERR = (74,)  # input/output error
        EX_TEMPFAIL = (75,)  # temp failure; user is invited to retry
        EX_PROTOCOL = (76,)  # remote error in protocol
        EX_NOPERM = (77,)  # permission denied
        EX_CONFIG = (78,)  # configuration error

        # Linux / Unix codes
        EX_CANTEXECUTE = (126,)  # command invoked cannot execute
        EX_NOTFOUND = (127,)  # command not found; possible $PATH error
        EX_BADARG = (128,)  # invalid argument
        EX_FATALARG = (129,)  # fatal error
        EX_CTRL_C = (130,)  # script terminated by Control-C

    err = ErrC

    class Error(Exception):
        """ Custom Exception handler.

            Generic class for C type error codes and messages
            """

        errno: int
        errmsg: str

        def __init__(self, *args, **kwargs):
            self.with_traceback = True
            self.args = args
            self.kwargs = kwargs
            # dbprint('error')
            # dbprint('args: ', self.args)
            # dbprint('kwargs: ', self.kwargs)
            for kwarg in self.kwargs:
                if kwarg == "errno":
                    self.errno = self.kwargs[kwarg]
                    self.errmsg = [
                        msg for num, msg in ErrC.items() if num == self.errno
                    ]
                    # dbprint(self.errno, ' ', self.errmsg)
                if kwarg == "message":
                    self.message = self.kwargs[kwarg]
            Exception.__init__(self)

    class Terminal:  # !------------------------ Terminal Class
        from io import TextIOWrapper
        DEFAULT_TERMINAL_SIZE: NamedTuple = (80, 24)
        # !------------------------------ initialize

        def __init__(self, stream: TextIOWrapper = stdout):
            super().__init__()
            self._stream = stream
            self._SUPPORTS_COLOR = self._get_supports_color()
            self._size: Tuple[int, int] = self._get_terminal_size()

            if False:
                self._show_debug_info()

        # !------------------------------ properties
        @property
        def cols(self):
            return self._size[0]  # if self._IS_A_TTY else 0

        @property
        def rows(self):
            return self._size[1]  # if self._IS_A_TTY else 0

        @property
        def size(self):
            return self._size

        @property
        def SUPPORTS_COLOR(self):
            return self._SUPPORTS_COLOR

        # !------------------------------ methods

        def __str__(self) -> str:
            return f"Terminal object (Supports color? {self.SUPPORTS_COLOR})"

        def __repr__(self):
            _repr_list = [self.__str__()]
            # ? s += f'Terminal properties:{NL}'
            for p in sorted(dir()):
                if not p.startswith("_"):
                    f = f"{p}"
                    _repr_list.append(f"  {p}: {eval(f)}")
            return NL.join(_repr_list)

        @staticmethod
        def _ioctl_get_win_size(fd: int) -> (Tuple[int, int]):
            """ Return Tuple 'cr' - columns, rows of tty """
            try:
                from fcntl import ioctl
                from struct import unpack
                from termios import TIOCGWINSZ

                retval = unpack("hh", ioctl(fd, TIOCGWINSZ, "1234"))
                info(f"_ioctl_get_win_size returns: {retval=}")
                return int(retval[1]), int(retval[0])
            except Exception as e:
                return e

        def _get_terminal_size(self) -> Tuple[int, int]:
            """ Return terminal size as a tuple(COLS, ROWS).

                Attempts to locate a valid terminal size using various fallback methods.

                Default is 80 columns x 24 lines (rows).

                (uses `dbprint()` for debug output)

                Reference: https://stackoverflow.com/questions/566746/how-to-get-linux-console-window-width-in-python
                """
            import os
            import sys
            from shutil import get_terminal_size as SH_SIZE

            cr: Tuple[int, int] = None

            try:
                cr = (
                    _ioctl_get_win_size(0)
                    or _ioctl_get_win_size(1)
                    or _ioctl_get_win_size(2)
                )
                if cr:
                    info(f"cr from 'or' ioctl's: {cr}")
                    return cr
            except:
                pass
            info(f"no cr from 'or' ioctl's")

            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = _ioctl_get_win_size(fd)
                os.close(fd)
                if cr:
                    info(f"cr from cterm(): {cr}")
                    return cr
            except:
                pass
            info(f"no cr from cterm()")

            try:
                if ENV.get("LINES") and ENV.get("COLUMNS"):
                    cr = (ENV.get("LINES"), ENV.get("COLUMNS"))
                if cr:
                    info(f"env.get returns {cr}")
                    return cr
            except:
                pass
            info(f"no return from env.get")

            try:
                # 'fallback' also sets default if nothing else has worked
                cr = SH_SIZE(fallback=Terminal.DEFAULT_TERMINAL_SIZE)
                if cr:
                    info(
                        f"shutil.get_terminal_size returns ({cr.columns},{cr.lines})")
                    return cr.columns, cr.lines
            except:
                pass
            info("no return from shutil.get_terminal_size")
            info(f"using {Terminal.DEFAULT_TERMINAL_SIZE} for cr")

            return Terminal.DEFAULT_TERMINAL_SIZE[0], Terminal.DEFAULT_TERMINAL_SIZE[1]

        def _get_supports_color(self) -> bool:
            # generic script level stderr output characteristics
            self._IS_A_TTY: bool = self._stream.isatty() and hasattr(
                self._stream, "isatty"
            )
            self._IS_PPC: bool = PLATFORM == "Pocket PC"
            self._IS_WIN32: bool = PLATFORM == "win32"
            self._IS_ANSICON: bool = "ANSICON" in ENV
            self._IS_WIN_COLOR: bool = self._IS_WIN32 and self._IS_ANSICON
            self._IS_EDGE_CASE: bool = self._IS_WIN_COLOR or self._IS_PPC
            self._IS_EDGE_TTY: bool = self._IS_EDGE_CASE and self._IS_A_TTY
            return self._IS_A_TTY or self._IS_EDGE_TTY

        def _show_debug_info(self):
            dbprint("---------------------------------------")
            dbprint("Terminal Properties:")
            dbprint("---------------------------------------")
            dbprint(f"  {self._IS_A_TTY=}")
            dbprint(f"  {self._IS_PPC=}")
            dbprint(f"  {self._IS_WIN32=}")
            dbprint(f"  {self._IS_ANSICON=}")
            dbprint(f"  {self._IS_WIN_COLOR=}")
            dbprint(f"  {self._IS_EDGE_CASE=}")
            dbprint(f"  {self._IS_EDGE_TTY=}")
            dbprint(f"  {self._stream.isatty()=}")
            dbprint(f"  {hasattr(self._stream, 'isatty')=}")
            dbprint("---------------------------------------")

        def out(self, *args, sep=" ", end=NL, flush=False):
            print(*args, sep=sep, end=end, flush=False, file=self.stream)


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

    def _test_terminal_():
        dbprint(f"{PLATFORM=}")
        dbprint("Variable name for _debug_: ", v_name(_debug_="_debug_"))
        dbprint(f"Terminal size is set to ({term.cols}, {term.rows})")

        dbprint(
            "Variable name for SUPPORTS_COLOR: ", v_name(
                SUPPORTS_COLOR=SUPPORTS_COLOR)
        )
        br()
        dbprint(
            f"Python version (sys.version_info): {sys.version_info.major}.{sys.version_info.minor}"
        )
        br()

    def _tests_():
        """ Debug Tests for script. """
        # COLS, ROWS = _term.
        COLS, ROWS = term.size
        # db_column_ruler(12, COLS)

        _test_terminal_()
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
