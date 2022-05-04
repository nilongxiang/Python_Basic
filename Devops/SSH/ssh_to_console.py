#!/usr/bin/python3
# -*- coding=utf-8 -*-
import paramiko
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
import time
import re


def ssh_client(ip, username, password):
    ssh = paramiko.SSHClient()  # 创建ssh实例
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加主机密钥策略known_hosts，不在文件中记录的主机将无法连接
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)  # 连接SSH服务端

    f_cmd = open(r"cmds.txt", 'r')
    for cmd in f_cmd.readlines():
        if not re.match(r'\w', cmd):
            break
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(cmd, end='')
        print(stdout.read().decode('utf-8'))
        time.sleep(1)
    f_cmd.seek(0)
    f_cmd.close()


if __name__ == '__main__':
    # cpus = cpu_count()
    # pool = ThreadPool(processes=cpus)
    f_host = open(r"hosts.txt", 'r')

    for text in f_host.readlines():
        if not re.match(r'\w', text):
            break
        text = text.strip().split(",")
        ip1, username1, passwd1 = text[0], text[1], text[2]  # 交互对称赋值

        ssh_client(ip1, username1, passwd1)
    #     pool.apply_async(ssh_client, args=(ip1, username1, passwd1))
    # pool.close()
    # pool.join()
    f_host.close()
