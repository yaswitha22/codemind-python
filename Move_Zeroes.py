n=int(input())
a=list(map(int,input().split()))
k=[]
t=[]
for i in a:
    if i==0:
        k.append(i)
    else:
        t.append(i)
s=t.extend(k)
print(*t)