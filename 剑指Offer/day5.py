#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# ------------------------------------------- 14-II. 剪绳子 -------------------------------------------
# ---------------------------------------------------
# import math
n1 = 2
n2 = 10


def cuttingRope(n):
    """
    贪婪算法
    Python 中常见有三种幂计算函数： * 和 pow() 的时间复杂度均为 O(loga) ；
    而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)。
    """
    # if n <= 3:
    #     return n - 1  # 题目要求必须切割
    # a, b = n // 3, n % 3
    # if b == 0:
    #     return int(math.pow(3, a)) % 1000000007
    # if b == 1:
    #     return int(math.pow(3, a - 1) * 4) % 1000000007
    # return int(math.pow(3, a) * 2) % 1000000007  # b == 1的情况
    # 这样做会因为math.pow(3, a) 在大数下有精度损失导致最后结果出错

    # ---------------------------------------------------
    if n <= 3:
        return n - 1  # 题目要求必须切割
    a, b = n // 3, n % 3
    if b == 0:
        return (3 ** a) % 1000000007
    if b == 1:
        return (3 ** (a - 1) * 4) % 1000000007
    return ((3 ** a) * 2) % 1000000007  # b == 1的情况


# ---------------------------------------------------
def cuttingRope(n):
    """
    贪婪算法
    此题与 面试题14-I. 剪绳子主体等价，唯一不同在于本题目涉及 “大数越界情况下的求余问题”
    https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
    """
    if n <= 3:
        return n - 1
    a, b, p, x, rem = n // 3 - 1, n % 3, 1000000007, 3, 1
    while a > 0:  # 快速幂求余,a只用来控制循环次数，从而实现次幂
        if a % 2:
            rem = (rem * x) % p
        x = x ** 2 % p
        a //= 2
    if b == 0:
        return (rem * 3) % p  # = 3^(a+1) % p
    if b == 1:
        return (rem * 4) % p  # = 3^a * 4 % p
    return (rem * 6) % p  # = 3^(a+1) * 2  % p


print(cuttingRope(n1))
print(cuttingRope(n2))

# ------------------------------------------- 15. 二进制中1的个数 -------------------------------------------
# ---------------------------------------------------14-II. 剪绳子,15. 二进制中1的个数,
n1 = 00000000000000000000000000001011
n2 = 11111111111111111111111111111101


def hammingWeight(n):
    """
    逐位判断
    https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
    """
    res = 0
    while n:
        res += n & 1
        n >>= 1  # 将二进制数字 n 无符号右移一位
    return res


# ---------------------------------------------------
def hammingWeight(n):
    """
    巧用 n&(n−1)
    https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
    """
    res = 0
    while n:
        res += 1
        n &= n - 1
    return res


print(hammingWeight(n1))
print(hammingWeight(n2))

# ------------------------------------------- 16. 数值的整数次方 -------------------------------------------
# ---------------------------------------------------
x1, n1 = 2.00000, 10
x2, n2 = 2.10000, 3
x3, n3 = 2.00000, -2


def myPow(x, n):
    """
    快速幂解析（二进制角度）将时间复杂度降低至 O(log_2 n)
    https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/
    """
    if x == 0:
        return 0
    res = 1
    if n < 0:
        x, n = 1 / x, -n
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res


print(myPow(x1, n1))
print(myPow(x2, n2))
print(myPow(x3, n3))
