#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# ------------------------------------------- 12. 矩阵中的路径 -------------------------------------------
# ---------------------------------------------------
board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCCED"
board2 = [["a", "b"], ["c", "d"]]
word2 = "abcd"


def exist(board, word):
    """
    回溯法
    矩阵中走路的题目，很大可能都是用回溯来进行求解。
    回溯可以理解为树的遍历，可以是DFS也可以是BFS，由于每种情况都遍历，所以时间复杂度一般来说是很高的
    矩阵搜索问题。此类问题通常可使用 深度优先搜索（DFS） 或 广度优先搜索（BFS） 解决
    https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/
    """

    def dfs(i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        tmp, board[i][j] = board[i][j], ''
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        """
        递归搜索匹配字符串过程中，需要 board[i][j] = '' 来防止 ”走回头路“ 。
        当匹配字符串不成功时，会回溯返回，此时需要board[i][j] = tmp 来”取消对此单元格的标记”。 
        在DFS过程中，每个单元格会多次被访问的， board[i][j] = ''只是要保证在当前匹配方案中不要走回头路。
        """
        board[i][j] = tmp  # 若此时res是False，因为要回溯，所以要还原board[i][j]
        return res

    for i in range(len(board)):  # 这两层循环的目的是找起始元素
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False


print(exist(board1, word1))
print(exist(board2, word2))

# ------------------------------------------- 13. 机器人的运动范围 -------------------------------------------
# ---------------------------------------------------
m1, n1, k1 = 2, 3, 1
m2, n2, k3 = 3, 1, 0


def movingCount(m, n, k):
    """
    深度优先遍历 DFS:通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推
    时间复杂度 O(MN)： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN) 。
    空间复杂度 O(MN)： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN)的额外空间
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
    """

    def dfs(i, j, si, sj):  # 元素在矩阵中的行列索引 i 和 j ，两者的数位和 si, sj
        if i >= m or j >= n or k < si + sj or (i, j) in visited:
            return 0
        visited.add((i, j))
        down = dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj)
        right = dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        return 1 + down + right

    visited = set()  # 将索引 (i, j) 存入 Set visited 中，代表此单元格已被访问过
    return dfs(0, 0, 0, 0)


# ---------------------------------------------------
def movingCount1(m, n, k):
    """
    广度优先遍历 BFS:利用队列实现广度优先遍历
    DFS 是朝一个方向走到底，再回退，以此类推；BFS 则是按照“平推”的方式向前搜索。
    时间复杂度 O(MN)： 最差情况下，机器人遍历矩阵所有单元格，此时时间复杂度为 O(MN) 。
    空间复杂度 O(MN)： 最差情况下，Set visited 内存储矩阵所有单元格的索引，使用 O(MN)的额外空间
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
    """
    queue, visited, = [(0, 0, 0, 0)], set()
    while queue:
        i, j, si, sj = queue.pop(0)
        if i >= m or j >= n or k < si + sj or (i, j) in visited:
            continue
        visited.add((i, j))
        queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
        queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
    return len(visited)


print(movingCount(m1, n1, k1))
print(movingCount1(m2, n2, k3))

# ------------------------------------------- 14-I. 剪绳子 -------------------------------------------
# ---------------------------------------------------
n1 = 2
n2 = 10

"""
def cuttingRope(n):
    """
# 动态规划
# 不知道为什么会报错
# TypeError: unsupported operand type(s) for *: 'int' and 'builtin_function_or_method'
"""
if n < 2:
    return 0
if n == 2:
    return 1
if n == 3:
    return 2
product = [0] * (n + 1)
product[1] = 1
product[2] = 2
product[3] = 3
for i in range(4, n + 1):
    max_res = 0
    for j in range(1, i // 2 + 1):
        product_res = product[j] * product[i - j]
        if max_res < product_res:
            max_res = product_res
        product[i] = max
res = max(product)

return res
"""


# ---------------------------------------------------
def cuttingRope(n):
    """
    动态规划,自下而上的求解
    """
    dp = [0] * (n + 1)  # 相当于不切割，分成0和n两条线段，0*n=0
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
    return dp[n]


# ---------------------------------------------------
import math


def cuttingRope(n):
    """
    贪婪算法
    Python 中常见有三种幂计算函数： * 和 pow() 的时间复杂度均为 O(loga) ；
    而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)。
    https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/
    """
    if n <= 3:
        return n - 1  # 题目要求必须切割
    a, b = n // 3, n % 3
    if b == 0:
        return int(math.pow(3, a))
    if b == 1:
        return int(math.pow(3, a - 1) * 4)
    return int(math.pow(3, a) * 2)  # b == 1的情况


print(cuttingRope(n1))
print(cuttingRope(n2))
