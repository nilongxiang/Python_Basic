#!/usr/bin/env python3
# -*- coding=utf-8 -*-

count = 0


def hello(name):
    print('你好', name)
    global count
    count += 1
    print("locals() 返回：", locals())


hello('小张')
hello('小李')
print("hello 函数被调用", count, '次')