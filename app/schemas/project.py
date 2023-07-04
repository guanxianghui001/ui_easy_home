# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：project.py
@Author ：guanxianghui
@Date ：2023/6/30 15:00 
"""
from typing import Union
from pydantic import BaseModel, Field
from fastapi import Path, Query


class AddProject(BaseModel):
    project_name: Union[str, None] = Field(
        default=None, title="项目名称", max_length=30
    )


class DeleteProject(BaseModel):
    project_name: str


class UpdateProject(BaseModel):
    project_name: str
    id: int = Path(title="项目id", ge=0)
