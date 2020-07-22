# Ref: https://wiki.python.org/moin/PythonSpeed/PerformanceTips

# Only if you are using older versions of Python (before 2.4) does the following advice from Guido van Rossum apply:

# An alternative way to speed up sorts is to construct a list of tuples whose first element is a sort key that will sort properly using the default comparison, and whose second element is the original list element. This is the so-called Schwartzian Transform, also known as DecorateSortUndecorate(DSU).

# Suppose, for example, you have a list of tuples that you want to sort by the n-th field of each tuple. The following function will do that.


def sortby(somelist, n):
    nlist = [(x[n], x) for x in somelist]
    nlist.sort()
    return [val for (key, val) in nlist]


# Matching the behavior of the current list sort method (sorting in place) is easily achieved as well:


def sortby_inplace(somelist, n):
    somelist[:] = [(x[n], x) for x in somelist]
    somelist.sort()
    somelist[:] = [val for (key, val) in somelist]
    return
