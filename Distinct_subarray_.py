n=int(input())
m=int(input())
c=0
a=[]
for i in range(n,m+1):
    a.append(i)
for i in range(len(a)):
    sum2=0
    for j in range(i,len(a)):
        sum2+=a[j]
        if(sum2%2==1):
            c+=1
print(c)