n=int(input())
l=list(map(int,input().split()))
k=min(l)
c=0
z=0
x=0
while k:
    d=k%10
    k=k//10
    c+=1
for i in l:
    z=0
    temp=i
    while i:
        d=i%10
        i=i//10
        z+=1
    if(z==c):
        x+=1
print(x)