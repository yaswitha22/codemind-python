n=int(input())
temp=n
c=0
rev=0
t=0
h=0
k=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
for i in range(1,temp+1):
    if temp%i==0:
        c+=1
if c==2:
    k+=1
for j in range(1,rev+1):
    if rev%j==0:
        t+=1
if t==2:
    h+=1
if k>0 and h>0:
    print('circular prime')
elif k>0 and h==0:
    print('prime but not a circular prime')
else:
    print('not prime')