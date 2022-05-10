#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from volume_get import get_volume
import requests
import time
import urllib3
import pprint
urllib3.disable_warnings()


def modify_volume(mgmtip, username, password, vol_name):
    result = get_volume(mgmtip, username, password, vol_name)
    vol_uuid = result['uuid']
    url = f"https://{mgmtip}/api/storage/volumes/{vol_uuid}"

    volume_json = {"size": '1G'}

    try:
        result = requests.patch(url, auth=(username, password), json=volume_json, verify=False)
        # pprint.pprint(result.json())
        time.sleep(10)

        # 获取 job状态
        job_url = f"https://{mgmtip}/{result.json()['job']['_links']['self']['href']}"
        job_response = requests.get(job_url, auth=(username, password), verify=False)
        job_status = job_response.json()['state']
        print(f'{vol_name} modify {job_status}.')

    except Exception as err:
        print(err)


if __name__ == '__main__':
    vol_python1 = ['192.168.153.101', 'admin', 'P@ssw0rd', 'vol_python1']
    modify_volume(*vol_python1)


