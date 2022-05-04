#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from ping_one import ping_one_subprocess, ping_one_scapy
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
import ipaddress
from datetime import datetime


def ping_scan(network):
    cpus = cpu_count()  # 获取CPU数量
    pool = ThreadPool(processes=100)  # 多线程池

    result_obj_dict = {}
    net = ipaddress.ip_network(network)
    for ip in net:
        # result_obj是<multiprocessing.pool object at 0x7f8ec6f6e100>对象，循环中不要使用get方法
        result_obj = pool.apply_async(ping_one_subprocess, args=(str(ip),))
        # result_obj = pool.apply_async(ping_one_scapy, args=(str(ip),))
        result_obj_dict[str(ip)] = result_obj

    print(datetime.now().strftime('%X'))
    pool.close()
    pool.join()
    print(datetime.now().strftime('%X'))

    active_ip_list = []
    for ip, obj in result_obj_dict.items():
        if obj.get()[1] == 'ok':
            active_ip_list.append(ip)
        # print(ip, obj.get()[1], obj.get()[2], obj.get()[3])  # 192.168.151.1 ok 9546 140431203497728
    return active_ip_list


if __name__ == '__main__':
    print(ping_scan('192.168.151.0/24'))
