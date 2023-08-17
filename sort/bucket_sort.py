# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 22:26
# @Author  : Curry
# @File    : bucket_sort.py

def bucket_sort(li, n=100, max_num=10000):
    buckets = [[] for _ in range(n)]
    for val in li:
        i = min(val // (max_num // n), n-1)
        buckets[i].append(val)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1]= buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)

    return sorted_li

import random
li = list(random.randint(0, 10000) for _ in range(100000))
random.shuffle(li)
new = bucket_sort(li)
print(new)

