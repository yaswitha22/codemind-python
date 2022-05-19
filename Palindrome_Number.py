t=int(input())
rev=0
for i in range(0,t):
    a=int(input())
    rev=0
    temp=a
    while a>0:
        d=a%10
        rev=rev*10+d
        a//=10
    if temp==rev:
        print("True")
    else:
        print("False")
