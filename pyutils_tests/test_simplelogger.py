import unittest
import pyutils.simplelogger as logger


class TestSimplelogger(unittest.TestCase):
    def test_hook_info(self):
        """测试 hook_info 功能
        """
        log = "Test hook info"
        default_method = logger.info
        with logger.hook_info(lambda msg: self.assertEqual(msg, log)):
            logger.info(log)
        self.assertEqual(logger.info, default_method)

    def test_hook_warning(self):
        """测试 hook_warning 功能
        """
        log = "Test hook warning"
        default_method = logger.warning
        with logger.hook_warning(lambda msg: self.assertEqual(msg, log)):
            logger.warning(log)
        self.assertEqual(logger.warning, default_method)

    def test_hook_error(self):
        """测试 hook_error 功能
        """
        log = "Test hook error"
        default_method = logger.error
        with logger.hook_error(lambda msg: self.assertEqual(msg, log)):
            logger.error(log)
        self.assertEqual(logger.error, default_method)

    def test_error_raise_exception(self):
        """测试 ErrorRaiseExcpetion 功能
        """
        try:
            logger.ErrorRaiseExcpetion = True
            log = "Test hook error"
            with self.assertRaises(Exception) as e:
                logger.error(log)
            self.assertEqual(str(e.exception), log)
        finally:
            logger.ErrorRaiseExcpetion = False
