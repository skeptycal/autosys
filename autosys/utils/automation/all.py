import sys


def public(f):
    """"Use a decorator to avoid retyping function/class names.

        * Blog post by Sam Denton:
        http://code.activestate.com/recipes/576993-public-decorator-adds-an-item-to-__all__/

        * Based on an idea by Duncan Booth:
        http://groups.google.com/group/comp.lang.python/msg/11cbb03e09611b8a

        * Improved via a suggestion by Dave Angel:
        http://groups.google.com/group/comp.lang.python/msg/3d400fb22d8a42e1
        """
    all = sys.modules[f.__module__].__dict__.setdefault('__all__', [])
    if f.__name__ not in all:  # Prevent duplicates if run from an IDE.
        all.append(f.__name__)
    return f


x: int = 2

public(public)  # Emulate decorating ourself
public(x)
