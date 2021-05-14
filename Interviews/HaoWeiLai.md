### [旋转数组查找指定值](https://blog.csdn.net/MDreamlove/article/details/82699400?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161813031216780255270424%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161813031216780255270424&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-1-82699400.pc_search_result_no_baidu_js&utm_term=%E6%97%8B%E8%BD%AC%E6%95%B0%E7%BB%84%E6%89%BE)


### 子链表反转
没做出来。。。
```
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class Node():
    def __init__(self, root):
        self.node = root
        self.next = None


def func_1(node, times):
    if not node:
        return None
    pre = None
    cur = node
    while times >= 0:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
        times -= 1
    return pre, cur


def func(node, n, m):
    head = node
    while n > 1:
        node = node.next
        n -= 1
    times = m - n

    pre, tmp = func_1(node, times)
    node.next = pre
    while pre:
        if not pre.next:
            pre.next = tmp
        pre = pre.next

    return head


def show_link(root):
    while root:
        print(root.node)
        root = root.next


a = Node(7)
b = Node(6)
c = Node(5)
d = Node(8)
e = Node(9)
f = Node(19)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a = None
n, m = 3, 4
res = func(a, n, m)
head = res

show_link(head)

```

