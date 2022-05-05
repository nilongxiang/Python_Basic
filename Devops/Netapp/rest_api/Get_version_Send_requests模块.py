#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json


def get_netapp(ip=None):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # 关闭SSL警告

    url = 'https://' + ip + '/api//cluster/software'
    headers = {'Authorization': 'Basic YWRtaW46UEBzc3cwcmQ='}  # Base 64编码 admin:P@ssw0rd

    request = requests.get(url, headers=headers, verify=False)

    # 获取response内容
    context = request.text

    # 将结果转换为字典格式
    context_json = json.loads(context)

    # 获取节点name和version
    # print(context_json['nodes'])
    # print(context_json['nodes'][0])  # [{'name': 'Cluster1-01', 'version': '9.6'}]的最外层[]去掉,得到里面字典
    if context_json['nodes'][0]['version']:
        return context_json['nodes'][0]['name'], context_json['nodes'][0]['version']
    else:
        print('空值')


if __name__ == '__main__':
    with open('hosts.txt', 'r', encoding='utf-8') as f_host:
        for text in f_host.readlines():
            if not text:
                break
            text = text.strip().split(",")
            host = text[0]
            cluster_name, cluster_version = get_netapp(host)
            print("存储名：%s" % cluster_name)
            print("存储版本：%s" % cluster_version)


