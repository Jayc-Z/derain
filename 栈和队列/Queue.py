# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 2:29
# @Author  : Curry
# @File    : Queue.py

class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.front = 0
        self.rear = 0
        self.size = size

    def push(self, element):
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError
    #判断队空
    def is_empty(self):
        return self.front == self.rear

    #判断队满
    def is_full(self):
        return (self.rear + 1) % self.size == self.front


