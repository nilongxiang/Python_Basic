#!/usr/bin/env python3
# -*- coding=utf-8 -*-

class Person:
    def __init__(self, name, age, pay=0, job=None):  # 初始化函数
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__(self):
        return f'Class: {self.__class__.__name__:7} ==> Name: {self.name:10}, Pay: {self.pay:5}, Job: {self.job}'

    def getlastname(self):
        return self.name.split()[1]

    def giveraise(self, percent):
        return int(self.pay * (1 + percent))

if __name__ == '__main__':
    print("=" * 15 + ' result ' + "=" * 15)
    bob = Person('Bob Smith', 22, 5000)
    sue = Person('Sue John', 25, 6000, 'engineer')
    print(bob.name)
    print(bob.job)
    print(bob.pay)
    bob.pay = int(bob.pay * (1 + 0.1))  # 修改了 bob.pay的属性值
    print(bob.pay)
    print(bob.getlastname())
    print(bob.giveraise(0.1))
    print(bob.giveraise(0.1))

    print(sue.job)


