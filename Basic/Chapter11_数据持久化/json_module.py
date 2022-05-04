#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import json
file = open('test.json', 'w')
d1 = {'key1': 1, "key2": 'andy', 'key3': [1, 2, 3], 'key4': False}

# json.dump(d1, file)     # python对象 到 json文件
# file.close()

# file_read = open('test.json', 'r').read()
# print(file_read)

# d2 = json.load(open('test.json')) # json文件 到 python对象
# print(d2)

s1 = json.dumps(d1)  # python对象 到 字符串
print(s1)
print(type(s1))     # <class 'str'>

s2 = json.loads(s1)     # 字符串 到 python对象
print(s2)
print(type(s2))     # <class 'dict'>


if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
