s=input()
s=s.lower()
c=0
max1=0
s=s.split()
for i in s:
    for j in range(len(i)):
        if i[j] in 'aeiou':
            c+=1
    if c>max1:
        max1=c
    c=0
print(max1)