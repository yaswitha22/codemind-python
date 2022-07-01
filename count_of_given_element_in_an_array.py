a=int(input())
arr=list(map(int,input().split()))
k=int(input())
c=0
for i in arr:
    if i==k:
        c+=1
print(c)