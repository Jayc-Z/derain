# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 0:11
# @Author  : Curry
# @File    : 冒泡排序(bubble sort).py

#时间复杂度：O(n**2)
import random

def bubble_sort(li):
    for i in range(len(li)): #第i趟
        exchange = False
        for j in range(len(li) - i -1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return

li = [random.randint(0, 10000) for i in range(1000)]
print(li)
bubble_sort(li)
print(li)