#!/usr/bin/python3
# -*- coding=utf-8 -*-
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='P@ssw0rd', database='python', charset='utf8')
cursor = conn.cursor()

# 执行操作
cursor.execute("select version()")

# 获取执行结果
result = cursor.fetchall()
print(result)

# *.fetchone() :取一行数据
# *.fecthmany(3) ：取三行数据
# *.fectchall() : 取所有数据

# 关闭cursor对象
cursor.close()
conn.close()
