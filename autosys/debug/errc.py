from enum import IntEnum, unique


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

    EX_OK = (0, )  # successful termination
    EX_ERROR = (1, )  # catchall for general errors
    EX_SHELLERR = (2, )  # misuse of shell builtins; missing keyword
    EX_USAGE = (64, )  # command line usage error
    EX_DATAERR = (65, )  # data format error
    EX_NOINPUT = (66, )  # cannot open input
    EX_NOUSER = (67, )  # addressee unknown
    EX_NOHOST = (68, )  # host name unknown
    EX_UNAVAILABL = (69, )  # service unavailable
    EX_SOFTWARE = (70, )  # internal software error
    EX_OSERR = (71, )  # system error (e.g., cant fork)
    EX_OSFILE = (72, )  # critical OS file missing
    EX_CANTCREAT = (73, )  # cant create (user) output file
    EX_IOERR = (74, )  # input/output error
    EX_TEMPFAIL = (75, )  # temp failure; user is invited to retry
    EX_PROTOCOL = (76, )  # remote error in protocol
    EX_NOPERM = (77, )  # permission denied
    EX_CONFIG = (78, )  # configuration error

    # Linux / Unix codes
    EX_CANTEXECUTE = (126, )  # command invoked cannot execute
    EX_NOTFOUND = (127, )  # command not found; possible $PATH error
    EX_BADARG = (128, )  # invalid argument
    EX_FATALARG = (129, )  # fatal error
    EX_CTRL_C = (130, )  # script terminated by Control-C


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
