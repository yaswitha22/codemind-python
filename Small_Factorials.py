t=int(input())
sf=1
for i in range(t):
    a=int(input())
    sf=1
    for j in range(a,1,-1):
        sf*=j
    print(sf)