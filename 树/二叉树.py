# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 21:26
# @Author  : Curry
# @File    : 二叉树.py

from collections import deque
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

root = e
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f


# 前序遍历 -- 先访问根节点 再左右孩子
def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


# 中序遍历 -- 先访问左孩子 再访问根节点 再访问右孩子
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


# 后序遍历 -- 先访问左右孩子 再访问根节点
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")

# 层次遍历 -- 从上到下、从左到右依次访问
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        print(root.data, end=",")
        if root.lchild:
            queue.append(root.lchild)
        if root.rchild:
            queue.append(root.rchild)

