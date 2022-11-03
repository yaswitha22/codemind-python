n=int(input())
a=[]
while n:
    d=n%10
    n=n//10
    a.append(d)
for j in range(len(a)-1,-1,-1):
    if a[j]==6:
        a[j]=9
        break
s=""
a=a[::-1]
for i in a:
    s+=str(i)
print(s)