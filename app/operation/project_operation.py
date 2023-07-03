# -*- coding: UTF-8 -*-
"""
@Project ：ui_easy_home
@File ：project_operation.py
@Author ：guanxianghui
@Date ：2023/6/30 10:31
"""
from app.conf import config
from app.common import snow
from app.common.sql_involve import SqlInvolve

from app.utils.generate_string import get_current_timestamp


# class ProjectOperation:
#     def __int__(self):
#         self.table = config.project_table


def add_project(project_name):
    project_id = snow.IdWorker(1, 2, 0).get_id()
    # create_time = get_current_timestamp()
    # update_time = get_current_timestamp()
    data_list = [['id', project_id], ['name', project_name]]
    # data_list = [['id', project_id], ['name', project_name], ['create_time', create_time],
    #              ['update_time', update_time]]
    # print(SqlInvolve().get_all('count(*)', 'project', {"name": project_name, "is_del": 0})[0][0])
    if SqlInvolve().get_all('count(*)', 'project', {"name": project_name, "is_del": 0})[0][0] == 0:
        data = dict(data_list)
        SqlInvolve().insert_table_datas('project', data)
        return project_id, project_name
    else:
        return False


def search_project():
    table = config.project_table
    field = "id, name, create_time,update_time"
    condition = {"is_del": 0}
    data = SqlInvolve().get_all(field, table, condition, 1, 'create_time desc')
    total = SqlInvolve().get_all('count(*)', table, condition)[0][0]
    # print(total)
    list_result = []
    if data == ():
        return list_result
    else:
        data_list = list(data)
        for i in data_list:
            list_field = ['id', 'name', 'create_time', 'update_time']
            list_result.append(dict(zip(list_field, i)))
        return list_result


if __name__ == '__main__':
    # add_project('分類分級21')
    # search_project()
    print(search_project())
