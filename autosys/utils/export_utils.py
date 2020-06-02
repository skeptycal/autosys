from pathlib import Path
from sys import argv
from typing import Any, Iterable, List


def LOG_PATH(f: str = __name__) -> Path:
    return Path().cwd().resolve() / f


def export(fn: Any) -> Any:
    """ Decorator to export functions and classes. """
    from sys import modules
    mod: Any = modules[fn.__module__]
    if hasattr(mod, "__all__"):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn


def filter_list(d: Iterable = dir(),
                prefix: str = "_",
                whitelist: Iterable = [],
                blacklist: Iterable = []) -> List:
    """ Filter a list with prefix to exclude, whitelist, and blacklist. """
    return [
        x for x in sorted(d) if x in whitelist or (
            (not x.startswith(prefix) and x not in blacklist))
    ]


_EXPORT_BLACKLIST: str = ["arepl_store", "howdoi", "help"]
_EXPORT_WHITELIST: str = ["_debug_", "_log_flag_", "_verbose_"]


def all_export(d: Iterable = dir(),
               prefix: str = "_",
               whitelist: Iterable = _EXPORT_WHITELIST,
               blacklist: Iterable = _EXPORT_BLACKLIST) -> List:
    """ Return a list of all exports not starting with `_` """
    return filter_list(d=d,
                       prefix=prefix,
                       whitelist=whitelist,
                       blacklist=blacklist)


__all__ = all_export()

if __name__ == '__main__':
    print(__all__)