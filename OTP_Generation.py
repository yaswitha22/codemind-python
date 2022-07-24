n=input()
for i in n:
    if int(i)%2==0:
        continue
    else:
        print(int(i)*int(i),end='')