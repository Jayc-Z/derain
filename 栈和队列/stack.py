# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 2:02
# @Author  : Curry
# @File    : stack.py

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def gettop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack)==0

# 括号匹配问题
def brace_match(s):
    match = {"}":"{", "]":"[", ")":"("}
    stack = Stack()
    for ch in s:
        if ch in ["{", "[", "("]:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.gettop() == match[ch]:
                stack.pop()
            else:
                return False
    return stack.is_empty()
s = "{}{}{{[]}}"

solution = brace_match(s)
print(solution)