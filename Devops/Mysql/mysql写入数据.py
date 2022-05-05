#!/usr/bin/python3
# -*- coding=utf-8 -*-
import pymysql

teacher_list = [{'姓名': 'andy', '年龄': 18, '部门': 'Python', '职位': '讲师'},
                {'姓名': 'suse', '年龄': 19, '部门': 'Huawei', '职位': '讲师'},
                {'姓名': 'john', '年龄': 20, '部门': 'Docker', '职位': '讲师'}]

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='P@ssw0rd', database='python', charset='utf8')
cursor = conn.cursor()

# 创建表
# cursor.execute("create table teachers_info (姓名 varchar(40), 年龄 int, 部门 varchar(40), 职务 varchar(40))")

# 写入数据
for teacher in teacher_list:
    name = teacher['姓名']
    age = teacher['年龄']
    department = teacher['部门']
    job = teacher['职位']
    cursor.execute(f"insert into teachers_info values ('{name}', {age}, '{department}', '{job}')")

# 获取执行结果
cursor.execute("select * from teachers_info")
result = cursor.fetchall()
for i in result:
    print(i)

# 删除表
# cursor.execute("drop table teachers_info")

# 提交并写入数据库
# conn.commit()

# 关闭cursor对象
cursor.close()
conn.close()
