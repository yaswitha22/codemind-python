def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
a=int(input())
b=int(input())
i=1
while True:
    tot=a+b+i
    if isprime(tot):
        print(i)
        break
    i+=1
    