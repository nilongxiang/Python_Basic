#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from netapp_ontap import config, HostConnection
from netapp_ontap.resources import Volume
import pprint


if __name__ == '__main__':
    config.CONNECTION = HostConnection('192.168.153.101', 'admin', 'P@ssw0rd', verify=False)
    pprint.pprint(list(Volume.get_collection()))
