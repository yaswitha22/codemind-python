s=input()
c=0
if ' ' not in s:
    print(len(s))
else:
    s=s.split()
    for i in s:
       print(len(i),end=' ')