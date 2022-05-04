#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import ipaddress

net = ipaddress.ip_network('192.168.151.0/24')

for i in net:
    print(i)



if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
