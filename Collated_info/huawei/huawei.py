# -*- coding=utf-8 -*-
# !/usr/bin/env python3
# -*- coding=utf-8 -*-
import pprint
import re
import os

os.chdir(os.path.dirname(__file__))


def get_model(file):
    file.seek(0)
    model = re.search(r'Product Model: (\d{4}\s\w+)', file.read()).group(1)
    return model


def get_hostname(file):
    file.seek(0)
    hostname = re.search(r'System Name: (\S+)', file.read()).group(1)
    return hostname


def get_sn(file):
    file.seek(0)
    sn = re.search(r'Product Serial Number: (\w*)', file.read()).group(1)
    return sn


def get_version(file):
    file.seek(0)
    version = re.search(r'Product Version: (\w+).*?Patch Version: ([\w{3}\d{3}\s]*).*?System Name', file.read(), re.S)
    return version.group(1) + ' ' + version.group(2)


def get_disk(file):
    file.seek(0)
    disk_all = re.findall(r'(\w{3}\d{1,3}).\d{1,2}\s*Normal\s*Online\s*(\w{3,6})\s*\w*.\w*\s*\w*\s\w*'
                          r'\s*\S*\s*\S*\s*\S*\s*\w{20}\s*(\d{5}\w{3})', file.read())
    # disk_all = re.findall(r'(\w{3}\d{1,3}).\d{1,2}\s*Normal\s*Online\s*(\w{3,6})\s*\w*.\w*\s*\w*\s\w*'
    #                       r'\s*\S*\s*\S*\s*\S*\s*\w{20}\s*\w*\s*\w*\s*(\d{1,4}.\d{3}\w{2})', file.read())
    # print(disk_all)

    return disk_all


def get_disk_include_contro(file):
    file.seek(0)
    contr_all = re.findall(r'Enclosure ID:\s(CTE\d).*?Logic Type: Engine.*?SN:\s(\w{20}).*?OceanStor (\d{4}\s\w{2})',
                           file.read(), re.S)
    file.seek(0)
    shelf_all = re.findall(r'Enclosure ID:\s(DAE\d{3}).{1,10}?Logic Type: Expansion Enclosure.*?SN: (\w{20}).*?Disk Units?\S(\w{1,10})', file.read(), re.S)
    # print(shelf_all)
    contr_list = list(set(contr_all))
    shelf_list = list(set(shelf_all))
    # pprint.pprint(contr_list)
    # pprint.pprint(shelf_list)

    contr_list.extend(shelf_list)
    # print(contr_list)

    file.seek(0)
    disk_info = get_disk(file)
    # pprint.pprint(disk_info)

    l2 = []
    [l2.append(i) for i in disk_info if i not in l2]  # 去重
    # pprint.pprint(sorted(l2))
    info_one_shelf = []
    for i in sorted(l2):
        if i[0] not in info_one_shelf:
            info_one_shelf.append(i[0])
        info_one_shelf.append(disk_info.count(i))
        info_one_shelf.append(i[2])
        info_one_shelf.append(i[1])
    # print(info_one_shelf)
    return contr_list, info_one_shelf


def pretty_output(info):
    device = info[0]
    disk = info[1]

    # pprint.pprint(device)
    pprint.pprint(f'device:{device}')
    print(f'disk:{disk}')
    # 获取设备类型['CTE0', 'DAE010', 'DAE020']
    device_type_list = []
    for single_device in device:
        device_type = single_device[0]
        device_type_list.append(device_type)
    # print(device_type_list)

    for x in device:
        # info_for_single_device = x[0]
        info_for_single_device = ''
        ind = disk.index(x[0])
        ind += 1
        i = 0
        last = False
        while True and ind < len(disk):
            value = disk[ind]
            if value in device_type_list:
                last = False
                break
            i = i + 1
            if i == 1:
                if last:
                    value = '+ ' + str(value)
                value = str(value) + '块 '
            if i == 2:
                value = str(value)
            if i == 3:
                value = ' ' + value + ' 硬盘 '
                i = 0
                last = True
            info_for_single_device += str(value)
            # print(info_for_single_device)

            s1 = info_for_single_device.replace('02351KBT', '1.2TB')
            s2 = s1.replace('02351KES', '600GB')
            s3 = s2.replace('02351SBG', '960GB')
            s4 = s3.replace('02352WEB', '1.2TB')
            s5 = s4.replace('02352WFV', '8TB')
            s6 = s5.replace('02351KEN', '8TB')
            s7 = s6.replace('02350MQG', '8TB')

            # print(info_for_single_device)
            ind += 1
        # print(info_for_single_device)
        # s1 = ''
        # for i in info_for_single_device.split(' '):
        #     # print(i)
        #     if i == '02350MQ':
        #         s1 + '8TB'
        #     else:
        #         s1 = ' '.join(i)
        # print(s1)
        print(f'{x[0]:<6} {x[2]:<10} ({x[1]}), {s7}')
        # print(f'info_for_device:{info_for_single_device}')


def get_license(file):
    file.seek(0)
    license1 = re.findall(r'Feature Name:(\w+\s?\w+)', file.read())
    return license1

if __name__ == '__main__':
    f = open('Operating_Data20200508171822.txt', 'r', encoding='utf-8')
    print(get_model(f))
    print(get_hostname(f))
    print(get_sn(f))
    print(get_version(f))
    f.seek(0)
    Model = re.search(r'Product Model:\s(\d{4})', f.read()).group(1)
    x, y = None, None
    if Model in ['5300', '5500', '5310', '5510', '5800']:
        x = get_disk_include_contro(f)
    # elif Model in '5500':
    #     x = get_disk_include_contro(f)
    else:
        pass
    # result = pretty_output(x)
    license2 = get_license(f)
    print("、".join(license2))

    f.close()
