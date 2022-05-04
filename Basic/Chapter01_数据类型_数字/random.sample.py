#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import random

choice_list = ['cisco', 'huawei', 'netapp', 'kubernetes']

result = random.sample(choice_list, 2)

print(result)


# ====== result ======
# ['cisco', 'netapp']

