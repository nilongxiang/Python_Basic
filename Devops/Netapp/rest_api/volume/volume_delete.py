#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from Devops.Netapp.rest_api.netapp_storage_info import username, password, mgmt_ip
from Devops.Netapp.rest_api.job_status import status_job
from volume_get import get_volume
import requests
import time


def delete_volume(vol_name):
    # 获取 vol uuid
    result = get_volume(vol_name)
    vol_uuid = result['uuid']

    url = f"https://{mgmt_ip}/api/storage/volumes/{vol_uuid}"
    result = requests.delete(url, auth=(username, password), verify=False)
    # print(result)
    # print(result.json())
    time.sleep(10)

    # 获取 job状态
    job_uuid = result.json()['job']['uuid']
    status_job(job_uuid, vol_name)

if __name__ == '__main__':
    delete_volume('vol_python1')
