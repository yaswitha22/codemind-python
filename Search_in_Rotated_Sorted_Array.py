n=int(input())
a=list(map(int,input().split()))
b=int(input())
c=0
if b in a:
    print(a.index(b))
    c+=1
if c==0:
    print('-1')