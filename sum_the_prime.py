def prime(n):
    c=0
    if n==2:
        c=2
    else:
        for i in range(2,n):
            if n%i==0:
                break
        if i==n-1:
            c=n
    return c
n=int(input())
l=[]
c=0
for i in range(2,n):
    l.append(prime(i))
if l.count(0)!=0:
    l.remove(0)
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]==n:
            c=c+1
print(c)
#sum of prime
