t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sum1=n*(n+1)/2
    sum2=0
    for i in a:
        sum2+=i
    print(int(sum1-sum2))
    sum1=0
    sum2=0