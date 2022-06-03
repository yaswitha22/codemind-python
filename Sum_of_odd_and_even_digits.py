n=int(input())
os=0
es=0
a=list(map(int,input().split()))
for i in range(n):
    if i%2==0:
        es+=a[i]
    elif i%2==1:
        os+=a[i]
if abs(es-os):
    print("NO")
else:
    print("YES")