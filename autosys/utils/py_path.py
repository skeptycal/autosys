#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 'Standard Library'
import sys

from pathlib import Path

from typing import List

PYTHON_PATH = sys.path


def find_python_root(here: str):
    for d in Path(__file__).resolve().parents:
        if Path.exists((d / "README.md")):
            return d
    return None


def check_add_path(here: str):
    import sys

    here_path = Path(here).resolve().parents[0].as_posix()
    if not (here_path in sys.path):
        sys.path.append(here_path)


def listf(
    p: Path,
    pattern: str = "*",
    color: bool = True,
    dirs_first: bool = True,
    options: str = "lAhFp",
) -> List[str]:
    """ Generate file list for ls command.
        p - Path object to search
        pattern - pattern to match (default "*")
        color - use color (default True)
        sort - priority order in [none, alpha, size, owner, classify, type]

        bonus: A Brief History of the 'ls' command
        http://www.tldp.org/LDP/LG/issue48/fischer.html
        """
    for d in p.glob(pattern):
        if d.is_dir():
            details = d.exists() * "*"
            details += d.is_dir() * "/"
            details += d.is_file() * "f"
            details += d.is_symlink() * "l"
            name = d.stem
            ext = d.suffix
            fmt = 'f" {details:<6.6} {name:<15.15} {ext:<5.5}"'
            print(f"{eval(fmt)}")


def ls(p: str = "."):
    print("-" * 50)
    print(f"Path contents of {str(p):<25}")
    print("-" * 50)
    print(listf(Path(p)))
