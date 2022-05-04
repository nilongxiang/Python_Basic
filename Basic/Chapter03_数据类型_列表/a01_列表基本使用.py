#!/usr/bin/python3
# -*- coding=utf-8 -*-

name_list = ["zhangsan", "lisi", "wangwu"]

# name_list.append("王小二")
# name_list.insert(1, "小美眉")
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

print(name_list)

print("=" * 15 + ' result ' + "=" * 15)