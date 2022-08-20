n=input()
k=''
for i in n:
    if i in 'aeiouAEIOU' and i not in k:
        k+=i+' '
if k=='':
    print("-1")
else:
    print(k.strip())