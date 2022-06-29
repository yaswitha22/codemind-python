x=int(input())
l=list(map(int,input().split()))
y=int(input())
k=set(l)
c=0
for i in k:
    if l.count(i)==y:
        c+=1
        print(i,end=" ")
if c==0:
    print("-1")