# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 21:30
# @Author  : Curry
# @File    : 插入排序(insert sort).py

#时间复杂度：O(n**2)
def insert_sort(li):
    for i in range(1, len(li)):  #i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1  #j指的是手里的牌的下标
        while li[j] > tmp and j >= 0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

li = [3, 1, 4, 6, 8, 2, 5]
insert_sort(li)



