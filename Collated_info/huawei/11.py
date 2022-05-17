#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from itertools import chain
import re
# s1 = 'System Name: IMG_HFENAS_02'
# s2 = 'System Name: IMG-HFENAS02'
# result = re.search(r'System Name: (\S+)', s2).group(1)
# print(result)

# a = [(('p1', 'p2'), ('m1',)), (('p2', 'p1'), ('m1',))]
# b = [tuple(chain(*i)) for i in a]
# print(b)

# l1 = [('CTE0', 'SSD', '02351KES'), ('CTE0', 'SSD', '02351KES')]
# l2 = []
#
# for i in l1:
#     print(i)
#     l2.append(list(i))
#
# print(l2)
# # for i in range(len(l1)):
# #     print(i)
# #     l1[i] = l1

f = open('config_hfe_yx.txt', 'r', encoding='utf-8')
Model = re.search(r'Product Model:\s(\d{4})', f.read()).group(1)

print(Model)
if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
