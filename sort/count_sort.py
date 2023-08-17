# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 21:58
# @Author  : Curry
# @File    : count_sort.py
import numpy as np

def count_sort(li):
    l = []
    count_dict = dict(zip(range(10), np.zeros(10)))
    for i in li:
        count_dict[i] += 1
    for k, v in count_dict.items():
        for i in range(int(v)):
            l.append(k)

    return  l

li = [1, 2, 5, 4, 3, 2, 5]
new = count_sort(li)
print(new)