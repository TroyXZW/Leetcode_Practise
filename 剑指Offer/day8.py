# ------------------------------------------- 24. 反转链表 -------------------------------------------
# ---------------------------------------------------

# -*- coding:utf-8 -*-

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        cur = pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
        
# ------------------------------------------- 25. 合并两个排序的链表 -------------------------------------------
# ---------------------------------------------------
"""
时间复杂度
给出一个递归算法，其时间复杂度 O(T) 通常是递归调用的数量（记作 R） 和计算的时间复杂度的乘积
（表示为 O(s)）的乘积：O(T) = R∗O(s)
时间复杂度：O(m+n)
空间复杂度：O(m+n)
"""


def mergeTwoLists(l1, l2):
    """
    使用递归
    """
    if not l1: return l2  # 终止条件，直到两个链表都空
    if not l2: return l1
    if l1.val <= l2.val:  # 递归调用
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2    
        
# ------------------------------------------- 26. 树的子结构 -------------------------------------------
# ---------------------------------------------------    
