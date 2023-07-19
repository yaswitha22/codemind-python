def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a,b,c,d=map(int,input().split())
f=0
for i in range(a,b+1):
    f=0
    for j in range(c,d+1):
        if(prime(i+j)==1):
            f=1
            break
    if(f==0):
        print("Takahashi")
        break
else:
    print("Aoki")
