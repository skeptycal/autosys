#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" usage: twine_setup

Twine Setup.

Usage:
  twine_setup [dist] [-f]

  twine_setup -h | --help
  twine_setup --version

Options:
  dist          Location of dist directory [default: dist/*]
  --force       Force Upload (no test server) [default: False]
  -h --help     Show this screen.
  --version     Show version.

positional arguments:
  dist                  The distribution files to upload to the repository
                        (package index). Usually dist/* . May additionally
                        contain a .asc file to include an existing signature
                        with the file upload.

    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

# cleanup old data
# python3 setup.py clean

# build project:
# python3 setup.py sdist bdist_wheel

# test upload to 'legacy' server
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# upload to live server
# twine upload dist/*
