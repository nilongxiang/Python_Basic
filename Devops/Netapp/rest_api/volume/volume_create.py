#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
import time
import base64
import urllib3
import pprint
urllib3.disable_warnings()


def create_volume(mgmtip, headers_ins, vol_name, svm_name, aggr_name, vol_size, guarantee, snapshot_policy, reserve_percent):

    v_size = int(vol_size) * 1024 * 1024  # MB -> Bytes

    url = f"https://{mgmtip}/api/storage/volumes"

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
        result = requests.post(url, headers=headers_ins, json=volume_json, verify=False)
        # pprint.pprint(result.json())
        time.sleep(10)

        # 获取 job状态
        job_url = f"https://{mgmtip}/{result.json()['job']['_links']['self']['href']}"
        job_response = requests.get(job_url, headers=headers_ins, verify=False)
        job_status = job_response.json()['state']
        print(f'{vol_name} create {job_status}.')

    except Exception as err:
        print(err)


if __name__ == '__main__':
    str_base64 = base64.b64encode(b'admin:P@ssw0rd').decode('utf-8')
    headers = {
        'authorization': f"Basic {str_base64}",
        'content-type': "application/json",
        'accept': "application/json"
    }

    vol_python1 = ['192.168.153.101', headers, 'vol_python1', 'svm_data', 'aggr1', 30, 'none', 'none', 0]
    # vol_python2 = ['192.168.153.101', headers, 'vol_python2', 'svm_data', 'aggr1', 40, 'volume', 'default', 5]
    create_volume(*vol_python1)
    # create_volume(*vol_python2)

