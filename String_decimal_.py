t=int(input())
for i in range(t):
    a=input()
    c=0
    for k in a:
        if k>='0' and k<='9':
            c+=1
    if c==len(a):
        print("True")
    else:
        print("False")