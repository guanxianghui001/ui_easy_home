# -*- coding: utf-8 -*-


class ArgumsErrException(Exception):
    """
    自定义异常类，该类为参数错误指定异常
    :key
    """
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        result = '参数异常，请检查传参是否正确'
        return result