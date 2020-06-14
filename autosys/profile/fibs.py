#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 'Standard Library'
import os

from time import *

from typing import List


def fib_basic(n: int) -> (int, int):
    if n < 2:
        return n
    return fib_basic(n - 1) + fib_basic(n - 2)


if __name__ == "__main__":
    for i in range(20):
        print(i, fib_basic(i))
