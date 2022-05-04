#!/usr/bin/python3
# -*- coding=utf-8 -*-

from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host='192.168.151.51', port=3306, user='root', password='P@ssw0rd', database='mysql', charset='utf8')
    # 获得cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数，查询一条数据
    cs1.execute('select version()')
    version = cs1.fetchone()

    # 打印受影响的行数
    print("Database version: %s" % version)

    # 关闭cursor对象
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
