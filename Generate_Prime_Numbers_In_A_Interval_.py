a=int(input())
b=int(input())
for i in range(a,b+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        if i==1:
            continue
        else:
            print(i)