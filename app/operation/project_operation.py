# -*- coding: UTF-8 -*-
"""
@Project ：ui_easy_home
@File ：project_operation.py
@Author ：guanxianghui
@Date ：2023/6/30 10:31
"""

from app.common import snow
from app.common.sql_involve import SqlInvolve

from app.utils.generate_string import get_current_timestamp


def add_project(project_name):
    project_id = snow.IdWorker(1, 2, 0).get_id()
    print(project_id)
    project_name = project_name
    create_time = get_current_timestamp()
    update_time = get_current_timestamp()
    data_list = [['id', project_id], ['name', project_name], ['create_time', create_time],
                 ['update_time', update_time]]
    data = dict(data_list)
    SqlInvolve().insert_table_datas('project', data)


class ProjectOperation:
    def __int__(self):
        pass


if __name__ == '__main__':
    add_project('分類分級21')
