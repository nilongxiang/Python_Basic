#!/usr/bin/python3
# -*- coding=utf-8 -*-

def f1():
    n = 999

    def f2():
        print(n)

    return f2


result = f1()
result()