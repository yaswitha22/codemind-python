n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n):
        if a[i]>a[j]:
            c+=1
    print(c,end=' ')
    c=0