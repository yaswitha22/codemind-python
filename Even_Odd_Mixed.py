a=int(input())
c=0
t=0
k=0
while a!=0:
    d=a%10
    c+=1
    if d%2==0:
        k+=1
    elif d%2==1:
        t+=1
    a=a//10
if k==c:
    print('Even')
elif t==c:
    print('Odd')
else:
    print('Mixed')