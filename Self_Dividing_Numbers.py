a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    while temp:
        d=temp%10
        if d==0 or i%d!=0:
            break
        temp//=10
    if temp==0:
        print(i,end=' ')
        
        
        