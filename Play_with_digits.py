n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
for i in a:
    while i:
        d=i%10
        sum1+=d
        i//=10
    sum2+=sum1
    sum1=0
print(sum2)