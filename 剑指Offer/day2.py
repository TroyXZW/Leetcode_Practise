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
class Solution:
    """
    大佬用的递归，分治思想
    https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/mian-shi-ti-07-zhong-jian-er-cha-shu-di-gui-fa-qin/
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dic, self.po = {}, preorder
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i  # 字典的键为中序遍历的值，值为对应的索引
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, pre_root, in_left, in_right):  # pre_root为前序遍历中根节点的索引，in_left, in_right分别为中序遍历中左边界索引和右边界索引
        if in_left > in_right:
            return None  # 终止条件：中序遍历为空
        root = TreeNode(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        root.left = self.recur(pre_root + 1, in_left, i - 1)  # 开启左子树的下层递归
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)  # 开启右子树的下层递归，i - in_left为左子树长度
        return root  # 返回根节点，作为上层递归的左（右）子节点


class Solution:
    """
    相当简洁
    https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/solution/di-gui-jie-fa-by-ml-zimingmeng-3/
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:  # 终止条件：中序遍历为空
            return None

        # 根节点
        root = TreeNode(preorder[0])
        # 获取根节点在 inorder 中的索引
        idx = inorder.index(preorder[0])
        # 左子树
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        # 右子树
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root


# ------------------------------------------- 9. 用两个栈实现队列 -------------------------------------------
# ---------------------------------------------------
class CQueue:
    """
    不会，直接抄袭大佬滴
    https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/
    """

    def __init__(self):
        self.A, self.B = [], []  # A，B两个栈

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1  # 若队列中没有元素，deleteHead 操作返回 -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()
