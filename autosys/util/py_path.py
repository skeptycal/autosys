#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
from pathlib import Path
from typing import List

sys.
print(sys.path)


def listf(
    p: Path,
    pattern: str = "*",
    color: bool = True,
    dirs_first: bool = True,
    options: str = "lAhFp",
) -> List[str]:


"""
p - Path object to search
pattern - pattern to match (default "*")
color - use color (default True)
sort - priority order in [none, alpha, size, owner, classify, type, ]

bonus: A Brief History of the 'ls' command
http://www.tldp.org/LDP/LG/issue48/fischer.html
"""
for d in p.glob(pattern):
    if d.is_dir():
        details = d.exists()
        name = d.stem
        ext = d.suffix
        fmt = 'f" {details} {name:<10.10} {ext:<5.5}"'
        print(f"{eval(fmt)}")


def ls(p):
    print("-" * 50)
    print(p)
    print("-" * 50)
    print(dirlist(Path(p)))

    for d in Path(p).glob("*"):
        if not d.is_dir():
            details = d.exists()
            name = d.stem
            ext = d.suffix
            fmt = 'f" {details} {name:<10.10} {ext:<5.5}"'
            print(f"{eval(fmt)}")


for p in sys.path:
    print(ls(p))

"""
comment
"""
