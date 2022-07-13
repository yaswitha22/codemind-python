s=input()
s=s.split()
s1=0
s2=0
for i in s:
    m=max(i)
    t=min(i)
    s1+=ord(m)
    s2+=ord(t)
print(abs(s2-s1))
    