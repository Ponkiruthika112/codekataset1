def prime(n):
    c=0
    if n==2:
        c=1
    elif n==1:
        c=0
    else:
        for i in range(2,n):
            if n%i==0:
                break
        if i==n-1:
            c=1
    return c
def sum(n):
    k=str(n)
    s=0
    for i in range(0,len(k)):
        s=s+int(k[i])
    return s
a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    d=sum(i)
    p=prime(d)
    if p==1:
        c=c+1
print(c)    

#sum
