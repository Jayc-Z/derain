# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 20:01
# @Author  : Curry
# @File    : shell_sort.py

def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] >= tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp
    return li

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2
