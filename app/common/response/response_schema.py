#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional, Any, Union, Set, Dict

from fastapi.encoders import jsonable_encoder
from pydantic import validate_arguments, BaseModel

_JsonEncoder = Union[Set[Union[int, str]], Dict[Union[int, str], Any]]

__all__ = [
    'ResponseModel',
    'response_base',
    'ResponseBase'
]


class ResponseModel(BaseModel):
    """
    统一返回模型, 可以在 FastAPI 接口请求中使用 response_model=ResponseModel 及更多操作, 前提是当它是一个非 200 响应时
    """
    code: int = 200
    msg: str = 'Success'
    data: Optional[Any] = None

    class Config:
        json_encoders = {
            datetime: lambda x: x.strftime("%Y-%m-%d %H:%M:%S")
        }


class ResponseBase(BaseModel):

    @staticmethod
    def __encode_json(data: Any):
        return jsonable_encoder(
            data,
            custom_encoder={
                datetime: lambda x: x.strftime("%Y-%m-%d %H:%M:%S")
            }
        )

    @staticmethod
    @validate_arguments
    def success(*, code: int = 200, msg: str = 'Success', data: Optional[Any] = None,
                exclude: Optional[_JsonEncoder] = None):
        """
        请求成功返回通用方法

        :param code: 返回状态码
        :param msg: 返回信息
        :param data: 返回数据
        :param exclude: 排除返回数据(data)字段
        :return:
        """
        data = data if data is None else ResponseBase.__encode_json(data)
        return ResponseModel(code=code, msg=msg, data=data).dict(exclude={'data': exclude})

    @staticmethod
    @validate_arguments
    def fail(*, code: int = 400, msg: str = 'Bad Request', data: Any = None, exclude: Optional[_JsonEncoder] = None):
        data = data if data is None else ResponseBase.__encode_json(data)
        return ResponseModel(code=code, msg=msg, data=data).dict(exclude={'data': exclude})

    @staticmethod
    @validate_arguments
    def response_200(*, msg: str = 'Success', data: Optional[Any] = None, exclude: Optional[_JsonEncoder] = None):
        data = data if data is None else ResponseBase.__encode_json(data)
        return ResponseModel(code=200, msg=msg, data=data).dict(exclude={'data': exclude})


# response_base = ResponseBase()
if __name__ == '__main__':
    response_base = ResponseModel()
    response_base1 = ResponseBase.response_200()

    print(response_base)
    print(response_base1)