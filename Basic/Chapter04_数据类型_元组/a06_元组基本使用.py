#!/usr/bin/python3
# -*- coding=utf-8 -*-
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1. 取值和取索引
print(info_tuple[0])

print(info_tuple.index("zhangsan"))
print(info_tuple.index(18))


# 2. 统计
print(info_tuple.count("zhangsan"))
# 统计元组中包含的元素个数
print(len(info_tuple))
