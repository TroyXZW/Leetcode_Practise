# ------------------------------------------- 判断单链表是否有环，并找出环的入口 -------------------------------------------

class Node():  # 定义一个Node类，构造两个属性，一个是item节点值，一个是节点的下一个指向
    def __init__(self, item=None):
        self.item = item
        self.next = None


def findbeginofloop(head):  # 判断是否为环结构并且查找环结构的入口节点
    slowPtr = head  # 将头节点赋予slowPtr
    fastPtr = head  # 将头节点赋予fastPtr
    loopExist = False  # 默认环不存在，为False
    if head == None:  # 如果头节点就是空的，那肯定就不存在环结构
        return False
    while fastPtr.next != None and fastPtr.next.next != None:  # fastPtr的下一个节点和下下个节点都不为空
        slowPtr = slowPtr.next  # slowPtr每次移动一个节点
        fastPtr = fastPtr.next.next  # fastPtr每次移动两个节点 
        if slowPtr == fastPtr:  # 当fastPtr和slowPtr的节点相同时，也就是两个指针相遇了
            loopExist = True
            print("存在环结构")
            break

    if loopExist == True:
        slowPtr = head
        while slowPtr != fastPtr:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next
        return slowPtr

    print("不是环结构")
    return False


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    print(findbeginofloop(node1).item)
    
    
# ------------------------------------------- 二叉树的右视图 -------------------------------------------

class Solution(object):
    """
    深度优先搜索：总是先访问右子树。那么对于每一层来说，我们在这层见到的第一个结点一定是最右边的结点。
    时间复杂度 : O(n)。深度优先搜索最多访问每个结点一次，因此是线性复杂度。
    空间复杂度 : O(n)。最坏情况下，栈内会包含接近树高度的结点数量，占用 O(n) 的空间。
    https://leetcode-cn.com/problems/binary-tree-right-side-view/solution/er-cha-shu-de-you-shi-tu-by-leetcode-solution/
    """
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val) # setdefault(depth, node.val)若depth不存在，则插入；若存在不做修改

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]


# -------------------------------------------

from collections import deque

class Solution(object):
    """
    广度优先搜索
    时间复杂度 : O(n)。 每个节点最多进队列一次，出队列一次，因此广度优先搜索的复杂度为线性。
    空间复杂度 : O(n)。每个节点最多进队列一次，所以队列长度最大不不超过 n，所以这里的空间代价为 O(n)。
    """
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]


# ------------------------------------------- 有向无环图拓扑排序的实现 -------------------------------------------
"""
https://leetcode-cn.com/problems/course-schedule/
https://leetcode-cn.com/problems/course-schedule-ii/
"""


# ------------------------------------------- 二叉搜索树的后序遍历序列 -------------------------------------------

https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/

# ------------------------------------------- 区间列表的交集 -------------------------------------------

class Solution:
    """
    由于每个区间列表都是成对不相交的，通过观察示例图像，我们可以发现相交的区间的low(设相交区间的区间为[low,high])
    为A，B两个区间列表中的max(A[i][0],B[j][0]),同理high为A，B两个区间列表中的min(A[i][1],B[j][1])。
    这样我们就可以设置两个指针i，j分别指向A，B两个区间列表，取low = max(A[i][0], B[j][0]),high = min(A[i][1], B[j][1]),
    如果 low <= high,则具有相交区间，否则根据A[i][1]，B[j][1]的关系，改变i，j的指针值，循环往复，直到遍历其中一个列表为止。
    
    https://leetcode-cn.com/problems/interval-list-intersections/solution/qu-jian-lie-biao-de-jiao-ji-by-leetcode/
    
    时间复杂度：O(M + N)，其中 M, N 分别是数组 A 和 B 的长度。
    空间复杂度：O(M + N)，答案中区间数量的上限。
    """
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i , j = 0 , 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans


