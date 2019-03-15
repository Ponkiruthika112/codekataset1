def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c
s=""
i=int(input())
for n in range(0,i+1):
    k=fact(2*n)//(fact(n)*fact(n+1))
    s=s+str(k)+" "

print(s)
#catalon
