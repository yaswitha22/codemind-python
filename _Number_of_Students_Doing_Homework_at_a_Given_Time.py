n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(m):
    if b[i]>=qt and a[i]<=qt:
        c+=1
print(c)