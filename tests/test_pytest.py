""" A few simple tests used to check pytest and coverage configuration. """


def __add(a: int, b: int) -> (int):
    return a + b


def test_add():
    for i in range(100):
        a = 3 * i
        b = 4 * i
        assert a + b == __add(a, b)


def test_true():
    """
    Test True
    """
    assert True


def test_false():
    """
    Test False
    """
    assert bool(0) == False


def test_bools():
    sample_true_test_values =\
        [2, 2.3, 'yes', '1', '1.7', __file__, True, (3 > 2)]

    sample_false_test_values = \
        [0, None, '', "", [], {}, (), (2 > 3)]

    for value in sample_false_test_values:
        assert bool(value) == False

    for value in sample_true_test_values:
        assert bool(value) == True
