#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ------------------------------------------- 17. 打印从1到最大的n位数 -------------------------------------------
# ---------------------------------------------------
class Solution:
    def printNumbers(self, n):
        """
        大数越界情况,大数的表示应用字符串 String 类型
        https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
        """

        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                s = ''.join(num[self.start:])  # 拼接 num 并添加至 res 尾部
                if s != '0':  # 1题目要求从1开始
                    res.append(int(s))
                if n - self.start == self.nine:
                    self.start -= 1
                return
            for i in range(10):  # 遍历 0 - 9
                if i == 9:
                    self.nine += 1
                num[x] = str(i)  # 固定第 x 位为 i
                dfs(x + 1)  # 开启固定第 x + 1 位
            self.nine -= 1

        num, res = ['0'] * n, []  # 起始数字定义为 n 个 0 组成的字符列表num
        self.nine = 0
        self.start = n - 1
        dfs(0)  # 开启全排列递归
        return res  # 拼接所有数字字符串，使用逗号隔开，并返回


# ---------------------------------------------------
def printNumbers(n):
    """
    常规做法
    """
    res = []
    for i in range(1, 10 ** n):
        res.append(i)
    return res


# ------------------------------------------- 18. 删除链表的节点 -------------------------------------------
# ---------------------------------------------------
def deleteNode(head, val):
    """
    常规删除节点操作,但时间复杂度比较高
    """
    if head.val == val:
        return head.next
    pre, cur = head, head.next  # 初始化
    while cur and cur.val != val:
        pre, cur = cur, cur.next
    if cur:
        pre.next = cur.next  # 跳过该节点
    return head


# ---------------------------------------------------
def deleteNode(head, val):
    """
    删除节点呗后面的节点替换，时间线复杂度降低
    # 怎么感觉和上一种方法一样，并不是替换
    """
    if head.val == val:
        return head.next
    pre, cur = head, head.next  # 初始化
    while cur and cur.val != val:  # 当未到指定节点且cur非空时
        pre, cur = cur, cur.next
    if cur and cur.next:  # 当到指定节点且其next非空，替换
        tmp = cur.next
        cur.val = tmp.val
        cur.next = tmp.next
    else:
        pre.next = cur.next  # 当指定节点未最后一个，则像上一种方法跳过节点
    return head

# ------------------------------------------- 19. 正则表达式匹配 -------------------------------------------
# ---------------------------------------------------
def isMatch(self, s: str, p: str) -> bool:
    """
    放弃中。。。
    """
    pass
