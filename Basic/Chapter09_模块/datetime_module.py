#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import datetime
from datetime import timedelta, timezone, datetime
# now = datetime.datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
#
#
# threeDayBefore = now - datetime.timedelta(days=3)
# threeDayAfter = now + datetime.timedelta(days=3)
#
# print(threeDayBefore)
# print(threeDayAfter)
#
# thirtyMinAfter = now + datetime.timedelta(minutes=30)
# print(thirtyMinAfter)

tzutc_8 = timezone(timedelta(hours=8))
print(tzutc_8)

shanghaitime = datetime.now().astimezone(tzutc_8)
print(shanghaitime)

if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
