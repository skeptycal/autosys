# -*- coding: utf-8 -*-
import time
import numpy as np
from time import perf_counter_ns as timer

size_of_vec = 1000


def pure_python_version():
    t1 = timer()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X))]
    return timer() - t1


def numpy_version():
    t1 = timer()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    print(X.shape)
    print(Y.shape)
    Z = X + Y
    return timer() - t1


t1 = pure_python_version()
t2 = numpy_version()
print(f"Time 1: {t1:8}")
print(f"Time 2: {t2:8}")
print()
faster=t1
slower=t2
if t1 > t2:
    faster, slower = slower, faster
print(f"{faster} is {t1 / t2:7.5} % faster than {slower}!")
