# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 13:39
# @Author  : Curry
# @File    : 最长公共子序列.py

def solution(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    return c[m][n]


# 获取最长公共子序列
def get_lcs(x, y):
    i = len(x)
    j = len(y)
    c = [[0 for _ in range(i+1)] for _ in range(j+1)]
    res = ""
    while (i != 0) and (j != 0):
        if x[i-1] == y[j-1]:
            res += x[i-1]
            i -= 1
            j -= 1
        else:
            if c[i][j] == c[i-1][j]:
                i -= 1
            else:
                j -= 1
    return res[::-1]



x = "bdcaba"
y = "abcbda"
lcs = solution(x, y)
print(lcs)
l = get_lcs(x, y)
print(l)