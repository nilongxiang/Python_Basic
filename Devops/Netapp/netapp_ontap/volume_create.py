#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from netapp_ontap import config, HostConnection
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume


def create_volume(
        volume_name: str,
        svm_name: str,
        aggr_name: str,
        volume_size: int,
        guarantee='volume',
        snapshot_policy='none',
        reserve_percent=5) -> None:
    """Creates a new volume in a SVM"""

    v_size = int(volume_size) * 1024 * 1024  # MB -> Bytes
    volume = Volume.from_dict({
        'name': volume_name,
        'svm': {'name': svm_name},
        'aggregates': [{'name': aggr_name}],
        'size': v_size,
        'guarantee': {'_schema': guarantee},
        "snapshot_policy": {"name": snapshot_policy},
        "space": {"snapshot": {"reserve_percent": reserve_percent}}
    })

    try:
        volume.post()
        print("Volume %s created successfully" % volume.name)
    except NetAppRestError as err:
        print("Error: Volume was not created: %s" % err)


if __name__ == "__main__":
    config.CONNECTION = HostConnection('192.168.153.101', 'admin', 'P@ssw0rd', verify=False)

    vol_python1 = ['vol_python1', 'svm_data', 'aggr1', 30, 'none', 'none', 0]
    vol_python2 = ['vol_python2', 'svm_data', 'aggr1', 30, 'volume', 'default', 5]
    create_volume(*vol_python1)
    create_volume(*vol_python2)

