#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import uuid


def get_uuid() -> str:
    """
    生成uuid

    :return: str(uuid)
    """
    return str(uuid.uuid1())


def get_current_timestamp() -> float:
    """
    生成当前时间戳

    :return:
    """
    return datetime.datetime.now().timestamp()


if __name__ == '__mian__':
    a = get_uuid()
    print(a)
