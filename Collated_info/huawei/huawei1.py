# -*- coding=utf-8 -*-
# !/usr/bin/env python3
# -*- coding=utf-8 -*-
import pprint
import re
import os

os.chdir(os.path.dirname(__file__))


def get_model(file):
    file.seek(0)
    model = re.search(r'Product Model: (\w{4,10}\s\w+)', file.read()).group(1)
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
    # 根据Disk Info获取所有硬盘['CTE0', 'SSD', '02351KES']
    disk_all_old = re.findall(
        r'(\w{3}\d{1,3}).\d{1,2}\s*Normal\s*Online\s*(\w{3,6})\s*\w*.\w*\s*\w*\s\w*\s*\S*\s*\S*\s*\S*\s*\w{20}\s*(\d{5}\w{3})',
        file.read())
    # 将列表嵌套的元组修改为列表嵌套列表
    disk_all_new = []
    for i in disk_all_old:
        disk_all_new.append(list(i))
    # pprint.pprint(disk_all_new)
    # 根据编码，添加硬盘大小，输出['CTE0', 'SSD', '02351KES', '600GB']
    for i in disk_all_new:
        if i[2] == '02351KES':
            i.append('600GB')
        elif i[2] == '02351FMY':
            i.append('600GB')
        elif i[2] == '02351SBG':
            i.append('960GB')
        elif i[2] == '02351KEU':
            i.append('900GB')
        elif i[2] == '02352CLK':
            i.append('960GB')
        elif i[2] == '02351SCD':
            i.append('1.92TB')
        elif i[2] == '02354DRS':
            i.append('3.84TB')
        elif i[2] == '02351KBT':
            i.append('1.2TB')
        elif i[2] == '02352WEB':
            i.append('1.2TB')
        elif i[2] == '02350CDV':
            i.append('1.2TB')
        elif i[2] == '02350GDA':
            i.append('1.8TB')
        elif i[2] == '02350MQG':
            i.append('8TB')
        elif i[2] == '02351KEN':
            i.append('8TB')
        elif i[2] == '02352WFV':
            i.append('8TB')
    # pprint.pprint(disk_all_new)
    return disk_all_new


def get_one_shelf_disk(file):
    """输出shelf中disk信息到数据库中"""
    result = get_disk(file)
    # 删除编码，以便于去重，计算['CTE0', 'SSD', '600GB']出现个数
    for i in result:
        i.pop(2)
    disk_kind_withshelf = []  # disk_kind_withshelf种类
    [disk_kind_withshelf.append(j) for j in result if j not in disk_kind_withshelf]
    # 添加种类的数量['CTE0', 'SSD', '600GB', 9]
    for i in disk_kind_withshelf:
        num = result.count(i)
        i.append(num)

    # pprint.pprint(result)
    # print(disk_kind_withshelf)
    # 写入数据库
    for kind in disk_kind_withshelf:
        device = kind[0]
        typedisk = kind[1]
        size = kind[2]
        num = kind[3]
        cursor.execute(f"insert into disk_kind_shelf values ('{device}', '{typedisk}', '{size}', {num})")


def get_shelf_include_contr(file):
    """输出shelf信息表到数据库中"""
    file.seek(0)
    contr_all = re.findall(r'Enclosure ID:\s(CTE\d).*?Logic Type: Engine.*?SN:\s(\w{20}).*?OceanStor (\d{4}\s\w{2})',
                           file.read(), re.S)
    file.seek(0)
    shelf_all = re.findall(
        r'Enclosure ID:\s(DAE\d{3}).{1,10}?Logic Type: Expansion Enclosure.*?SN: (\w{20}).*?Disk Units?\S(\w{1,10})',
        file.read(), re.S)
    contr_list = list(set(contr_all))
    shelf_list = list(set(shelf_all))
    # pprint.pprint(contr_list)
    # pprint.pprint(shelf_list)

    # 写入数据库
    for kind in contr_list:
        device = kind[0]
        sn = kind[1]
        typeshelf = kind[2]
        cursor.execute(f"insert into shelf_include_contr values ('{device}', '{sn}', '{typeshelf}')")

    for kind in shelf_list:
        device = kind[0]
        sn = kind[1]
        typeshelf = kind[2]
        cursor.execute(f"insert into shelf_include_contr values ('{device}', '{sn}', '{typeshelf}')")


def get_shelf_exclude_contr(file):
    """输出shelf信息表到数据库中"""
    file.seek(0)

    shelf_all = re.findall(
        r'Enclosure ID:\s(DAE\d{3}).{1,10}?Logic Type: Expansion Enclosure.*?SN: (\w{20}).*?Disk Units?\S(\w{1,10})',
        file.read(), re.S)
    shelf_list = list(set(shelf_all))
    # pprint.pprint(shelf_list)

    # 写入数据库
    for kind in shelf_list:
        device = kind[0]
        sn = kind[1]
        typeshelf = kind[2]
        cursor.execute(f"insert into shelf_include_contr values ('{device}', '{sn}', '{typeshelf}')")


def get_license(file):
    file.seek(0)
    license1 = re.findall(r'Feature Name:(\w+\s?\w+)', file.read())
    return license1


if __name__ == '__main__':
    import pymysql
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='P@ssw0rd', database='python', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("create table disk_kind_shelf (device varchar(40), typedisk varchar(40), size varchar(40), number int)")
    cursor.execute("create table shelf_include_contr (device varchar(40), sn varchar(40), typeshelf varchar(40))")

    f = open('config_szu_lcsl.txt', 'r', encoding='utf-8')
    print(get_model(f))
    print(get_hostname(f))
    print(get_sn(f))
    print(get_version(f))

    f.seek(0)
    Model = re.search(r'Product Model:\s(\d{4})', f.read()).group(1)
    if Model in ['5300', '5500', '5310', '5510']:
        get_one_shelf_disk(f)
        get_shelf_include_contr(f)
    else:
        get_one_shelf_disk(f)
        get_shelf_exclude_contr(f)

    # 根据数据库中表，输出shelf 和 disk信息
    # 获取device
    cursor.execute("select device from shelf_include_contr")
    response1 = cursor.fetchall()
    for i in response1:
        device = i[0]

        # 根据device，在两张表中搜索并输出结果
        # 获取shelf信息
        cursor.execute("select * from shelf_include_contr where device=%s", device)
        response2 = cursor.fetchall()
        s1 = ''
        for j in response2:
            s1 += f'{j[0]:<6} {j[2]:<10} ({j[1]}), '
            # 获取硬盘信息
            cursor.execute("select * from disk_kind_shelf where device=%s", i[0])
            response3 = cursor.fetchall()
            for k in response3:
                if response3.index(k) == len(response3) - 1:
                    s1 += f'{k[3]}块 {k[2]} {k[1]}硬盘'
                else:
                    s1 += f'{k[3]}块 {k[2]} {k[1]}硬盘 + '
        print(s1)
    cursor.execute("drop table disk_kind_shelf")
    cursor.execute("drop table shelf_include_contr")
    conn.commit()
    cursor.close()
    conn.close()
    # 输出license信息
    license2 = get_license(f)
    print("、".join(license2))

    f.close()
