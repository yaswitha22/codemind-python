n=int(input())
for i in range(0,pow(2,n)):
    k=bin(i)[2:]
    
    if len(k)==n:
        print(k)
    else:
        s=""
        for i in range(n-len(k)):
            s+='0'
        k=str(k)
        s+=k
        print(s)
    