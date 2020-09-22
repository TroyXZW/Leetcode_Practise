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
    '''
    时间复杂度为O(NV)，空间复杂度为O(NV)
    :param N: 物品的个数
    :param V: 包的容积
    :param volumn: 物品容积的列表
    :param value: 物品价值的列表
    :param f: 二维数组
    :return: 返回最大价值
    '''
    for i in range(1, N + 1):
        for j in range(1, V + 1):
            if volumn[i] <= j:
                f[i][j] = max(f[i - 1][j - volumn[i]] + value[i], f[i - 1][j])
            else:
                f[i][j] = f[i - 1][j]

    return f[-1][-1]


if __name__ == '__main__':
    print(Backpack_problem_lessspace(N, V, volumn, value, f))

```
上面的基本实现时间复杂度为O(nW)，空间复杂度为O(nW)，事实上空间可以做优化。\
我们可以看到，第 i 层的状态至于第 i-1 层的状态有关，与第 i-2 层的状态没有直接关系，\
除了第一层的初始条件，其他每一层的状态值的求解依赖于上一层。

[一维数组实现](https://blog.csdn.net/sinat_30973431/article/details/85119871)
```
N, V = map(int, input().split())  # 物品数， 背包容量

volumn = [0] * (N + 1)  # 体积 索引从1开始到n
value = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    volumn[i], value[i] = map(int, input().split())

f = [0 for i in range(V + 1)]  # 只用了一维数组,初始化全0


def Backpack_problem_lessspace(N, V, volumn, value, f):
    '''
    时间复杂度为O(NV)，空间复杂度为O(V)
    :param N: 物品的个数
    :param V: 包的容积
    :param volumn: 物品容积的列表
    :param value: 物品价值的列表
    :param f: 二维数组
    :return: 返回最大价值
    '''
    for i in range(1, N + 1):
        for j in range(V, volumn[i] - 1, -1):  # 从后到前的顺序遍历
            f[j] = max(f[j - volumn[i]] + value[i], f[j])

    return f[-1]


if __name__ == '__main__':
    print(Backpack_problem_lessspace(N, V, volumn, value, f))

```

扩展分析\
扩展题目要求：求解将哪些物品装入背包，可使这些物品的总体积**刚好等于**背包容量，且总价值最大。输出最大价值。
```

```

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
