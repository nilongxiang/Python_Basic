#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def sum_numbers(*qyt):
    num = 0
    # 遍历 args 元组顺序求和
    for n in qyt:
        num += n
    return num

print(sum_numbers(1, 2, 3))