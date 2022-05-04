#!/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
函数的传参方式在能确定形参能唯一匹配到相应实参的情况下可以任意组合

位置参数（序列传参）要在 关键字传参（字典关键字传参）的左侧
"""


def myfun1(a, b, c):
    print(f"a 的值是：{a}")
    print(f"b 的值是：{b}")
    print(f"c 的值是：{c}")


# myfun1(1, *[2, 3])  # 正确
# myfun1(*[2, 3], 1)  # 正确
# myfun1(1, c=3, b=2)  # 正确
myfun1(1, 3, c=2)  # 错误

# myfun1(c=3, b=2, 1)  # 错误
