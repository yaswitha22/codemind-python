def notprime(n):
    if n==1:
        return 1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 1
    else:
        return 0
n=int(input())
k=[]
for i in range(1,n+1):
    if n%i==0:
        k.append(i)
c=[]
for i in range(len(k)):
    if notprime(k[i]):
        c.append(k[i])
print(len(c))