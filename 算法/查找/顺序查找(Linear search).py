# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 23:41
# @Author  : Curry
# @File    : 顺序查找(Linear search).py

# 时间复杂度O(n)
def linear_search(li, val):
    '''
    :param li: 输入线性表
    :param val: 待查找元素
    :return:
    '''
    for ind, value in enumerate(li):
        if value == val:
            return ind
        else:
            return None

li = [1, 2, 3, 4]
val = 3
ind = linear_search(li, val)
print(ind)