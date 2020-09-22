# 背包问题（Python）:stuck_out_tongue_winking_eye:
[0-1背包问题，完全背包问题，多重背包问题](https://blog.csdn.net/z_feng12489/article/details/105638210 )

## 0-1背包问题

题目描述：\
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。第 i 件物品的体积是 v i，价值是 w i。\
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
 
输入样例(第一行为 N 件物品和一个容量是 V 的背包,下面每行为重量和价值)\
4 5\
1 2\
2 4\
3 4\
4 5

输出样例：\
8

```
N, V = map(int, input().split())  # 物品数， 背包容量

volumn = [0] * (N + 1)  # 体积 索引从1开始到n
value = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    volumn[i], value[i] = map(int, input().split())

f = [[0 for i in range(V + 1)] for i in range(N + 1)]  # 初始化全0


def Backpack_problem(N, V, volumn, value, f):
    for i in range(1, N + 1):
        for j in range(1, V + 1):
            if volumn[i] <= j:
                f[i][j] = max(f[i - 1][j - volumn[i]] + value[i], f[i - 1][j])
            else:
                f[i][j] = f[i - 1][j]

    return f[-1][-1]


if __name__ == '__main__':
    print(Backpack_problem(N, V, volumn, value, f))

```

扩展分析\
扩展题目要求：求解将哪些物品装入背包，可使这些物品的总体积**刚好等于**背包容量，且总价值最大。输出最大价值。


## 完全背包问题
```
输入样例
4 5
1 2
2 4
3 4
4 5

输出样例：
8


```

## 多重背包问题
```
输入样例
4 5
1 2
2 4
3 4
4 5

输出样例：
8


```
