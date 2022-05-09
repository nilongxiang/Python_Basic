#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pprint
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = 'https://192.168.153.101/api/storage/volumes'
result = requests.get(url, auth=('admin', 'P@ssw0rd'), verify=False)
# result = requests.get(url, auth=requests.auth.HTTPBasicAuth('admin', 'P@ssw0rd'), verify=False)


if __name__ == '__main__':
    # 获取结果
    # print(type(result.text))  # str
    print(result.text)

    print('')
    print("=" * 100)
    print('')

    # 获取结果并转换成json格式
    pprint.pprint(result.json())  # dict
    # pprint.pprint(result.json()['records'][1]['name'])

