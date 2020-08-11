# ------------------------------------------- 724. 寻找数组的中心索引 -------------------------------------------
# ---------------------------------------------------数组
nums = [-1, -1, -1, -1, -1, 0]


def pivotIndex(nums):
    """
    炸了。此题自己做的放弃，还是大佬们靠谱
    https://leetcode-cn.com/problems/find-pivot-index/solution/xun-zhao-shu-zu-de-zhong-xin-suo-yin-by-leetcode/
    """
    # pre_sum = 0
    # last_sum = 0
    # pre = 0
    # last = len(nums) - 1
    # if not nums:
    #     return -1
    # while pre < last:
    #     if pre_sum < last_sum:
    #         pre_sum += nums[pre]
    #         pre += 1
    #     else:
    #         last_sum += nums[last]
    #         last -= 1
    # if pre_sum == last_sum:
    #     return pre
    # else:
    #     return -1

    s = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (s - leftsum - x):  # 直接判断i的左边和右边和是否相等
            return i
        leftsum += x
    return -1


print(pivotIndex(nums))

# ------------------------------------------- 35. 搜索插入位置 -------------------------------------------
# ---------------------------------------------------数组
nums, target = [1, 3, 5, 6], 2
nums1, target1 = [1, 3, 5, 6], 5


def searchInsert(nums, target):
    """
    二分查找（循环）
    """
    pre = 0
    last = len(nums) - 1
    if not nums or (target <= nums[0]):
        return 0
    if target > nums[last]:
        return len(nums)
    while pre <= last:
        mid = pre + ((last - pre) >> 1)
        if target > nums[mid]:
            if target < nums[mid + 1]:
                return mid + 1
            pre = mid + 1
        elif target < nums[mid]:
            if target > nums[mid - 1]:
                return mid
            last = mid - 1
        else:
            return mid
    return pre  # mid也可以


# ---------------------------------------------------
def searchInsert(nums, target):
    """
    二分
    https://leetcode-cn.com/problems/search-insert-position/submissions/
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


print(searchInsert(nums, target))
print(searchInsert(nums1, target1))

# ------------------------------------------- 56. 合并区间 -------------------------------------------
# ---------------------------------------------------数组
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals1 = [[1, 3], [8, 10], [2, 6], [15, 18]]


def merge(intervals):
    """
    https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
    """
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


print(merge(intervals))
