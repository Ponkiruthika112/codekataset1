def call(i):
    s=list(str(i))
    c=0
    for i in range(0,len(s)):
        c=c+int(s[i])
    return c
n=int(input())
c=0
d=[]
i=1
j=n-1
while i<n and j>0:
    if i==call(j) and i+j==n:
        c=c+1
        d.append(j)
        break
    
    elif call(i)==j and i+j==n:
        c=c+1
        d.append(i)
        break
    else:
        j=j-1
        i=i+1
print(c)
print(*d)
        
            
#r
