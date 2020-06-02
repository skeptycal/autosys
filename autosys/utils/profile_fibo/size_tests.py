#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import math
import sys
from sys import stdin

list_of_doubles = [math.sin(x) for x in range(10 * 1000 * 1000)]

for arg in sys.__dir__():
    print(arg)

def main():
    '''
    CLI script main entry point.
    '''
    arg = sys.argv[1]


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
