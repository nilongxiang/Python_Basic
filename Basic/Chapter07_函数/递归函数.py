#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def age1(x):
    if x == 1:
        return 10
    return 2 + age1(x - 1)

print(age1(5))
