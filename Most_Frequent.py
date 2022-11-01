n=int(input())
a=list(map(int,input().split()))
k=[]
t=set(a)
t=list(t)
for i in t:
    k.append(a.count(i))
s=max(k)
f=k.index(s)
print(t[f])