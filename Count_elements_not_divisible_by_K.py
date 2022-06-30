n,k=map(int,input().split())
c=0
arr=list(map(int,input().split()))
for i in range(n):
    if abs(arr[i])%k!=0:
        c+=1
print(c)