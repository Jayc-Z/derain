# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 0:35
# @Author  : Curry
# @File    : radix_sort.py

# 基数排序
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)
        li.clear()
        for bucket in buckets:
            li.extend(bucket)

        it += 1
    return li


import random
li = list(random.randint(0, 10000) for _ in range(100000))
random.shuffle(li)
new = radix_sort(li)
print(new)
