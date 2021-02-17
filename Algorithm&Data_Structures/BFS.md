# 解密码锁 p56-算法小炒

```
def replace_char(string, char, index):
    string = list(string)
    string[index] = char
    return ''.join(string)


def plus(string, i):
    if string[i] == "9":
        return replace_char(string, "0", i)
    else:
        num = 1 + int(string[i])
        return replace_char(string, str(num), i)


def minus(string, i):
    if string[i] == "0":
        return replace_char(string, "9", i)
    else:
        num = int(string[i]) - 1
        return replace_char(string, str(num), i)


def bfs(start, target, deadends):
    if start == target:
        return 0
    q = [start]
    visited = [start]
    num = 0
    while q:
        length = len(q)
        for i in range(length):
            cur = q.pop(0)
            if cur == target:
                return num
            if cur in deadends:
                continue
            for j in range(len(cur)):
                plus_num = plus(cur, j)
                if plus_num not in visited:
                    q.append(plus_num)
                    visited.append(plus_num)
                minus_num = minus(cur, j)
                if minus_num not in visited:
                    q.append(minus_num)
                    visited.append(minus_num)
        num += 1
    return -1


if __name__ == "__main__":
    # deadends = ["1234", "5678"]
    # result = bfs("0000", "1111", deadends)
    # print(result)
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    result = bfs("0000", "8888", deadends)
    print(result)

```
