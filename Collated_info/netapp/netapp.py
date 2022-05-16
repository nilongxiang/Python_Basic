#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import re
import pprint


def get_model(file):
    file.seek(0)
    # result = re.findall(r'Model Name:\s+(\w+\S?\w{0,5})', file.read())   # c-mode
    result = re.findall(r'Model Name:\s*(\w+)', file.read())  # 7-mode
    for i in list(set(result)):
        print(i)


def get_hostname(file):
    file.seek(0)
    result = re.search(r'(\w+)>', file.read()).group(1)
    print(result)


def get_sn(file):
    file.seek(0)
    result = re.findall(r'System Serial Number:\s(\d+)\s', file.read())
    for i in list(set(result)):   # 去重
        print(i)


def get_shelf(file):
    file.seek(0)
    result_all = re.findall(r'Shelf: (\d{1,2}).*?product identification=(\w{2}\d{3,4}\-?\d{0,2}).*?Product Serial Number: (\w{15})', file.read(), re.S)
    result = list(set(result_all))
    for i in result:
        print(f'{i[0]} {i[1]}盘柜 ({i[2]})')
    # print(result)


def get_version(file):
    file.seek(0)
    # result = re.search(r'NetApp Release\s(\d\.\d*\.*\d*P\d*)', file.read()).group(1)
    result = re.search(r'NetApp Release\s(\S*\s\S*):', file.read()).group(1)
    return result


def get_disk(file):
    file.seek(0)
    result = re.findall(r'(\d{2})\.(\d{1,2})\s*\:\sNETAPP\s+(X\d{3})\_\w+\s+\w+\s+\d{3,4}\.\d+\w+', file.read())
    result_disk = sorted(list(set(result)))


    # 去除磁盘 ID，将嵌套的元组转为列表
    l1 = []
    for i in result_disk:
        l1.append(list(i))
    # print(l1)
    # 弹出列表第2项元素并删除重复元素
    [j.pop(1) for j in l1]
    l2 = []
    [l2.append(i) for i in l1 if i not in l2]
    # print(l2)
    for i in l2:
        # print(i)
        i.append(l1.count(i))
        if i[1] == "X318":
            i.append('8TB')
            i.append('SATA')
        elif i[1] == 'X371':
            i.append('960GB')
            i.append('SSD')
        elif i[1] == 'X448':
            i.append('200GB')
            i.append('SSD')
        elif i[1] == 'X477':
            i.append('4TB')
            i.append('SATA')
        elif i[1] == 'X446':
            i.append('200GB')
            i.append('SSD')
        elif i[1] == 'X423':
            i.append('900GB')
            i.append('SAS')
        elif i[1] == 'X422':
            i.append('600GB')
            i.append('SAS')
    # print(l2)

    for i in l2:
        print(f'{i[0]} {i[2]}块 {i[3]} {i[4]}硬盘（{i[1]}）')
    # info_one_shelf = []
    # for i in l2:
    #     if i[0] not in info_one_shelf:
    #         info_one_shelf.append(i[0])
    #     info_one_shelf.append(l1.count(i))
    #     info_one_shelf.append(i[1])
    # print(info_one_shelf)

    # return info_one_shelf

if __name__ == '__main__':
    f1 = open(r'fas8020b.txt', 'r', encoding='utf-8')
    get_model(f1)
    get_hostname(f1)
    get_sn(f1)
    print(get_version(f1))
    get_shelf(f1)
    get_disk(f1)