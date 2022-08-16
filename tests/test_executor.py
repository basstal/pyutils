import unittest

from pyutils.executor import Executor


class TestExecutor(unittest.TestCase):
    def test_executor_wrap_blank_with_double_quotes(self):
        """测试 executor 自动包装双引号
        """
        program = 'C:\\Program Files\\Python37\\python.exe'
        executor = Executor(True)
        result = executor.execute_straight(program, ['--version'], ignore_error=True)
        self.assertEqual(result.code, 1)
        self.assertTrue("'C:\\Program'" in result.error)
        result = executor.execute_straight(program, ['--version'], wrap_blank_with_double_quotes=True)
        self.assertEqual(result.out_str, "Python 3.7.0")
        hello_path = 'E:\\Documents\\git-repository\\basstalpyutils\\tests\\data\\wrap blank\\hello.py'
        hello_result = executor.execute_straight(program, [hello_path], wrap_blank_with_double_quotes=True, ignore_error=True)
        self.assertEqual(hello_result.out_str, "hello")
