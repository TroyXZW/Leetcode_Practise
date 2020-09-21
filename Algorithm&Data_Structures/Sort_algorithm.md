# 常见排序算法:smile:

**比较类：
    交换类排序：冒泡排序、快速排序
    选择类排序：选择排序、堆排序
    插入类排序：插入排序、希尔排序
    归并类排序：归并排序
非比较类：
    分布类排序：基数排序，计数排序，桶排序
    并发类排序
    混合类排序
    其他
**


## 选择排序 
```
def selectionSort(lyst):
    """
    时间复杂度 O(n2)
    """
    for i in range(len(lyst)):
        minIndex = i
        for j in range(i + 1, len(lyst)):
            if (lyst[j] < lyst[minIndex]):
                minIndex = j
        if minIndex != i:
            lyst[i], lyst[minIndex] = lyst[minIndex], lyst[i]
    print("selectionSort:", lyst)
```

## 冒泡排序
```
def bubbleSort_improved(items):
    """
    原本要排序的列表即为有序列表，则添加一个bool变量用做判断，如无交换则直接return
    m每次冒泡其实就是把当前最大元素放最后，下一次循环所以就可以不考虑len(items) - 1 - i
    时间复杂度 O(n2)
    """
    for i in range(len(items) - 1):
        flag = False
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                flag = True
        if not flag:
            break
    return items


if __name__ == '__main__':
    a = [7, 5, 9, 8, 1, 4]
    print(bubbleSort_improved(a))
```

## 插入排序
```
def insertionSort(arr):
    """
    这种是直接将新数字放到已排好数据里一个个比较后插入
    时间复杂度 O(n2)
    """
    n = len(arr)
    for i in range(1, n):
        for j in range(i, -1, -1):
            if j > 1 and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


# ---------------------------------------------------
def InsertSort(lst):
    """
    这种是先把待排序数据腾出，然后把其他数据补上，这样待排序数组的排序位置就会腾空，再补上就好
    """
    n = len(lst)
    if n <= 1:
        return lst
    for i in range(1, n):
        j = i
        target = lst[i]  # 每次循环的一个待插入的数
        while j > 0 and target < lst[j - 1]:  # 比较、后移，给target腾位置
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = target  # 把target插到空位
    return lst
```

## 快速排序
```
lyst = [8, 7, 3, 1, 2, 3, 6, 0, 12, 7]
a = deepcopy(lyst)
# 快速排序的基本思想为：
"""两个哨兵变量，一个pivot，j--，i++，，lyst[j]<pivot停，lyst[i]>pivot停，ij相碰时将lyst[i]与pivot进行对调"""
"""需要把list作为一个接口参数，不然deecopy的引用参数无法传入，直接传入lyst的引用，会修改原始的lyst变量"""


def quickSort(lyst, left, right):
    """
    时间复杂度 O(nlogn)
    """
    # 需要加上left和right的判断，不然会超过最大迭代次数，导致栈内存溢出
    if left > right:
        return
    temp = lyst[left]
    i, j = left, right
    while i < j:
        while lyst[j] >= temp and i < j:
            j -= 1
        while lyst[i] <= temp and i < j:
            i += 1
        if i < j:
            lyst[j], lyst[i] = lyst[i], lyst[j]  # 找到一个比基准大的书，和一个比基准小的数，将他们互换位置
    lyst[i], lyst[left] = lyst[left], lyst[i]
    quickSort(lyst, left, i - 1)
    quickSort(lyst, i + 1, right)


def print_quicksort(lyst):
    quickSort(lyst, 0, len(lyst) - 1)
    print("quickSort:", lyst)


print_quicksort(a)
print("initial list:", lyst)


# ---------------------------------------------------
def QuickSort(lst):
    # 此函数完成分区操作
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left += 1
            # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置
            (arr[left], arr[right]) = (arr[right], arr[left])

        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换
        (arr[left], arr[key]) = (arr[key], arr[left])
        # 返回目前基准所在位置的索引
        return left

    def quicksort(arr, left, right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr, left, right)
        # 递归调用
        # print(arr)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(lst)
    if n <= 1:
        return lst
    quicksort(lst, 0, n - 1)
    return lst
```

## 归并排序
```
"""快排与合并排序的基础思想都是递归。对于合并排序每一次都拆成了两个子序列，直到最后两个子序列的长度均为1，"""


def mergeSort(lyst):
    """
    时间复杂度 O(nlogn)
    """
    if len(lyst) == 1:
        return lyst
    # 取拆分的中间位置，拆分成左右两个子串
    mid = len(lyst) // 2
    left = lyst[:mid]
    right = lyst[mid:]
    ll = mergeSort(left)
    rl = mergeSort(right)
    return merge(ll, rl)


# 每次取小数放入新开辟的列表空间
# 左右子序列进行比较，比较完成后会留下对应的需要加合的left和right序列
def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res


print("mergeSort:", mergeSort(lyst))
```

## 堆排序
```
'''堆排序'''
'''1.从下至上，从右至左，对每个节点进行调整，以得到一个大顶堆'''
'''2.首尾互换，尾部元素已是有序序列，堆元素个数减1，此部分仍为无序序列，继续调整'''
'''最坏，最好，平均时间复杂度均为O(nlogn)'''


def big_endian(lyst, start, end):
    '''
    构造大顶堆
    '''
    root = start  # 取出当前元素,令其为根节点
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and lyst[child] < lyst[child + 1]:
            child += 1
        if lyst[root] < lyst[child]:
            lyst[root], lyst[child] = lyst[child], lyst[root]
            root = child
        else:
            break


def heap_sort(lyst):
    """
    时间复杂度 O(nlogn)
    """
    first = len(lyst) // 2 - 1
    for start in range(first, -1, -1):
        big_endian(lyst, start, len(lyst) - 1)
    for end in range(len(lyst) - 1, 0, -1):  # 交换堆顶和最后一个元素，并调整堆结构
        lyst[0], lyst[end] = lyst[end], lyst[0]
        big_endian(lyst, 0, end - 1)


l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
print(l)
heap_sort(l)
print(l)
```

## 基数排序
```
import math


def radix_sort(arr):
    """
    时间复杂度 O(n)
    """
    radix = 10  # 基数
    k = int(math.ceil(math.log(max(arr), radix)))  # k可以表示任意整数
    # math.log对arr中最大的数取对数，log(max(arr),10),并对其取整得到最大值的位数
    bucket = [[] for i in range(radix)]
    for i in range(1, k + 1):
        for value in arr:
            bucket[int(value % (radix ** i) / (radix ** (i - 1)))].append(value)  # 析取整数第k位数字（从低到高）10**2位10的二次方
        del arr[:]
        for each in bucket:
            arr.extend(each)  # 桶合并
        bucket = [[] for i in range(radix)]


# ---------------------------------------------------
def radix_sort(arr):
    """基数排序"""
    i = 0  # 记录当前正在排哪一位，最低位为1
    max_num = max(arr)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list = [[] for _ in range(10)]  # 初始化桶数组
        for x in arr:
            bucket_list[int(x // (10 ** i)) % 10].append(x)  # 找到位置放入桶数组
        arr.clear()
        for x in bucket_list:  # 放回原序列
            for y in x:
                arr.append(y)
        i += 1
    return arr


if __name__ == "__main__":
    a = [10, 2, 13, 44, 22, 33, 100, 612, 333, 262]
    radix_sort(a)
    print(a)
```

## 计数排序
```
def countingSort(arr):
    """
    计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数
    桶内排序,插入排序
    时间复杂度 O(n)
    """
    bucketLen = max(arr) + 1
    bucket = [0] * bucketLen
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    # arr = []#额外多了len(arr)的空间
    # for i in range(0, num + 1):
    #     for j in range(0, count[i]):
    #         arr.append(i)
    for j in range(bucketLen):  # 直接在原序列上排序，省空间
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr


if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list)
    result = countingSort(list)
    print("List sort is:", result)
```

## 桶排序
```
def insertionSort(b):
    """
    桶内排序,插入排序
    时间复杂度 O(n)
    """
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def bucketSort(list):
    arr = []
    slot_num = 10  # 10 means 10 slots, each slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

        # Put array elements in different buckets
    for j in list:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

        # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

        # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k += 1
    return list


if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list)
    result = bucketSort(list)
    print("List sort is:", result)
```
