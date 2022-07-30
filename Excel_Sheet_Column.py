def exc(n):
        ans=[]
        while n>0:
            ans.append(chr(65+(n-1)%26))
            n=(n-1)//26
        return "".join(reversed(ans))
n=int(input())
print(exc(n))