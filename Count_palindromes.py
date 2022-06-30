n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if str(i)==str(i)[::-1]:
        c+=1
print(c)