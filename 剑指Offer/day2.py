#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# ------------------------------------------- 6.从尾到头打印链表 -------------------------------------------
# ---------------------------------------------------
head = [1, 3, 2]


class Solution:
    def reversePrint(self, head):
        """
        递归，大佬的思路就是简洁
        https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/
        """
        return self.reversePrint(head.next) + [head.val] if head else []


# ---------------------------------------------------
def reversePrint(head):
    """
    利用栈先进后出的特性
    https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/
    """
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    return stack[::-1]  # 或者 reverse(res)


# ---------------------------------------------------
def reversePrint(head):
    """
    利用栈先进后出的特性
    """
    stack = []
    while head:  # push
        stack.append(head.val)
        head = head.next
    res = []
    while stack:  # pop
        res.append(stack.pop())
    return res

# ------------------------------------------- 7. 重建二叉树 -------------------------------------------
# ---------------------------------------------------
