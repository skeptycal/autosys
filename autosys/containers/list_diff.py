# 'package imports'
from autosys.text_utils.random_string import *

from typing import (
    List,
    Sequence,
)


def difference(a: Sequence, b: Sequence) -> (List):
    """ Return a list of items from `a` that are not in `b`.
    """
    return [item for item in set(a) if item not in set(b)]


a = [random_string() for i in range(100)]
b = [random_string() for i in range(100)]

# for i in dir():

# print(i)

print(dir())
