#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by tianjun on 16/2/21

import MySQLdb


class DB(object):
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

    def get_conn(self):
        return MySQLdb.Connect(
            host=self.DB_HOST,  # 设置MYSQL地址
            port=self.DB_PORT,  # 设置端口号
            user=self.DB_USER,  # 设置用户名
            passwd=self.DB_PWD,  # 设置密码
            db=self.DB_NAME,  # 数据库名
            charset='utf8'  # 设置编码
        )

    def query(self, sqlString, db_data=None):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            cursor.execute(sqlString, db_data)
            # returnData = cursor.fetchall()
            data = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in cursor.fetchall()]
            cursor.close()
            conn.close()
            return data
        except Exception, e:
            print '数据库连接失败:%s' % e

    # 更细单条
    def update(self, sql, db_data=None):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            cursor.execute(sql, db_data)
            conn.commit()
        except Exception, e:
            print '数据库插入失败:%s' % e
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True

    # 更新数组
    def update_all(self, sql, blog_list=None):
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            cursor.executemany(sql, blog_list)
            conn.commit()
        except Exception, e:
            print '数据库插入失败:%s' % e
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
        return True


if __name__ == '__main__':
    db = DB('localhost', 3306, 'root', '123456', 'myimg')
    print db.query("select * from blog limit 0,1")[0].get("subTitle")
    print db.query("select * from blog limit 0,1")[0].get("subTitle")
    pass
