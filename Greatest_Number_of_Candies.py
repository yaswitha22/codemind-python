n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in range(n):
    if (a[i]+b)>=max(a):
        print("True",end=' ')
    else:
        print("False",end=' ')