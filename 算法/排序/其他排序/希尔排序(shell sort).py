# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 20:16
# @Author  : Curry
# @File    : 希尔排序(shell sort).py

'''
1、取一个整数d1=n/2,将元素分为d1组,每组相邻元素之间距离为d1,在组内直接插入排序
2、取d2=d1/2,重复操作，直到dn=1
'''

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  #i表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  #j指的是手里的牌的下标
        while li[j] > tmp and j >= 0:
            li[j+1] = li[j]
            j -= gap
        li[j+gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d = d // 2

li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)

shell_sort(li)
print(li)
