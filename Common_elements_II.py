a,b=map(int,input().split())
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
k=[]
for i in s1:
    if i not in s2 and i not in k:
        k.append(i)
for i in s2:
    if i not in s1 and i not in k:
        k.append(i)
print(*k)
