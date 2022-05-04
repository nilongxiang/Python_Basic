#!/usr/bin/python3
import sys


def mysum(a, b):
    if int(a) == 0:
        sys.exit()
    print(int(a) + int(b))

if __name__ == '__main__':
    mysum(sys.argv[1], sys.argv[2])
