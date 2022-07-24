n=int(input())
a=list(map(int,input().split()))
c=0
a=list(set(a))
for i in a:
    if i%2==1 and a.count(i)==1:
        c+=1
print(c)