n=int(input())
l=list(map(int,input().split()))
t=sum(l)//n
c=0
for i in l:
    if i>=t:
        c+=1
print(c)