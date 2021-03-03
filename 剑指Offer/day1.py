#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# ------------------------------------------- 3. 数组中重复的数字 -------------------------------------------
# ---------------------------------------------------
nums = [2, 3, 1, 0, 2, 5, 3]


def findRepeatNumber(nums):
    """
    不知道为什么超时,已解决
    """
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                """
                tmp = nums[i] # 将nums[i]（2）赋值给tmp
                nums[i] = nums[nums[i]] # nums[nums[i]]（1）替换nums[i]（2）
                nums[nums[i]] = tmp # 将tmp（2）赋值给nums[nums[i]]（nums[1]），但本来要赋值给nums[0]
                这样替换错误，本来要2和1替换
                因此nums[i],nums[nums[i]] = nums[nums[i]],nums[i]就是这个错误
                """
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                """
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
                不会出现此类错误
                """


# ---------------------------------------------------

def findRepeatNumber(nums):
    i = 0

    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]:
            return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


print(findRepeatNumber(nums))


# ---------------------------------------------------
# 不修改数组找出重复数字 P41
#!/usr/bin/env python
# -*- coding:utf-8 -*-

def count_range(numbers, length, start, end):
    if not numbers:
        return 0
    count = 0
    for i in range(length):
        if numbers[i] >= start and numbers[i] <= end:
            count += 1
    return count


def get_duplications(numbers, length):
    if not numbers or length == 0:
        return -1
    start = 1
    end = length - 1
    while end >= start:
        mid = (start + end) >> 1
        count = count_range(numbers, length, start, mid)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1
    return -1


if __name__ == "__main__":
    res = get_duplications([2, 3, 5, 4, 3, 2, 6, 7], 8)
    print(res)

# ------------------------------------------- 4. 二维数组中的查找 -------------------------------------------
# ---------------------------------------------------
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 20


def findNumberIn2DArray(matrix, target):
    """
    从右上角开始找
    """
    if not matrix:
        return False
    i = 0
    n = len(matrix) - 1
    m = len(matrix[0]) - 1

    while (i <= n) and (m >= 0):
        if target > matrix[i][m]:
            i += 1
        elif target < matrix[i][m]:
            m -= 1
        else:
            return True
    return False


print(findNumberIn2DArray(matrix, target))

# ------------------------------------------- 5. 替换空格 -------------------------------------------
# ---------------------------------------------------
s = "We are happy."


def replaceSpace(s):
    s_new = ""

    for letter in s:
        if letter.isspace():
            s_new += "%20"
        else:
            s_new += letter
    return s_new


print(replaceSpace(s))
