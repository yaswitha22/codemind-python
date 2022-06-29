x=input()
x=x.split()
c=0
for i in x:
    k=list(i)
    if k[0] in 'AEIOUaeiou' and k[-1] not in 'AEIOUaeiou':
        c+=1
        
print(c)