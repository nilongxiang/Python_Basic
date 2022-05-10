#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from Devops.Netapp.rest_api.netapp_storage_info import username, password, mgmt_ip
from Devops.Netapp.rest_api.job_status import status_job
import requests
import time
import urllib3
urllib3.disable_warnings()


def create_volume(vol_name, svm_name, aggr_name, vol_size, guarantee, snapshot_policy, reserve_percent):

    v_size = int(vol_size) * 1024 * 1024  # MB -> Bytes

    url = f"https://{mgmt_ip}/api/storage/volumes"

    volume_json = {
        "aggregates": [{'name': aggr_name}],
        "svm": {'name': svm_name},
        "name": vol_name,
        "size": v_size,
        "guarantee": {"type": guarantee},
        "snapshot_policy": {"name": snapshot_policy},
        "space": {"snapshot": {"reserve_percent": reserve_percent}}
    }
    try:
        result = requests.post(url, auth=(username, password), json=volume_json, verify=False)
        # pprint.pprint(result.json())
        time.sleep(10)

        # 获取 job状态
        job_uuid = result.json()['job']['uuid']
        status_job(job_uuid, vol_name)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    vol_python1 = ['vol_python1', 'svm_data', 'aggr1', 30, 'none', 'none', 0]
    # vol_python2 = ['vol_python2', 'svm_data', 'aggr1', 40, 'volume', 'default', 5]
    create_volume(*vol_python1)
    # create_volume(*vol_python2)

