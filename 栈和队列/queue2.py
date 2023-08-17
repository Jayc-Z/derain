# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 2:52
# @Author  : Curry
# @File    : queue2.py

from collections import deque

q = deque()
q.append(1) # 队尾进队
q.popleft() # 队首出队

# 用于双向队列
q.appendleft(1) # 队首进队
q.pop() # 队尾出队
