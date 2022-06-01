#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from datetime import datetime
import os


print(f'当前时间： {datetime.now().strftime("%Y_%m-%d %H:%M:%S")}')

for path, dirs, files in os.walk(r'/tmp'):
    for file in files:
        absPathFile = os.path.join(path, file)
        modifyTime = datetime.fromtimestamp(os.path.getatime(absPathFile))
        now = datetime.now()
        diffTime = now - modifyTime
        print(f'{absPathFile:27s}修改时间[{modifyTime.strftime("%Y_%m-%d %H:%M:%S")}] 距今[{diffTime.days:3d}天{diffTime.seconds//3600:2d}时{(diffTime.seconds%3600)//60:2d}分 ]')
if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
