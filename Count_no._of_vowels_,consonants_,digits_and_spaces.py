a=input()
vc=0
cc=0
dc=0
sc=0
for i in a:
    if i==" ":
        sc+=1
    elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vc+=1
    elif i>='0' and i<='9':
        dc+=1
    elif i!='a' or i!='e' or i!='i' or i!='o' or i!='u':
        cc+=1
    else:
        continue
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sc)