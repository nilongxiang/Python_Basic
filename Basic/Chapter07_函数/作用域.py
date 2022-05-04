#!/usr/bin/env python3
# -*- coding=utf-8 -*-

v = 100


def f1():
    v = 200
    print(f"f1的 v = {v}")

    def f2():
        nonlocal v
        v = 300
        print(f"f2的 v = {v}")

    f2()
    print(f"f2 执行完后 v = {v}")

f1()
print(f"全局的 v = {v}")