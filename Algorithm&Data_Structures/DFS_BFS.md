# 2020.9.17 京东算法岗笔试题目分享

## 王子与公主

题目描述:\
在一个n行m列的二维地图中，王子的位置为(x1,y1),公主的位置为(x2,y2)。\
在地图中设有一些障碍物，王子只能朝上、下、左、右四个方向行走，且不允许走出地图也不允许穿越障碍物。\
请编写一个程序判断王子是否可以顺利走到公主所在的位置。

输入描述:\
多组输入，第1行输入一个正整数T表示输入数据的组数。\
对于每一组输入数据: 输入n+1行。\
其中，第1行输入两个正整数n和m表示地图的大小，n为行数，m为列数。(n<=100,m<=100)\
接下来n行表示地图，每一行都有m个字符， 其中S表示王子的位置，E表示公主的位置，':表示可以通行，'#'表示障碍物(不能通行)。

输出描述:\
针对每一组输入数据， 判断王子是否能够到达公主所在位置?如果可以输出"YES"，否则输出"NO"。

样例输入\
2\
2 2\
.E\
S.\
2 2\
#E\
S#

样例输出\
YES \
NO

```
def dfs(graph, i, j):
    if i < 0 or j < 0 or i >= len(graph) or j >= len(graph[0]) or graph[i][j] == '#': return False
    if graph[i][j] == 'E': return True
    graph[i][j] = '#'
    res = dfs(graph, i+1, j) or dfs(graph, i-1, j) or dfs(graph, i, j+1) or dfs(graph, i, j-1)
    graph[i][j] = '.'
    return res

t = int(input().strip())
while t > 0:
    line = input().strip().split()
    n, m = [int(x) for x in line]
    graph = []
    for i in range(n):
        line = input().strip()
        graph.append(list(line))
    res = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'S':
                res = dfs(graph, i, j)
    if res: print("YES")
    else: print("NO")
    t -= 1
```
```
def dfs(graph,i,j):
    if i<0&nbs***bsp;j<0&nbs***bsp;i >= len(graph)&nbs***bsp;j >= len(graph[0])&nbs***bsp;graph[i][j]=='#':return False
    if graph[i][j] =="E":return True
    graph[i][j] = '#'#这一步是让这个位置在下一步不会重复走到
    bz = dfs(graph,i+1,j)&nbs***bsp;dfs(graph,i-1,j)&nbs***bsp;dfs(graph,i,j+1)&nbs***bsp;dfs(graph,i,j-1)
    graph[i][j] = '.'#恢复这个位置的.
    return bz




t = int(input())
while t>0:
    n , m = map(int,input().split())
    graph = []
    for i in range(n):
        graph.append(list(input()))
    for i in range(n):
        for j in range(m):
            if graph[i][j] =='S':
                res = dfs(graph,i,j)
    if res:
        print('YES')
    else:
        print('NO')
    t -= 1
```
