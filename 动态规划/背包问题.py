# -*- coding: utf-8 -*-
# @Time    : 2023/8/8 22:38
# @Author  : Curry
# @File    : 背包问题.py


'''
w表示货物重量，v表示货物价值，bag表示背包容量，返回最大价值
'''

# 1.暴力递归
class Solution1:
    def maxValue(self, w ,v, bag):
        '''
        :param w: []
        :param v: []
        :param bag: int
        :return:
        '''
        if len(w) == 0 or len(v) == 0 or len(w) != len(v):
            return 0
        return self.process(w, v, 0, bag)

    def process(self, w, v, index, bag):
        '''
        :param w:
        :param v:
        :param index: 当前货物的下标
        :param bag:
        :return:
        '''
        if bag < 0:
            return -1
        if index >= len(w):
            return 0

        # 不选择当前index的货物
        p1 = self.process(w, v, index + 1, bag)

        # 选择当前index的货物
        p2 = 0
        next = self.process(w, v, index + 1, bag - w[index])
        if next != -1:
            p2 = v[index] + next
        return max(p1, p2)

# 3.dp
class Solution2:
    def dp_maxValue(self, w ,v, bag):
        '''
        :param w: []
        :param v: []
        :param bag: int
        :return:
        '''
        if len(w) == 0 or len(v) == 0 or len(w) != len(v):
            return 0
        n = len(w)
        dp = [[0 for _ in range(bag + 1)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for rest in range(bag+1):
                p1 = dp[i+1][rest]
                p2 = 0
                next = dp[i+1][rest-w[i]] if rest-w[i] >= 0 else -1
                if next != -1:
                    p2 = v[i] + next
                dp[i][rest] = max(p1, p2)
        return dp[0][bag]


if __name__ == '__main__':
    w = [1, 5, 6, 4 ,5]
    v = [2, 5, 4, 6 ,4]
    bag = 12
    solution = Solution1()
    maxvalue = solution.maxValue(w, v, bag)
    print(maxvalue)

    dp_solution = Solution2()
    dp_maxvalue = dp_solution.dp_maxValue(w ,v, bag)
    print(dp_maxvalue)