s=input()
s=s.lower()
s=s.split()
l=[]
c=0
for i in s:
    k=[char for char in i]
    for j in k:
        if j in 'aeiou':
            c+=1
    l.append(c)
    c=0
print(min(l))