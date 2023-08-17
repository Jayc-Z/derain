# -*- coding: utf-8 -*-
# @Time    : 2023/3/1 16:39
# @Author  : Curry
# @File    : heap_sort.py

# 堆排序 时间复杂度O(nlogn)

def sift(li, low, high):
    '''
    :param li:列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    '''
    i = low # 初始根节点
    j = 2 * i + 1 # j初始左孩子
    tmp = li[low]  # 初始根节点值
    while j <= high:
        if j+1<=high and li[j+1] < li[j]:#右孩子有，且右孩子较大
            j = j+1   # 指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j     # 往下看一层
            j = 2 * i + 1
        else:
            break
    li[i] = tmp

# topk 问题 O(nlogk)
def topk(li, k):
    assert isinstance(k, int), "k is not a int"
    heap = li[:k]
    # 建堆
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 遍历剩余元素
    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 出数
    for i in range(k-1, -1, -1):   # 倒序遍历叶子节点
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap

def heap_sort(li):
    # 构造堆 农村包围城市
    n = len(li)
    for i in range((n-2)//2, -1, -1):  # 倒序遍历根节点
        # i 表示建堆时候调整的部分的根的下标
        sift(li, i, n-1) # for循环结束建堆完成
    for i in range(n-1, -1, -1):   # 倒序遍历叶子节点
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)
    return li

li = [i for i in range(1000)]
import random
random.shuffle(li)

new = topk(li, 10)
print(new)

