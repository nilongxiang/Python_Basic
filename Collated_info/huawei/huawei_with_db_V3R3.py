# !/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
该脚本需要利用到华为存储巡检日志压缩包里InspectorResult\data\config\10.5.189.107_2102351QLH9WKB800013下config.txt
支持设备： V3R3 & 2600 V3R6 & Dorado 5000V3
"""

import pprint
import re
import os

print(os.path.dirname(__file__))  # 获取脚本运行路径
os.chdir(os.path.dirname(__file__))


def get_model(file):
    file.seek(0)
    model = re.search(r'Product Model:\s{1,2}(.*)', file.read()).group(1)
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
        r'(\w{3}\d{1,3}).\d{1,2}\s*Normal\s*Online\s*(\w{3,8})\s*\w*.\w*\s*\w*\s\w*\s*\S*\s*\S*\s*\S*\s*\w{20}\s*(\d{5}\w{3})',
        file.read())
    # 将列表嵌套的元组修改为列表嵌套列表
    disk_all_new = []
    for i in disk_all_old:
        disk_all_new.append(list(i))
    # pprint.pprint(disk_all_new)
    # 根据编码，添加硬盘大小，输出['CTE0', 'SSD', '02351KES', '600GB']
    for i in disk_all_new:
        # SSD
        if i[2] == '02351KES' or i[2] == '02351FMY' or i[2] == '02351FPP' or i[2] == '02350LHE':
            i.append('600GB')
        elif i[2] == '02351KEU':
            i.append('900GB')
        elif i[2] == '02351SBG' or i[2] == '02352CLK':
            i.append('960GB')
        elif i[2] == '02351KCM':
            i.append('1.8TB')
        elif i[2] == '02351SCD' or i[2] == '02352AND' or i[2] == '02352ANE' or i[2] == '02353JWM' or i[2] == '02352AND' \
                or i[2] == '02352XBN':
            i.append('1.92TB')
        elif i[2] == '02354DRS' or i[2] == '02352XBP' or i[2] == '02353JWB' or i[2] == '02352SGG' or i[2] == '02354MFN' \
                or i[2] == '02351SCN' or i[2] == '02352CMF' or i[2] == '02353LQH' or i[2] == '02354MBR':
            i.append('3.84TB')

        # SAS
        elif i[2] == '02350BVP' or i[2] == '02351KBS' or i[2] == '02350WLE' or i[2] == '02351SGE':
            i.append('600GB')
        elif i[2] == '02350SLV':
            i.append('900GB')
        elif i[2] == '02351KBT' or i[2] == '02351SGB' or i[2] == '02350CDU' or i[2] == '02352WEB' or i[2] == '02350CDV' \
                or i[2] == '02311JBM':
            i.append('1.2TB')
        elif i[2] == '02350GDA' or i[2] == '02351KEG':
            i.append('1.8TB')
        elif i[2] == '02352WEK' or i[2] == '02352UNV':
            i.append('2.4TB')

        # NL_SAS
        elif i[2] == '02350BVT':
            i.append('4TB')
        elif i[2] == '02351KEN' or i[2] == '02350MQG' or i[2] == '02352WFV':
            i.append('8TB')

    # pprint.pprint(disk_all_new)
    return disk_all_new


def get_disk_kind_for_shelf(file):
    """输出shelf中disk信息到数据库中"""
    result = get_disk(file)
    # pprint.pprint(result)
    # 删除编码，以便于去重，计算['CTE0', 'SSD', '600GB']出现个数
    for i in result:
        i.pop(2)
    disk_kind_withshelf = []  # disk_kind_withshelf种类
    [disk_kind_withshelf.append(j) for j in result if j not in disk_kind_withshelf]
    # 添加种类的数量['CTE0', 'SSD', '600GB', 9]
    for i in disk_kind_withshelf:
        num = result.count(i)
        i.append(num)
    # print(disk_kind_withshelf)

    # 写入数据库
    for kind in disk_kind_withshelf:
        device = kind[0]
        typedisk = kind[1]
        size = kind[2]
        num = kind[3]
        cursor.execute(f"insert into disk_kind_shelf values ('{device}', '{typedisk}', '{size}', {num})")


def get_contr(file):
    """输出shelf信息表到数据库中"""
    result = get_model(file)

    file.seek(0)
    contr_all = re.findall(r'Enclosure ID:\s(CTE\d).{0,10}Logic Type:.*?SN:\s(\w{20})', file.read(), re.S)
    contr_list = list(set(contr_all))
    # pprint.pprint(contr_list)

    # 写入数据库
    for kind in contr_list:
        device1 = kind[0]
        sn = kind[1]
        typeshelf = result
        cursor.execute(f"insert into shelf_include_contr values ('{device1}', '{sn}', '{typeshelf}')")


def get_shelf(file):
    """输出shelf信息表到数据库中"""
    file.seek(0)
    shelf_all = re.findall(r'Enclosure ID:\s(DAE\d{3}).{1,10}?Logic Type:.*?SN: (\w{20})', file.read(), re.S)
    shelf_list = list(set(shelf_all))
    # pprint.pprint(shelf_list)

    # 写入数据库
    for kind in shelf_list:
        device3 = kind[0]
        sn = kind[1]
        typeshelf = 'DAE22525U2'
        cursor.execute(f"insert into shelf_include_contr values ('{device3}', '{sn}', '{typeshelf}')")


def get_license(file):
    file.seek(0)
    license1 = re.findall(r'Feature Name:(\w+\s?\w+)', file.read())
    return license1


if __name__ == '__main__':
    import pymysql
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='P@ssw0rd', database='python',
                           charset='utf8')
    cursor = conn.cursor()

    for i in os.scandir(r'/PyCharmProject/Collated_info/huawei/'):
        if i.name.endswith('.txt') or i.name.endswith('.log'):
            cursor.execute(
                "create table disk_kind_shelf (device varchar(40), typedisk varchar(40), size varchar(40), number int)")
            cursor.execute(
                "create table shelf_include_contr (device varchar(40), sn varchar(40), typeshelf varchar(40))")
            f = open(i.name, 'r', encoding='utf-8', errors='ignore')
            print(get_model(f))
            print(get_hostname(f))
            print(get_sn(f))
            print(get_version(f))

            f.seek(0)
            Model = re.search(r'Product Model:\s{1,2}(.*)', f.read()).group(1)
            Model = re.search(r'(\d{4,5})', Model).group(1)
            # print(Model)
            if Model in ['2600', '5000', '5300', '5500', '5310', '5510']:
                get_disk_kind_for_shelf(f)
                get_contr(f)
                get_shelf(f)
            else:
                get_disk_kind_for_shelf(f)
                get_shelf(f)

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
                    cursor.execute("select * from disk_kind_shelf where device=%s", j[0])
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

            # 输出license信息
            license2 = get_license(f)
            print("、".join(license2))
            f.close()
            print('=' * 100)
            print()
    cursor.close()
    conn.close()

