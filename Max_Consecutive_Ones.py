n=int(input())
a=list(map(int,input().split()))
max1=0
c=0
for i in a:
    if i==1:
        c+=1
    else:
        if c>max1:
            max1=c
            c=0
if a[-1]==1 and c>max1:
    print(c)
else:
    print(max1)