#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Examples of scopes and tests to show results of scope changes
    between global, local, and nonlocal scopes. """


def scope_test():
    def do_local():
        spam = "local spam (l in l)"
        print("In local env: ", spam)
        print("local var is printed")
        print(f"{id(spam)=}")

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam (n in l)"
        print("In local env: ", spam)
        print(f"{id(spam)=}")

    def do_global():
        global spam
        spam = "global spam (g in l)"

    spam = "test spam(l in l ... in scope_test)"
    print("Before: ", spam)
    print()

    # spam assigned to "local spam" in local env
    do_local()
    print("After local assignment:", spam)
    print()

    # spam assigned to "nonlocal spam" as nonlocal var
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    print()

    # spam assigned to "local spam" in local env
    do_global()
    print("After global assignment:", spam)
    print()


# ? ------------------------ tests

spam: str = "initial spam (g in g)"
print("Initial spam (global in global env): ", spam)
scope_test()
print("In global scope:", spam)
print(
    """The global variable was carried into the 'scope_test'
      function, changed to (l in l), """
)
