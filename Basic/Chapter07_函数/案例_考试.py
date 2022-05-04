#!/usr/bin/python3
# -*- coding=utf-8 -*-
import random


def exam():
    nums = [random.randint(1, 100) for i in range(2)]  # 随机生成2个数字
    nums.sort(reverse=True)  # 降序排列
    op = random.choice('+-')  # 随机选+-
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    counter = 0
    while counter < 3:
        prompt = "%s %s %s = " % (nums[0], op, nums[1])
        try:
            answer = int(input(prompt))
        except ValueError:
            continue
        except (KeyboardInterrupt, EOFError):
            continue

        if answer == result:
            print('很好很强大')
            break

        print('不对哟')
        counter += 1
    else:
        print('%s%s' % (prompt, result))


if __name__ == '__main__':
    while True:
        exam()
        try:
            yn = input("Continue(y/n)").strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'nN':
            print('Bye-bye')
            break

