n=int(input())
sd=0
pd=1
while n!=0:
    d=n%10
    sd+=d
    pd*=d
    n=n//10
print(pd-sd)
