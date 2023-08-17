# -*- coding: utf-8 -*-
# @Time    : 2023/6/12 22:40
# @Author  : Curry
# @File    : 最长回文子串.py

'''
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

输入：s = "cbbd"
输出："bb"
'''

def lpr(s):
    n = len(s)
    if n < 2:
        return s
    c = [["O" for _ in range(n)] for _ in range(n)]
    max_len = 1
    begin = 0
    for i in range(n):
        for j in range(n):
            if i <= j:
                if i == j:
                    c[i][j] = "O"
                elif s[i] == s[j]:
                    c[i][j] = "T"
                    l = j - i + 1
                    if l > max_len:
                        begin = i
                        max_len = l
                else:
                    c[i][j] = "F"
    for _ in c:
        print(_)

    return s[begin:begin + max_len]

# s = "aacabdkacaa"
# stri = lpr(s)
# print(stri)

def longestPalindrome(s: str):
    n = len(s)
    if n < 2:
        return s

    max_len = 1
    begin = 0
    # dp[i][j] 表示 s[i..j] 是否是回文串
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    # 递推开始
    # 先枚举子串长度
    for L in range(2, n + 1):
        # 枚举左边界，左边界的上限设置可以宽松一些
        for i in range(n):
            # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
            j = L + i - 1
            # 如果右边界越界，就可以退出当前循环
            if j >= n:
                break
            if s[i] != s[j]:
                dp[i][j] = False
            else:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]

            # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i
    return s[begin:begin + max_len]
s = "aacabdkacaa"
srt = longestPalindrome(s)