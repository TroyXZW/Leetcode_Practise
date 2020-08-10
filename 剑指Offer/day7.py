# ------------------------------------------- 20. 表示数值的字符串 -------------------------------------------
# ---------------------------------------------------
def isNumber(s):
    pass


# ------------------------------------------- 21. 调整数组顺序使奇数位于偶数前面 -------------------------------------------
# ---------------------------------------------------
nums = [1, 2, 3, 4]
nums1 = [11, 9, 3, 16, 7, 4, 2, 0]


def exchange(nums):
    pre = 0
    last = len(nums) - 1
    # while pre <= last  # 注意下标越界！[1, 3, 5]
    while pre < last and pre + 1 != last:  # 注意判断pre + 1 == last时的情况
        if nums[pre] % 2 == 1:
            pre += 1
        if nums[last] % 2 == 0:
            last -= 1
        if nums[pre] % 2 == 0 and nums[last] % 2 == 1:
            nums[pre], nums[last] = nums[last], nums[pre]
            pre += 1
            last -= 1
    return nums


print(exchange(nums))
print(exchange(nums1))


# ------------------------------------------- 22. 链表中倒数第k个节点 -------------------------------------------
# ---------------------------------------------------
def getKthFromEnd(head, k):
    former, latter = head, head
    if not head:
        return
    for _ in range(k):
        if not latter:
            return
        latter = latter.next
    while latter:
        former = former.next
        latter = latter.next
    return former
