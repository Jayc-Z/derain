# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 21:51
# @Author  : Curry
# @File    : 快速排序(quick sort).py

'''
快速排序思路：
1、取一个元素p（第一个数），使元素p归位
2、列表被p分为两部分，左边都比p小，右边都比p大
3、递归完成排序
'''
# 时间复杂度O(nlogn)
def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:#从右边找比tmp小的数
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left

def quick_sort(data, left, right):
    '''
    :param data: 列表
    :param left: 左下标
    :param right: 右下标
    :return:
    '''
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid-1)
        quick_sort(data, mid+1, right)

li = [3, 1, 2, 5, 4, 6, 8]
# partition(li, 0, len(li)-1)
quick_sort(li, 0, len(li)-1)
print(li)