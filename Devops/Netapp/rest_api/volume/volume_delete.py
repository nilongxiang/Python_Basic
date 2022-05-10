#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from volume_get import get_volume
import pprint
import requests
import time


def delete_volume(mgmtip, username, password, vol_name):
    result = get_volume(mgmtip, username, password, vol_name)
    # pprint.pprint(result['uuid'])
    vol_uuid = result['uuid']

    url = f"https://{mgmtip}/api/storage/volumes/{vol_uuid}"
    result = requests.delete(url, auth=(username, password), verify=False)
    # print(result)
    # print(result.json())
    time.sleep(10)

    # 获取 job状态
    job_url = f"https://{mgmtip}/{result.json()['job']['_links']['self']['href']}"
    job_response = requests.get(job_url, auth=(username, password), verify=False)
    job_status = job_response.json()['state']
    print(f'{vol_name} delete {job_status}.')


if __name__ == '__main__':
    delete_volume('192.168.153.101', 'admin', 'P@ssw0rd', 'vol_python1')
