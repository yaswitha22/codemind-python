a=int(input())
rev=0
s=0
if a>0:
    while a:
        d=a%10
        rev=rev*10+d
        a=a//10
    print(rev)
else:
    s=abs(a)
    while s:
        d=s%10
        rev=rev*10+d
        s=s//10
    print(-rev)
    
    