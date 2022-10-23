n=int(input())
a=list(map(int,input().split()))
os=0
es=0
for i in range(n):
    if i%2==0:
        es+=a[i]
    else:
        os+=a[i]
if abs(os-es)%4==0:
    print("X")
else:
    print("Y")