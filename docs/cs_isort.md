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

### Using isort:

priority of settings:

-   Settings manually passed into the Python SortImports class.
-   Settings manually passed into the command line utility.
-   Settings placed in a setup.cfg file within the project's directory
-   Settings placed in a .isort.cfg file within the project's directory.
-   Settings placed in a .isort.cfg file within the users home directory.
-   Settings placed in a .editorconfig file within the project's directory.
-   Settings placed in a .editorconfig file within the users home directory.

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

# Settings

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

[isort Wiki: full list of settings][wiki]

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

## The `-c` (`--check-only`) option

Check from command line, output to `stderr`, no changes

One great place this can be used is with a pre-commit git hook, such as [this one by @acdha][isort_git_hook]:

## Git hook

To cause the commit to fail if there are isort errors (strict mode), include the following in `.git/hooks/pre-commit`:

    from isort.hooks import git_hook

    if **name** == '**main**':
    sys.exit(git_hook(strict=True))

To display warnings but commit anyway, remove 'strict'

## Setuptools integration

    $ python setup.py isort

or:

    setup(
        name="project",
        packages=["project"],

        setup_requires=[
            "isort"
        ]
    )

source: [isort ReadtheDocs][1]

---

## Full reference of isort settings

Below is a full reference of every setting isort accepts, alongside a basic explanation of its use:

-   force_to_top: Forces a list of imports to the top of their respective section. This works well for handling the unfortunate cases of import dependencies that occur in many projects.

-   skip: A list of files to skip sorting completely.

-   skip_glob: A list of glob patterns to skip sorting completely.

-   not_skip: A list of files to never skip sorting.

-   line_length: An integer that represents the longest line-length you want a single import to take. Defaults to 79.

-   wrap_length: An integer that represents the longest line-length you want when wrapping. If not set will default to line_length.

-   known_future_library: A list of imports that will be forced to display within the future library category.

-   known_standard_library: A list of imports that will be forced to display within the standard library category.

-   known_third_party: A list of imports that will be forced to display within the third party category.

-   known_first_party: A list of imports that will be forced to display within the first party category.

-   virtual_env: Virtual environment to use for determining whether a package is third-party.

-   multi_line_output: An integer that represents how you want imports to be displayed if they're long enough to span multiple lines. A full definition of all possible modes can be found here.

-   forced_separate:- A list of modules that you want to appear in their own separate section. NOTE: This does not work with custom organized sections. For that use known\_{section} instead.

-   indent: An integer that represents the number of spaces you would like to indent by or Tab to indent by a single tab.

-   length_sort: If set to true - imports will be sorted by their length instead of alphabetically.

-   force_single_line: If set to true - instead of wrapping multi-line from style imports, each import will be forced to display on its own line.

-   force_grid_wrap: Force from imports to be grid wrapped regardless of line length, where the value given is the number of imports allowed before wrapping occurs.

-   default_section: The default section to place imports in, if their section can not be automatically determined. FIRSTPARTY, THIRDPARTY, etc.

-   import_heading_future: A comment to consistently place directly above future imports.

-   import_heading_stdlib: A comment to consistently place directly above imports from the standard library.

-   import_heading_thirdparty: A comment to consistently place directly above thirdparty imports.

-   import_heading_firstparty: A comment to consistently place directly above imports from the current project.

-   import_heading_localfolder: A comment to consistently place directly above imports that start with '.'.

-   balanced_wrapping: If set to true - for each multi-line import statement isort will dynamically change the import length to the one that produces the most balanced grid, while staying below the maximum import length defined.

-   order_by_type: If set to true - isort will create separate sections within "from" imports for CONSTANTS, Classes, and modules/functions.

-   atomic: If set to true - isort will only change a file in place if the resulting file has correct Python syntax. This defaults to false because it can only work if the version of code having it's imports sorted is running the same version of Python as isort itself.

-   lines_after_imports: Forces a certain number of lines after the imports and before the first line of functional code. By default this is 2 lines if the first line of code is a class or function. Otherwise it's 1.

-   lines_between_types: Forces a certain number of lines between the two import types (import mylib and from mylib import foo) within a section.

-   combine_as_imports: If set to true - isort will combine as imports on the same line within for import statements. By default isort forces all as imports to display on their own lines.

-   force_adds: If set to true - isort will add imports even if the file specified is currently completely empty.

-   combine_star: If set to true - ensures that if a star import is present, nothing else is imported from that namespace.

-   verbose: If set to true - isort will print out verbose information such as when a file is skipped intentionally or when a file check is successful.

-   settings-path: Can be used from the command line to manually specify the location of a settings file.

-   include_trailing_comma: Will set isort to automatically add a trailing comma to the end of from imports.

-   use_parentheses: Tells isort to use parenthesis for line continuation instead of \ for lines over the allotted line length limit.

-   from_first: If set, from imports will be displayed above normal (straight) imports.

-   case_sensitive: If set, import sorting will take case in consideration when sorting.

-   add_imports: A comma-delimited list of imports to add to every file ran through isort.

-   filter_files: Tells isort to filter files even when they are explicitly passed in as part of the command. This is especially useful to get skip and skip_glob to work when running isort through pre-commit.

-   force_sort_within_sections: If set, imports will be sorted within their section independent to the import_type.

-   force_alphabetical_sort: If set, forces all imports to be sorted as a single section, instead of within other groups (such as straight vs from).

    For example:

        from os import path
        import os

    and not the default behavior of:

        import os
        from os import path

-   reverse_relative: If set, forces relative import to be sorted as Google style guide.

    For example:

        from . import y
        from ..import x

    and not the default behaviour (alphabetical order) of:

        from .. import x
        from . import y

---

[editor_config]: (http://editorconfig.org/)
[isort_rtd]: (https://isort.readthedocs.io/en/latest/)
[isort_git_hook]: (https://gist.github.com/acdha/8717683)
[isort_github_docs]: (https://timothycrosley.github.io/isort/)
[isort_github_repo]: (https://www.github.com/timothycrosley/isort)
[isort_plugins]: (https://github.com/timothycrosley/isort/wiki/isort-Plugins)
[pies]: (https://github.com/timothycrosley/pies)
[wiki]: (https://github.com/timothycrosley/isort/wiki/isort-Settings)
