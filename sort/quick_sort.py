# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 1:47
# @Author  : Curry
# @File    : quick_sort.py

# 快速排序时间复杂度 O(nlogn)
# [5, 1, 2, 6, 7, 3, 8]
from numpy.random import rand

def partition(data, left, right):
    temp = data[left]
    while left < right:
        while left < right and data[right] >= temp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= temp:
            left += 1
        data[right] = data[left]
        print(data)
    data[left] = temp
    return left

def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)
    return data

data = [5, 1, 2, 6, 7, 3, 8]
left = 0
right = len(data) - 1
new = quick_sort(data, left, right)
print(new)