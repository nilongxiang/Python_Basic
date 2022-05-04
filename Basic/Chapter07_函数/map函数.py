#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# def power(x):
#     return x ** 2
#
# for i in map(power, range(1, 10)):
#     print(i)


# for x in map(lambda x: x ** 4, range(1, 5)):
#     print(x)


# s = sum(map(lambda x: x ** 3, range(1, 3)))
# print(s)


def k_v(a, b):
    return a, b

# print(dict(map(k_v, range(1, 10), range(9, 0, -1))))

for i in map(k_v, range(1, 10), range(9, 0, -1)):
    print(i)

