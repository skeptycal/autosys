#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" dict_tools.py - utilities for Python directories.
    Reference: https://stackoverflow.com/a/26853961
    ---
    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

from pathlib import Path
from sys import path as PYTHONPATH
from dataclasses import dataclass, field, Field
from sys import version_info
from os import linesep as NL
import timeit

colors = {
    'K': '\x1b[30m',  # K is black
    'B': '\x1b[34m',  # Blue
    'C': '\x1b[36m',  # Cyan
    'G': '\x1b[32m',  # Green
    'M': '\x1b[35m',  # Magenta
    'R': '\x1b[31m',  # Red
    'W': '\x1b[37m',  # White
    'Y': '\x1b[33m',  # Yellow
    'LK': '\x1b[90m',  # light colors
    'LB': '\x1b[94m',
    'LC': '\x1b[96m',
    'LG': '\x1b[92m',
    'LM': '\x1b[95m',
    'LR': '\x1b[91m',
    'LW': '\x1b[97m',
    'LY': '\x1b[93m',
    'X': '\x1b[0m',  # X is for reset
}

here = Path(__file__).resolve().parent

if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)


@dataclass
class QuickTime:
    ''' QuickTime class - an accurate autoranging execution timer with
        a speed boost multiplier.

        (Use `QuickTime.example()` to see examples)

        ```
        from quicktime import QuickTime as t

        # print formatted class instance
        example_timer = QuickTime('lambda: {{**x, **y}}')
        print('str value (default): ', example_timer)
        $ str value (default):  0.0536

        # get and print unformatted minimum value from the repeats method
        print(f'march method: {example_timer.march=}')
        $ march method: example_timer.march=0.0549292990000001

        # 'on the fly' setup, just to grab the value
        print(t('lambda: {{**x, **y}}'))
        $ 0.0554
        ```
        '''
    number: int = 20000
    statement: str = True
    _repeat: int = 5
    _speedup: int = 5
    _autorange: bool = True
    _quicken: bool = True
    DEFAULT_TIMER_NUMBER: int = field(init=False)

    def __post_init__(self):
        self.t = timeit.Timer(self.statement)
        self.DEFAULT_TIMER_NUMBER = 100000

    @property
    def quicken(self):
        ''' Return the safe speedup multiplier. (not zero)'''
        if self._quicken:
            return 1 + self.speedup
        return 1

    @quicken.setter
    def quicken(self, value: bool):
        ''' Set the quicken flag to a bool value; ignore type errors '''
        self._quicken = bool(value)

    @property
    def speedup(self):
        ''' Return raw speedup multiplier. '''
        return self._speedup

    @speedup.setter
    def speedup(self, value: int):
        ''' Set an integer speedup value between 0 and 5, inclusive.
            Zero represents no speedup, other integers are multipliers. '''
        if isinstance(value, int):
            if 0 <= value <= 5:
                self._speedup = value
                if value:
                    self.quicken = True

    @property
    def autorange(self):
        ''' Return the <number> used that retrieves the best time. '''
        if self._autorange:
            return self.t.autorange()[0] // self.quicken
        return self.DEFAULT_TIMER_NUMBER

    @autorange.setter
    def autorange(self, value: bool):
        ''' Set the autorange flag to a bool value. '''
        self._autorange = bool(value)

    @property
    def march(self):
        ''' Boom! Get the show on the road! This is the main calculation!

            Return the min time from the timeit.repeat function using all
            parameters supplied (or defaults). <Min> is documented to be more appropriate than <average> in most cases. '''
        return min(self.t.repeat(repeat=self._repeat, number=self.autorange))

    def __str__(self):
        return f"{self.march:.4f}"

    def _doc_it(self):
        ''' Format and return class docstring. '''
        doc = self.__doc__.splitlines()
        tmp = []
        tmp.append(f"{colors.get('LG', '')}")
        tmp.extend(doc[:5])
        for line in doc[5:]:
            line = line.strip()
            line = line.replace('#', f"{colors.get('G', '')}#")
            line = line.replace('$', f"{colors.get('C', '')}$")
            tmp.append(f"{line}{colors.get('Y', '')}")
        doc = NL.join(x.strip() for x in tmp)
        doc = doc.replace('`', '')
        return doc

    def code_it(self, code):
        ''' Return the result of executing the code in <code> '''
        return exec(code)

    def example(self):
        ''' Print an example of the quicktime class. '''
        code = '''
        # ------------------------------------------------
        t = QuickTime

        # print formatted class instance
        example_timer = QuickTime('def timer_example():
        ')
        print('str value (default): ', example_timer)

        # get and print unformatted minimum value from the repeats method
        print(f'march method: {example_timer.march=}')

        # 'on the fly' setup, just to grab the value
        print(t('lambda: {**x, **y}'))
        '''
        print(self._doc_it())
        self.code_it(code)


def merge_two_dicts(x, y):
    print('merge')
    try:
        assert version_info > (3, 5)

        def merge_two_dicts_new(x, y):
            print('new_version')
            return {**x, **y}
        return merge_two_dicts_new(x, y)

    except AssertionError:
        def merge_two_dicts_old(x, y):
            """Given two dictionaries, merge them into a new dict as a shallow copy."""
            print('old_version')
            z = x.copy()
            z.update(y)
            return z
        return merge_two_dicts_old(x, y)


def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def main():
    global version_info

    x = dict(a=1, b=2, c=3)
    y = dict(d=4, e=5, f=6)

    t = QuickTime

    version_info = 4
    new = t('merge_two_dicts(x,y)', _autorange=False)
    version_info = 2
    old = t('merge_two_dicts(x,y)', _autorange=False)

    print(old)
    print(new)


if __name__ == '__main__':
    main()


'''
old_version
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_version
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

'''
