# autosys Changelog

## UNRELEASED

-   Finalize Python 3.9 support
-   Move to automated git submodules
-   docopt support
-   C and C++ extension support
-   data pipeline support
-   Redo Sphinx documentation

## autosys 0.5.2

-   Add more pytest tests
-   Update pytest and tox config

## autosys 0.5.1

-   Change to pyproject.toml
-   Change to poetry instead of setup.py
-   Move project metadata to pyproject.toml
-   Move mypy settings to pyproject.toml

## autosys 0.5.0

-   Remove support for python < 3.8
-   package_metadata has more info and utilities
-   Begin support for PEP 590, Vectorcall: a fast calling protocol for CPython
-   Begin C and C++ extension support

## autosys 0.4.5

-   Refactor Setup to include sphinx and package_metadata
-   streamline CI path (add Azure and Github hooks)
-   added twine_setup script file to run twine outside of setup.py

## autosys 0.4.4

-   Refactor all code by category
-   Continue Python 3.9 support testing
-   Finalize Python 3.8 support
-   Remove support for python < 3.8
-   Python 3.8 features driving the deprecation of Python < 3.8
    -   Parallel filesystem cache for compiled bytecode
    -   f-strings support a handy = specifier for debugging
    -   multiprocessing can now use shared memory segments
    -   Typing-related: PEP 591 (Final qualifier)
    -   PEP 586 (Literal types)
    -   PEP 589 (TypedDict)
    -   and, yes, just a few (PEP 572) assignment expressions

## autosys 0.4.3

-   Begin Python 3.9 support
-   Continue Python 3.8 support
-   Deprecate support for python < 3.8

## autosys 0.4.2

-   Add Python 3.7 and 3.8 support
-   Remove support for end-of-life Pythons 2.x, 3.2, and 3.3

## autosys 0.4.1

-   Don't import autosys from setup.py
-   Dev Release. Not Stable

## autosys 0.3.0

-   Add file_ops
-   Add Implore

## autosys 0.2.0

-   add data and profiling sections
-   add logging

## autosys 0.1.0

-   CLI features, including ANSI color text
