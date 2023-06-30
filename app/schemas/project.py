# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：project.py
@Author ：guanxianghui
@Date ：2023/6/30 15:00 
"""
from typing import Optional
from pydantic import BaseModel


class AddProject(BaseModel):
    project_name: str
