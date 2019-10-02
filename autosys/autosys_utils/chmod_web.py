#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
# chmod_web.py
#
# Setup standard file permissions in current directory (for typical web server)
# - Changes all file_names (recursively!) to chmod 644
# - Changes all directories (recursively!) to chmod 755
###############################################################################

import os
from pathlib import Path
from typing import List

import text_colors

color_encode = text_colors.color_encode
cp = text_colors.color_print

# def color_encode(fg_color, bg_color, flags_color)
# def color_print(color_code, *args, **kwargs):
RED = color_encode("RED", "COLOR230", "ITALIC")
MAIN = color_encode("MAIN", "BG_BLACK", "ITALIC")


def chmod_web(path: str = ".") -> List[str]:
    """ Set standard permissions for web directories:
            - all directories 755
            - sall files 644
            Returns a list of errors.  """
    error_list: List = []
    p = Path("path").resolve()
    # p.chmod(p.stat().st_mode | stat.S_IEXEC)
    if not p.exists():
        error_list.append(path)
    else:
        for d in p.rglob("*.*"):
            if d.is_dir():
                try:
                    d.chmod(0o755)
                except OSError:
                    error_list.append(d)
            else:
                try:
                    d.chmod(0o644)
                except OSError:
                    error_list.append(d)

    return error_list

    # p=pathlib.Path(".")
    # for dir_path, dir_names, file_names in os.walk(path):
    #     for dir_name in dir_names:
    #         tmp = os.path.join(dir_path, dir_name)
    #         try:
    #             os.chmod(tmp, 0o755)
    #         except OSError as e:
    #             error_list.append(tmp)
    #             cp(RED, "The permissions for directory", tmp,
    #                "could not be changed.")
    #         else:
    #             cp(MAIN, "The permissions for directory", tmp,
    #                "were set to 755.")

    # for file_name in file_names:
    #     tmp = os.path.join(dir_path, file_name)
    #     try:
    #         os.chmod(tmp, 0o644)
    #     except OSError as e:
    #         error_list.append(tmp)
    #         cp(RED, "The permissions for file", tmp,
    #            "could not be changed.")
    #     else:
    #         cp(MAIN, "The permissions for file", tmp,
    #            "were set to 644.")
    # return error_list


if __name__ == "__main__":
    # TEST SAMPLE to use if script is run from the command lines
    # if
    result = chmod_web(".")
    if result != []:
        cp(
            MAIN,
            "Permissions for the following files or directories could not be modified:",
        )
        print()
        for s in result:
            cp(MAIN, s)
    else:
        cp(MAIN, "Permissions successfully modified.")


###############################################################################
# - Tested on macOS version ...
# ProductName:	Mac OS X
# ProductVersion:	10.14.3
# BuildVersion:	18D109
# 13-Feb-2019
#
# @author    Michael Treanor  <skeptycal@gmail.com>
# @copyright (c) 2019 Michael Treanor
# @license   MIT <https://opensource.org/licenses/MIT>
# @link      http://www.github.com/skeptycal
#
# Inspired by https://superuser.com/questions/234647/how-to-remove-executable-bit-recursively-from-files-not-directories
###############################################################################
