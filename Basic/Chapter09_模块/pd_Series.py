#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import pandas as pd
l1 = [1, 2, 3, 4, 5]

# s1 = pd.Series(data=l1)
# print(s1)
# print(s1[1])
# print(s1[1:3])

# 指定索引
# s2 = pd.Series(data=l1, index=['a', 'b', 'c', 'd', 'e'])
# print(s2)
# print(s2[1])
# print(s2['a'])
# print(s2[1:3])


# 指定列名称
s3 = pd.Series(data=l1)
s3.index.name = 'xuhao'
s3.name ='num'
print(s3)
print(s3['xuhao'])





if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
