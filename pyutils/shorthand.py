######################
######################
#       操作系统      #
######################
######################


import os
import sys


def is_win():
    return sys.platform.lower().startswith('win')


def is_macOS():
    return sys.platform.lower().startswith('darwin')
