n=int(input())
l=list(map(int,input().split()))
c=0
t=max(l)
s=len(str(t))
for i in l:
    if len(str(i))==s:
        c+=1
print(c)