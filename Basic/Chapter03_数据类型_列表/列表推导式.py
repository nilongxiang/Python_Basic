#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# L = [x ** 2 for x in range(1, 10)]

# L =[]
# for x in range(1, 10):
#     L.append(x ** 2)

L = [x for x in range(1, 10) if x % 2 == 1]
print(L)

print("=" * 15 + ' result ' + "=" * 15)