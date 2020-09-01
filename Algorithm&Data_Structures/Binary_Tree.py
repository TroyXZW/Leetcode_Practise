#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。


#----------------------------------------------------------------
"""
二叉树的前中后序,递归
"""
    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print (root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)


    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print (root.elem)
        self.middle_digui(root.rchild)


    def later_digui(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print (root.elem)

#----------------------------------------------------------------
"""
二叉树的前中后序,非递归
"""
    def front_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print (node.elem)
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rchild                  #开始查看它的右子树


    def middle_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print (node.elem)
            node = node.rchild                  #开始查看它的右子树


    def later_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print (myStack2.pop().elem)


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print (node.elem)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

# ------------------------------------------- 二叉查找树的搜索、插入、删除 -------------------------------------------

class BinarySearchTree(object):
    def __init__(self, key):  # 定义节点结构
        self.key = key 
        self.left = None
        self.right = None

    def find(self, x):
        if x == self.key:
            return True
        elif x < self.key and self.left:  # 如果x小，则去左子树找
            return self.left.find(x)
        elif x > self.key and self.right:  # 如果x大，则去右子树找
            return self.right.find(x)
        else:
            return None  # 找不到返回None

    def findMin(self):
        if self.left:  # 如果左节点存在，最小值一定在左节点的最深处
            return self.left.findMin()
        else:
            return self.key  # 如果左节点没有，那么根节点最小

    def findMax(self):
        if self.right:  # 如果右节点存在，最大值一定在右节点的最深处
            return self.right.findMax()
        else:
            return self.key  # 如果右节点没有，那么根节点最大

    def insert(self, x):
        if self.find(x):  # 如果找到了该节点，则什么也不做
            return None
        else:  # 如果没有找到则开始插入
            if x < self.key:  # 如果插入值小，则插入左子树
                if self.left:  # 先判断左子树是否存在
                    return self.left.insert(x)
                else:
                    newTree = BinarySearchTree(x)
                    self.left = newTree  # 如果左子树不存在，则把该节点设为左子树
            elif x > self.key:  # 如果插入值大，则插入右子树
                if self.right:
                    return self.right.insert(x)
                else:
                    newTree = BinarySearchTree(x)
                    self.right = newTree

    def delete(self, x):
        if self.find(x):  # 首先判断该节点是否存在
            if x < self.key:  # 如果要删的数据比该数据self.key小，从左子树删起
                self.left = self.left.delete(x)
                return self
            elif x > self.key:  # 如果要删的数据比self.key大，从右子树删起
                self.right = self.right.delete(x)
                return self
            else:  # 如果就是该数据，判断他是否有左右子树
                if self.left and self.right:  # 如果左右子树都存在
                    minkey = self.right.findMin().key  # 把右子树中最小的点连接原来x的父节点, 并且右子树中删除该点
                    self.key = minkey
                    self.right = self.right.delete(minkey)
                    return self
                else:  # 如果左右节点不全存在
                    if self.left:
                        return self.left
                    else:
                        return self.right
        else:
            return self


bst = BinarySearchTree(17)
node_list = [17, 5, 29, 38, 35, 2, 9, 8, 16, 11]
for l in node_list:
    bst.insert(l)
print(bst.findMax())
print(bst.findMin())
print(bst.find(10))
print(bst.delete(11))            
