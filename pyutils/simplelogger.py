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


def _color_message(message, color_code, bold=False):
    if shd.is_win():
        os.system('')
    result = '\033[{}m{}\033[0m'.format(color_code, message)
    if bold:
        result = '\033[1m' + result
    return result


def _log(message, level=LOG_LEVEL_NORMAL, noident=False, bold=False):
    global LOG_INDENT, LOG_LEVEL

    if LOG_LEVEL is None:
        LOG_LEVEL = int(os.getenv('LoggerLevel', -1))

    if level >= LOG_LEVEL:
        if level == LOG_LEVEL_INFO:
            message = _color_message(message, 0, bold)

        if level == LOG_LEVEL_WARNING:
            message = _color_message('warning: {}'.format(message), 33, bold)

        if level == LOG_LEVEL_ERROR:
            message = _color_message('error: {}'.format(message), 31, bold)

        if level == LOG_LEVEL_SUCCESS:
            message = _color_message('success: {}'.format(message), 32, bold)

        if not shd.is_win():
            message = message.replace('=>', '➜').replace('<=', '✔')

        message += '\n'

        pipe = sys.stdout if level != LOG_LEVEL_ERROR else sys.stderr

        pipe.write(('' if noident else ('\t' * LOG_INDENT)) + message)


def info(message, bold=False):
    _log(message, LOG_LEVEL_INFO, False, bold)


def warning(message, bold=False):
    _log(message, LOG_LEVEL_WARNING, False, bold)


def error(message, bold=False):
    if ErrorRaiseExcpetion:
        raise Exception(message)
    _log(message, LOG_LEVEL_ERROR, False, bold)


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
            if original_func == warning:
                __dict__['warning'] = real_hook_func
            elif original_func == info:
                __dict__['info'] = real_hook_func
            elif original_func == error:
                __dict__['error'] = real_hook_func

        def __exit__(self, exception_type, exception_value, traceback):
            if original_func == warning:
                __dict__['warning'] = original_func
            elif original_func == info:
                __dict__['info'] = original_func
            elif original_func == error:
                __dict__['error'] = original_func
    return Restore()


def hook_info(assertion):
    """给 logger.info 加钩子以检测 info 信息是否符合预期"""
    return __hook__dispatch(assertion, info)


def hook_warning(assertion):
    """给 logger.warning 加钩子以检测 warning 信息是否符合预期

    Args:
        assertion (func(str)->None): 钩子函数

    Returns:
        class Restore: Restore class that can be used in with statement
    """
    return __hook__dispatch(assertion, warning)


def hook_error(assertion):
    """给 logger.error 加钩子

    Args:
        assertion (func(str)->None): 钩子函数

    Returns:
        class Restore: Restore class that can be used in with statement
    """
    return __hook__dispatch(assertion, error)


__dict__ = {
    'info': info,
    'warning': warning,
    'error': error,
    'ErrorRaiseExcpetion': ErrorRaiseExcpetion,
    'hook_info': hook_info,
    'hook_warning': hook_warning,
    'hook_error': hook_error
}
