#!/usr/bin/python3
# -*- coding=utf-8 -*-

xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量K是每一次循环中，获取到的键值对的key
# for k in xiaoming_dict:
#     print("%s %s" % (k, xiaoming_dict[k]))

for k, v in xiaoming_dict.items():
    print(k, v)

print("=" * 15 + ' result ' + "=" * 15)