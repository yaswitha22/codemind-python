n=int(input())
a=list(map(int,input().split()))
if len(a)%2==1:
    m=len(a)//2+1
else:
    m=n//2
for i in range(len(a)-1,m-1,-1):
    print(a[i],end=' ')
for i in range(m):
    print(a[i],end=' ')