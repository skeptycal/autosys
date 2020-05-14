from typing import NamedTuple, Sequence, Tuple
from sys import stdout
from os import linesep as NL, environ as ENV
from platform import platform
from io import TextIOWrapper
from dataclasses import dataclass

from autosys.debug.dbprint import *

PLATFORM = platform()
DEFAULT_COLOR = 'MAIN'


def replace_all(needle: Sequence,
                haystack: Sequence,
                volunteer: Sequence = '') -> Sequence:
    ''' return a sequence with all `needles` in `haystack` replaced with `volunteers` '''
    return ''.join(volunteer if c in needle else c for c in haystack)


def rep_whitelist(needle: Sequence,
                  haystack: Sequence,
                  volunteer: Sequence = '') -> Sequence:
    ''' return a sequence with all `needles` in `haystack` saved and all other characters replaced with `volunteers` '''
    return ''.join(volunteer if c not in needle else c for c in haystack)


def make_safe_id(haystack: Sequence, volunteer: Sequence = '_') -> Sequence:
    ''' return a string that has only alphanumeric and _ characters.
    
        others are replaced with `volunteer` (default `_`) '''
    return ''.join(volunteer if not c.isidentifier() else c for c in haystack)


@dataclass
class FakeLog:
    def _fakelog(self, *args, line_color: str = 'MAIN'):
        args = arg_str(*args)
        fmt = eval(f"color.{line_color}")
        print(f"{fmt}{args}{color.RESET}")

    def info(self, *args):
        ''' placeholder for logging function... '''
        self._fakelog(*args, line_color='BLUE')

    def error(self, *args):
        ''' placeholder for logging function ... '''
        self._fakelog(*args, line_color='WARN')

    def var(self, my_var: str = ''):
        ''' log value of a variable. 
        
            my_var is translated to a safe version before processing.'''
        try:
            my_var = str(my_var)
            evl: Sequence = replace_all(':=/!#;\\', my_var, '_')
            # evl: Sequence = make_safe_id(my_var)
            fmt: str = f"{my_var} | {eval(evl)}"
            self._fakelog(fmt, line_color='RAIN')
        except Exception as e:
            self.error(f'ERROR: {my_var=} | {type(my_var)=} |  {e.args[0]}')


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


color = BasicColors()


@dataclass
class LogColors:
    LC_50: str = color.WARN
    LC_40: str = color.ATTN
    LC_30: str = color.CANARY
    LC_20: str = color.BLUE
    LC_10: str = color.GO

    def str(self):
        print(self.LC_50, f'{self.LC_50}color')


lc = LogColors()

if __name__ == "__main__":
    from pprint import pprint

    def _test_terminal_():

        hr()
        log.var('PLATFORM')
        log.var('term')
        log.var("term.SUPPORTS_COLOR")
        log.var("SUPPORTS_COLOR")
        log.var('term._stream')
        log.var("term._SIZE")
        log.var("term.SIZE")
        log.info(f"Terminal SIZE is set to ({term.cols}, {term.rows})")
        hr()
        print(str(lc))
        print(lc.str())
        print(dir(lc))

        # term._show_debug_info()

    _test_terminal_()
