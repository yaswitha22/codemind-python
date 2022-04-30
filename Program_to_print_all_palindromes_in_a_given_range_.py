a=int(input())
b=int(input())
rev=0
temp=0
for i in range(a,b+1):
    temp=i
    while i!=0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if temp==rev:
       print(rev,end=' ')
    rev=0
    