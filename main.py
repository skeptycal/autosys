#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Part of the `AutoSys` package
        copyright (c) 2019 Michael Treanor
        https://www.github.com/skeptycal/autosys
        https://www.twitter.com/skeptycal

    `AutoSys` is licensed under the `MIT License
        `<https://opensource.org/licenses/MIT>`
    """
import autosys

from autosys import *

import typer

from colorama import Back, Fore, Style


def main(name: str):
    typer.echo(f"{Fore.GREEN}Hello, {Fore.CYAN}{name}")


if __name__ == "__main__":
    typer.run(main)
