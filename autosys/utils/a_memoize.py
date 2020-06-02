# these functions should be available, but seem to come and go ... so here they are
# /Users/skeptycal/Documents/coding/references/documentation/lib/python3.8/site-packages/pip/_vendor/html5lib/_utils.py
try:
    from html5lib._utils import memoize
except ImportError:
    def memoize(func):
        cache = {}

        def wrapped(*args, **kwargs):
            key = (tuple(args), tuple(kwargs.items()))
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]

        return wrapped

    class MethodDispatcher(dict):
        """Dict with 2 special properties:

        On initiation, keys that are lists, sets or tuples are converted to
        multiple keys so accessing any one of the items in the original
        list-like object returns the matching value

        md = MethodDispatcher({("foo", "bar"):"baz"})
        md["foo"] == "baz"

        A default value which can be set through the default attribute.
        """

        def __init__(self, items=()):
            # Using _dict_entries instead of directly assigning to self is about
            # twice as fast. Please do careful performance testing before changing
            # anything here.
            _dict_entries = []
            for name, value in items:
                if isinstance(name, (list, tuple, frozenset, set)):
                    for item in name:
                        _dict_entries.append((item, value))
                else:
                    _dict_entries.append((name, value))
            dict.__init__(self, _dict_entries)
            assert len(self) == len(_dict_entries)
            self.default = None

        def __getitem__(self, key):
            return dict.get(self, key, self.default)
