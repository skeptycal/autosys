# a quirky import to allow temporary (quick and dirty) debugging
_debug_: bool = True
START: str = "="
MID: str = "-"
END: str = "#"
REPEAT: int = 30


def _debug_it(func):
    global _debug_

    def _debug_it_(*a, **kw):
        global _debug_
        print(START * REPEAT)
        print(f"{a=},  {kw=}")
        try:
            _debug_ = bool(kw.pop("debug"))
            print(f"set _debug_ to: {_debug_}")
        except:
            _debug_ = False
        print(f"{_debug_=}")
        print(a, kw)
        print(MID * REPEAT)
        result = func(*a, **kw)
        print(MID * REPEAT)
        print(f"{_debug_=}")
        print(END * REPEAT)
        return result

    return _debug_it_


@_debug_it
def stuff(number=0, *args, **kw):
    print(f"function number: {number}")
    print(f"  ==> {_debug_=}")
    return number * 5


__all__ = ["_debug_", "_debug_it"]

print(stuff(1, "number 1", debug=False))
print(stuff(0, "number 0", debug=True))
print(stuff(1, "number 1", debug=5))
print(stuff(2, "number2", debug=True))


"""
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        dt = (te - ts) * 1000

        time_list.append({method.__name__: f"{dt:4.4}"})
        dbprint(time_list[-1])
        return (result, dt)

    return timed
"""
