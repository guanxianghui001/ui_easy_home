# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：module.py
@Author ：guanxianghui
@Date ：2023/7/4 14:22 
"""
from fastapi import Path, Query
from pydantic import BaseModel, Field


class AddModule(BaseModel):
    name: str = Query(title="模块名称", min_length=2, max_length=30)
    project_id: int = Path(title="项目名称", ge=0)
    father_node_id: int = Path(title="父级id", ge=0)


class SearchModule(BaseModel):
    project_id: int = Path(title="项目名称", ge=0)


class UpdateModule(BaseModel):
    module_name: str
    id: int = Path(title="模块id", ge=0)
