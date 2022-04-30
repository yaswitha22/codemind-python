n=int(input())
ld=0
while n!=0:
    d=n%10
    if d>ld:
        ld=d
    n=n//10
print(ld)