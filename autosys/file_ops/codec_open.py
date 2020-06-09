#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" `AutoSys` package
        copyright (c) 2018 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`


        """

from codecs import open as codec_open
from pathlib import Path

from autosys.log.autosys_logger import *

HERE = Path(__file__).resolve().parent


@log_it
def load_file_contents(file_path, as_list=True):
    """ Load file as string or list.

        Inspiration and portions of `load_file_contents`:
            :copyright: Copyright 2017 Andrew Pinkham
            :website: https://github.com/jambonrose/roman-numerals
            :license: Simplified BSD, see LICENSE_BSD for details.
        """
    # abs_file_path = path.join(HERE, file_path)
    try:
        abs_file_path = HERE / file_path
        d = c
    except:
        try:
            log.error(e)
        except:
            pass
        raise
    with codec_open(abs_file_path, encoding="utf-8") as fp:
        if as_list:
            return fp.read().splitlines()
        return fp.read()


print(load_file_contents("codec_open.py", as_list=False))


""" LICENSE_BSD

 BSD 2-Clause License

 Copyright (c) 2017, Andrew Pinkham
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 """
