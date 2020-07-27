#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# -------------------------------------------53. 最大子序和 -------------------------------------------
# ---------------------------------------------------
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSubArray(nums):
    """
    动态规划
    """
    if not nums:
        return 0
    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], nums[i])
    return max(nums)


# ---------------------------------------------------
def maxSubArray(nums):
    """
    分治
    #mid=(left+right)>>1的含义
    #右移运算符>>,运算结果正好能对应一个整数的二分之一值，这就正好能代替数学上的除2运算，但是比除2运算要快。
    #mid=(left+right)>>1相当于mid=(left+right)/2
    出处：https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
    """
    size = len(nums)

    def __max_sub_array(nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(__max_sub_array(nums, left, mid),
                   __max_sub_array(nums, mid + 1, right),
                   __max_cross_array(nums, left, mid, right))

    def __max_cross_array(nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1
        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max

    if not nums:
        return 0
    return __max_sub_array(nums, 0, size - 1)


print(maxSubArray(nums))
