#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from random import randint
from scapy.all import *
from scapy.layers.inet import ICMP, IP
import subprocess
import os
import threading
import logging


def ping_one_subprocess(host):
    result = subprocess.run([f'ping -c 2 {host} &> /dev/null'], shell=True)
    # print(result)

    if result.returncode == 0:
        return host, "ok", os.getpid(), threading.currentThread().ident
    else:
        return host, "fail", os.getpid(), threading.currentThread().ident


def ping_one_scapy(host):
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

    id_ip = randint(1, 65535)  # 随机产生IP ID位
    id_ping = randint(1, 65535)  # 随机产生Ping ID位
    seq_ping = randint(1, 65535)  # 随机产生Ping序列号位

    # 构造ping数据包
    packet1 = IP(dst=host, ttl=1, id=id_ip)/ICMP(id=id_ping, seq=seq_ping)/b'hello world'
    # print(packet1.show())

    # 发送数据包，获取响应信息，超时为2秒，关闭详细信息
    ping = sr1(packet1, timeout=2, verbose=False)
    # print(ping)

    if ping:
        return host, "ok", os.getpid(), threading.currentThread().ident
    else:
        return host, "fail", os.getpid(), threading.currentThread().ident


if __name__ == '__main__':
    print(ping_one_subprocess('192.168.151.22'))
    print(ping_one_scapy('192.168.151.25'))
