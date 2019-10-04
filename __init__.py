# -*- coding: utf-8 -*-
from __future__ import absolute_import

__version__ = '1.0.2'

# set default package name to parent folder name
name = __file__.split('/')[-2]
__package__ = name

if __name__ == "__main__":
    print()
    print('Debug print values')
    print('******************')
    print()
    print('name        : {:<25.25} '.format(name))
    print('__name__    : {:<15.15} '.format(__name__))
    print('__file__    : {:<45.45} '.format(__file__))
    print('__version__ : {:<15.15} '.format(__version__))
    print('__package__ : {:<25.25} '.format(__package__))
    print()
