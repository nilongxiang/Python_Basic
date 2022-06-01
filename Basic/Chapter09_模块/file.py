#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import sys


with open('1.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)

# f = open('1.txt', 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()


print(sys.getdefaultencoding())


if __name__ == '__main__':
    pass

