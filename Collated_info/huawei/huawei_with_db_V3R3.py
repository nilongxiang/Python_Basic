# !/usr/bin/env python3
# -*- coding=utf-8 -*-
"""
该脚本需要利用到华为存储巡检日志压缩包里InspectorResult\data\config\10.5.189.107_2102351QLH9WKB800013下config.txt
支持设备： V3R3 & 2600 V3R6 & Dorado 5000V3
"""
from huawei_with_db import get_model, get_hostname, get_sn, get_version, get_disk_kind_for_shelf, get_license
import pprint
import re
import os

print(os.path.dirname(__file__))  # 获取脚本运行路径
os.chdir(os.path.dirname(__file__))


def get_contr(file):
    result = get_model(file)
    file.seek(0)
    contr_all = re.findall(r'Enclosure ID:\s(CTE\d).{0,10}Logic Type:.*?SN:\s(\w{20})', file.read(), re.S)
    contr_list = list(set(contr_all))
    # pprint.pprint(contr_list)
    return contr_list


def get_shelf(file):
    file.seek(0)
    shelf_all = re.findall(r'Enclosure ID:\s(DAE\d{3}).{1,10}?Logic Type:.*?SN: (\w{20})', file.read(), re.S)
    shelf_list = list(set(shelf_all))
    # pprint.pprint(shelf_list)
    return shelf_list


if __name__ == '__main__':
    import pymysql
    # 连接数据库
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='P@ssw0rd', database='python', charset='utf8')
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

            # 获取shelf 和 disk 详细信息
            result_disk_kind_list = get_disk_kind_for_shelf(f)
            # 写入数据库
            for kind in result_disk_kind_list:
                device = kind[0]
                typedisk = kind[1]
                size = kind[2]
                num = kind[3]
                cursor.execute(f"insert into disk_kind_shelf values ('{device}', '{typedisk}', '{size}', {num})")

            f.seek(0)
            Model = re.search(r'Product Model:\s{1,2}(.*)', f.read()).group(1)
            Model = re.search(r'(\d{4,5})', Model).group(1)
            # print(Model)

            result_model = get_model(f)
            if Model in ['2600', '5000', '5300', '5500', '5310', '5510']:

                result_contr_list = get_contr(f)
                # 写入数据库
                for kind in result_contr_list:
                    device1 = kind[0]
                    sn = kind[1]
                    typeshelf = result_model
                    cursor.execute(f"insert into shelf_include_contr values ('{device1}', '{sn}', '{typeshelf}')")

                result_shelf_list = get_shelf(f)
                # 写入数据库
                for kind in result_shelf_list:
                    device3 = kind[0]
                    sn = kind[1]
                    typeshelf = 'DAE22525U2'
                    cursor.execute(f"insert into shelf_include_contr values ('{device3}', '{sn}', '{typeshelf}')")
            else:
                result_shelf_list = get_shelf(f)
                # 写入数据库
                for kind in result_shelf_list:
                    device3 = kind[0]
                    sn = kind[1]
                    typeshelf = 'DAE22525U2'
                    cursor.execute(f"insert into shelf_include_contr values ('{device3}', '{sn}', '{typeshelf}')")

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

