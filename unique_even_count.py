n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i%2==0 and i not in k:
        k.append(i)
print(len(k))