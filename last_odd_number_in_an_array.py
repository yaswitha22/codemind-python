n=int(input())
arr=list(map(int,input().split()))
k=[]
for i in arr:
    if i%2==1:
        k.append(i)

print(k[-1])
