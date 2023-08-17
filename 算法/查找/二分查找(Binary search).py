# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 23:53
# @Author  : Curry
# @File    : 二分查找(Binary search).py


#时间复杂度 O(logn)
def binary_search(li, val):
    '''
    :param li: 输入有序线性表
    :param val: 待查找元素
    :return:
    '''
    left = 0
    right = len(li)
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

li = range(99)
val = 98
ind = binary_search(li, val)
print(ind)