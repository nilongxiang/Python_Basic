#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from dateutil import parser

strtime = '2022-05-01 20:45:35.764868'

i = parser.parse(strtime)

print(i)
print(i.year)
if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
