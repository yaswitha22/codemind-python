n=input()
n=n.split()
k=''
for i in range(len(n)):
    if i%2==0:
        k+=n[i][::-1]+' '
    else:
        k+=(n[i])+' '
print(k.strip())
        