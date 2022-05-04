#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import xmltodict
from pprint import pprint

xml_file = open('test.xml', 'r').read()
xmldict = xmltodict.parse(xml_file, encoding='utf-8')
# pprint(xmldict)

departs = xmldict['root']['公司']['部门']
depart_teacher_dict = {}

for i in departs:
    # pprint(i)
    # pprint(i['课程']['@name'])
    # pprint(i['师资']['老师'])
    depart_teacher_dict.update({i['课程']['@name']: [j['@name'] for j in i['师资']['老师']]})

pprint(depart_teacher_dict)


if __name__ == '__main__':
    print("=" * 15 + ' result ' + "=" * 15)
