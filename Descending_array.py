n=int(input())
a=list(map(int,input().split()))
if a[::-1]==sorted(a):
    print("yes")
else:
    print("no")