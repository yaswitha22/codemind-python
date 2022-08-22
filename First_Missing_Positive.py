n=int(input())
a=list(map(int,input().split()))
k=sorted(a)
if 1 not in k:
    print('1')
else:
    i=1
    while i<=0 or i>0:
        if i not in k:
            print(i)
            break
        i+=1
