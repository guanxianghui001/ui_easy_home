# -*- coding: UTF-8 -*-
"""
@Project ：ui_easy_home
@File ：project_operation.py
@Author ：guanxianghui
@Date ：2023/6/30 10:31
"""
import time
from datetime import datetime

from sqlmodel import SQLModel, Field, create_engine, Session, select
from app.common import snow
from app.conf import config
from app.conf.config import *
from app.utils.generate_string import get_current_timestamp

# 数据库连接
DATABASE_URL = config.project_table  # 确保在 config 中有这个 URL
engine = create_engine(f'mysql+pymysql://root:Qa123456@localhost:3306/ui_easy_home?charset=utf8')

class Project(SQLModel, table=True):
    id: int = Field(default_factory=lambda: snow.IdWorker(1, 2, 0).get_id(), primary_key=True)
    name: str
    is_del: int = Field(default=0)
    create_time: str = Field(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    update_time: str = Field(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def add_projects(project_name: str):
    with Session(engine) as session:
        if not session.exec(select(Project).where(Project.name == project_name, Project.is_del == 0)).first():
            project = Project(name=project_name)
            session.add(project)
            session.commit()
            return project.id, project.name
        else:
            return False

def search_project():
    with Session(engine) as session:
        projects = session.exec(select(Project).where(Project.is_del == 0)).all()
        return [project.model_dump() for project in projects]

def delete_projects(project_name: str):
    with Session(engine) as session:
        project = session.exec(select(Project).where(Project.name == project_name, Project.is_del == 0)).first()
        if project:
            project.is_del = 1
            session.add(project)
            session.commit()
            return True
        else:
            return False

def update_projects(id: int, project_name: str):
    with Session(engine) as session:
        project = session.exec(select(Project).where(Project.id == id)).first()
        if project:
            project.name = project_name
            session.add(project)
            session.commit()
            return True
        else:
            return False

if __name__ == '__main__':
    add_projects('1111')
    # search_project()
    update_projects(1872553663130640384,'2222')
    print(search_project())

