#!/usr/bin/env python
# grep_some_condition.py
# https://stackoverflow.com/a/5463419

# import fileinput
from typing import Dict, List


def protected_exec(code: str):
    """ Restrict access to only ['__builtins__'] for code execution. """
    return exec(code, {})


def limited_exec(code: str, global_dict: Dict = {}):
    """ Restrict access to only `global_dict` for code execution. 

        The default global_dict of {} restricts access to only ['__builtins__'] for code execution.

        e.g. 
        limited_exec("print(factorial(5))", {"factorial": factorial})

        # https://www.geeksforgeeks.org/exec-in-python/
        """
    return exec(code, global_dict)


def remove_lines(
    test_condition='line.startswith("#TT")', inplace=True, backup=".bak"
):
    for line in fileinput.input(inplace=inplace, backup=backup):
        if line.startswith("#TT"):
            print(line),  # this goes to the current file


def remove_inplace(filenames: List[str]):
    try:
        import in_place
    except ImportError as e:
        raise ImportError("module <in_place> was not imported correctly", e)
    else:
        with in_place.InPlace(filenames) as file:
            for line in file:
                line = line.replace("test", "testZ")
                file.write(line)


remove_inplace('line.startswith("#ST")')


""" alternative to `fileinput`

    fileinput module has very ugly API, I find beautiful module for this task - in_place, example for Python 3:

    import in_place

    with in_place.InPlace('data.txt') as file:
        for line in file:
            line = line.replace('test', 'testZ')
            file.write(line)
    main difference from fileinput:

    Instead of hijacking sys.stdout, a new filehandle is returned for writing.
    The filehandle supports all of the standard I/O methods, not just readline().
    """
