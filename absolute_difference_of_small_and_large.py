s=input()
s=s.split()
for i in s:
    m=max(i)
    t=min(i)
    print(abs(ord(t)-ord(m)),end=' ')