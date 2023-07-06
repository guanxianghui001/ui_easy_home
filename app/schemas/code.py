# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：code.py
@Author ：guanxianghui
@Date ：2023/7/6 13:42 
"""
from fastapi import Path, Query
from pydantic import BaseModel, Field


class CodeInfo(BaseModel):
    code_type: int = Path(title="步骤类型", ge=0)