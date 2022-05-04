#!/usr/bin/python3
# -*- coding=utf-8 -*-

# def myadd(x, y):
#     result = x + y
#     print(result)
#
#
# myadd(100, 200)
#
# # myadd('abc', '100')
#
# # def mysum(x):
# #     num = 0
# #     for i in range(x+1):
# #         num += i
# #     print(num)
# #
# mysum(100)

# def mymax(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# v = mymax(100, 200)
# print('v=', v)
# print(mymax('ABC', 'abc'))


# def mymax(a, b):
#     if a > b:
#         return a
#     return b
#
# v = mymax(100, 200)
# print('v=', v)
# print(mymax('ABC', 'abc'))

#
# def mymax(a, b):
#     return max(a, b)
#
# v = mymax(100, 200)
# print('v=', v)
# print(mymax('ABC', 'abc'))


def input_number():
    list1 = []
    while True:
        promt = int(input("请输入数字："))
        if promt < 0:
            break
        list1.append(promt)
    return list1


L = input_number()
print(L)
print('用户输入的最大数是：', max(L))
print('用户输入的最小数是：', min(L))
print('用户输入的数的和是：', sum(L))

