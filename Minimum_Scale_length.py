n=int(input())
a=list(map(int,input().split()))
k=min(a)
for i in range(k,0,-1):
    res=0
    for j in range(n):
        if a[j]%i!=0:
            res=1
            break
    if res==0:
        print(i)
        break