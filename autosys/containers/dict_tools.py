#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' dict_tools.py - utilities for Python directories.
    Reference: https://stackoverflow.com/a/26853961
    '''
from sys import version_info
from os import linesep as NL
import timeit

PY_MAJOR: int = version_info.major
PY_MINOR: int = version_info.minor

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
try:
    assert version_info > (3, 5)

    def merge_two_dicts(x, y):
        print('new_version')
        return {**x, **y}

except AssertionError:
    def merge_two_dicts(x, y):
        """Given two dictionaries, merge them into a new dict as a shallow copy."""
        print('old_version')
        z = x.copy()
        z.update(y)
        return z


def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


x = dict(a=1, b=2, c=3)
y = dict(d=4, e=5, f=6)


class TimeItQuick:
    ''' `----------------------------------------------------------------`
        TimeItQuick class - an accurate autoranging execution timer with
        a speed boost multiplier.

        (Use `TimeItQuick.example()` to see examples)
        `----------------------------------------------------------------`
        ```
        import TimeItQuick as t

        # print formatted class instance
        example_timer = TimeItQuick('lambda: {{**x, **y}}')
        print('str value (default): ', example_timer)
        $ str value (default):  0.0536

        # get and print unformatted minimum value from the repeats method
        print(f'repeat method: {example_timer.repeat=}')
        $ repeat method: example_timer.repeat=0.0549292990000001

        # 'on the fly' setup, just to grab the value
        print(t('lambda: {{**x, **y}}'))
        $ 0.0554
        ```
        '''

    def __init__(self, statement='True'):
        self.statement: str = statement
        self.number: int = 20000
        self._repeat: int = 5
        self._autorange: bool = True
        self._quicken: bool = True
        self._speedup: int = 5
        self.DEFAULT_TIMER_NUMBER = 100000
        self.t = timeit.Timer(self.statement)

    @property
    def quicken(self):
        if self._quicken:
            return 1 + self.speedup
        return 1

    @quicken.setter
    def quicken(self, value: bool):
        ''' Set the quicken flag to a bool value. '''
        if isinstance(value, bool):
            self._quicken = value

    @property
    def speedup(self):
        return self._speedup

    @speedup.setter
    def speedup(self, value: int):
        ''' Set an integer speedup value between 0 and 5, inclusive. '''
        if isinstance(value, int):
            if 0 <= value <= 5:
                self._speedup = value
                if value:
                    self.quicken = True

    @property
    def autorange(self):
        if self._autorange:
            return self.t.autorange()[0] // self.quicken
        return self.DEFAULT_TIMER_NUMBER

    @autorange.setter
    def autorange(self, value: bool):
        ''' Set the autorange flag to a bool value. '''
        if isinstance(value, bool):
            self._autorange = value

    @property
    def repeat(self):
        return min(self.t.repeat(repeat=self._repeat, number=self.autorange))

    def __str__(self):
        return f"{self.repeat:.4f}"

    def _doc_it(self):
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
        exec(code)

    def example(self):
        code = '''
# ------------------------------------------------
t = TimeItQuick

# print formatted class instance
example_timer = TimeItQuick('lambda: {**x, **y}')
print('str value (default): ', example_timer)

# get and print unformatted minimum value from the repeats method
print(f'repeat method: {example_timer.repeat=}')

# 'on the fly' setup, just to grab the value
print(t('lambda: {**x, **y}'))
'''
        print(self._doc_it())
        self.code_it(code)


t = TimeItQuick('True')
t.example()

'''
old_version
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_version
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

'''
