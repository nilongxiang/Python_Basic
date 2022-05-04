#!/usr/bin/env python3
# -*- coding=utf-8 -*-

var = 100


def outter():
    var = 200
    print("outter内的var = ", var)

    def inner():
        nonlocal var
        var = 300
        print("inner内的var = ", var)
    inner()
    print("outter结束时的的var = ", var)

outter()
print("全局的var = ", var)