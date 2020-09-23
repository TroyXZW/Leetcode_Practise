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
                # f[i][j], 代表前i个物品，存入容量为j的背包里的最大价值
                f[i][j] = max(f[i - 1][j - volumn[i]] + value[i], f[i - 1][j])
            else:
                f[i][j] = f[i - 1][j]

    return f[-1][-1]


def show_res(N, V, volumn, f):
    """
    显示哪些被选中
    :param N: 
    :param V: 
    :param volumn: 
    :param f: 
    :return: 
    """
    x = [False for i in range(N)]
    j = V
    for i in range(N, 0, -1):
        if f[i][j] > f[i - 1][j]:
            # 说明x[i - 1]加进来了，不是取f[i - 1][j]而是f[i - 1][j - volumn[i]] + value[i]
            x[i - 1] = True
            j -= volumn[i - 1]
    print('选择的物品为:')
    for i in range(N):
        if x[i]:
            print('第', i, '个,')


if __name__ == '__main__':
    print(Backpack_problem(N, V, volumn, value, f))
    show_res(N, V, volumn, f)

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
    时间复杂度为O(NV*max(V/volumn i))，空间复杂度为O(V)
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
尽管滚动数组、一维数组能省一些空间，但是，这两种做法比较适合只求最大价值的需求。\
当需要输出最佳方案时，我们常常要回溯历史信息，这时，一般就只能用二维数组这种保存有各个状态值的方法了。

## 完全背包问题

有 N 件物品和一个容量是 V 的背包。每件物品使用**次数不限**。第 i 件物品的体积是 v i，价值是 w i。\
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。

背包承重量的固定性导致每种最多只能取某个值，再多就放不下了，这个值就是W / wi。也就是说，对于第 i 种物品，\
它可以取0,1,2，......，W / wi（向下取整）件。而在01背包中，对于第 i 种物品，只能取0,1件。\
**0-1背包其实就是完全背包的一个特例**。所以我们可以用类似01背包的思路写出完全背包的基本算法。

输入样例\
4 5\
1 2\
2 4\
3 4\
4 5

输出样例：\
10

```
N, V = map(int, input().split())  # 物品数， 背包容量

volumn = [0] * (N + 1)  # 体积 索引从1开始到n
value = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    volumn[i], value[i] = map(int, input().split())

f = [[0 for i in range(V + 1)] for i in range(N + 1)]  # 初始化全0


def Backpack_problem(N, V, volumn, value, f):
    '''
    时间复杂度为O(NV*max(W/wi))，空间复杂度为O(NV)
    :param N: 物品的个数
    :param V: 包的容积
    :param volumn: 物品容积的列表
    :param value: 物品价值的列表
    :param f: 二维数组
    :return: 返回最大价值
    '''
    for i in range(1, N + 1):
        for j in range(1, V + 1):
            f[i][j] = f[i - 1][j]
            for k in range(1, j // volumn[i] + 1):
                f[i][j] = max(f[i - 1][j - k * volumn[i]] + k * value[i], f[i][j])

    return f[-1][-1]


if __name__ == '__main__':
    print(Backpack_problem(N, V, volumn, value, f))
```
二维dp转一维dp代码\
转换的等价性证明：由于第i层状态只与第i-1层状态有关，从后往前更新确保更新第i层用的是第i-1层的状态值。(与0-1背包同理)

```
f = [0 for i in range(V + 1)]  # 初始化全0


def Backpack_problem_lessspace(N, V, volumn, value, f):
    '''
    时间复杂度为O(NV*max(W/wi))，空间复杂度为O(V)
    :param N: 物品的个数
    :param V: 包的容积
    :param volumn: 物品容积的列表
    :param value: 物品价值的列表
    :param f: 二维数组
    :return: 返回最大价值
    '''
    for i in range(1, N + 1):
        for j in range(V, volumn[i] - 1, -1):  # 从后到前的顺序遍历
            for k in range(1, j // volumn[i] + 1):
                f[j] = max(f[j - k * volumn[i]] + k * value[i], f[j])

    return f[-1]


if __name__ == '__main__':
    print(Backpack_problem_lessspace(N, V, volumn, value, f))

```

## 多重背包问题

有 N 种物品和一个容量是 V 的背包。第 i 种物品最多有 s i 件，每件体积是 v i，价值是 w i。\
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。输出最大价值。
 
如果所有ni都满足ni ≥ W / wi，就变成完全背包的问题了。可见，完全背包的基本实现思路也可以应用到\
多重背包的基本实现。对于多重背包的基本实现，与完全背包是基本一样的，不同就在于物品的个数上界不再\
是v/c[i]而是n[i]与v/c[i]中较小的那个。所以我们要在完全背包的基本实现之上，再考虑这个上界问题。

输入样例\
4 5\
1 2 3\
2 4 1\
3 4 3\
4 5 2

输出样例：\
10

```
N, V = map(int, input().split())  # 物品数， 背包容量

volumn = [0] * (N + 1)  # 体积 索引从1开始到n
value = [0] * (N + 1)  # 价值 索引从1开始到n
num = [0] * (N + 1)  # 个数 索引从1开始到n

for i in range(1, N + 1):
    volumn[i], value[i], num[i] = map(int, input().split())

f = [0 for i in range(V + 1)]  # 初始化全0


def Backpack_problem_lessspace(N, V, volumn, value, num, f):
    '''
    时间复杂度为O()，空间复杂度为O(V)
    :param N: 物品的个数
    :param V: 包的容积
    :param volumn: 物品容积的列表
    :param value: 物品价值的列表
    :param num: 物品个数的列表
    :param f: 二维数组
    :return: 返回最大价值
    '''
    for i in range(1, N + 1):
        for j in range(V, volumn[i] - 1, -1):  # 从后到前的顺序遍历
            for k in range(1, min(num[i], j // volumn[i]) + 1):
                f[j] = max(f[j - k * volumn[i]] + k * value[i], f[j])

    return f[-1]


if __name__ == '__main__':
    print(Backpack_problem_lessspace(N, V, volumn, value, num, f))

```

本质上，完全背包是多重背包的一个特例：当n[i]都大于等于 V / c[i]  时，多重背包就变为完全背包问题了；\
01背包是完全背包的一个特例：当第i种物品由可以取0,1,2，...件变为只能取0,1件时（也就是从V / c[i] + 1 \
种状态 变为2种状态），完全背包就变为01背包问题了。三者两两之间的关系有点像集合之间的包含关系。

# 2020.9.17 京东算法岗笔试题目分享

## 道具的魅力值(多重背包问题)

题目描述:\
在某网络游戏中提供了一个道具库，在道具库中每种道具均有若干件(数量已知)，游戏玩家购买一件道具将获得一\
定的魅力值。已知每种道具的价格和魅力值，请编写一个程序，在总价格不超过某个上限的情况下使得所购道具的\
魅力值之和达到最大。

输入描述:\
单组输入。\
每组测试数据的输入有n+ 1行，n表示道具的种类。\
第1行包含两个正整数，分别表示道具种类数n和总价值的上限p，两个数字之间用空格隔开。(n<=100, p<= 10000)\
第2行到第n+ 1行分别对应于第1种道具到第n种道具的信息，每1行包含三个正整数，两个数字之间用空格隔开，三个\
正整数分别表示某一种道具的数量、单个道具的价格和魅力值。

输出描述:\
每组测试数据的输出只有一行，即道具魅力值的最大和。

样例输入\
3 10\
2 2 3\
1 5 10\
2 4 12

样例输出\
27

```
N, V = map(int, input().split())  # 物品数， 背包容量

num = [0] * (N + 1)  # 个数 索引从1开始到n
volumn = [0] * (N + 1)  # 体积 索引从1开始到n
value = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    num[i], volumn[i], value[i] = map(int, input().split())

f = [0 for i in range(V + 1)]  # 初始化全0


def Backpack_problem_lessspace(N, V, volumn, value, num, f):
    '''
    时间复杂度为O()，空间复杂度为O(V)
    :param N: 物品的个数
    :param V: 包的容积
    :param volumn: 物品容积的列表
    :param value: 物品价值的列表
    :param num: 物品个数的列表
    :param f: 二维数组
    :return: 返回最大价值
    '''
    for i in range(1, N + 1):
        for j in range(V, volumn[i] - 1, -1):  # 从后到前的顺序遍历，只遍历到volumn[i]，再往前遍历放不下的
            for k in range(1, min(num[i], j // volumn[i]) + 1):
                f[j] = max(f[j - k * volumn[i]] + k * value[i], f[j])

    return f[-1]


if __name__ == '__main__':
    print(Backpack_problem_lessspace(N, V, volumn, value, num, f))

```
