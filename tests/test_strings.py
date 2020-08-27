from autosys.parse.strings import *


def test_my_list():
    test_lists = [['a', 'b', 'c'], ['1', '2', '3'], [1, 2, 3]]
    assert type(test_lists) == 'list'
