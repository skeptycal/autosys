timeit_results: List[float] = []


def timeit_init(arg: str = "init") -> bool:
    global timeit_results
    if arg == "init":
        timeit_results = []
    elif arg == "log_on":
        timeit_log = True
    elif arg == "log_off":
        timeit_log = False


class TimeIt(list):
    log: bool = False

    def __init__(self, log_flag: bool = True, print_flag: bool = True):
        self.log_flag = log_flag
        self.print_flag = print_flag

    def reset():
        self.clear()


def timeit(method):
    """
    Decorator - code timer for comparing and optimizing snippets
    """

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        timeit_results.append(te - ts)
        print("%r (%r, %r) %2.2f sec" % (method.__name__, args, kw, te - ts))
        return result

    return timed
