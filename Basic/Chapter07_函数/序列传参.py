#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def myfun1(a, b, c):
    print(f"a 的值是：{a}")
    print(f"b 的值是：{b}")
    print(f"c 的值是：{c}")


l1 = [1, 2, 3]
# myfun1(l1[0], l1[1], l1[2])
# myfun1(*l1)


t1 = (1, 2, 3)
myfun1(t1[0], t1[1], t1[2])
myfun1(*t1)


# s1 = "123"
# myfun1(s1[0], s1[1], s1[2])
# myfun1(*s1)
