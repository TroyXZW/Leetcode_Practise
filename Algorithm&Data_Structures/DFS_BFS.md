# 深度优先（DFS）和广度优先（BFS）

***深度优先搜索（Depth-First-Search）***是搜索算法的一种。是沿着树的深度遍历树的节点，尽可能深的搜索树的分支。\
当节点v的所有边都己被探寻过，搜索将回溯到发现节点v的那条边的起始节点。这一过程一直进行到已发现从源节点可\
达的所有节点为止。如果还存在未被发现的节点，则选择其中一个作为源节点并重复以上过程，整个进程反复进行直到\
所有节点都被访问为止，属于盲目搜索。\
由于时间复杂度太高，我们也叫做暴力搜索。

***广度优先搜索（Breadth-First-Search）***是从根节点开始，沿着树的宽度遍历树的节点。如果所有节点均被访问，则算法中止。


## 定义一个图的结构

```
'''
    /B--D-F
   A  / |
    \C--E
'''
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}
```
## DFS 深度优先搜索(使用栈实现)  回溯法
```
def DFS(graph, s):  # graph图,s指的是开始结点
    stack = []  # 使用列表作为栈
    stack.append(s)  # 将首个元素添加到队列中
    seen = set()  # 使用集合来存放已访问过的节点,看是否访问过该结点
    seen.add(s)  # 将首个节点添加到集合中表示已访问
    while (len(stack) > 0):  # 当队列不为空时进行遍历
        vertex = stack.pop()  ## 从栈尾取出一个节点并查询该节点的相邻节点
        nodes = graph[vertex]
        for w in nodes:  # 判断节点是否存在于已访问集合中,即是否已被访问过
            if w not in seen:  # 如何判断是否访问过，使用一个数组
                stack.append(w)  # 若未被访问,则添加到队列中
                seen.add(w)  # 同时添加到已访问集合中,表示已被访问
        print(vertex)
```
## BFS 广度优先搜索(使用队列实现)  层序遍历
```
def BFS(graph, s):  # graph图,s指的是开始结点
    queue = []  # 需要一个队列
    queue.append(s)  # 将首个节点添加到队列中
    seen = set()  # 使用集合来存放已访问过的节点,看是否访问过该结点
    seen.add(s)  # 将首个节点添加到集合中表示已访问
    while (len(queue) > 0):  # 当队列不为空时进行遍历
        vertex = queue.pop(0)  # 从队列头部取出一个节点并查询该节点的相邻节点
        nodes = graph[vertex]  # 子节点的数组
        for w in nodes:  # 判断节点是否存在于已访问集合中,即是否已被访问过
            if w not in seen:  # 判断是否访问过，使用一个数组
                queue.append(w)  # 若未被访问,则添加到队列中
                seen.add(w)  # 同时添加到已访问集合中,表示已被访问
        print(vertex)      
```
输出结果
```
print("BFS", end=" ")
BFS(graph, "A")
print("")
print("DFS", end=" ")
DFS(graph, "A")
```

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
接下来n行表示地图，每一行都有m个字符， 其中S表示王子的位置，E表示公主的位置，'.'表示可以通行，'#'表示障碍物(不能通行)。

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
