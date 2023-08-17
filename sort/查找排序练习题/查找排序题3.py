# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 1:30
# @Author  : Curry
# @File    : 查找排序题3.py
'''
给定一个列表和数，返回列表中两数之和为该数的下标
'''

def solution(li, target):
    for index, num1 in enumerate(li):
        num2 = target - num1
        li_right = li[index:]
        if num2 in li_right:
            return (index, li[index:].index(num2))

li = [1, 5, 2, 4, 8, 3, 9]
target = 10
print(solution(li, target))