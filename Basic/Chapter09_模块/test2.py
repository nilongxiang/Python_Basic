#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import sys
import os
env1 = os.environ
print(env1.get('PYTHONPATH'))
print(sys.path)

if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
