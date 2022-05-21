t=int(input())
c=0
for i in range(t):
    a=input()
    for i in a:
        if i>='0' and i<='9':
            print("Yes")
            c+=1
            break
    if c==0:
        print("No")
    c=0
