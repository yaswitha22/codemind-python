k=[]
c=0
for i in range(int(input())):
    n=int(input())
    k.append(n)
tw=int(input())
for i in k:
    if i<=tw:
        c+=1
    else:
        c+=2
print(c)