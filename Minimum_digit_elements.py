n=int(input())
l=list(map(int,input().split()))
s=min(l)
k=len(str(s))
c=0
for i in l:
    if len(str(i))==k:
        c+=1
print(c)