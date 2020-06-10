#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" AutoSys.py

Usage:
  autosys.py [run|add|del|list|info] <script_name> [-q | -v]
  autosys.py [start|stop|config|test] <service_name> [--args=<args>]
  autosys.py info [--args=<args>]
  autosys.py (-h | --help)
  autosys.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --args=<args>  Arguments to pass along.

 `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`

"""

from docopt import docopt

if __name__ == "__main__":
    test_args: List[str] = [ "--verbose", "--help" ]
    arguments = docopt(__doc__, version=f"AutoSys version{}")
    print(arguments)
docopt(doc, argv=None, help=True, version=None, options_first=False)
