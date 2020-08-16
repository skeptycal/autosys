import inspect


class TestMyName:

    def my_name(self):
        try:
            return inspect.stack()[1][3]
        except:
            return -1

    def test_inspect_stack_calls(self):
        assert inspect.stack()[0][3] == 'test_inspect_stack_calls'
        assert inspect.stack()[1][3] == 'pytest_pyfunc_call'
        assert inspect.stack()[2][3] == '_multicall'
        assert inspect.stack()[3][3] == '<lambda>'
        assert inspect.stack()[4][3] == '_hookexec'
        assert inspect.stack()[5][3] == '__call__'
        assert inspect.stack()[6][3] == 'runtest'
        assert inspect.stack()[7][3] == 'pytest_runtest_call'

    def test_my_name(self):
        assert self.my_name() == 'test_my_name'
