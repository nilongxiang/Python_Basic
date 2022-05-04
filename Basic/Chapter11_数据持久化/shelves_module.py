#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import shelve

l1 = [1, 2, 'hello']
d1 = {'name': "andy", 'age': 18, 'address': [4, 5, 6]}

dbwrite = shelve.open('andy-shelve')
dbwrite["key1"] = l1
dbwrite["key2"] = d1

dbwrite.close()

dbread = shelve.open('andy-shelve')

for i in dbread:
    print(i, "==>", dbread[i])

dbread.close()


if __name__ == '__main__':
    print("=" * 15 + ' result ' + "=" * 15)
