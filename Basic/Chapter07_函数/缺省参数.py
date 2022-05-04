#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def info(name, age=18, address='未填写'):
    print(f'我叫{name}, 我今年{age}, 我家住址{address}。')

info('andy', 10, '上海市浦东新区')
info('andy', address='上海市浦东新区', age=15)
info('tedy', 15)
info('jack')
