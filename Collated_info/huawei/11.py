#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re
f = open('config.txt', 'r', encoding='utf-8')

shelf_all = re.findall(r'Enclosure ID:\s(DAE\d{3}).{1,10}?Logic Type: Expansion Enclosure.*?SN: (\w{20}).*?Disk Units?\S(\w{1,10})', f.read(), re.S)
print(shelf_all)



if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
