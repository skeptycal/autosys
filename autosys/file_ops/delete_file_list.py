#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'Standard Library'
import pathlib

# remove xxx to use this list
file_list_xxx = [
    "/usr/local/lib/libcdt.la",
    "/usr/local/lib/libcgraph.la",
    "/usr/local/lib/libgcrypt.la",
    "/usr/local/lib/libgpg-error.la",
    "/usr/local/lib/libgvc.la",
    "/usr/local/lib/libgvpr.la",
    "/usr/local/lib/libksba.la",
    "/usr/local/lib/liblab_gamut.la",
    "/usr/local/lib/libnpth.la",
    "/usr/local/lib/libntbtls.la",
    "/usr/local/lib/libpathplan.la",
    "/usr/local/lib/libxdot.la",
]


def del_file_list(file_list):
    for file in file_list:
        p = pathlib.Path(file)
        if p.is_file():
            print(p.name)
            p.unlink()


def main():
    """
    CLI script main entry point.
    """
    del_file_list(file_list=file_list)


if __name__ == "__main__":  # if script is loaded directly from CLI
    main()
