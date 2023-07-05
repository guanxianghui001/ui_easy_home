# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome
@File ：log_util.py
@Author ：huxueyan
@Date ：2023/7/5 15:32
"""
import logging.handlers
import logging
import sys
import datetime


class LogUtil:
    def __init__(self, root, level=None):
        self.log = logging.getLogger()
        self.root = root
        self.set_level(level)

    def set_level(self, level=None):
        # 日志输出到文件
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y/%b/%d-%H:%M:%S")
        handle1 = logging.handlers.RotatingFileHandler(self.root, maxBytes=4096, backupCount=4 ,encoding='utf-8')
        handle1.setFormatter(formatter)
        # 同时输出到屏幕
        handle2 = logging.StreamHandler(stream=sys.stdout)  # sys.stdout标准输出
        handle2.setFormatter(formatter)
        # 将handle加入到log对象中
        self.log.addHandler(handle1)
        self.log.addHandler(handle2)
        # 设置输出级别，不设置无法打出输出
        if level == 'info' or 'INFO' or 'Info':
            self.log.setLevel(logging.INFO)
        elif level == 'warning' or 'WARNING' or 'Warning':
            self.log.setLevel(logging.WARNING)
        elif level == 'error' or 'ERROR' or 'Error':
            self.log.setLevel(logging.ERROR)
        else:
            self.log.setLevel(logging.INFO)  # 无输入时，默认级别

    def info(self, msg):
        self.log.info(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)


if __name__ == '__main__':
    nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print(nowtime)
    root = '/Users/huhu/Documents/apiTest/testCases'
    ro1 = root + '/' + nowtime + '.log'
    print(root)
    log = LogUtil(ro1)
    log.info('22222')
    log.warning('33333')
    log.error('44444')