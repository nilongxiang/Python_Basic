#!/usr/bin/python3
# -*- coding=utf-8 -*-
l1 = ["zhangsan", "lisi", "wangwu"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每一次循环过程中数据都会保存在
my_name 这个变量中，在循环体内部可以访问到当前这一次获取到的数据

for my_name in 列表变量:
    print("我的名字叫 %s" % 列表变量)
"""
for i in l1:
    print(l1.index(i))
    print(i)

for i in range(len(l1)):
    print(i)
    print(l1[i])

for i, j in enumerate(l1):
    print(i)
    print(j)

print(l1)
print("=" * 15 + ' result ' + "=" * 15)