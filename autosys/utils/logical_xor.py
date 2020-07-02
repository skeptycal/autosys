#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" logical_xor.py """
# copyright (c) 2020 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal


def logical_xor_so(a, b):
    """ Return True or False based on the truth table below

        | a | b  | xor   |             |
        |---|----|-------|-------------|
        | T | T  | F     |             |
        | T | F  | T     | a and not b |
        | F | T  | T     | not a and b |
        | F | F  | F     |             |

        Python logical or: A or B:
            returns A if bool(A) is True, otherwise returns B
        Python logical and: A and B:
            returns A if bool(A) is False, otherwise returns B

        https://stackoverflow.com/a/432901
        """
    if bool(a) == bool(b):
        return False
    else:
        return a or b


def logical_xor(a, b):
    """ Return True or False based on the truth table below

        | a | b  | xor   |             |
        |---|----|-------|-------------|
        | T | T  | F     |             |
        | T | F  | T     | a and not b |
        | F | T  | T     | not a and b |
        | F | F  | F     |             |

        Python logical or: A or B:
            returns A if bool(A) is True, otherwise returns B
        Python logical and: A and B:
            returns A if bool(A) is False, otherwise returns B
        """
    if a == b:
        return False
    else:
        return a or b


def xor(a, b):
    return (a and not b) or (not a and b)


class Int2(int):
    def __new__(cls, value):
        return super().__new__(cls, value + 42)

    def __xor__(self, other):
        a = self
        b = other
        return 42

    # def __str__(self):
    #     return str(self.value + 42)
    # lambda a, b: (a and not b) or (not a and b)


a = Int2(3)
b = 3
c = 4
d: Int2 = 4

print(d)
print(type(d))
print(dir(d))
print(d ^ 1)

print(a, bool(a), id(a))
print(b, bool(b), id(b))
print(c, bool(c), id(c))

print()
print(logical_xor_so(a, b))
print(logical_xor(a, b))
print(xor(a, b))
print(a ^ b)
print()
print(logical_xor_so(a, c))
print(logical_xor(a, c))
print(xor(a, c))
print()
print(logical_xor_so(c, b))
print(logical_xor(c, b))
print(xor(c, b))
