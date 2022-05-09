#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
import pprint
import urllib3
urllib3.disable_warnings()


def get_volume(mgmtip, username, password, vol_name):
    try:
        # 获取全部 volume
        vol_url = f"https://{mgmtip}/api/storage/volumes"
        vol_result = requests.get(vol_url, auth=(username, password), verify=False)
        # pprint.pprint(vol_result.json())

        # 获取全部 volume结果并转换成 json格式
        for i in vol_result.json()['records']:
            # 匹配想要的卷，并得到其 suffix_url (/api/storage/volumes/710b36f4-1887-11ea-85ab-000c29196662)
            if i['name'] == vol_name:
                vol_suf_url = i['_links']['self']['href']
                vol_detail_url = f"https://{mgmtip}/{vol_suf_url}"
                vol_detail_result = requests.get(vol_detail_url, auth=(username, password), verify=False)
                pprint.pprint(vol_detail_result.json())
                break
        else:
            print(f'{vol_name} not found.')

    except Exception as err:
        print(err)


if __name__ == '__main__':
    get_volume('192.168.153.101', 'admin', 'P@ssw0rd', 'vol_python')
    get_volume('192.168.153.101', 'admin', 'P@ssw0rd', 'vol_python3')




