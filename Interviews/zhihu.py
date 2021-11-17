"""
两个没有重复元素的数组list1,list2。其中list1是list2的子集。找出 list1 中每个元素在 list2 中的下一个比其大的值。如果不存在，则为-1
list1=[5,3,2]
list2=[6,5,2,1,3,4]
res=[-1,4,3]
"""

from collections import defaultdict


def solution(list1, list2):
    stack = [list2[0]]
    hash_map = defaultdict(int)
    res = []
    for i in range(1, len(list2)):
        if stack[-1] >= list2[i]:
            stack.append(list2[i])
        else:
            tmp = stack[-1]
            while tmp < list2[i]:
                aaa = stack.pop()
                hash_map[aaa] = list2[i]
                tmp = stack[-1]

    for i in range(list1):
        if hash_map[i] != 0:
            res.append(hash_map[i])
        else:
            res.append(-1)
    return res
