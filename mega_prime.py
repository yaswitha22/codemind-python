n=int(input())
for i in range(2,int(n**0.5)+1):
    if (n%i==0 or n==1):
        print("Not Mega Prime")
        break
else:
    k=0
    pd=0
    while n:
        d=n%10
        k+=1
        if d==2 or d==3 or d==5 or d==7:
            pd+=1
        n//=10
    if k==pd:
        print("Mega Prime")
    else:
        print("Not Mega Prime")