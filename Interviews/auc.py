lista=[[0, 0.2], [1, 0.5], [0, 0.6], [1, 0.8]]
lista.sort(key=lambda x:x[1])
pos_num,neg_num=0,0
ranking_sum=0
for i in range(len(lista)):
    if lista[i][0]==1:
        pos_num+=1
        ranking_sum+=i+1
    else:
        neg_num+=1
auc=(ranking_sum-(pos_num*(pos_num+1)/2))/(pos_num*neg_num)
print(auc)
