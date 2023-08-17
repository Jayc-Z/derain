# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 0:49
# @Author  : Curry
# @File    : 查找排序题1.py

'''
给定两个字符串s和t，判断t是否是s重新排序后的词
example: s = "anagram" , t = "nagaram"  ---> return true
        s = "dog" , t = "cat"  ---> return false
'''

def solution(s, t):
    len_s = len(s)
    len_t = len(t)
    if len_s != len_t:
        return False
    s_list = list(s)
    t_list = list(t)
    for i in s_list:
        if i not in t_list:
            return False
        else:
            t_list.remove(i)
    if len(t_list) == 0:
        return True

# s = "anagram"
# t = "nagaram"
s = "dog"
t = "cat"
get = solution(s, t)
print(get)