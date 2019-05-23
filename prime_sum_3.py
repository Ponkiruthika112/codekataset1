def prime(n):
    l=[]
    for k in range(2,n):
        if k==2:
            l.append(2)
        else:
            for i in range(2,k):
                if k%i==0:
                    break
            if i==k-1:
                l.append(k)
    return l
n=int(input())
l=prime(n)
c=0
p=[]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(j,len(l)):
            if l[i]+l[j]+l[k]==n:
                p.append([l[i],l[j],l[k]])
if len(p)>1:
    for i in p:
        if len(list(set(i)))==len(i):
            d=i
            break
else:
    d=p[0]
print(*d)
    
#prime
