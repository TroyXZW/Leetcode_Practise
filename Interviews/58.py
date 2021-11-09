"""
题目名称：快速找出第一个错误的下标位置
题目描述：假设你有 n 个版本 [1, 2, ..., n]，以数组/列表的形式顺序存储，每次系统迭代后版本号加1，然后存入列表。当前从某个版本号开始版本号发生错误。现在实现一个函数找出列表中第一个错误版本对应的下标位置。
例子：
eg1. 列表 [1,2,4] 中第一个发生错误的下标位置是2
eg2. 列表 [1,2,3,4,6,7,8,9,10] 中第一个发生错误的下标位置是4
"""


def find_wrong_index(lista):
    left, right = 0, len(lista) - 1
    while left < right:
        mid = (left + right) >> 1
        if mid == lista[mid] - 1:
            left = mid + 1
        else:
            right = mid
    return left


print(find_wrong_index([1,2,3,4,6,7,8,9,10]))
