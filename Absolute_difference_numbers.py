x,n=map(int,input().split())
c=0
diff=0
temp=x
temp1=x
while x:
    d=x%10
    c+=1
    x=x//10
while temp:
    d=temp%pow(10,n)
    d1=temp1//pow(10,(c-n))
    temp//=10
    break
diff=abs(d1-d)
print(diff)

    
    