import os
import sys

import pyutils.shorthand as shd

######################
######################
#       Log          #
######################
######################

LOG_LEVEL = None
LOG_LEVEL_NORMAL = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_WARNING = 2
LOG_LEVEL_ERROR = 3
LOG_LEVEL_SUCCESS = 4
LOG_LEVEL_NONE = 99
LOG_INDENT = 0
ErrorRaiseExcpetion = False


class SimpleLogger(object):
    @staticmethod
    def _color_message(message, color_code, bold=False):
        if shd.is_win():
            os.system('')
        result = '\033[{}m{}\033[0m'.format(color_code, message)
        if bold:
            result = '\033[1m' + result
        return result

    @staticmethod
    def _log(message, level=LOG_LEVEL_NORMAL, noident=False, bold=False):
        global LOG_INDENT, LOG_LEVEL

        if LOG_LEVEL is None:
            LOG_LEVEL = int(os.getenv('LoggerLevel', -1))

        if level >= LOG_LEVEL:
            if level == LOG_LEVEL_INFO:
                message = SimpleLogger._color_message(message, 0, bold)

            if level == LOG_LEVEL_WARNING:
                message = SimpleLogger._color_message('warning: {}'.format(message), 33, bold)

            if level == LOG_LEVEL_ERROR:
                message = SimpleLogger._color_message('error: {}'.format(message), 31, bold)

            if level == LOG_LEVEL_SUCCESS:
                message = SimpleLogger._color_message('success: {}'.format(message), 32, bold)

            if not shd.is_win():
                message = message.replace('=>', '➜').replace('<=', '✔')

            message += '\n'

            pipe = sys.stdout if level != LOG_LEVEL_ERROR else sys.stderr

            pipe.write(('' if noident else ('\t' * LOG_INDENT)) + message)

    @staticmethod
    def info(message, bold=False):
        SimpleLogger._log(message, LOG_LEVEL_INFO, False, bold)

    @staticmethod
    def warning(message, bold=False):
        SimpleLogger._log(message, LOG_LEVEL_WARNING, False, bold)

    @staticmethod
    def error(message, bold=False):
        if ErrorRaiseExcpetion:
            raise Exception(message)
        SimpleLogger._log(message, LOG_LEVEL_ERROR, False, bold)


def info(message, bold=False):
    SimpleLogger.info(message, bold)


def warning(message, bold=False):
    SimpleLogger.warning(message, bold)


def error(message, bold=False):
    SimpleLogger.error(message, bold)


def __hook__dispatch(assertion, original_func):
    class Restore:
        def __enter__(self):
            def real_hook_func(message, *args):
                """NOTE:ignore any parameters after 'message'

                Args:
                    message (_type_): _description_
                """
                assertion(message)
                original_func(message, *args)
            if original_func == SimpleLogger.warning:
                SimpleLogger.warning = real_hook_func
            elif original_func == SimpleLogger.info:
                SimpleLogger.info = real_hook_func
            elif original_func == SimpleLogger.error:
                SimpleLogger.error = real_hook_func

        def __exit__(self, exception_type, exception_value, traceback):
            if original_func == SimpleLogger.warning:
                SimpleLogger.warning = original_func
            elif original_func == SimpleLogger.info:
                SimpleLogger.info = original_func
            elif original_func == SimpleLogger.error:
                SimpleLogger.error = original_func
    return Restore()


def hook_info(assertion):
    """给 logger.info 加钩子以检测 info 信息是否符合预期"""
    return __hook__dispatch(assertion, SimpleLogger.info)


def hook_warning(assertion):
    """给 logger.warning 加钩子以检测 warning 信息是否符合预期

    Args:
        assertion (func(str)->None): 钩子函数

    Returns:
        class Restore: Restore class that can be used in with statement
    """
    return __hook__dispatch(assertion, SimpleLogger.warning)


def hook_error(assertion):
    """给 logger.error 加钩子

    Args:
        assertion (func(str)->None): 钩子函数

    Returns:
        class Restore: Restore class that can be used in with statement
    """
    return __hook__dispatch(assertion, SimpleLogger.error)
