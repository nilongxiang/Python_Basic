# #!/usr/bin/env python3
# # -*- coding=utf-8 -*-
import re, os


def get_model(file):
    file.seek(0)
    model = re.search(r'(cisco MDS \d{4}\w*)', file.read()).group(1)
    return model


def get_hostname(file):
    file.seek(0)
    hostname = re.search(r'ip host (\S*)', file.read()).group(1)
    return hostname


def get_version(file):
    file.seek(0)
    version = re.search(r'kickstart: version (\S*)', file.read()).group(1)
    return version


def get_sn(file):
    file.seek(0)
    sn = re.search(r'License hostid: VDH=(\S*)', file.read()).group(1)
    return sn


def get_port(file):
    file.seek(0)
    port_acquired = re.findall(r'fc1/\d{1,2}\s*\d{8}\s*acquired', file.read())

    file.seek(0)
    port_eligible = re.findall(r'fc1/\d{1,2}\s*\d{8}\s*eligible', file.read())

    port_all = len(port_acquired) + len(port_eligible)

    file.seek(0)
    no_sfp = re.findall(r'sfpAbsent', file.read())
    sfp_num = port_all - len(no_sfp)

    file.seek(0)
    speed = re.search(r'\d/\d/\d/(\d{1,2})', file.read()).group(1)

    return f'{port_all}口 * {speed}GB, {len(port_acquired)}口激活, {sfp_num}个光模块'


def get_vsan_id(file):
    file.seek(0)
    vsan_id = re.findall(r'fc\d/\d{1,2}\s*(\d{1,4})\s{2,3}0x', file.read())

    return list(set(vsan_id))


if __name__ == '__main__':
    for i in os.scandir(r'/PyCharmProject/Collated_info/mds/'):
        if i.name.endswith('.txt') or i.name.endswith('.log'):
            f = open(i.name, 'r', encoding='utf-8', errors='ignore')
            print(get_model(f))
            print(get_hostname(f))
            print(get_version(f))
            print(get_sn(f))
            print(get_port(f))
            vsan_id_list = get_vsan_id(f)
            for j in vsan_id_list:
                print(j)

            f.close()
            print("=" * 15 + ' result ' + "=" * 15)
            print()
