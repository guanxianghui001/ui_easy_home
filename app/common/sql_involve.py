import pymysql
from app.conf import config
from pymysql.err import OperationalError as OpErr
from app.common.log import Logger


class SqlInvolve:
    def __init__(self):
        self.cursor = None
        self.conn = None
        self.host = config.db_host
        self.port = config.db_port
        self.user = config.db_user
        self.password = config.db_password
        self.database = config.database
        self.log = Logger()

    @property
    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user, port=self.port, password=self.password,
                                        database=self.database, charset='utf8')
            self.cursor = self.conn.cursor()
        except OpErr as e:
            self.log.error("mysql Error %d : %s" % (e.args[0], e.args[1]))
        except Exception as e:
            self.log.error("mysql Error %d : %s" % (e.args[0], e.args[1]))
            self.log.error("数据库连接异常失败，域名:{} 端口:{} 用户名:{}".format(self.host, self.port, self.user))

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
                    get_sql = f"SELECT {table_fields} FROM {table_name} "
                else:
                    get_sql = f"SELECT {table_fields} FROM {table_name}  Order BY {args[0]}"
            else:
                cond = ''
                for k, v in conditions.items():
                    if isinstance(v, int):
                        cond = cond + f' {k} ={v} and'
                    else:
                        cond = cond + f" {k} ='{v}' and"
                cond = cond[:-4]
                # print(cond)
                if args == ():
                    get_sql = f"SELECT {table_fields} FROM {table_name} WHERE {cond}"
                else:
                    get_sql = f"SELECT {table_fields} FROM {table_name} WHERE {cond} ORder BY {args[0]}"
            self.connect
            self.log.info(get_sql)
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
            insert_cond1 = ''
            insert_cond2 = ''
            for k, v in table_datas.items():
                insert_cond1 = insert_cond1 + f"{k},"
                if isinstance(v, int):
                    insert_cond2 = insert_cond2 + f'{v},'
                else:
                    insert_cond2 = insert_cond2 + f"'{v}',"
            insert_cond1 = insert_cond1[:-1]
            insert_cond2 = insert_cond2[:-1]
            insert_cond = f"INSERT INTO {table_name} ({insert_cond1}) VALUES ({insert_cond2})"
            print(insert_cond)
            self.connect
            self.cursor.execute(insert_cond)
            self.conn.commit()
            return True
        except OpErr as e:
            self.conn.rollback()
            self.log.error(f"mysql Error{e.args[0]} {e.args[1]}")
            return False
        except pymysql.err.IntegrityError as e:
            self.conn.rollback()
            self.log.error(f"mysql Error{e.args[0]} {e.args[1]}")
            return False

    def update_table_datas(self, table_name: str, update_datas: dict, condition: dict):
        """
        更新数据库
        :param table_name: 库名称
        :param update_datas: 更新字段,字典类型
        :param condition: 更新条件
        :return:
        """
        try:
            update_cond1 = ''
            update_cond2 = ''
            # 将变更字段和条件组合成string
            for k, v in update_datas.items():
                if isinstance(v, int):
                    update_cond1 = update_cond1 + f' {k} ={v},'
                else:
                    update_cond1 = update_cond1 + f" {k} ='{v}',"
            update_cond1 = update_cond1[:-1]

            for k, v in condition.items():
                if isinstance(v, int):
                    update_cond2 = update_cond2 + f' {k} ={v} and'
                else:
                    update_cond2 = update_cond2 + f" {k} ='{v}' and"
            update_cond2 = update_cond2[:-4]
            update_sql = f"UPDATE {table_name} SET  {update_cond1} WHERE  {update_cond2}"
            # print(update_sql)
            self.connect
            self.cursor.execute(update_sql)
            self.conn.commit()
            self.cursor.execute(update_sql)
            update_result = True
            return update_result
        except OpErr as e:
            self.conn.rollback()
            update_result = False
            self.log.error(f"mysql Error{e.args[0]} {e.args[1]}")
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
            self.log.error(f"mysql Error{e.args[0]} {e.args[1]}")
            clear_result = {'code': '9999', 'message': '执行清除任务失败！', 'datas': {}}
        except AttributeError as e:
            self.conn.rollback()
            self.log.error(f"mysql Error{e.args[0]} {e.args[1]}")
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
    data = result.get_all(table_field, 'project', condition)
    # data_total = result.get_all('count(*)', 'project', condition)
    # data1 = result.insert_table_datas('project', {"id": 1239811, "name": "资产"})
    # data2 = result.update_table_datas('project', {"name": "测试1","is_del":1}, {"id": 167580065657062195})
    module_data = {"father_node_id": 0, "project_id": 1675800569601728512, "name": "分类一下"}
    data3 = result.insert_table_datas('module', module_data)
    # print("输出{}".format(data_total))
    # print(data_total[0][0])
    print(data)
    # print(data3)
