# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：scene.py
@Author ：guanxianghui
@Date ：2023/7/6 13:49 
"""
from fastapi import Path, Query
from pydantic import BaseModel, Field
from typing import Union

class AddScene(BaseModel):
    project_id: int = Path(title="项目id", ge=0)
    name: str = Query(title="场景名称", min_length=2, max_length=30)
    description: Union[str, None] = Query(title="描述信息", max_length=200)
    module_id: Union[int, None] = Query(title="模块id", ge=0)

