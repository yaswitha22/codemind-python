def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
p,np=1,1
for i in a:
    if prime(i):
        p*=i
    else:
        np*=i
print(abs(np-p))
       
