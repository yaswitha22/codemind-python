n=int(input())
a=0
b=1
c=0
j=0
k=[]
for i in range(1,n+1):
    k.append(a)
    c=a+b
    a=b
    b=c
    j+=1
for i in range(1,n):
    if k[i]>n:
      break
if n-k[i-1]==k[i]-n:
    print(k[i-1],k[i],end=" ")
elif n-k[i-1]>k[i]-n:
    print(k[i])
else:
    print(k[i-1])