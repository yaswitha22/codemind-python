vowel=['a','e','i','o','u']
a=list(input())
b=[a[0]]
c=0
for i in range(1,len(a)):
    if(b[c] in vowel)and(a[i] in vowel):
        continue
    elif(b[c] not in vowel)and(a[i] not in vowel):
        continue
    else:
        b.append(a[i])
        c+=1
s=''
for i in b:
    if i in vowel:
        s+='V'
        continue
    s+='C'
print(s)

'''s="whereabou"
v='aeiou'
x,y='',''    
ans=''        
for i in range(len(s)):
    if s[i] not in v:  
        if len (y)!=0:
            ans+='V'
            y=''
        x+=s[i]
    else:
        if len(x)!=0:
            x=''
            ans+='C'
        y+=s[i]
if x!='':ans+='C'
if y!='':ans+='V'
print(ans)'''
