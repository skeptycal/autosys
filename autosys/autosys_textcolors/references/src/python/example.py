#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" text_colors version 0.8.3 """

from text_colors import color_cycle, color_encode, color_print, py_shell, pyver

SHELL: str = py_shell()
PYVERSION: str = pyver()
PURPLE: str = color_encode("PURPLEHAZE")


def main():
    print()
    print("Python version is: ", PYVERSION)
    print("Python shell is: ", SHELL)
    color_print(PURPLE, "Jimmi sang a fabulous song.")
    color_cycle(17, "CRazy sTuFF is craZY StufF.")
    print()
    print()


main()
