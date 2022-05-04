#!/usr/bin/python3
# -*- coding=utf-8 -*-
import time
a = 1
b = 6

while a < 6:
    if a == 4:
        a += 1
        # print("a 等于 4")
        continue
    print(a)
    a += 1
    time.sleep(5)
else:
    print("执行完毕")
