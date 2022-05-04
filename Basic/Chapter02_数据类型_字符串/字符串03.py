#!/usr/bin/env python3
# -*- coding=utf-8 -*-

try:
    number = int(input("请输入一个数字："))
except ValueError:
    print('请输入数字')
except NameError:
    print('请输入数字')

if number > 2:
    print("#" * number)
    print("#", end="")
    print(" " * (number-2), end="")
    print("#")
    print("#", end="")
    print(" " * (number - 2), end="")
    print("#")
    print("#" * number)
else:
    print('请重新输入')
