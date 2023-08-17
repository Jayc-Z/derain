# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 0:03
# @Author  : Curry
# @File    : 数字字母对应.py


'''
自左到右
1 -> A ,2 -> B, 3 -> C, ..., 26 -> Z
给一个数字字符串能变多少种字母字符串
如 111：
AAA、AK、KA
'''

# 1.暴力递归
class Solution1:
    def MaxString(self, s):
        if len(s) <= 1:
            return 0
        return self.process(s, 0)

    # str[0, ..., index-1]无需过问
    # str[index,....]去转化，返回多少种转化方法
    def process(self, s, index):
        # 终止一次表示一种选择
        if index == len(s):
            return 1
        # 没到最后，说明有字符
        # 如果index单独面对0，则无效
        if s[index] == "0":
            return 0
        else:
            # 可能性1，index单转
            ways = self.process(s, index + 1)
            # 可能性2，index和index+1双转
            if index + 1 < len(s) and int(s[index]) * 10 + int(s[index+1]) < 27:
                ways += self.process(s, index + 2)
        return ways

# 3.dp
class Solution2:
    def dp_MaxString(self, s):
        if len(s) <= 1:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] != "0":
                # 可能性1，index单转
                dp[i] = dp[i+1]
                # 可能性2，index和index+1双转
                if i + 1 < len(s) and int(s[i]) * 10 + int(s[i + 1]) < 27:
                    dp[i] += dp[i + 2]

        return dp[0]

if __name__ == '__main__':
    s = "1231342131231231231231"
    solution = Solution1()
    ways = solution.MaxString(s)
    print(ways)

    dp_solution = Solution2()
    dp_ways = dp_solution.dp_MaxString(s)
    print(dp_ways)