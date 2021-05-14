### 给定一组数，设定x=2，在改变这组数后使其成为等差数列。求改变的最小次数。 <br>
eg:<br>
5 2 <br>
2 7 6 5 10
```
def min_magic(n, x, tree):
    new_list = [tree[i] - i * 2 for i in range(n)]
    print(new_list)
    hmap = {}
    for i in new_list:
        hmap[i] = 1 if hmap.get(i, 0) == 0 else hmap[i] + 1
    max_num = 0
    print(hmap)
    for key in hmap.keys():
        max_num = max(max_num, hmap[key])
    return n - max_num


if __name__ == "__main__":
    lis = list(map(int, input().split(" ")))
    n, x = lis[0], lis[1]
    tree = list(map(int, input().split(" ")))
    res = min_magic(n, x, tree)
    print(res)

```

### 给定n台机器，每台机器有两个数a，b。a为准备时间，b为执行时间，准备后才可执行。多台机器的准备可同时进行，但不可同时执行。求最短的时间所有机器执行完毕。 <br>
eg:<br>
2 <br>
5 1 <br>
2 4


### 杨辉三角 <br>

```
def triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]

    while n - 3 >= 0:
        tmp = res[-1]
        sub_res = [1]
        i = 0
        while i < len(tmp) - 1:
            sub_res.append(tmp[i] + tmp[i + 1])
            i += 1
        sub_res.append(1)
        res.append(sub_res)
        n -= 1
    return res


if __name__ == "__main__":
    # res = triangle(2)
    # print(res)
    print(triangle(5))

```
