n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in arr:
    if i%2==0:
        k.append(i)
k=sorted(k)
print(k[-1])