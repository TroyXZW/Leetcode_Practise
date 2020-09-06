# ------------------------------------------- 反转链表 -------------------------------------------

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
        
        
# ------------------------------------------- 两个链表的第一个公共结点 -------------------------------------------

class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        node1, node2 = pHead1, pHead2
        
        while node1 != node2:
            node1 = node1.next if node1 else pHead2
            node2 = node2.next if node2 else pHead1

        return node1
        
    
# ------------------------------------------- 二叉树先序，中序和后序打印所有的节点 -------------------------------------------    

class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        self.list3 = []
    
    def front(self, root):
        if root:
            self.list1.append(root.val)
            self.front(root.left)
            self.front(root.right)
    
    def middle(self, root):
        if root:
            self.middle(root.left)
            self.list2.append(root.val)
            self.middle(root.right)
    
    def later(self, root):
        if root:
            self.later(root.left)
            self.later(root.right)
            self.list3.append(root.val)

    def threeOrders(self, root):
        if root == None:
            return [[], [], []]

        list_res = []
        self.front(root)
        self.middle(root)
        self.later(root)
        list_res.append(self.list1)
        list_res.append(self.list2)
        list_res.append(self.list3)

        return list_res
        
        
# ------------------------------------------- 求平方根 -------------------------------------------  

class Solution:
    def sqrt(self, x):
        """
        只返回整数部分
        """
        if x < 0:
            return
        start, end = 0, x
        while start <= end:
            tmp = (start + end) >> 1
            if tmp ** 2 < x and (tmp + 1) ** 2 > x:
                return tmp
            if tmp ** 2 > x:
                end = tmp - 1
            elif tmp ** 2 < x:
                start = tmp + 1
            else:
                return tmp
        return start


# ------------------------------------------- 快速排序的思路，找出数组中第K大的数 -------------------------------------------  

class Solution(object):
    """
    未完
    """
    
    def getLeastNumbers(self, arr, k):
        if k > len(arr) or k <= 0:
            return [] 
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k-1:
            print(index)
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low <high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low

# ------------------------------------------- 快速排序的思路，找出数组中第K大的数 -------------------------------------------

