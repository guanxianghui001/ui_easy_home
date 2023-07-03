import pymysql
from app.conf import config
from pymysql.err import OperationalError as OpErr


class SqlInvolve:

    def __init__(self):
        self.cursor = None
        self.conn = None
        self.host = config.db_host
        self.port = config.db_port
        self.user = config.db_user
        self.password = config.db_password
        self.database = config.database

    @property
    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password,
                                        database=self.database, charset='utf8')
            self.cursor = self.conn.cursor()
        except OpErr as e:
            print("mysql Error %d : %s" % (e.args[0], e.args[1]))
        except Exception as e:
            print("mysql Error %d : %s" % (e.args[0], e.args[1]))
            print("数据库连接异常失败，域名:{} 端口:{} 用户名:{}".format(self.host, self.port, self.user))

    def get_all(self, table_fields, table_name, conditions: dict, type=1, *args):
        """
          查询数据

          :param table_fields: 查询数据的列名
          :param type:查询类型
          :param table_name: 数据表名称
          :param condition: 查询条件，以字典形式存储，当一个参数时，condition = {'eid':1},condition = {'eid':1,'name':'dded'}
          :return:
        """
        # print("args的值:{}".format(args))
        try:
            if conditions == {}:
                if args == ():
                    get_sql = "SELECT {} FROM {} ".format(table_fields, table_name)
                else:
                    get_sql = "SELECT {} FROM {}  Order BY {}".format(table_fields, table_name, args[0])
            else:
                cond = ''
                for k, v in conditions.items():
                    if isinstance(v, int):
                        cond = cond + ' {} ={} and'.format(k, v)
                    else:
                        cond = cond + " {} ='{}' and".format(k, v)
                cond = cond[:-4]
                # print(cond)
                if args == ():
                    get_sql = "SELECT {} FROM {} WHERE {}".format(table_fields, table_name, cond)
                else:
                    get_sql = "SELECT {} FROM {} WHERE {} ORder BY {}".format(table_fields, table_name, cond, args[0])
            self.connect
            # print(get_sql)
            self.cursor.execute(get_sql)
            if type == 1:
                datas = self.cursor.fetchall()
            elif type == 2:
                datas = self.cursor.fetchone()
            else:
                print("类型错误")
            self.conn.commit()
            return datas
        except Exception as e:
            print(e)
            return datas

    def insert_table_datas(self, table_name, table_datas: dict):
        """

        :param table_name:
        :param table_datas: 字典形式数据,当字段有空的情况，直接不用写入字典变量即可,单条数据插入
        :return:
        """
        try:
            for key in table_datas:
                # 将value值添加双引号，便于后面sql语句拼接使用，注意只要添加一层引号即可，如果是int型直接输入。
                table_datas[key] = "'" + str(table_datas[key]) + "'"
            key = ','.join(table_datas.keys())
            value = ','.join(table_datas.values())
            insert_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value + ") "
            self.connect
            self.cursor.execute(insert_sql)
            self.conn.commit()
            insert_result = {'code': '0000', 'message': '执行插入成功！'}
        except OpErr as e:
            self.conn.rollback()
            print('mysql Error %d :%s ' % (e.args[0], e.args[1]))
            insert_result = {'code': '9999', 'message': '执行插入失败！', 'datas': {}}
        except pymysql.err.IntegrityError as e:
            self.conn.rollback()
            insert_result = {'code': '9999', 'message': '执行插入失败！', 'datas': {}}
            print('mysql Error {}:{} '.format(e.args[0], e.args[1]))
        return insert_result

    def update_table_datas(self, table_name: str, update_datas: dict, condition):
        """
        更新数据库
        :param table_name: 库名称
        :param update_datas: 更新字段,字典类型
        :param condition: 更新条件
        :return:
        """
        try:
            if update_datas == {}:
                print('更新字段不能为空！')
                update_result = {'code': '9999', 'message': '更新字段不能为空', 'datas': {}}
                return update_result
            elif condition == {}:
                print('更新条件不能为空！')
                update_result = {'code': '9999', 'message': '更新条件不能为空', 'datas': {}}
                return update_result
            else:
                # 更新字段处理
                for key in update_datas:
                    update_datas[key] = "'" + str(update_datas[key]) + "'"
                    # print(update_datas[key])
                for key in condition:
                    condition[key] = "'" + str(condition[key]) + "'"
                    # print(condition[key])
                data_keys = list(update_datas.keys())
                condition_keys = list(condition.keys())
                if len(data_keys) == 1 and len(condition_keys) == 1:
                    for k in update_datas:
                        for key in condition:
                            update_sql = "UPDATE " + table_name + " SET " + k + " = " + update_datas[
                                k] + " WHERE " + key + "  = " + condition[key]
                elif len(data_keys) == 1:
                    for k in data_keys:
                        condition = ''
                        for key in condition:
                            condition = condition + key + " = " + str(condition[key]) + " or "
                        condition = condition[:-3]
                        update_sql = "UPDATE " + table_name + " SET " + k + " = " + update_datas[
                            k] + " WHERE " + condition
                elif len(condition_keys) == 1:
                    for k in condition_keys:
                        upg_data = ''
                        for key in update_datas:
                            upg_data = upg_data + key + " = " + update_datas[key] + " , "
                        upg_data = upg_data[:-2]
                        update_sql = "UPDATE " + table_name + " SET " + upg_data + " WHERE " + k + " = " + condition[k]
                else:
                    upg_data = ''
                    for k in data_keys:
                        condt = ''
                        for key in condition:
                            condt = condt + key + " = " + condition[key] + " or "
                        condt = condt[:-3]
                        upg_data = upg_data + key + " = " + update_datas[key] + " , "
                    upg_data = upg_data[:-2]
                    update_sql = "UPDATE " + table_name + " SET " + upg_data + " WHERE " + condt
                    # print(update_sql)
            self.connect
            self.cursor.execute(update_sql)
            self.conn.commit()
            update_result = {'code': '0000', 'message': '更新数据完成！', 'datas': {}}
        except OpErr as e:
            self.conn.rollback()
            update_result = {'code': '9999', 'message': '更新失败！', 'datas': {}}
            print("mysql Error %d :%s " % (e.args[0], e.args[1]))
        return update_result

    def clear_table_data(self, table_name):
        """

        :param table_name: 表名称
        :return:
        """
        try:
            # sql = "delete from " + table_name
            clear_sql = 'truncate table ' + table_name
            self.connect
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            self.cursor.execute(clear_sql)
            clear_result = {'code': '0000', 'message': '执行清除任务成功！', 'datas': {}}
            self.conn.commit()
        except OpErr as e:
            self.conn.rollback()
            print("mysql Error %d :%s " % (e.args[0], e.args[1]))
            clear_result = {'code': '9999', 'message': '执行清除任务失败！', 'datas': {}}
        except AttributeError as e:
            self.conn.rollback()
            print("mysql Error %d :%s " % (e.args[0], e.args[1]))
            clear_result = {'code': '9999', 'message': '执行清除任务失败！', 'datas': {}}
        return clear_result

    def close(self):
        self.cursor.close()

    def __del__(self):
        self.conn.close()


if __name__ == '__main__':
    result = SqlInvolve()
    table_field = "id, name, create_time, update_time"
    condition = {"is_del": 0, "name": "菲asd菲"}
    data = result.get_all(table_field, 'project', condition,(1))
    data_total = result.get_all('count(*)', 'project', condition)
    # data1 = result.insert_table_datas('project', {"id": 1239811, "name": "资产"})
    # data2 = result.update_table_datas('project', {"name": "测试项目"}, {"id": 123981})

    # print("输出{}".format(data_total))
    # print(data_total[0][0])
    print(data)
    # print(data2)
