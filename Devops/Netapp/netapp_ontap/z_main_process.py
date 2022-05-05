#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from netapp_ontap import config, HostConnection
from Devops.Netapp.netapp_ontap.volume_create import create_volume

# 1.连接存储
config.CONNECTION = HostConnection('192.168.153.101', 'admin', 'P@ssw0rd', verify=False)

# 创建volume
volume_list = [('vol_python1', 'svm_data', 'aggr1', 30, 'none', 0),
               ('vol_python2', 'svm_data', 'aggr1', 40, 'none', 0)]

for i in volume_list:
    create_volume(*i)


if __name__ == '__main__':
    pass
