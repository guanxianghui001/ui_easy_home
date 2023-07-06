# -*- coding: UTF-8 -*-
"""
@Project ：uieasyhome 
@File ：code_operation.py
@Author ：guanxianghui
@Date ：2023/7/5 16:46 
"""
from app.conf import config
from app.common.log import Logger
from app.utils.encoding_tree import ram_list_to_tree
from app.common.sql_involve import SqlInvolve

sql = SqlInvolve()
code_table = config.code_table
log = Logger()


def get_codes(code_type):
    field = "distinct code_type, code_type_name"
    conndition = {"code_type": code_type}
    first_data = sql.get_all(field, code_table, conndition)
    log.info(first_data)
    log.info(f'请求参数为:{code_type}')
    first_list_result = []
    if first_data == ():
        return first_list_result
    else:
        first_data_list = list(first_data)
        log.info(f"数据转化为列表数据{first_data_list}")
        for i in first_data_list:
            first_list_field = ['code_type', 'code_type_name', 'sub']
            first_list_result.append(dict(zip(first_list_field, i)))
    for i in first_list_result:
        field = " id, code_value,code_desc"
        conndition = {"code_type": i["code_type"]}
        second_data = sql.get_all(field, code_table, conndition)
        second_list_result = []
        if second_data == ():
            return second_list_result
        else:
            second_data_list = list(second_data)
            for j in second_data_list:
                second_list_field = ['id', 'code_value', 'code_desc']
                second_list_result.append(dict(zip(second_list_field, j)))
        i['sub'] = second_list_result
    log.info(f"数据转化为列表数据{first_list_result}")
    return first_list_result


if __name__ == "__main__":
    get_codes()
