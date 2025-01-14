# -*- coding: UTF-8 -*-
"""
@module ：uieasyhome
@File ：module_operation.py
@Author ：guanxianghui
@Date ：2023/7/4 14:13 
"""
from app.common import snow
from app.conf import config
from app.common.log import Logger
from app.utils.encoding_tree import ram_list_to_tree
from app.common.sql_involve import SqlInvolve

sql = SqlInvolve()
module_table = config.module_table
log = Logger()


def add_modules(module_data: dict):
    # module_id = snow.IdWorker(1, 2, 0).get_id()
    # log.info(module_id)
    module_name = module_data["name"]
    # father_node_id = module_data["father_node_id"]
    project_id = module_data["project_id"]
    # module_data.update({"id": module_id})
    # if sql.get_all('count(*)', 'module', {"id": father_node_id, "is_del": 0})[0][0]:
    # 判断project_id是否存在
    if sql.get_all('count(*)', 'project', {"id": project_id, "is_del": 0})[0][0]:
        # 判断形同项目下是否含有相同模块名
        if not sql.get_all('count(*)', 'module', {"name": module_name, "project_id": project_id, "is_del": 0})[0][0]:

            date=sql.insert_table_datas(module_table, module_data)
            if date:
                return module_data
            else:
                status_code = 40001
                detail = '数据库报错'
                log.info(date)
                return status_code, detail
        else:
            status_code = 40001
            detail = '同一项目下含有重复的模块名称'
            log.info(detail)

            return status_code, detail
    else:
        status_code = 40003
        detail = "项目id不存在或已删除"
        return status_code, detail
    # else:
    #     status_code = 40004
    #     detail = "父级id不存在或已删除"
    #     return status_code, detail


def search_module(project_id):
    field = "id, name, father_node_id"
    condition = {"project_id": project_id}
    data = sql.get_all(field, module_table, condition)
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


def delete_modules(module_name):
    update_datas = {"is_del": 1}
    condition = {"name": module_name}
    if SqlInvolve().get_all('count(*)', module_table, condition)[0][0] > 0:
        result = SqlInvolve().update_table_datas(module_table, update_datas, condition)
    else:
        result = False
    return result


def update_modules(id, module_name):
    condition = {"id": id}
    update_datas = {"name": module_name}
    if SqlInvolve().get_all('count(*)', module_table, condition)[0][0] > 0:
        result = SqlInvolve().update_table_datas(module_table, update_datas, condition)
        print(result)
    else:
        result = False
    return result


if __name__ == '__main__':
    # module_data = {"father_node_id": 1, "module_id": 167613652810086912, "name": "分"}
    # print(add_modules(module_data))
    print(search_module(1676136523810086912))
