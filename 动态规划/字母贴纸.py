# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 22:47
# @Author  : Curry
# @File    : 字母贴纸.py


'''
arr每一个字符串，代表一张贴纸，你可以把单个字符剪开使用，目的是拼出str来。
返回需要至少多少张贴纸可以完成这个任务。
例子：str= "babac"，arr = {"ba","c","abcd"}。
'''
class Solution:
    def MinNum(self, s, a):
        minnum = self.process(s, a)
        if minnum != float("inf"):
            return minnum
        else:
            return -1

    def process(self, s, a):
        if len(s) == 0 or len(a) == 0:
            return 0
        minnum = float("inf")
        # 选中每一张贴纸，然后递归出此情况下最少的张数
        for first in a:
            rest = self.minus(s, first)
            if len(rest) != len(s):
                minnum = min(minnum, self.process(rest, a))
        if minnum != float("inf"):
            minnum += 1
        else:
            minnum += 0
        return minnum

    def minus(self, s1, s2):
        hashtable = dict()
        s1 = sorted(s1)
        for i in s1:
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        for item in s2:
            if item in hashtable:
                hashtable[item] -= 1
        rest = ""
        for key, value in hashtable.items():
            rest += key * value
        return rest


# 后续优化思路
# 1、s作字符统计
# 2、a作二维数组的字符统计
# 3、**从原本的a中第一个开始遍历改为先消掉s中某字符开始遍历

if __name__ == '__main__':
    s = "babacdadabc"
    a = {"ba", "c", "abcd"}
    solution = Solution()
    res = solution.process(s, a)
    print(res)
