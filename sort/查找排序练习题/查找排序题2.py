# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 1:11
# @Author  : Curry
# @File    : 查找排序题2.py

'''
给定一个m*n的二维列表，查找一个数是否存在
列表特性：1、每行从左到右升序排列 2、每行第一个数比上一行最后一个数大
'''
import numpy as np

def solution(li, num):
    for sub_l in li:
        for i in sub_l:
            if num == i:
                return True

    else:
        return False

li = np.array(
    [[1, 3, 4, 6, 8],
    [10, 13, 15, 16, 18],
    [20, 21, 23, 25, 26]])

nums = [1, 5, 4, 30, 15, 2]
for num in nums:
    solution(li, num)