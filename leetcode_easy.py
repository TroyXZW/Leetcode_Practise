#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# -------------------------------------------1.两数之和-------------------------------------------
nums = [0, 0, 3, 3]
target = 6


def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        rest = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == rest:
                result.append(i)
                result.append(j)
    return result


print(twoSum(nums, target))


# ---------------------------------------------------

def twoSum(self, nums, target):
    """
    如果数相同（比如3），遍历得到的i是第一个3的索引，
    通过字典得到的j是nums中最后一个3的索引，
    所以不会重复
    """

    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind  # {0: 1, 3: 3}
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]


# hashmap = {}
# for ind, num in enumerate(nums):
#     hashmap[num] = ind
print(twoSum1(nums, target))

# -------------------------------------------7.整数反转-------------------------------------------
x = 12300
y = -123


def reverse(x):
    to_str = str(x)
    A = False
    if to_str[0] == '-':
        A = True
        to_str = to_str[1:]
        new_str = to_str[::-1]
    else:
        new_str = to_str[::-1]
    B = True
    while B:
        if new_str[0] == '0':
            new_str = new_str[1:]
        else:
            B = False
    if A:
        new_str = '-' + new_str
    return int(new_str)


reverse(x)
reverse(y)

# -------------------------------------------9.回文数-------------------------------------------
x = 121
y = -121
z = 10


def isPalindrome(x):
    to_str = str(x)
    if to_str == to_str[::-1]:
        print("true")
    else:
        print("false")


def isPalindrome1(x):
    to_str = str(x)
    return to_str == to_str[::-1]


isPalindrome(x)
isPalindrome(y)
isPalindrome(z)

# -------------------------------------------13.罗马数字转整数-------------------------------------------
s = 'XXVII'
s1 = 'II'
s2 = 'XII'
s3 = 'CD'
s4 = "LVIII"
s5 = "MCMXCIV"


def romanToInt(s):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    toint = 0
    for i in range(len(s)):
        if s[i] == 'I' and s[i + 1] == 'V':
            toint += 4
            s = s[i + 2:]
        elif s[i] == 'I' and s[i + 1] == 'X':
            toint += 5
            s = s[i + 2:]
        elif s[i] == 'X' and s[i + 1] == 'L':
            toint += 40
            s = s[i + 2:]
        elif s[i] == 'X' and s[i + 1] == 'C':
            toint += 90
            s = s[i + 2:]
        elif s[i] == 'C' and s[i + 1] == 'D':
            toint += 400
            s = s[i + 2:]
        elif s[i] == 'C' and s[i + 1] == 'M':
            toint += 900
            s = s[i + 2:]
        else:
            for j in a:
                if s[i] == j:
                    toint += a[j]
    return toint


def romanToInt(s):
    d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
         'CM': 900, 'M': 1000}
    toint = 0
    for i, n in enumerate(s):
        if len(s)==2:

        subs = s[i:i + 1]
        toint += d[n]
    return toint


print(romanToInt(s))
