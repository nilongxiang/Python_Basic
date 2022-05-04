#!/usr/bin/python3
# -*- coding=utf-8 -*-

row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    # 这一行代码的目的就是在一行星星输出完成后，增加换行
    print("")
    row += 1
