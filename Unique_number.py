n=int(input())
a=0
b=0
c=0
e=0
f=0
g=0
h=0
i=0
j=0
while n:
    d=n%10
    if d==1:
        a+=1
    elif d==2:
        b+=1
    elif d==3:
        c+=1
    elif d==4:
        e+=1
    elif d==5:
        f+=1
    elif d==6:
        g+=1
    elif d==7:
        h+=1
    elif d==8:
        i+=1
    elif d==9:
        j+=1
    n//=10
if a==2 or b==2 or c==2 or e==2 or f==2 or g==2 or h==2 or i==2 or j==2:
    print("Not Unique Number")
else:
    print("Unique Number")