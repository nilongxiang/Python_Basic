#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
import pprint
import urllib3
urllib3.disable_warnings()


def get_volume(mgmtip, username, password, vol_name):
    try:
        vol_url = f"https://{mgmtip}/api/storage/volumes"
        # 获取全部 volume
        # vol_result = requests.get(vol_url, auth=(username, password), verify=False)

        # 获取指定 volume
        vol_result = requests.get(vol_url, params={'name': vol_name}, auth=(username, password), verify=False)
        if vol_result.json()['num_records'] == 0:
            return f'{vol_name} not found.'
        # pprint.pprint(vol_result.json())

        else:
            vol_suf_url = vol_result.json()['records'][0]['_links']['self']['href']
            vol_detail_url = f"https://{mgmtip}/{vol_suf_url}"
            vol_detail_result = requests.get(vol_detail_url, auth=(username, password), verify=False)
            return vol_detail_result.json()

    except Exception as err:
        print(err)


if __name__ == '__main__':
    # result = get_volume('192.168.153.101', 'admin', 'P@ssw0rd', 'vol_python')
    result = get_volume('192.168.153.101', 'admin', 'P@ssw0rd', 'vol_python1')
    pprint.pprint(result)






