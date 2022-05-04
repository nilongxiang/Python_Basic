#!/usr/bin/python3
# -*- coding=utf-8 -*-
from pymysql import *


# 创建connection连接
conn = connect(host='192.168.151.51', port=3306, user='root', password='P@ssw0rd', database='jing_dong', charset='utf8')
# 获得cursor对象
cursor = conn.cursor()

# 执行select语句，并返回受影响的行数，查询一条数据
count = cursor.execute("select id,name from goods where id>=4")

for i in range(count):
    result = cursor.fetchone()
    print(result)


# 关闭cursor对象
cursor.close()
conn.close()
