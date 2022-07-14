s=input()
c=0
k=''
for i in s:
    if i in 'aeiouAEIOU' and i not in k:
       k+=i
if k=='':
    print("-1")
else:
    for i in k:
        print(i,end=' ')