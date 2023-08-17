# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 17:45
# @Author  : Curry
# @File    : heap2.py

import heapq
import random

li = list(range(100))
random.shuffle(li)
print(li)
heapq.heapify(li) # 建小根堆
n=len(li)
for i in range(10): # 每次弹出最小值
    print(heapq.heappop(li), end=",")