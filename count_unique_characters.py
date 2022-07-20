s=input()
k=''
s=s.lower()
for i in s:
    if s.count(i)==1 and i!=' ':
        k+=i

print(len(k))