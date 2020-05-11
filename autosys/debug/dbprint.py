from autosys import NL, stderr, stdout
from typing import List


def arg_str(*data, arg_sep: str = "", **kwargs):
    """ Return string from an iterable of variously typed arguments. Each item is converted separately so

        data: iterable - iterable containing items
        sep: str  - separator between list items

        Errors in types and formatting are ignored.
        """
    tmp: List[str] = []
    if len(data) == 0 or data == None:
        return ""

    # weed out values that do not convert to str cleanly
    for item in data:
        try:
            tmp.append(str(item))
        except (AttributeError, TypeError, ValueError, IndexError) as e:
            pass  # ignore errors

    # convert list to str and return
    try:
        return arg_sep.join(data)
    except (AttributeError, TypeError, ValueError, IndexError) as e:
        return ""  # return valid string even if errors present


def dbprint(*db_args, sep=" ", end=NL, file=stderr, flush=False):
    """ Prints debug messages if _debug_ flag is True.

        The default <sep> and <end> are empty strings which allows for easier custom formatting. Change the defaults as needed.

        Example:
        ```py
        if arg == '--version':
            dbprint(f"anansi.py version {Ansi.lime}{__version__}.")
        ```
        """
    if _debug_:
        # PREFIX    args    SUFFIX   Newline
        print(
            f"{_DB_PREFIX}{arg_str(*db_args)}{_DB_SUFFIX}",
            sep="",
            end=end,
            file=file,
            flush=flush,
        )
