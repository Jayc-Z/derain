# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 20:47
# @Author  : Curry
# @File    : 计数排序(count sort).py

def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

import random
li = [random.randint(0, 100) for i in range(1000)]
random.shuffle(li)
print(li)
count_sort(li)
print(li)