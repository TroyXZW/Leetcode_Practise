# 动脑子认老乡:smile:

[OJ输入输出例题](https://exercise.acmcoder.com/online/online_judge_ques?ques_id=9579&konwledgeId=137&opencustomeinput=true)

## 题目描述:								
大学的同学来自全国各地，对于远离家乡步入陌生大学校园的大一新生来说，碰到老乡是多么激动的一件事，\
于是大家都热衷于问身边的同学是否与自己同乡，来自新疆的小赛尤其热衷。但是大家都不告诉小赛他们来自哪里，\
只是说与谁是不是同乡，从所给的信息中，你能告诉小赛有多少人确定是她的同乡吗？

## 输入
包含多组测试用例。\
对于每组测试用例：\
第一行包括2个整数，N（1 <= N <= 1000），M(0 <= M <= N*(N-1)/2)，代表现有N个人（用1~N编号）和M组关系；\
在接下来的M行里，每行包括3个整数，a，b, c，如果c为1，则代表a跟b是同乡；如果c为0，则代表a跟b不是同乡；\
已知1表示小赛本人。

## 样例输入
3 1\
2 3 1\
5 4\
1 2 1\
3 4 0\
2 5 1\
3 2 1

## 样例输出
0\
3

```

#循环测试样例
while True:
	#每个样例第一行是人数和组数
    first_line = list(map(int,input().split(" ")))
    N = first_line[0]
    M = first_line[1]
    res = []
    for i in range(M):
        other_line_temp = list(map(int,input().split()))
        a, b, c = other_line_temp[0],other_line_temp[1],other_line_temp[2]
        #挑选有效组并排序，后续遍历方便
        if c == 1:
            r = [a, b] if a < b else [b, a]
            res.append(r)
	#排序
    s = set()
    s.add(1)
    res.sort() # 将1放到最前面，这样接下来的就会找1的老乡
	#一次遍历寻找同乡
    for i in res:
    	#两人之中有一个同乡，则都是同乡
        for j in (0,1):
            if i[j] in s:
            	#认识的同乡加入同乡集合，同乡的同乡还是同乡
                s.add(i[1-j])
    print(len(s) - 1)
```
