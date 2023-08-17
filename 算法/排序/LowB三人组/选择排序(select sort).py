# -*- coding: utf-8 -*-
# @Time    : 2023/6/8 0:56
# @Author  : Curry
# @File    : 选择排序(select sort).py

#时间复杂度：O(n**2)
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]

li = [3, 1, 2, 5, 4, 6, 8]
select_sort(li)
print(li)