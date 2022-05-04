#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from Person_class import Person


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, job='Manager')    # 调用父类的方法，将其关联起来，而不是重新完全重写类的方法

    def getfirstname(self):
        return self.name.split()[0]

    def giveraise(self, percent, bonus=0.1):  # 重新定制类的方法
        # return int(self.pay * (1 + percent + bonus))  # 不将父类的giveraise方法关联起来，导致父类修改后，子类却不变
        return Person.giveraise(self, percent + bonus)  # 调用父类的方法，将其关联起来，而不是重新完全重写类的方法


if __name__ == '__main__':
    bob = Person('Bob Smith', 22, 5000)
    sue = Person('Sue John', 25, 6000, 'engineer')
    tom = Manager('Tom Doe', 50, 10000)

    print(bob.getlastname())    # 继承
    print(tom.getlastname())    # 继承
    print(tom.getfirstname())   # 定制，Manager特有的方法

    print(tom.job)

    print(bob.giveraise(0.1))
    print(tom.giveraise(0.1))

    # person_list = [bob, sue, tom]
    # for i in person_list:
    #     print(i.giveraise(0.1))

    print(bob)
    print(tom)