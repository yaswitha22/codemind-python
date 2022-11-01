import math
n=int(input())
a=list(map(int,input().split()))
sum1=0
for i in a:
    t=int(math.sqrt(i))
    if t*t==i:
        sum1+=i
print(sum1)