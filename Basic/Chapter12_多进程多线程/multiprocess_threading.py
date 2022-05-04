#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import multiprocessing
import threading
import time
from datetime import datetime


def fun1():
    time.sleep(2)

# 进程
p1 = multiprocessing.Process(target=fun1)  # 创建子进程
p1.start()
print(datetime.now().strftime('%X'))
p1.join()
print(datetime.now().strftime('%X'))

# 进程池，使用场景：任务周期短且需要频繁创建
p2 = multiprocessing.Pool(processes=4)
p2.apply_async(fun1)
p2.close()  # 关闭进程池，无法再加入事件
p2.join()  # 回收进程池

# 线程
p3 = threading.Thread(target=fun1)
p3.start()
p3.join()


if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
