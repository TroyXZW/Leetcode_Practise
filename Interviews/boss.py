"""
xj
1001	001:5.6|002:3.2|010:5.1|003:5.2|004:3.7|005:3.1|006:5.0|007:2.8|008:1.1
1002	001:5.1|002:3.2|010:5.5|003:5.2|004:3.7|005:3.1|006:5.0|007:2.8|008:8.1
1003	001:5.1|002:2.2|010:5.5|003:1.2|004:3.7|005:3.1|006:5.0|007:2.8|008:8.1
1004	001:1.1|002:2.2|010:5.5|003:1.2|004:3.7|005:2.1|006:5.0|007:2.8|008:8.1
xj
1001	001:8.6|002:1.2|010:5.1|003:5.2|004:3.7|005:1.1|006:5.0|007:2.8|008:7.1
1002	001:1.1|002:3.2|010:2.5|003:7.2|004:3.7|005:3.1|006:5.0|007:3.8|008:8.1
1003	001:5.1|002:5.2|010:5.5|003:1.2|004:2.7|005:3.1|006:5.0|007:2.8|008:2.1
1004	001:2.1|002:2.2|010:3.5|003:1.2|004:3.7|005:1.1|006:2.0|007:2.8|008:8.1
xj
uid	pid_score
xj
统计两个文件 相同uid下的  分数前3/5/7对应的pid交集比例
xj
如
1001    x/3、x/5、x/7
1002   x/3、x/5、x/7
1003   x/3、x/5、x/7
1004   x/3、x/5、x/7

"""


def read_file(file1):
    res1 = {}
    with open(file1, "r") as f1:
        for line in f1.readlines():
            line = line.split("\t")
            uid = line[0]  # str
            pid_score = line[1].split("|")
            res1[uid] = pid_score
    return res1


def topN(lista, n):
    tmp = []
    for i in lista:
        pid_score = i.split(":")
        # print(pid_score)
        tmp.append([pid_score[0], float(pid_score[1])])
    tmp.sort(key=lambda x: x[1], reverse=True)
    res = tmp[:n]
    # print(res)
    return res


from collections import defaultdict


def find_same(f1_uid, f2_uid):
    n = 0
    tmp = defaultdict(int)
    for i in f1_uid:
        tmp[i[0]] = 1
    for j in f2_uid:
        if tmp[j[0]] == 1:
            tmp[j[0]] += 1
    # print(tmp)
    for v in tmp.values():
        if v == 2:
            n += 1
    return n


def func(f1, f2):
    for uid, pid in f1.items():
        toplist = []
        if not f1[uid]:
            continue
        for i in [3, 5, 7]:
            f1_uid = topN(f1[uid], i)
            f2_uid = topN(f2[uid], i)
            # print(f1_uid,f2_uid)
            toplist.append((find_same(f1_uid, f2_uid) / i))
        print(f"uid: {uid}    {toplist[0]} {toplist[1]} {toplist[2]}")


if __name__ == "__main__":
    file1 = "C:/Users/Troy/Desktop/111.csv"
    file2 = "C:/Users/Troy/Desktop/222.csv"
    f1 = read_file(file1)
    f2 = read_file(file2)
    func(f1, f2)
