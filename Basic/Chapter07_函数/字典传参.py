#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def myfun1(a, b, c):
    print("a 的值是：", a)
    print("b 的值是：", b)
    print("c 的值是：", c)


d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

myfun1(**d1)

