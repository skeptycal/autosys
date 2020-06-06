#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import time
from collections import deque
from typing import Deque, List  # , Iterator,

# TODO interesting features of patterns of numbers
# when looking for primes, you first do the easy things:
# get rid of even numbers ... well, is there a way to easily
#   and 'cheaply' get rid of numbers divisible by 3?
#   maybe keeping track of the most recent number divisible by 3?
#   maybe ... counting by 3's as you proceed through the loop?
#                      1111111111222222222223333333334
#            01234567890123456789012345678901234567890
#   evens      2 x x x x x x x x x x x x x x x x x x x
#   threes      3  .  x  .  x  .  x  .  x  .  x  .  x
#   fives        45    .    .    .    x    .    x    .
#   ... which I guess amounts to skipping every 6th number?
#   fours are accounted for ...
#   fives? since the even numbers are already gone ... this amounts to
#   figuring out which numbers are divisible by 5, starting at 5 and ...
#   counting by 10's
#   maybe we can take this number, change it to base 3 instead of 2 ...
#   and look to the low bit, just like the binary odd/even test?
#
#   how hard is it to change numbers to prime number bases and count by <base>
#   I bet there are a great many numbers that can be eliminated this way
#   maybe some other way?

# ---------------------------- Utilities


def var_name(*args):
    for arg in args:
        return f"{arg.__name__}"


def timeit(method):
    def timed(*args, **kw):
        s0 = sys.getsizeof(method)
        t0 = time.time()
        result = method(*args, **kw)
        dt = time.time() - t0
        s1 = sys.getsizeof(method)
        print(method.__name__)
        fn = var_name(kw.get("func"))
        # print(func_name)

        # if 'log_time' in kw:
        #     name = kw.get('log_name', method.__name__.upper())
        #     kw['log_time'][name] = int((dt) * 1000)
        # else:
        print(f"{fn:25.25} - {dt*1000:>6.6} \t{'ms':>3.2}")
        return result

    return timed


# ---------------------------- Test Functions
if True:

    def fibonacci(n: int = 2) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def fibonacci_2(n: int = 2) -> int:
        if n > 1:
            return fibonacci(n - 1) + fibonacci(n - 2)
        else:
            return n

    def fibomemo(n: int = 2) -> int:
        memo: List[int] = [0, 1]
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]

    def fibo_deque(n: int = 2) -> int:
        memo: Deque[int] = deque([0, 1], 2)
        for i in range(2, n + 1):
            memo.append(memo[0] + memo[1])
        return memo[-1]

    @timeit
    def fibo_fake_deque(n: int = 2) -> int:
        v1: int = 0
        v2: int = 1
        v3: int = 0
        for i in range(2, n + 1):
            v3 = v1 + v2
            v1 = v2
            v2 = v3
        return v3

    def fibo_fake_deque_2(n: int = 2) -> int:
        v1: int = 0
        v2: int = 1
        v3: int = 0
        for i in range(2, n + 1):
            v3 = v1 + v2
            v1 = v2
            v2 = v3
        return v3

    def fibo_fake_deque_3(n: int = 2) -> int:
        v1: int = 0
        v2: int = 1
        v3: int = 0
        for i in range(2, n + 1):
            v3 = v1 + v2
            v1 = v2
            v2 = v3
        return v3

    # ---------------------------- Caller Functions


@timeit
class Profiler_(list):
    DEFAULT_REPS = 10
    DEFAULT_DURATION = 100
    DEFAULT_MAX_DURATION = 1000

    class Code:
        """ Objects containing code blocks and/or data for a function.

            Code objects contain the following:

            - code           : string or existing function
            - description    : short description used for reporting
            - args           : list of arguments required by the function
            """

        def __init__(self, code, description, args):
            super().__init__()
            self.code = code
            self.description = description
            self.args = Profiler_.arg_list(args)

        def function(self):
            """ Return function with arguments ready to call. """
            return f"{self.code.__name__}({self.args})"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add external functions
        self.clear()

    def add(self, code):
        """ Add a Code object to the profiler list.

            - create Code object
            - add item to test list
            """
        if type(code) == "function":
            c = Code(code, code.__doc__, args)
        if type(code) == str:
            pass
        self.append()

    def add_internal(self, func_list):
        """ Add a list of Code objects to the profiler list.

            - create Code objects from function list
            - add Codes to Profiler list
            """
        for (func, desc, args) in func_list:
            if desc == "doc":
                desc = func.__doc__
            c = Code(func, func.__doc__, args)
            print(func)
            self.append(Code(func))

    def add_external(self, func_list):
        """ Add a list of Code objects to the profiler list.

            - allows addition of outside functions to the profiler
            - uses function objects instead of code snippets
            """
        for code in func_list:
            print(code)
            self.append(Code(code))

    @timeit
    def test_func(self, **kwargs):
        """ Run a function for the purpose of timing the operation.

            - Only keyword arguments <kwargs> are passed.
            - Return value is the normal function retval.
            - Decorator function used for consistent timing and to collate results.
            """
        # remove kwargs used for testing
        func = kwargs.pop("func", None)
        reps = kwargs.pop("reps", 1)

        # repeat tests <reps> times
        for _ in range(reps):
            f = func(**kwargs)
        return f

    def profile(self, func_list, reps=10, **kwargs):
        for func in self:
            self.test_func(func=func, reps=reps, **kwargs)

    @staticmethod
    def arg_list(args):
        return ", ".join(f"{arg}={{{arg}}}" for arg in args)


def main():

    reps: int = 1000
    n: int = 10
    s: str = "test"

    func_list: List[tuple] = [
        (fibonacci, "doc", ["n"]),
        (fibonacci_2, "doc", ["n"]),
        (fibomemo, "doc", ["n"]),
        (fibo_deque, "doc", ["n"]),
        (fibo_fake_deque, "doc", ["n"]),
        (fibo_fake_deque_2, "doc", ["n"]),
    ]

    # TODO: replace fibonacci.__name__
    code = Profiler_.Code(fibonacci, fibonacci.__name__, ["n"])
    print(code)
    print(code.code)
    print(code.description)
    print(code.args)
    print(code.function())


if __name__ == "__main__":
    main()
