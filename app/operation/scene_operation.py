# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：scene_operation.py
@Author ：guanxianghui
@Date ：2023/7/6 15:26 
"""
from app.conf import config
from app.common.log import Logger
from app.common.sql_involve import SqlInvolve
from app.common import snow
sql = SqlInvolve()
scene_table = config.scene_table
log = Logger()


def add_scenes(scene_data: dict):
    id=snow.IdWorker(1, 2, 0).get_id()
    scene_name = scene_data["name"]
    project_id = scene_data["project_id"]
    module_id = scene_data["module_id"]
    description = scene_data["description"]
    scene_data.update({"id":id})
    # 判断模块id是否存在
    if module_id is None:
        pass
    else:
        if not sql.get_all('count(*)', 'module', {"id": module_id, "is_del": 0})[0][0]:
            status_code = 40001
            detail = '选择模块不存在或删除'
            log.info(detail)
            return status_code, detail
    # 判断project_id是否存在
    if sql.get_all('count(*)', 'project', {"id": project_id, "is_del": 0})[0][0]:
        pass
    else:
        status_code = 40003
        detail = "项目id不存在或已删除"
        return status_code, detail
        # 判断形同项目下是否含有相同模块名
    if not sql.get_all('count(*)', 'scenario', {"name": scene_name, "project_id": project_id, "is_del": 0})[0][0]:
        sql.insert_table_datas(scene_table, scene_data)
        return scene_data
    else:
        status_code = 40001
        detail = '同一项目下含有重复的场景名称'
        log.info(detail)
        return status_code, detail

def search_scene(project_id):
    field = "id, name, father_node_id"
    condition = {"project_id": project_id}
    data = sql.get_all(field, scene_table, condition)
    list_result = []
    if data == ():
        return list_result
    else:
        data_list = list(data)
        for i in data_list:
            list_field = ['id', 'name', 'parent_id']
            list_result.append(dict(zip(list_field, i)))

        list_result = (ram_list_to_tree(list_result))
        return list_result

def delete_scenes(scene_name):
    update_datas = {"is_del": 1}
    condition = {"name": scene_name}
    if SqlInvolve().get_all('count(*)', scene_table, condition)[0][0] > 0:
        result = SqlInvolve().update_table_datas(scene_table, update_datas, condition)
    else:
        result = False
    return result

def update_scenes(id, scene_name):
    condition = {"id": id}
    update_datas = {"name": scene_name}
    if SqlInvolve().get_all('count(*)', scene_table, condition)[0][0] > 0:
        result = SqlInvolve().update_table_datas(scene_table, update_datas, condition)
        print(result)
    else:
        result = False
    return result