#!/usr/bin/python3
# -*- coding=utf-8 -*-
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='P@ssw0rd', database='python', charset='utf8')
cursor = conn.cursor()

# 执行操作
# cursor.execute("select version()")
# cursor.execute("select * from 硬盘信息 where 设备名='CTE0'")
cursor.execute("select 设备名 from 硬盘信息")

# 获取执行结果
result = cursor.fetchall()
print(result)
# s1 = ''
# for i in result:
#     if result.index(i) == len(result)-1:
#         s1 += f'{i[3]}块 {i[2]} {i[1]}硬盘'
#     else:
#         s1 += f'{i[3]}块 {i[2]} {i[1]}硬盘 + '
# print(s1)

# *.fetchone() :取一行数据
# *.fecthmany(3) ：取三行数据
# *.fectchall() : 取所有数据

# 关闭cursor对象
cursor.close()
conn.close()
