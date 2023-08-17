# -*- coding: utf-8 -*-
# @Time    : 2023/3/9 22:58
# @Author  : Curry
# @File    : 两端取K个数和最大.py

'''
给定数组，两端取K个数，使得和最大
example: a = [4, 5, 1, 6, 7, 3, 1, 4], k=5
'''

def get_sum(li, k):
    assert k > 0 and k <= len(li)
    max_sum = None
    right = len(li) + 1 - k
    for left in range(k-1):
        item_sum = sum(li[:left+1]) + sum(li[right:])
        right += 1
        if max_sum is None or item_sum > max_sum:
            max_sum = item_sum
    return max_sum


a = [4, 5, 1, 6, 7, 3, 1, 4]
k=5
ms = get_sum(a, k)
print(ms)


