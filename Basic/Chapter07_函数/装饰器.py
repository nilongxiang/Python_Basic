#!/usr/bin/env python3
# -*- coding=utf-8 -*-

def mydeco(fn):
    def fx():
        print("=========")
        fn()        # 调用原 myfun函数
        print("---------")
    return fx


@mydeco     # 替换原来的函数，等同于 myfun = mydeco(myfun)
def myfun():
    print("myfun被调用")


myfun()

if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
