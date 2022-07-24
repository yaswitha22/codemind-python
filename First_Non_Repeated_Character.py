t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    c=0
    for j in s:
        if s.count(j)==1:
            print(j)
            c=1
            break
    if c==0:
        print("-1")
    