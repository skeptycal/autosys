#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://pymotw.com/2/traceback/index.html#module-traceback
The examples below use the module traceback_example.py (provided in the source package for PyMOTW). The contents are:
"""

import dis
import sys
import traceback

"""
Add parens around print arguments
VS Code regex replacement for print function:
    print ([']{1}.*)\n
    print($1)\n
"""

def produce_exception(recursion_level=2): 
    sys.stdout.flush()
    if recursion_level:
        produce_exception(recursion_level-1)
    else:
        raise RuntimeError()

def call_function(f, recursion_level=2):
    if recursion_level:
        return call_function(f, recursion_level-1)
    else:
        return f()

def _show_stack_example():
    traceback.print_stack(file=sys.stdout)

    print('Calling _show_stack_example() directly:')
    _show_stack_example()

    print
    print('Calling _show_stack_example() from 3 levels deep:')
    call_function(_show_stack_example)
 
def show_exception():
    print(('-> print_exc() with no exception:'))
    traceback.print_exc(file=sys.stdout)

    print(())
    try:
        produce_exception()
    except Exception as err:
        print(('-> print_exc():'))
        traceback.print_exc(file=sys.stdout)
        print(())
        print(('-> print_exc(1):'))
        traceback.print_exc(limit=1, file=sys.stdout)

def tb_limit(e: Exception=None, limit=1):
    print('-> print_exc() with no exception:')
    traceback.print_exc(file=sys.stderr)

    try:
        raise # with no 
    except Exception as err:
        print('-> print_exc():')
        traceback.print_exc(limit=5, file=sys.stderr)
        print()
        print('-> print_exc(1):')
        traceback.print_exc(limit=5, file=sys.stderr)

    print(' ->',sep='', end='',file=sys.stderr)
    traceback.print_exc(limit=1,file=sys.stderr)

# show_exception()
# tb_limit()
_show_stack_example() 
