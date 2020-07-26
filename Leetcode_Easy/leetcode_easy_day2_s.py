#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# -------------------------------------------13.最长公共前缀-------------------------------------------
s1 = ["flower", "flow", "flight"]
s2 = ["dog", "racecar", "car"]


def longestCommonPrefix(strs):
    length = len(strs[0])
    total = 0
    for s in strs:
        if len(s) < length:
            length = len(s)
            min_s = s
    for i in range(length):
        for j in range(len(strs)):
            if min_s[:i + 1] == strs[j][:i + 1]:
                total = total + 1
        if total == len(strs):
            res = min_s[:i + 1]
        else:
            if res != '':
                continue
            else:
                return ''
                break
    return res


# ---------------------------------------------------

def longestCommonPrefix(strs):
    """
    以s1 = ["flower", "flow", "flight"]为例
    这个操作有点骚啊。。。
    """
    res = ""
    for tmp in zip(*strs):  # zip(*strs)返回[('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        tmp_set = set(tmp)  # [('f'), ('l'), ('o', 'i'), ('w', 'g')]
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res


# ---------------------------------------------------

def longestCommonPrefix(strs):
    """
    a.find(s) 如果找到此字符串s，返回s在a的索引，否则返回-1
    """
    if not strs:
        return ""
    else:
        res = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(res) != 0:
                res = res[0:len(res) - 1]
            i += 1
        return res


print(longestCommonPrefix(s1))

# -------------------------------------------20.有效的括号-------------------------------------------
s = "()"
s1 = "()[]{}"
s2 = "([)]"
s3 = "{[]}"


def isValid(s):
    stack = ['?']
    list = ['(', '[', '{']
    dict = {']': '[', '}': '{', ')': '(', '?': '?'}
    for c in s:
        if c in list:
            stack.append(c)
        else:
            if dict[c] == stack.pop():
                continue
            else:
                return False
    return len(stack) == 1


# ---------------------------------------------------

def isValid(s):
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1


print(isValid(s))

# -------------------------------------------21.合并两个有序链表-------------------------------------------
# 不会，直接上答案吧

"""
时间复杂度
给出一个递归算法，其时间复杂度 O(T) 通常是递归调用的数量（记作 R） 和计算的时间复杂度的乘积
（表示为 O(s)）的乘积：O(T) = R∗O(s)
时间复杂度：O(m+n)
空间复杂度：O(m+n)
"""


def mergeTwoLists(l1, l2):
    """
    使用递归
    """
    if not l1: return l2  # 终止条件，直到两个链表都空
    if not l2: return l1
    if l1.val <= l2.val:  # 递归调用
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


print(mergeTwoLists(l1, l2))

# -------------------------------------------26. 删除排序数组中的重复项-------------------------------------------
nums = [1, 1, 2]
nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    """
    双指针
    """
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


print(removeDuplicates(nums))
print(removeDuplicates(nums1))
# -------------------------------------------27. 移除元素-------------------------------------------
nums = [3, 2, 2, 3]
nums1 = [0, 1, 2, 2, 3, 0, 4, 2]


def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            i += 1
            nums[i - 1] = nums[j]
    return i


print(removeElement(nums, 3))
print(removeElement(nums1, 2))

# -------------------------------------------28. 实现 strStr()-------------------------------------------
haystack, needle = "hello", "ll"
haystack1, needle1 = "aaaaa", "bba"


def strStr(haystack, needle):
    """
    BF算法
    子串逐一比较的解法最简单，将长度为 L 的滑动窗口沿着 haystack 字符串逐步移动，并将窗口内的子串与 needle 字符串相比较，
    时间复杂度为 O((N - L)L)
    """
    L, n = len(needle), len(haystack)

    for start in range(n - L + 1):
        if haystack[start: start + L] == needle:
            return start
    return -1


def strStr(haystack, needle):
    """
    双指针方法虽然也是线性时间复杂度，不过它可以避免比较所有的子串，因此最优情况下的时间复杂度为 O(N)，
    但最坏情况下的时间复杂度依然为 O((N - L)L)。
    """
    L, n = len(needle), len(haystack)
    if L == 0:
        return 0

    pn = 0
    while pn < n - L + 1:
        # find the position of the first needle character
        # in the haystack string
        while pn < n - L + 1 and haystack[pn] != needle[0]:
            pn += 1

        # compute the max match string
        curr_len = pL = 0
        while pL < L and pn < n and haystack[pn] == needle[pL]:
            pn += 1
            pL += 1
            curr_len += 1

        # if the whole needle string is found,
        # return its start position
        if curr_len == L:
            return pn - L
        else:
            # otherwise, backtrack
            pn = pn - curr_len + 1

    return -1


def strStr(haystack, needle):
    """
    Rabin-Karp，通过哈希算法实现常数时间窗口内字符串比较（RK算法）
    比特位操作，通过比特掩码来实现常数时间窗口内字符串比较。
    时间复杂度：O(N)，计算 needle 字符串的哈希值需要 O(L) 时间，之后需要执行 (N - L) 次循环，每次循环的计算复杂度为常数。
    空间复杂度：O(1)。
    """
    L, n = len(needle), len(haystack)
    if L == 0:
        return 0
    if L > n:
        return -1

    # base value for the rolling hash function
    a = 26
    # modulus value for the rolling hash function to avoid overflow
    modulus = 2 ** 31

    # lambda-function to convert character to integer
    h_to_int = lambda i: ord(haystack[i]) - ord('a')
    needle_to_int = lambda i: ord(needle[i]) - ord('a')

    # compute the hash of strings haystack[:L], needle[:L]
    h = ref_h = 0
    for i in range(L):
        h = (h * a + h_to_int(i)) % modulus
        ref_h = (ref_h * a + needle_to_int(i)) % modulus
    if h == ref_h:
        return 0

    # const value to be used often : a**L % modulus
    aL = pow(a, L, modulus)  # pow(x,y,z)：这个是表示x的y次幂后除以z的余数。
    for start in range(1, n - L + 1):
        # compute rolling hash in O(1) time
        h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
        if h == ref_h:
            return start

    return -1


print(strStr(haystack, needle))
print(strStr(haystack1, needle1))

# 题解来源
https: // leetcode - cn.com / problems / implement - strstr / solution / shi - xian - strstr - by - leetcode /

# -------------------------------------------35. 搜索插入位置-------------------------------------------
nums0, target0 = [1, 3, 5, 6], 5
nums1, target1 = [1, 3, 5, 6], 2
nums2, target2 = [1, 3, 5, 6], 7
nums3, target3 = [1, 3, 5, 6], 0
nums4, target4 = [1, 3, 5], 4


def searchInsert(nums, target):
    """
    非常暴力
    """
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    else:
        if target < min(nums):
            return 0
        elif target > max(nums):
            return len(nums)
        else:
            for i in range(len(nums) - 1):
                if (target > nums[i]) & (target < nums[i + 1]):
                    return i + 1


def searchInsert(nums, target):
    """
    二分法怎么没想到？
    “ // ” 表示整数除法，返回整数 比如 7/3 结果为2
    “ / ” 表示浮点数除法，返回浮点数 （即小数） 比如 8/2 结果为4.0
    “ %” 表示取余数 比如7/4 结果为3
    """
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2  # 防溢出
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


print(searchInsert(nums0, target0))
