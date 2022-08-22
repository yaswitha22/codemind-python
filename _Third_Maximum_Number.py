n=int(input())
a=list(map(int,input().split()))
k=sorted(a)
t=[]
if(n<3):
    print(max(a))
else:
    for i in k:
        if i not in t:
           t.append(i)
    print(t[-3])
