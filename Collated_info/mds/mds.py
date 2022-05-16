# #!/usr/bin/env python3
# # -*- coding=utf-8 -*-
#
# import re
# import pprint
#
#
# def get_model(file):
#     file.seek(0)
#     model = re.search(r'CS_NAME (\w{6,11})', file.read()).group(1)
#     return model
#
#
# def get_hostname(file):
#     file.seek(0)
#     hostname = re.search(r'(\w+\S?\w+):\w*:admin', file.read()).group(1)
#     return hostname
#
#
# def get_version(file):
#     file.seek(0)
#     version = re.search(r'Fabos Version (\d.\d.\d\w)', file.read()).group(1)
#     return version
#
#
# def get_sfp(file):
#     file.seek(0)
#     port = re.findall(r'(\d{1,2})\s{2,3}(\d{1,2})\s*\w{6}\s*\S{2}\s*\w(\d{1,2})\s*\S*\s*FC\s{2}', file.read())
#     port_all_num = len(list(set(port)))
#     # print(port)
#
#     file.seek(0)
#     keyStart = 'dbgshow'
#     keyEnd = 'Power Supply #1'
#     pat = re.compile(keyStart + '(.*?)' + keyEnd, re.S)
#     result = pat.findall(file.read())
#     # pprint.pprint(result)
#     port_nolicense = re.findall(r'No POD [lL]icense', str(result))
#     port_nolicense_num = len(port_nolicense)
#     port_active_num = port_all_num - port_nolicense_num
#
#     file.seek(0)
#     port_nosfp = re.findall(r'No SFP installed in port', file.read())
#     port_nosfp_num = len(port_nosfp)
#     port_sfp_num = port_all_num - port_nosfp_num
#
#     port_speed = port[0][2]
#
#     return f'{port_active_num}口激活，{port_sfp_num}个{port_speed}GB光模块'
#
# if __name__ == '__main__':
#     f = open('config.txt', 'r', encoding='utf-8', errors='ignore')
#     print(get_model(f))
#     print(get_hostname(f))
#     print(get_version(f))
#     print(get_sfp(f))
#
#     f.close()
# if __name__ == '__main__':
#     pass
#     print("=" * 15 + ' result ' + "=" * 15)
