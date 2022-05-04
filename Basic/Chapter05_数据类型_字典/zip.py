#!/usr/bin/env python3
# -*- coding=utf-8 -*-

interface_list = ['fc1/1', "fc1/2", "fc1/3"]
status_list = ["up", "down", "up"]
speed_list = ["8G", "16G", "16G"]

z = zip(interface_list, status_list, speed_list)

print(z)
for i in z:
    print(i)
    print(i[0], i[1], i[2])


if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
