a=input()
c=0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c+=1
else:
    if c==0:
        print("0")
    else:
        print(c)