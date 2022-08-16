import re
import unittest
import sys
from pyutils.executor import Executor
from sys import executable
import pyutils.shorthand as sh


class TestExecutor(unittest.TestCase):
    def test_executor_wrap_blank_with_double_quotes(self):
        """测试 executor 自动包装双引号
        """
        executor = Executor(True)
        if sh.is_win() and re.search(r'\s', executable):
            result = executor.execute_straight(executable, ['--version'], ignore_error=True)
            self.assertEqual(result.code, 1)
            result = executor.execute_straight(executable, ['--version'], wrap_blank_with_double_quotes=True)
            self.assertEqual(result.out_str, f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        hello_path = 'tests\\data\\wrap blank\\hello.py'
        hello_result = executor.execute_straight(executable, [hello_path], wrap_blank_with_double_quotes=True, ignore_error=True)
        print("hello_result.error", hello_result.error)
        print("hello_result.code", hello_result.code)
        print("hello_result.out", hello_result.out)
        print("hello_result.out_str", hello_result.out_str)
        self.assertEqual(hello_result.out_str, "hello")
