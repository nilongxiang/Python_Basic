#!/usr/bin/python3
# -*- coding=utf-8 -*-

def func1(name, age):
    print('%s is %d years old' % (name, age))

# 正确
func1('andy', 18)
func1('andy', age=18)  # 'andy'位置参数；age=18关键字参数
func1(name='andy', age=18)
func1(age=18, name='andy')

# func1(18, name='andy', )