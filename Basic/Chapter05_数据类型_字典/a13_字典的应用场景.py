#!/usr/bin/python3
# -*- coding=utf-8 -*-
# 使用多个键值对，存储描述一个物体的相关信息 —— 描述更复杂的数据信息
# 将多个字典放在一个列表中，再进行遍历，在循环体内部针对每一个字典进行相同的处理

card_list = [
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "54321",
     "phone": "10086"}
]

for card_info in card_list:
    print(card_info)

