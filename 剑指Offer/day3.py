#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# ------------------------------------------- 10-I. 斐波那契数列 -------------------------------------------
# ---------------------------------------------------
class Solution:
    def fib(self, n: int) -> int:
        """
        https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/solution/cong-di-gui-dao-dong-tai-gui-hua-by-lian-xi-shi-ch/
        """
        ####标准递归解法：
        # if n==0:return 0
        # if n==1:return 1
        # return (self.fib(n-1)+self.fib(n-2))%1000000007 # 但太多重复计算
        # ---------------------------------------------------
        ####带备忘录的递归解法
        # records = [-1 for i in range(n+1)] # 记录计算的值
        # if n == 0:return 0
        # if n == 1:return 1
        # if records[n] == -1: # 表明这个值没有算过
        #     records[n] = self.fib(n-1) +self.fib(n-2)
        # return records[n]
        # 递归输出超时,用记忆化递归规划，时间上优越很多。
        # ---------------------------------------------------
        ###DP方法：解决记忆化递归费内存的问题
        # dp={}
        # dp[0]=0
        # dp[1]=1
        # if n>=2:
        #     for i in range(2,n+1):
        #         dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]%1000000007
        # ---------------------------------------------------
        ###最优化DP方法：
        a, b = 0, 1
        for _ in range(n):
            """
            这样赋值没有改变b = a + b中a的值，但a = b,b = a + b这样a的值已改变
            或写成
            tmp = a
            a = b
            b = tmp +b
            """
            a, b = b, a + b
        return a % 1000000007


# ------------------------------------------- 10- II. 青蛙跳台阶问题 -------------------------------------------
# ---------------------------------------------------
def numWays(n: int) -> int:
    """
    其实就是斐波那契数列问题
    但台阶为0也是一种情况，所以不是0
    """
    a, b = 1, 1
    for _ in range(n):
        """
        这样赋值没有改变b = a + b中a的值，但a = b,b = a + b这样a的值已改变
        或写成
        tmp = a
        a = b
        b = tmp +b
        """
        a, b = b, a + b
    return a % 1000000007


# ------------------------------------------- 11. 旋转数组的最小数字 -------------------------------------------
# ---------------------------------------------------
def minArray(numbers):
    """
    二分法，利用旋转数组的特性
    """
    i, j = 0, len(numbers) - 1
    while i < j:
        m = (i + j) // 2
        if numbers[m] > numbers[j]:
            i = m + 1
        elif numbers[m] < numbers[j]:
            j = m
        else:
            j -= 1
    return numbers[i]
