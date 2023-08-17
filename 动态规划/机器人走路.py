# -*- coding: utf-8 -*-
# @Time    : 2023/8/7 22:47
# @Author  : Curry
# @File    : 机器人走路.py

"""
假设有排成一行的N个位置，记为：1~N，N一定大于或等于2
开始时机器人在其中的M位置上(M一定是1~N中的一个)
如果机器人来到1的位置，那么下一步只能往右来到2的位置
如果机器人来到N的位置，那么下一步只能往左来到N-1的位置
如果机器人来到中间位置，那么下一步可以往左走或者往右走
规定机器人开始在M位置，必须走K步，最终能来到P位置(P也是1~N中的一个)的方法有多少种
给定四个参数 N、M、K、P,返回方法数。
"""

# 1.暴力递归
def process(cur, rest, aim, N, dp):
    '''
    :param cur: 当前位置 1~N
    :param rest: 剩余步数 0~k
    :param aim: 目标位置
    :param N: 最大位置
    :return:
    '''
    if rest == 0:
        return 1 if cur == aim else 0
    if cur == 1:
        return process(2, rest-1, aim, N, dp)
    if cur == N:
        return process(N-1, rest-1, aim, N, dp)
    return process(cur-1, rest-1, aim, N, dp) + process(cur+1, rest-1, aim, N, dp)

# 2.傻缓存（带递归的DP）
def way1(cur, rest, aim, N):
    dp = [[-1 for _ in range(rest+1)] for _ in range(N+1)]
    if dp[rest][cur] != -1:
        return dp[rest][cur]

    else:
        ans = 0
        if rest == 0:
            ans = 1 if cur == aim else 0
        if cur == 1:
            ans = process(2, rest-1, aim, N, dp)
        if cur == N:
            ans = process(N-1, rest-1, aim, N, dp)
        else:
            ans = process(cur-1, rest-1, aim, N, dp) + process(cur+1, rest-1, aim, N, dp)
        dp[rest][cur] = ans
        return ans

# 3.找各位置依赖关系，填满DP表
def dp_solution(cur, rest, aim, N):
    dp = [[0 for _ in range(rest + 1)] for _ in range(N + 1)]
    for i in range(rest+1):
        for j in range(1, N+1):
            if i == 0:
                dp[i][aim] = 1
            if j == 1:
                dp[i][j] = dp[i-1][j+1]
            if j == N:
                dp[i][j] = dp[i-1][j-1]
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    ans = dp[rest][cur]
    return ans
cur, rest, aim, N = 3, 5, 6, 10

ans = dp_solution(cur, rest, aim, N)
print(ans)