#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from netapp_ontap import config, HostConnection
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume
import re


if __name__ == '__main__':
    config.CONNECTION = HostConnection('192.168.153.101', 'admin', 'P@ssw0rd', verify=False)

    for i in list(Volume.get_collection()):
        # print(i)
        # print(type(i))
        if 'vol_python' in str(i):
            j = re.search(r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', str(i)).group()
            try:
                Volume(uuid=j).delete()

            except NetAppRestError as error:
                print("Exception caught :" + str(error))
