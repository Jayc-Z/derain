# -*- coding: utf-8 -*-
# @Time    : 2023/6/7 23:24
# @Author  : Curry
# @File    : 汉诺塔.py

'''递归的两个条件：
1、调用自身
2、终止条件
'''
def hanoi(n, a, b, c):
    '''
    :param n: 盘子的个数
    :param a: 柱子的名字
    :param b: 柱子的名字
    :param c: 柱子的名字
    :return:
    '''
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s"%(a, c))
        hanoi(n-1, b, a, c)

hanoi(64, "A", "B", "C")
