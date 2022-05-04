#!/usr/bin/python3
# -*- coding=utf-8 -*-
import paramiko
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
import time
import re
from datetime import datetime


def ssh_client(ip, username, password):
    ssh = paramiko.SSHClient()  # 创建ssh实例
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加主机密钥策略known_hosts，不在文件中记录的主机将无法连接
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # 连接SSH服务端

    # 创建文件 /tmp/andycheck___192.168.151.22___22_05_04.txt
    new_file = datetime.now().strftime('%y_%m_%d')
    f_result = open(f"/tmp/andycheck___{ip}___{new_file}.txt", 'w')

    f_cmd = open(r"cmds.txt", 'r')
    for cmd in f_cmd.readlines():
        if not re.match(r'\w', cmd):
            break
        stdin, stdout, stderr = ssh.exec_command(cmd)

        # 写入文件
        f_result.write('=' * 100)
        f_result.write('\n')
        f_result.write('# ')
        f_result.write(cmd)
        f_result.write('\n')
        f_result.write(stdout.read().decode('utf-8'))
        f_result.write('\n')

        time.sleep(2)  # 每执行一条命令 sleep 2秒

    f_cmd.seek(0)
    f_cmd.close()
    f_result.close()


if __name__ == '__main__':
    cpus = cpu_count()
    pool = ThreadPool(processes=cpus)

    f_host = open(r"hosts.txt", 'r')

    for text in f_host.readlines():
        if not re.match(r'\w', text):
            break
        text = text.strip().split(",")
        ip1, username1, passwd1 = text[0], text[1], text[2]  # 交互对称赋值

        # ssh_client(ip1, username1, passwd1)
        pool.apply_async(ssh_client, args=(ip1, username1, passwd1))
    pool.close()
    pool.join()

    f_host.close()

