import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
val=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(val)
print('{:.2f}'.format(area))