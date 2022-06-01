#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import subprocess
import io


def system_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    proc.wait()
    stream_stdout = io.TextIOWrapper(proc.stdout)
    stream_stderr = io.TextIOWrapper(proc.stderr)

    return stream_stdout.read(), stream_stderr.read()


if __name__ == '__main__':
    exec_cmd = 'ls -l'
    # exec_cmd = 'lsl -l'
    # print(system_cmd(exec_cmd))     # 打印全部输出
    print(system_cmd(exec_cmd)[0])    # 打印正确输出
    # print(system_cmd(exec_cmd)[1])  # 打印错误输出

if __name__ == '__main__':
    pass
    print("=" * 15 + ' result ' + "=" * 15)
