a,b=map(int,input().split())
if abs(b-a)==1 or (a==10 and b==1) or (b==10 and a==1):
    print("Yes")
else:
    print("No")