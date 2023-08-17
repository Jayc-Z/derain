# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 18:37
# @Author  : Curry
# @File    : merge_sort.py

# 时间复杂度O(nlogn) 空间复杂度O(n)
# 一般情况下，运行时间：快速排序<归并排序<堆排序
# NB三人组小结
'''
缺点：
快速排序：极端情况下排序效率低
归并排序：需要额外的内存开销
堆排序：在快的排序算法中相对较慢
'''
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp

def mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(li, low, mid)
        mergesort(li, mid+1, high)
        merge(li, low, mid, high)

li = list(range(1000))
import random
random.shuffle(li)
mergesort(li, 0, 999)
print(li)
