#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

print(os.getcwd())
os.chdir(r'/PyCharmProject/python_basic/')
print(os.getcwd())
for i in os.scandir():
    print(i.name)
    print(i.path)
if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
