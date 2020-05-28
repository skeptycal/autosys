"""

 # TODO - this is a convoluted method ...

it produces this output:
[-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
[-1, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

and seems like a mess
"""
from autosys.text_utils.datetime import _DAYS_BEFORE_MONTH, _DAYS_IN_MONTH
from autosys.profile import autosys_time_it


@time_it
def test_OLD_method_of_populating_DAYS_BEFORE_MONTH():
    _DAYS_BEFORE_MONTH = [-1]
    dbm = 0

    for dim in _DAYS_IN_MONTH[1:]:
        _DAYS_BEFORE_MONTH.append(dbm)
        dbm += dim
    del dbm, dim
    assert _DAYS_BEFORE_MONTH == [
        -1,
        0,
        31,
        59,
        90,
        120,
        151,
        181,
        212,
        243,
        273,
        304,
        334,
    ]
    return _DAYS_BEFORE_MONTH


@time_it
def test_NEW_method_of_populating_DAYS_BEFORE_MONTH():
    _DAYS_BEFORE_MONTH = [-1]
    _DAYS_BEFORE_MONTH.extend(
        [sum(_DAYS_IN_MONTH[1 : -(12 - i)]) for i in range(len(_DAYS_IN_MONTH) - 1)]
    )
    assert _DAYS_BEFORE_MONTH == [
        -1,
        0,
        31,
        59,
        90,
        120,
        151,
        181,
        212,
        243,
        273,
        304,
        334,
    ]
    return _DAYS_BEFORE_MONTH
