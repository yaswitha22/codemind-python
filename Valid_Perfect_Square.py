t=int(input())
for i in range(t):
    a=int(input())
    c=0
    for j in range(1,int(a**0.5)+1):
        if(j*j)==a:
            print("True")
            c+=1
            break
    if c==0:
        print("False")