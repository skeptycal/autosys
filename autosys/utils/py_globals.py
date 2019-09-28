#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
""" py_globals.py """
# copyright (c) 2019 Michael Treanor
# https://www.github.com/skeptycal
# https://www.twitter.com/skeptycal


def print_all_vars():
    for var in globals():
        # print("%s = %s" % (k, repr(v)))
        print("%s => %s" % (var, globals()[var]))

def get_var_def(v):
    return globals().values() == v

def get_var_value(v):
    # this is a redundant function for testing ... just call 'v' if you want the value of v!
    # it does allow the setting of a default value, which may be handy at times?
    return globals().get(v, 'IDK')

def create_dict_table(*dict, color: str = '') -> str:
    """ Generate a table with ansi borders from a Python dictionary """
    """ works for 2 column Python tables, with width given, at this point """


a = 'this is a'
b = 'b has a number 32'
print('%(a)s    %(b)s' % globals())
print()
# print(globals())
print("return all globals: ")
print(print_all_vars())
print()
print("return the value of the variable who's name is '__doc__': ", get_var_value('__doc__'))
print("return the value of the variable who's name is 'pyglobals.py': ", get_var_value('pyglobals.py'))
print(get_var_def('__doc__'))
print(get_var_def('pyglobals.py'))
