# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 1:54
# @Author  : Curry
# @File    : search.py

def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return None

l = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(l, 10)
print(index)

