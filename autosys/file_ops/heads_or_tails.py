'''
Examples of <head> and <tail> functions
based on Python2 tail example at:
https://docs.python.org/2/library/collections.html
'''

from collections import deque
from os import linesep as NL


def head(filename, n=5):
    'Return the first n lines of a file'
    with open(filename) as fd:
        return fd.read().splitlines()[:n]


def tail(filename, n=5):
    'Return the last n lines of a file'
    with open(filename) as fd:
        return deque(fd.read().splitlines(), n)


def _example():
    n = 10
    s = '-'*40
    print(s)
    print(f'--> head({n})')
    print(NL.join(head('tail.py', n)))
    print(s)
    print(f'--> tail({n}')
    print(s)
    print(NL.join(tail('tail.py', n)))
    print(s)


if False:
    _example()
