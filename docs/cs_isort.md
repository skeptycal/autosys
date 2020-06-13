# CheatSheet - isort

Author: Timothy Crosley | License: ISC

> isort your python imports for you so you don’t have to.

`isort` is a Python utility/library to sort imports alphabetically, and automatically separated into sections and by type.

GitHub resources: ([docs][isort_github_docs] | [repo][isort_github_repo]).

## Installing isort

### Choose install options:

    pip install isort
    pip install isort[requirements]
    pip install isort[pipfile]
    pip install isort[requirements,pipfile]
    pip install isort[pyproject]

### Using isort from the command line:

    isort mypythonfile.py mypythonfile2.py
    isort -rc .                     # recursive
    isort **/*.py                   # also recursive
    isort mypythonfile.py --diff    # show changes only

### Using isort from within Python:

    import isort
    isort.file("pythonfile.py")

        # or:

    sorted_code = isort.code("import b\nimport a\n")

Several plugins have been written that enable to use isort from within a variety of text-editors. You can find a full list of them on [the isort wiki][wiki].

## How does isort work?

-   works for global imports (not in `try/except` blocks, functions, etc..)
-   removes duplicates
-   groups them alphabetically
-   wraps long lines (default over 80)

## Import types

`isort` groups imports based on type

-   Future
-   Python Standard Library
-   Third Party
-   Current Python Project
-   Explicitly Local (. before import)
-   Custom Separate Sections (in .isort.cfg)
-   Custom Sections (in .isort.cfg)

## Configuring isort

-   `~/.isort.cfg` file
-   `.isort.cfg` file at the root of your project.
-   `isort` section to your project’s `setup.cfg` with any desired settings.
-   use [editorconfig][editor_config] files
    (use a `*.py` section.)

## Settings

```
[settings]
line_length=120
force_to_top=file1.py,file2.py
skip=file3.py,file4.py
known_future_library=future,pies
known_standard_library=std,std2
known_third_party=randomthirdparty
known_first_party=mylib1,mylib2
indent='    '
multi_line_output=3
length_sort=1
forced_separate=django.contrib,django.utils
default_section=FIRSTPARTY
include_trailing_com=True
force_single_line=False
balanced_wrapping=True
length_sort=False
```

[isort Wiki settings][wiki]

## Multi line output modes

### 0 - Grid

    from third_party import (lib1, lib2, lib3,
                             lib4, lib5, ...)

### 1 - Vertical

    from third_party import (lib1,
                             lib2,
                             lib3
                             lib4,
                             lib5,
                             ...)

### 2 - Hanging Indent

    from third_party import \
        lib1, lib2, lib3, \
        lib4, lib5, lib6

### 3 - Vertical Hanging Indent

    from third_party import (
        lib1,
        lib2,
        lib3,
        lib4,
    )

### 4 - Hanging Grid

    from third_party import (
        lib1, lib2, lib3, lib4,
        lib5, ...)

### 5 - Hanging Grid Grouped

    from third_party import (
        lib1, lib2, lib3, lib4,
        lib5, ...
    )

### 6 - Hanging Grid Grouped, No Trailing Comma

    from third_party import (
        lib1, lib2, lib3, lib4,
        lib5
    )

### NOQA (do whatever you want ...)

    from third_party import lib1, lib2, lib3, ...  # NOQA

### Force Single Line

    from third_party import lib1
    from third_party import lib2
    from third_party import lib3
    ...

# Intelligently Balanced Multi-line Imports

Dynamically change the import length to produce the most balanced grid, while staying below the maximum import length defined.

Example:

    from __future__ import (absolute_import, division,
    print_function, unicode_literals)

Will be produced instead of:

    from __future__ import (absolute_import, division, print_function,
    unicode_literals)

# Custom Sections and Ordering

Change the section order

    sections=FUTURE,STDLIB,FIRSTPARTY,THIRDPARTY,LOCALFOLDER

Define your own sections and their order.

    known_django=django
    known_pandas=pandas,numpy
    sections=FUTURE,STDLIB,DJANGO,THIRDPARTY,KNOWN_PANDAS,FIRSTPARTY,LOCALFOLDER

## Auto-comment import sections

    import_heading_stdlib=Standard Library
    import_heading_firstparty=My Stuff

Would lead to output looking like the following:

    # Standard Library

    import os
    import sys

    import django.settings

    # My Stuff

    import myproject.test

## Ordering by import length

    from evn.util import (
        Pool,
        Dict,
        Options,
        Constant,
        DecayDict,
        UnexpectedCodePath,
    )

## Skip processing of imports (outside of configuration)

    import module # isort:skip

or:

    from xyz import (abc, # isort:skip
    yo,
    hey)

or: add `isort:skip_file` to the doc string:

    """ my_module.py
    Best module ever

    isort:skip_file
    """

    import b
    import a

## Adding an import to multiple files

isort makes it easy to add an import statement across multiple files, while being assured it’s correctly placed.

From the command line:

    isort -a "from __future__ import print_function" *.py

## Removing an import from multiple files

isort also makes it easy to remove an import from multiple files, without having to be concerned with how it was originally formatted.

From the command line:

    isort -r "os.system" *.py

## The `--check-only` option

isort can also be used to used to verify that code is correctly formatted by running it with `-c`. Any files that contain incorrectly sorted and/or formatted imports will be outputted to `stderr`.

    isort **/*.py -c -vb

    SUCCESS: /home/timothy/Projects/Open_Source/isort/isort_kate_plugin.py Everything Looks Good!
    ERROR: /home/timothy/Projects/Open_Source/isort/isort/isort.py Imports are incorrectly sorted.

One great place this can be used is with a pre-commit git hook, such as [this one by @acdha][isort_git_hook]:

## Git hook

isort provides a hook function that can be integrated into your Git pre-commit script to check Python code before committing.

To cause the commit to fail if there are isort errors (strict mode), include the following in `.git/hooks/pre-commit`:

    from isort.hooks import git_hook

    if **name** == '**main**':
    sys.exit(git_hook(strict=True))

If you just want to display warnings, but allow the commit to happen anyway, call git_hook without the strict parameter.

## Setuptools integration

Upon installation, isort enables a `setuptools` command that checks Python files declared by your project.

Running `python setup.py isort` on the command line will check the files listed in your `py_modules` and `packages`. If any warning is found, the command will exit with an error code:

    $ python setup.py isort

Also, to allow users to be able to use the command without having to install isort themselves, add isort to the setup_requires of your `setup()` like so:

    setup(
        name="project",
        packages=["project"],

        setup_requires=[
            "isort"
        ]
    )

## Why isort?

isort simply stands for import sort. It was originally called “sortImports” however I got tired of typing the extra characters and came to the realization camelCase is not pythonic.

I wrote isort because in an organization I used to work in the manager came in one day and decided all code must have alphabetically sorted imports. The code base was huge - and he meant for us to do it by hand. However, being a programmer - I’m too lazy to spend 8 hours mindlessly performing a function, but not too lazy to spend 16 hours automating it. I was given permission to open source sortImports and here we are :)

> Thanks and I hope you find isort useful!

> ~Timothy Crosley

---

source: [isort ReadtheDocs][1]

[editor_config]: (http://editorconfig.org/)
[isort_rtd]: (https://isort.readthedocs.io/en/latest/)
[isort_git_hook]: (https://gist.github.com/acdha/8717683)
[isort_github_docs]: (https://timothycrosley.github.io/isort/)
[isort_github_repo]: (https://www.github.com/timothycrosley/isort)
[isort_plugins]: (https://github.com/timothycrosley/isort/wiki/isort-Plugins)
[pies]: (https://github.com/timothycrosley/pies)
[wiki]: (https://github.com/timothycrosley/isort/wiki/isort-Settings)
