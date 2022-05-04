#!/usr/bin/python3
# -*- coding=utf-8 -*-
from netapp_ontap import config
from netapp_ontap import HostConnection
from netapp_ontap.resources import Cluster

conn = HostConnection('192.168.153.101', username='admin', password='P@ssw0rd', verify=False)
config.CONNECTION = conn

clus = Cluster()
clus.get()

print(clus.version)