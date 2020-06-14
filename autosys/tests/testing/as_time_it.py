# -*- coding: utf-8 -*-
# 'Standard Library'
import time

# 'package imports'
# from autosys.as_trace_it import traceit
from autosys.as_trace_it import traceit

from typing import (
    Any,
    Dict,
    FrozenSet,
    List,
    Sequence,
    Tuple,
)

__all__ = ["timeit"]


def timeit(method):
    """
    Decorator - code timer for comparing and optimizing snippets
    """

    @traceit
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("%r (%r, %r) %2.2f sec" % (method.__name__, args, kw, te - ts))
        return result

    return timed


if __name__ == "__main__":

    @timeit
    def _fake_math_test(n: int = 1000000) -> int:
        loop_list = [2 ** _ for _ in range(n)]
        return sum(loop_list)

    results: List[int] = []
    n: int = 10000
    i: int = 10
    for _ in range(i):
        results.append(_fake_math_test(n))
    # ... run your application ...
