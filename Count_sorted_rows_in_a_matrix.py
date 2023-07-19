n,m=map(int,input().split())
matrix=[]
c=0
for i in range(n):
    a=list(map(int,input().split()))
    b=a.copy()
    b.sort()
    x=b[::-1]
    if a==b or a==x:
        c+=1
print(c)