#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """


# 'Standard Library'
# !---------------------------------------------- Imports
# from autosys import *
import pathlib

# 'package imports'
from autosys.debug import db_column_ruler, dbprint

# !---------------------------------------------- CONSTANTS
_debug_: bool = True  # True => use Debug features
SCRIPT_PATH: str = pathlib.Path(__file__).resolve().parents[0].as_posix()
PARENT_PATH: str = pathlib.Path(__file__).resolve().parents[1].as_posix()

# !---------------------------------------------- String Utilities


def set_script_in_sys_path():
    """ Put this script in the system path if it is not. """
    dbprint(f"SCRIPT_PATH: {SCRIPT_PATH}")
    dbprint(f"PARENT_PATH: {PARENT_PATH}")
    br()

    if SCRIPT_PATH not in sys.path:
        sys.path.insert(0, SCRIPT_PATH)
        try:  # skip debug output if not available
            dbprint(f"SCRIPT_PATH *NOT* in sys.path.")
        except:
            pass
    else:
        try:  # skip debug output if not available
            dbprint(f"SCRIPT_PATH *IS* in sys.path.")
        except:
            pass


def _tests_():
    """ Debug Tests for script. """
    br()

    db_column_ruler(8)
    br()

    dbprint(f"Rows: {ROWS} x Columns:{COLS}")
    br()

    dbprint(
        f"Python version (sys.version_info): {sys.version_info.major}.{sys.version_info.minor}"
    )
    dbprint("Script version (__version__):     ", __version__)
    br()

    dbprint(f"SYS.PATH: ")
    for p in sys.path:
        dbprint(f"    {p}")
    br()


def main():
    """
    CLI script main entry point.
    """
    set_script_in_sys_path()
    if _debug_:
        _tests_()


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
