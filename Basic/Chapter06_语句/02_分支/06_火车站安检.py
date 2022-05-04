#!/usr/bin/python3
# -*- coding=utf-8 -*-

has_ticket = True
knife_length = 21

if has_ticket:
    print("车票检查通过，准备开始安检")
    if knife_length >= 20:
        print("您携带的刀太长了，有 %d 公分长" % knife_length)
        print("不允许上车")
    else:
        print("请上车")
else:
    print("不允许进入")
