#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# a = 1
# b = 2
# c = 3
#
#
# def fn(c, d):
#     e = 300
#     print("locals() 返回：", locals())
#     print("局部变量c的值是：", c)
#     print("全局变量c的值是：", globals()['c'])
#
#
# print("globals() 返回：", globals())
# fn(100, 200)


# def fa():
#     print("hello world")
#
# f1 = fa()
# print(f1)
#
# f1 = fa
# f1()


# def myinput(fn):
#     L = [5, 3, 1, 9, 7]
#     return fn(L)
#
# print(myinput(max))
# print(myinput(min))
# print(myinput(sum))
# print(myinput(len))


def test1():
    print("*" * 50)


def test2():
    print("-" * 50)
    test1()
    print("+" * 50)

test2()