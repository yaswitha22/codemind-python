l,r,k=map(int,input().split())
a=0
for i in range(l,r+1):
     if i%k==0:
         a+=1
print(a)