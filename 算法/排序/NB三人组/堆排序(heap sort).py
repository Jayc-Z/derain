# -*- coding: utf-8 -*-
# @Time    : 2023/6/10 19:21
# @Author  : Curry
# @File    : 堆排序(heap sort).py

# 时间复杂度O(nlogn)
# 调整
# 大根堆
def sift(li, low, high):
    '''
    :param li:列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    '''
    i = low  # i最开始指向根节点
    j = 2 * i + 1 # j开始是左孩子
    tmp = li[i] # 把堆顶存起来
    while j <= high:  # 只要j位置有数
        if j+1 < high and li[j+1] > li[j]:  # 如果右孩子大于左孩子
            j = j + 1   # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j               # 往下看一层
            j = 2 * i + 1
        else:
            li[i] = tmp  # 把tmp放在某一领导位置上
            break
    else:
        li[i] = tmp  # 把tmp放在叶子节点上

def heap_sort(li):
    n = len(li)
    # 建堆
    for i in range((n-2)//2, -1, -1):
        # i表示当前调整位置的根节点
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):
        # i指向最后一个位置
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high

li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)

