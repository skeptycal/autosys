import inspect
import unittest


class TestMyName(unittest.TestCase):

    def my_name(self):
        try:
            return inspect.stack()[1][3]
        except:
            return ''

    def test_my_name(self):
        assert self.my_name() == 'test_my_name'

    def test_inspect_stack_unittest(self):
        assert inspect.stack()[0][3] == 'test_inspect_stack_unittest'
        assert inspect.stack()[1][3] == '_callTestMethod'
        assert inspect.stack()[2][3] == 'run'
        assert inspect.stack()[3][3] == '__call__'
        assert inspect.stack()[4][3] == 'runtest'
        assert inspect.stack()[5][3] == 'pytest_runtest_call'
        assert inspect.stack()[6][3] == '_multicall'
        assert inspect.stack()[7][3] == '<lambda>'


def test_inspect_stack_with_pytest():
    assert inspect.stack()[0][3] == 'test_inspect_stack_with_pytest'
    assert inspect.stack()[1][3] == 'pytest_pyfunc_call'
    assert inspect.stack()[2][3] == '_multicall'
    assert inspect.stack()[3][3] == '<lambda>'
    assert inspect.stack()[4][3] == '_hookexec'
    assert inspect.stack()[5][3] == '__call__'
    assert inspect.stack()[6][3] == 'runtest'
    assert inspect.stack()[7][3] == 'pytest_runtest_call'
