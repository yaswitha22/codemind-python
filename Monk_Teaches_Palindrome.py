t=int(input())
k=0
for i in range(t):
    a=input()
    k=a[::-1]
    if k==a:
        if len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")