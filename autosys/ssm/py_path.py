# -*- coding: utf-8 -*-

import os
from os import path, environ, pathsep, linesep
import sys


def print_os_path(arg):
    """ Print path list in newline 'list' format. """
    print(*arg.split(pathsep), sep=linesep)


if __name__ == "__main__":
    print_os_path(environ['PYTHONPATH'])
    print_os_path(path)
    # print(path)
    # print(dir(os))

    # print('{:<12.12} : {:<25.25}'.format('function:', 'type:'))
    # for function in dir(os):
    #     print(function, type(function))
    # print("{:<10.10} : {:<25.25}".format(function, type(function)))
