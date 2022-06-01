#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import pandas as pd
pd.options.display.max_rows = 100
pd.options.display.max_columns = 100
# print(pd.__version__)

df1 = pd.read_csv('pd2.txt', sep='\s{2,}', engine='python')

print(df1[['ID', 'Type', 'Item']])


if __name__ == '__main__':
    pass

