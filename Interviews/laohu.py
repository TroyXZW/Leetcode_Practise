# coding=utf-8
import sys

"""
入参：表达式，str，包含 {,},[,],(,)

判断表达式是否正确：
1）是否成对出现；
2）嵌套关系：

{} -----> [] () 
[] -----> ()
() -----> null

{}{[][()()]()}()[]
"""


def is_valid(strings):
    if not strings:
        return False
    hash_map = {"{": "}", "[": "]", "(": ")"}
    stack = [strings[0]]
    for i in range(1, len(strings)):
        if stack and strings[i] == hash_map[stack[-1]]:
            stack.pop()
        else:
            if stack and ((stack[-1] == "{" and strings[i] == "{") or (stack[-1] == "[" and strings[i] != "(") or stack[
                -1] == "(" and strings[i] != ")"):
                return False
            stack.append(strings[i])
    if not stack:
        return True
    else:
        return False


s1 = "{}{[][()()]()}()[]"
s2 = "{{}}"
s2 = "{}["
print(is_valid(s1))
print(is_valid(s2))
print(is_valid(s2))
