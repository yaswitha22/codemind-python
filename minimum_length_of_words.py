s=input()
s=s.split()
min1=999
c=0
for i in s:
    if len(i)<min1:
        min1=len(i)
print(min1)