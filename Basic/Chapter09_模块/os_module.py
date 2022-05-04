#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

result = os.popen('ifconfig').read()
print(result)


if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
