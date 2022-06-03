n=int(input())
a=list(map(int,input().split()))
s=set(a)
k=0
for i in s:
    if a.count(i)%2==0:
        k+=(a.count(i)//2)
    elif a.count(i)%2==1:
        k+=(a.count(i)//2)
print(k)