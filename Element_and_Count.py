n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i not in k:
        k.append(i)
for j in k:
    print(j,l.count(j),end=' ')