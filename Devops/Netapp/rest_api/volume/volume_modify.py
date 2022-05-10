#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from Devops.Netapp.rest_api.netapp_storage_info import username, password, mgmt_ip
from Devops.Netapp.rest_api.job_status import status_job
from volume_get import get_volume
import requests
import time
import urllib3
urllib3.disable_warnings()


def modify_volume(vol_name):
    result = get_volume(vol_name)
    vol_uuid = result['uuid']
    url = f"https://{mgmt_ip}/api/storage/volumes/{vol_uuid}"

    volume_json = {"size": '40M'}

    try:
        result = requests.patch(url, auth=(username, password), json=volume_json, verify=False)
        # pprint.pprint(result.json())
        time.sleep(5)

        # 获取 job状态
        job_uuid = result.json()['job']['uuid']
        status_job(job_uuid, vol_name)

    except Exception as err:
        print(err)


if __name__ == '__main__':
    modify_volume('vol_python1')
    pass

