#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def make_power(y):
    def fn(arg):
        return arg ** y
    return fn

pow2 = make_power(2)
print('5的平方是：', pow2(5))

