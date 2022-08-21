s=input()
k=''
for i in s:
    if i==' ':
        pass
    else:
        k+=i
min1=min(k)
max1=max(k)
print(min1,s.count(min1),max1,s.count(max1),end=' ')