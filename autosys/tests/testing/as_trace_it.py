# -*- coding: utf-8 -*-
import linecache
# import logging
# import os
import tracemalloc  # 3.4
from typing import Any, Dict, FrozenSet, List, Sequence, Tuple


def trace_init():
    tracemalloc.start()


def trace_snap() -> tracemalloc.Snapshot:
    return tracemalloc.take_snapshot()


def display_top(snapshot: tracemalloc.Snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


def trace_top10(snapshot: tracemalloc.Snapshot):
    top_stats = snapshot.statistics('lineno')
    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)


def traceit(method):
    """
    Decorator - code timer for comparing and optimizing snippets
    """
    def traced(*args, **kw):
        tracemalloc.start()
        result: Any = method(*args, **kw)
        snapshot = tracemalloc.take_snapshot()
        print(f"... TraceIt : {method.__name__} {args} {kw}...")
        # trace_top10(snapshot)
        # display_top(snapshot)
        top_stats = snapshot.statistics('lineno')
        print(top_stats)
        return result

    return traced

# def trace_stats(snapshot: Snapshot, filename: str = 'trace_log.log'):
#     for i, stat in enumerate(snapshot.statistics(filename)[:5], 1):
#         logging.info(“top_current”, i=i, stat=str(stat))


@traceit
def _fake_math_test(n: int = 1000) -> int:
    return 2 ** i


if __name__ == "__main__":
    results: List[int] = []
    n: int = 10
    for i in range(n):
        results.append(_fake_math_test(i))
    # ... run your application ...
